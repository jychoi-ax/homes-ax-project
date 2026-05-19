# homes-ax-project

AX project 문서의 편집 원본, 변경 이력, 리뷰 기록을 관리하는 저장소다.

## 운영 원칙

- GitHub가 문서 편집의 원본이다.
- Notion은 최종 승인본 게시판이다.
- 모든 수정은 branch와 pull request를 통해 반영한다.
- 최종 승인된 버전만 Notion에 게시한다.
- 현재 저장소는 private repository이고 GitHub 플랜상 branch protection enforcement가 되지 않으므로, `main` 직접 수정 금지와 PR 기반 작업은 협업 규칙으로 운영한다.

## 구조

```text
.
├── README.md
├── CONTRIBUTING.md
├── NOTION_SETUP.md
├── docs/
│   ├── ax-whitepaper.md       # 전사 백서 (L0)
│   └── domains/               # 도메인별 심층 기획 (L1)
│       ├── investment-development.md
│       ├── product-planning.md
│       ├── marketing.md
│       ├── operations.md
│       └── brokerage.md
├── scripts/
│   └── publish_to_notion.py
└── .github/
    ├── pull_request_template.md
    └── workflows/
        └── publish-notion.yml
```

## 리뷰 흐름

1. `main`에서 branch 생성
2. 문서 수정
3. pull request 생성
4. 1명 이상 approval
5. merge
6. Notion 최종본 갱신

현재는 `main`에 문서가 반영되면 GitHub Actions가 Notion 최종본 페이지를 자동 갱신하도록 설정되어 있다.

## Notion 연결

Notion 페이지 상단에 아래 문구를 넣는 것을 권장한다.

```md
이 페이지는 최종 승인본만 관리합니다.
수정 이력과 검토 과정은 GitHub 저장소에서 확인합니다.
```

## 자동 배포 설정

자동 배포 설정 방법은 [NOTION_SETUP.md](NOTION_SETUP.md)에 정리했다.
