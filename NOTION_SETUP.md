# Notion 자동 배포 설정

이 저장소는 `main` 브랜치에 문서가 merge되면 `docs/ax-whitepaper.md`를 지정한 Notion 페이지 본문으로 자동 반영할 수 있다.

## 동작 방식

1. GitHub `main`에 push 또는 merge
2. GitHub Actions `Publish Notion` 실행
3. `docs/ax-whitepaper.md` 내용을 읽음
4. Notion markdown API로 대상 페이지 본문 전체 교체

## 먼저 준비할 것

### 1. Notion integration 또는 토큰 준비

Notion 개발자 플랫폼에서 API key를 만든다.

- 권장 secret 이름: `NOTION_API_KEY`

### 2. 대상 Notion 페이지 ID 준비

현재 페이지 URL 예시:

```text
https://www.notion.so/teamhomes/AX-project-v-01-0515-3612cb7f15c980019843cd364ff79e3e
```

위 URL 기준 페이지 ID는 아래 값이다.

```text
3612cb7f15c980019843cd364ff79e3e
```

- 권장 secret 이름: `NOTION_PAGE_ID`
- 하이픈 없는 값, 하이픈 있는 UUID, 전체 URL 모두 스크립트에서 처리 가능

### 3. integration에 페이지 접근 권한 부여

이 단계가 빠지면 API는 실패한다.

- Notion에서 대상 페이지 열기
- 우측 상단 `Share`
- 만든 integration 또는 연결을 페이지에 추가

## GitHub에 secret 넣기

저장소 `homes-ax-project`에서:

1. `Settings`
2. `Secrets and variables`
3. `Actions`
4. 아래 secret 2개 추가

- `NOTION_API_KEY`
- `NOTION_PAGE_ID`

## 배포 트리거

아래 파일이 `main`에 반영되면 자동 실행된다.

- `docs/ax-whitepaper.md`
- `scripts/publish_to_notion.py`
- `.github/workflows/publish-notion.yml`

원하면 GitHub Actions 탭에서 수동 실행도 가능하다.

## 주의점

- 이 배포는 대상 Notion 페이지의 **본문 전체를 교체**한다.
- 따라서 Notion 쪽에서만 따로 수정한 내용은 다음 배포 때 덮어써진다.
- 운영 원칙은 여전히 `GitHub = 원본`, `Notion = 게시본`이다.
