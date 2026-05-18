#!/usr/bin/env python3

import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path


NOTION_VERSION = "2026-03-11"


def strip_publish_only_metadata(markdown: str) -> str:
    text = markdown.lstrip("\ufeff")

    # Remove YAML frontmatter if present at the top of the document.
    if text.startswith("---\n"):
        parts = text.split("\n---\n", 1)
        if len(parts) == 2:
            text = parts[1]

    lines = text.splitlines()
    cleaned = []
    skipping_leading_quote = True

    for line in lines:
        if skipping_leading_quote and (line.startswith("> Source:") or line.startswith("> Notion URL:") or line.startswith("> Snapshot date:") or line.startswith("> Role:")):
            continue
        if skipping_leading_quote and line.strip() == "":
            continue
        skipping_leading_quote = False
        cleaned.append(line)

    return "\n".join(cleaned).strip() + "\n"


def normalize_page_id(raw: str) -> str:
    value = raw.strip()
    match = re.search(r"([0-9a-fA-F]{32})", value.replace("-", ""))
    if match:
        compact = match.group(1).lower()
        return (
            f"{compact[0:8]}-"
            f"{compact[8:12]}-"
            f"{compact[12:16]}-"
            f"{compact[16:20]}-"
            f"{compact[20:32]}"
        )

    match = re.search(
        r"([0-9a-fA-F]{8}-"
        r"[0-9a-fA-F]{4}-"
        r"[0-9a-fA-F]{4}-"
        r"[0-9a-fA-F]{4}-"
        r"[0-9a-fA-F]{12})",
        value,
    )
    if match:
        return match.group(1).lower()

    raise ValueError("NOTION_PAGE_ID must be a page UUID or a Notion URL containing one.")


def require_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise ValueError(f"Missing required environment variable: {name}")
    return value


def main() -> int:
    api_key = require_env("NOTION_API_KEY")
    page_id = normalize_page_id(require_env("NOTION_PAGE_ID"))
    doc_path = Path(os.getenv("DOC_PATH", "docs/ax-project-v01.md"))

    if not doc_path.exists():
        raise FileNotFoundError(f"Document not found: {doc_path}")

    markdown = strip_publish_only_metadata(doc_path.read_text(encoding="utf-8"))
    payload = {
        "type": "replace_content",
        "replace_content": {
            "new_str": markdown,
        },
    }

    request = urllib.request.Request(
        url=f"https://api.notion.com/v1/pages/{page_id}/markdown",
        data=json.dumps(payload).encode("utf-8"),
        method="PATCH",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Notion-Version": NOTION_VERSION,
        },
    )

    try:
        with urllib.request.urlopen(request) as response:
            body = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="replace")
        print(error_body, file=sys.stderr)
        raise RuntimeError(f"Notion API request failed with status {exc.code}") from exc

    truncated = body.get("truncated")
    unknown_block_ids = body.get("unknown_block_ids", [])

    print(f"Published {doc_path} to Notion page {page_id}")
    print(f"truncated={truncated}")
    print(f"unknown_block_ids={len(unknown_block_ids)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
