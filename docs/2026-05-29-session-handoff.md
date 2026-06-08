---
title: AX 발표 후속 세션 핸드오프 (2026-05-26 ~ 2026-05-29)
date: 2026-05-29
author: jychoi + Jay (Opus)
status: HANDOFF — ingest·wiki 합성 미실행 상태
prior_handoff: docs/2026-05-25-ceo-ax100-handoff.md
---

# AX 발표 후속 세션 핸드오프

> 이전 핸드오프 (5/25) 는 *백서 본문 작성 완료* 상태였음. 이번 세션은 *그 백서 → 발표 자료 (msseo HTML) → 5/26 피드백 → V-CTO 5/27 회의 → jychoi 정리본* 흐름.

## 새 세션 첫 명령 (복붙용)

```
docs/2026-05-29-session-handoff.md 읽고 진행 상태 파악.
이번 세션 산출물 = AX 프레임워크 thesis ("구성원의 머릿속을 회사 자산으로")
+ msseo HTML v3 + jychoi 정리본 + V-CTO 5/27 frame 흡수.
미실행 = Ingest·lint·schema update 5-step (§7 참조).
메모리 우선 로드: project_ax_anchor_cases / feedback_save_external_pastes /
project_ceo_ax100_deliverable / feedback_vcto_frame_automation_vs_model /
feedback_ceo_ax_anchor_frame.
```

---

## 1. 현재 상태 (5/29)

- **5/28 14:00 수습평가 본 발표 진행** — msseo 발표자 / jychoi PO. 결과 별도 확인 필요.
- **5/26 사전 피드백 회의** = C-level 임원 1인 (CEO 아님 / 본 발표 미참가) 의 사전 조언. msseo·jychoi 가 *일부만 차용 결정* (논리 부실 부분 인지).
- **7/1 영업일 = 100일 deadline** 확정 (5/26 회의).
- **V-CTO 5/27 회의 결과 흡수 완료** (Full AX·인프라 분리·점진 확산·Flex 첫 사인회·md+동영상 매개체).
- **이번 세션 ingest 작업 미실행** — 정리만 완료, 실 파일 저장·wiki 합성 X.

---

## 2. 이번 세션의 thesis 도출 — *"구성원의 머릿속을 회사 자산으로"*

발표 narrative 의 thesis 가 3 layer 로 진화:

```
백서 § 0.5 (수원·도쿄 두 갭)
   ↓ (의도적 미사용 결정 — 5/26 사전 회의 후 msseo·jychoi 합의)
msseo HTML v2·v3 (담당자 의존 · 데이터 파편화)
   ↓ (jychoi 가 추출·통합)
jychoi 정리본 (구성원 머릿속 → 회사 자산 + FQF + 5 단계)
   ← claude.ai gstack 분석 paste 흡수 ("AI 가 똑똑해서가 아니라 인간이 안 하던 기획 검증을 AI 가 악역 강제")
```

---

## 3. AX 프레임워크 정의 (이번 세션 산출)

### 큰 그림 — 5 단계

```
1. 사용자가 Claude 에 자동화 요구를 자연어로 작성
       ↓
2. LLM 이 사용자와 반복 대화 (선문답) 로 필요 정보 채움
       ↓
3. AX 본부가 정제된 요구를 받아 Agent 로 구현
       ↓
4. 반복 (다음 케이스)
       ↓
5. 산출물 축적 → 프레임워크 자체가 회사에 맞춰 고도화
```

### 내부 도구 — FQF (Forcing Questions Framework)

5 질문 강제:
1. 진짜 고통은 무엇인가? (실제 사례)
2. 지금은 어떻게 처리하나? (현 워크플로우)
3. 가장 작은 첫 버전은 무엇인가? (Wedge)
4. 누가 주 사용자인가? (사용자·빈도)
5. 성공·실패·예외 기준은 무엇인가? (criteria)

3 특성:
- 먼저 질문 (passive → active)
- 동조 X (anti-sycophancy)
- 모호하면 명확해질 때까지 반복 (Confusion Protocol)

### 매개체

- **md 파일 + 사용 동영상** — 전사 가이드 (V-CTO 5/27)
- **결과물 전달 경로** — 슬랙 채널 / DM / 이메일

### 첫 사인회

- **Flex** (V-CTO 5/27 확인) — 자발적 정리해서 들어온 1번째 케이스
- 다음 100일 = 4·5번째 케이스 발굴 → 전사 배포

### Thesis 한 줄

> *"AI 가 똑똑해서가 아닙니다. 인간이 귀찮아서 안 하던 기획·검증·명세를 AI 가 악역 맡아 강제 수행합니다."*

### Risk 3

| Risk | 대응 |
|---|---|
| 작은 작업까지 취조 → 피로 | 일정 규모 이상만 적용. 사소한 건 AX 본부 직접 |
| LLM frame 안 유도 → 독창성 축소 | 마지막 결정은 AX 본부·V-CTO 검토 |
| 답정너 깔때기 (특정 패턴 선호) | 회사 가이드북이 bias 균형추 |

---

## 4. 확정 결정 (재논의 X)

1. **5/26 피드백 = C-level 임원 1인** (CEO 아님) → msseo·jychoi *일부만 차용* (논리 부실 인지)
2. **Lv1/Lv2/Lv3 빌드업 frame = 미채택** (5/26 회의 임원 제안 → 부분 차용 결정에서 reject)
3. **수원·도쿄 evidence = 발표 미사용** — claude.ai 피드백 (*수원 회복 = 사람·B2B·접대 → 자동화 frame 과 안 맞음*) + msseo·jychoi 합의. **단 백서 § 0.5 안에는 유지.**
4. **OMA Mock MVP demo target = 신주쿠 한정** (stay 자산 제외)
5. **챗봇·dynamic pricing·내부 챗봇 옵션 B = reject** (3 함정 — p1 thesis 모순 / 외부 대체 가능 / 회의 결정 #3 위반)
6. **AX 발표 자료 frame** = msseo HTML v3 (6 챕터 narrative)
7. **시점 = 7/1 영업일** (100일 기준)
8. **AX 본부 운영 = V-CTO 5/27 frame** (Full AX·인프라 분리·점진 확산·Mycroft·md+동영상)

---

## 5. 산출물 list (이번 세션)

### 외부 자료 (paste / read)

| 자료 | 위치 | 상태 |
|---|---|---|
| msseo HTML v2 | `/Users/jy.choi/Documents/homes/AX _ _ 2_ _standalone_.html` | 본문 추출 완료 (텍스트 dump 만, raw 저장 X) |
| msseo HTML v3 | `iCloud/JOB/2026/homes-cloud/AX _ _ 2_ v3 _standalone_.html` | 본문 추출 완료 (동) |
| 5/26 발표 피드백 회의 | Notion `36c2cb7f-15c9-80a2-a692-c611de2c2fa6` | cache 에 ingest 완료 |
| 5/27 V-CTO 회의 | Notion `36d2cb7f-15c9-8029-9be6-f10f5f2a2c23` | cache 에 ingest 완료 |
| claude.ai gstack 분석 | 대화 paste | raw 저장 미실행 |
| jychoi 정리본 | 대화 paste | raw 저장 미실행 |
| 수원 회복 mechanism (사용자 challenge) | 외부 정보 | 회사 자료 confirm 못 함. spirit 만 흡수. |

### 내부 산출물 (이번 세션 작성)

| 산출물 | 위치 | 상태 |
|---|---|---|
| (이번 세션은 wiki·raw 직접 작성 X) | — | 다음 세션에서 ingest 실행 |

---

## 6. 백서 → 발표 → 프레임워크 narrative 흐름

| 산출물 | thesis · 위상 | 의도된 청중 |
|---|---|---|
| 백서 (`2026-05-25-ceo-ax100-whitepaper.md`) | 두 갭 (수원 Gap1 / 도쿄 Gap2) | CEO·CMO·COO·HR (서면 layer) |
| msseo HTML v3 | 담당자 의존 + 데이터 파편화 | 본 발표 청중 (이태현 대표·하진수 전무) |
| jychoi 정리본 (5/28) | 구성원 머릿속 → 회사 자산 + FQF | 프레임워크 설명 요청 응답용 |

3 layer 가 *같은 본질의 다른 표현*. 발표 자체는 v3 채택. 백서·정리본은 *underlying detail layer*.

---

## 7. 미실행 — Ingest·lint·schema update 5-step

`feedback_save_external_pastes` 메모리 패턴 정합. 미실행 상태로 다음 세션 인계.

### 🔴 Must (휘발 방지)

#### Step 1 — Raw 저장 (3 신규)

1. `raw/external/2026-05-28-claude-ai-gstack-analysis.md` — claude.ai gstack 분석 paste
2. `raw/sessions/2026-05-28-ax-framework-jychoi-draft.md` — jychoi 정리본
3. `raw/deliverables/2026-05-28-ax-presentation-v3.html` (또는 .md) — msseo HTML v3 본문 dump

#### Step 5 — 메모리 update (5건)

| # | 메모리 | update 내용 |
|---|---|---|
| 1 | `project_ax_audience_roles.md` | 5/26 피드백 = **C-level 임원 1인 (CEO 아님 / 본 발표 미참가)** 정정 |
| 2 | `project_ceo_ax100_deliverable.md` | 7/1 영업일 확정 + msseo HTML v3 path + jychoi 정리본 path + 의도적 미사용 evidence history |
| 3 | `feedback_ceo_ax_anchor_frame.md` | V-CTO 5/27 결정 추가 (Full AX·인프라 분리·점진 확산·Mycroft·md+동영상·Flex) |
| 4 | `project_ax_anchor_cases.md` | 발표 미사용 결정 + 수원 회복 mechanism 사용자 challenge (회사 confirm 못 함) + spirit 흡수 |
| 5 | 🆕 `project_ax_framework_thesis.md` | "구성원의 머릿속을 회사 자산으로" thesis + 5 단계 + FQF 5 질문 + Flex 첫 사인회. 향후 발표·deck 재사용 anchor |

### 🟡 Should

#### Step 2 — Wiki 합성

- 🆕 `wiki/ax-framework.md` — 큰 그림 5 단계 + FQF + Thesis + Risk 3
- 🔁 `wiki/ax-project-charter.md` — V-CTO 5/27 결정 + 7/1 시점 + 5/26 임원 피드백 history
- 🔁 `wiki/methodology-learnings.md §9` — 6번째 원칙 *본인 진단의 결여 risk*
- 🔁 `wiki/ontology-design.md` — AX 프레임워크 ↔ Semantic layer 관계

#### Step 3 — AGENT_INDEX 4 항목 추가

- "AX 프레임워크 / FQF / 선문답"
- "발표 자료 thesis 진화"
- "수원·도쿄 evidence 발표 미사용 이유"
- "Flex 첫 사인회 / 다음 케이스"

#### Step 4 — wiki/_log.md 2026-05-28·29 entry

#### Step 5 — Entity cross-ref

| Entity | Cross-ref |
|---|---|
| 🆕 AX 프레임워크 | ← FQF · ← 선문답 · → Mycroft · → Flex |
| 🆕 FQF | ← palantir-principles §6 · ← methodology-learnings §9 · → md 명세서 |
| 🆕 Flex 케이스 | → AX 프레임워크 §케이스 축적 · ← V-CTO 5/27 |
| 수원·도쿄 (기존) | + 발표 미사용 결정 (2026-05-28) |

### 🟢 Nice

- 의사결정 history 기록 (`feedback_rejected_options.md` 신규 또는 기존 확장):
  - Lv1/2/3 빌드업 reject
  - OMA 수원 demo target reject
  - 챗봇·dynamic pricing 옵션 B reject

---

## 8. 핵심 인용 (재사용 anchor)

### V-CTO 박현식 직접 발화 (5/27 transcript)

> *"저는 완전 이 구조가 마음에 들어서, 사실 저희가 프레임워크를 만들어서 질문을 받고, 그 질문에 이제 사용자가 선문답을 LLM 이 해주면서 사용자랑 하면 더 계속 고도화되는 프레임워크가 될 것 같아서 완전 마음에 드는데..."*

> *"한 명만 자르면 됩니다. (...) 그 외에는 다 저는 클리어. 자발적 최선은 제가 막을 수는 없겠지만."*

> *"홈즈 분들이 클로드·코덱스·재미나이 엄청 다 많이 쓰실 거라고 생각했던 게 저의 실수였던 것 같아요."*

> *"플렉스 케이스밖에 못봤어요. 자진해서 잘 정리해서 갖고온 케이스. (...) 4·5번째 케이스를 빨리 찾는 게 되게 중요할 것 같고, 2-3개만 더 쌓이다 보면 이제 그쯤 되면 저희가 전사기 뿌릴 때가 하나씩 나올 것 같습니다."*

> *"md 파일 있습니다. 사용 동영상 빨리 찍어 가지고 전사 뿌리고."*

### 5/26 회의 결정 사항 (Notion)

- 100일 = PMS (운영) 집중, IMA (투개) 별도 트랙
- AI 학습 X / 인간 정의 판단 로직 시스템화
- 업무 가이드북 = 신입에게 알려주듯 작성
- 7/1 영업일 = 100일 기준

### Thesis (jychoi 정리 + claude.ai 흡수)

> **"AX 프레임워크 = 구성원의 머릿속을 회사 자산으로 만드는 도구. AI 가 똑똑해서가 아니라, 인간이 귀찮아서 안 하던 기획·검증·명세를 AI 가 악역 맡아 강제 수행합니다."**

---

## 9. Open Questions (다음 세션 결정 필요)

| 질문 | 우선순위 |
|---|---|
| 5/28 본 발표 결과 — 평가·피드백? | 🔴 즉시 확인 |
| 수원 회복 mechanism = 사람·B2B·접대 — 회사 자료에서 confirm 가능한 source? | 🟡 (발표 미사용 결정이라 critical 은 아님) |
| 다음 100일 4·5번째 케이스 후보 — 어떤 자동화 요청? | 🔴 V-CTO frame 의 직접 next step |
| 가이드북 항목 list — TMT·PL 향 어떤 영역부터 인터뷰? | 🔴 5/26 회의 risk #5 미해결 |
| 검증 프로세스 (단위·통합·사람 개입) 정의 | 🟡 5/26 회의 risk #4 미해결 |
| 데이터 원천 (중간본 vs 최종본) 버전 관리 규칙 | 🟡 5/26 회의 risk #3 미해결 |

---

## 10. 외부 dependency

- **Luke (V-CTO 박현식)** — 격주 미팅 + 인프라 결정. 다음 격주 미팅 일정 미확정.
- **msseo** — 발표·시연 (5/28 완료). 다음 협업 = 일본 홈페이지 챗봇 (6/12 마감).
- **민석 (AWS)·진혁 (문서)·Luke (배포)** — V-CTO 5/27 결정 인프라 분담.
- **이충일 본부장 (CX)** — HTML 사례 제공자. 향후 가이드북 인터뷰 1순위 후보.
- **하진수 전무 (CMO·AX prj 리더)** — 사전 정렬·평가 라인. 본 발표 청중 1.

---

*— End of handoff —*
