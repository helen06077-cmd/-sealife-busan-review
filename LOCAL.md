# LOCAL · 남포 걸음 (GREEN ROUTE BUSAN) — Local 모듈 결과 안내 한 장

> 이 한 장만 열고 Local 여드레의 결과(인벤토리 · 페르소나 · 스토리보드)를 찾아가는 안내입니다. 파일은 옮기거나 복사하지 않았습니다. (작성 2026-11-20, 브랜치 `sunghan/keyword-map` 기준)

## 팀이 손으로 적을 두 칸

**브랜드 한 줄:**
- 후보가 있는 곳: `.claude/skills/nampo-geoleum/SKILL.md` 21~23줄(핵심 메시지 셋, 사람이 정함) · `sunghan/brand/persona.md` 28줄(한 줄 소개), 52줄(약속 한 문장) · `sunghan/brand/one-page.md` 3줄(기획 한 줄)

**대표 컷:**
- 후보가 있는 곳: `sunghan/story/storyboard.md` 25줄(1컷 훅), 29줄(5컷 전환) · `sunghan/story/first-scene.md` 1줄(내가 고른 첫 장면) · `sunghan/brand/image-prompt.md` 63줄(둘째 장면 · 자갈치시장)

> **먼저 알 것:** 맨 위 `brand/`와 `story/` 폴더는 **아직 없습니다.** 페르소나·세계관·스토리보드는 지금 팀원 폴더 `sunghan/` 아래에만 있습니다. 아래 표에 맨 위 경로는 '없음'으로, 지금 읽을 수 있는 곳은 '지금 있는 곳' 칸에 적었습니다.

## 파일 표 (처음 읽을 순서대로)

| 처음 읽을 순서 | 파일 경로 (맨 위 기준) | 무엇인가 한 줄 | 몇 일차 | 지금 있는 곳 |
|---|---|---|---|---|
| 1 | `inventory/top3.md` | 팀 표에서 고른 핵심 자산 셋(A01 자갈치시장 · A05 남포동건어물도매시장 · A03 국제시장)과 점수·근거 원문 | 7일차 1교시 | 그대로 있음 |
| 2 | `brand/persona.md` | 브랜드 페르소나(시장 길잡이)와 고객 페르소나(60대 어머니를 모시는 최민재), 브랜드 이름 '남포 걸음' | 7일차 1교시 | 없음 · `sunghan/brand/persona.md` |
| 3 | `.claude/skills/nampo-geoleum/SKILL.md` | 팀 스킬: 말투 · 핵심 메시지 셋 · 금칙어 넷 · 사실 규칙 | 7일차 3교시 | 그대로 있음 |
| 4 | `story/storyboard.md` | 숏폼 40초 8컷 샷 리스트(셔터 소리로 열고 5컷에서 전환) | 8일차 3교시 | 없음 · `sunghan/story/storyboard.md` |
| 5 | `story/first-scene.md` | 첫 장면 후보 셋, 맨 위에 '후보 ②'를 고름 | 8일차 1교시 | 없음 · `sunghan/story/first-scene.md` |
| 6 | `brand/worldview.md` | 세계관 다섯 칸(배경 · 인물 · 갈등 · 가치 · 톤), 칸마다 [사실]·[각색]·[창작] | 7일차 2교시 | 없음 · `sunghan/brand/worldview.md` |
| 7 | `brand/one-page.md` | AI 서비스 한 장 기획서(시장 셋을 걷는 순서, 모르는 것은 먼저 말함) | 7일차 4교시 · 오후 | 없음 · `sunghan/brand/one-page.md` |
| 8 | `brand/image-prompt.md` | 캐릭터(이름 없는 시장 길잡이) 기준 이미지 프롬프트, 한·영 | 7일차 4교시 · 오후 | 없음 · `sunghan/brand/image-prompt.md` (Git에 아직 안 올림) |
| 9 | `.claude/skills/nampo-geoleum/markets.md` | 스킬이 쓰는 시장 값 표(여는 날 · 점포수 · 직선거리) | 7일차 3교시 이후 | 그대로 있음 |
| 10 | `inventory/inventory-v1.csv` | 팀원 인벤토리를 합친 표(22줄) | 6일차 오후 1단계 | 그대로 있음 |
| — | `inventory/scoring.md` | top3를 고른 기준표·가중치 | 6일차 4교시 | 없음 (`top3.md`는 저장소 밖 `llm-academy/inventory/scoring.md`를 읽었다고 적음) |
| — | `story/channels.md` | 핵심 메시지 하나를 네 채널로 | 8일차 2교시 | 없음 (`storyboard.md` 1줄에도 '폴더에 없음') |
| — | `story/scene-prompts.md` | 장면 시안 · Kling 프롬프트 | 8일차 4교시 | 없음 |

- 몇 일차는 `llm-academy/` 안내 파일 제목줄의 교시 표시에서 옮겼습니다.
- 파일 안 날짜: `top3.md` · `persona.md` · `worldview.md` · `one-page.md` · `image-prompt.md` · `SKILL.md`는 2026-11-19, `first-scene.md` · `storyboard.md`는 2026-11-20입니다.

## 공개 점검 표

찾은 것만 적었습니다. 지우거나 고치지 않았습니다. 'Git'은 지금 브랜치에서 추적 중인지, 'main'은 `origin/main`에 이미 올라가 있는지입니다.

| 종류 | 파일 | 무엇이 있나 | Git | main |
|---|---|---|---|---|
| 닉네임 | `inputs/kakao-raw.txt` | 카카오맵 후기 원본 복사. 글쓴이 닉네임·레벨·후기 수·팔로워가 후기 120건마다 그대로 있음(예: 49줄) | 추적 중 | 올라가 있음 |
| 리뷰 원문 | `inputs/kakao-raw.txt` | 씨라이프 부산아쿠아리움 후기 본문 120건 | 추적 중 | 올라가 있음 |
| 리뷰 원문 | `inputs/team_reviews.csv` | 후기 본문 98건(닉네임은 뺌, `inputs/team_reviews_source.md` 15줄) | 추적 중 | 올라가 있음 |
| 리뷰 원문 | `report/tagged.csv` · `report/review-report.md` | 태그별 근거 문장으로 후기 문장을 옮김 | 추적 중 | 올라가 있음 |
| 리뷰 원문 | `sunghan/brand/worldview.md` 52 · 112 · 113줄 | 후기 25(휠체어 반납) · 76 · 91 원문 인용 | 추적 중 | — |
| 리뷰 원문 | `sunghan/story/first-scene.md` 41줄 | 후기 25 원문 인용('쓰지 않은 것'으로) | 추적 중 | — |
| 리뷰 원문 | `jaehee/scenario.md` | 3절에 후기 인용(worldview가 이 칸을 인용했다고 적음) | 추적 중 | 확인 필요 |
| 실제 인물 사진 | (그림 파일) | 저장소에 `.jpg` · `.png` 같은 그림 파일은 없음 | — | — |
| 실제 인물 사진 | `hyebeen/한국철도공사_…_부산_20210630.hwpx` | 문서 안에 그림 14개. 사람 얼굴이 있는지는 열어 보지 않음 [확인 필요] | 추적 중 | 올라가 있음 |
| 실제 인물 사진 | `sunghan/Sealife Busan Review - Report/…/부산 구별 여행 경로 개발 과정 .hwpx` | 문서 안에 그림 10개 [확인 필요] | 안 올림 | — |
| 실제 인물 사진 | `Sealife Busan Review - Report.zip` · `Ios 어플 UI 초안.hwpx` | `origin/main`에만 있음. 안을 열어 보지 않음 [확인 필요] | — | 올라가 있음 |
| 비밀값 | `.claude/settings.local.json` | 권한 설정뿐, 비밀값 없음. `.gitignore`로 빠져 있음 | 제외됨 | — |
| 비밀값 | `sunghan/Sealife Busan Review - Report/…/나머지 API 주소.txt` | API 문서 주소 목록. 인증키처럼 보이는 값은 없지만 추적용 긴 URL 꼬리가 붙어 있음 | 안 올림 | — |
| 비밀값 | (저장소 전체) | `serviceKey` · `api_key` · `token` · `password` · `인증키`를 찾음 → `sunghan/CLAUDE.md`의 '인증키를 적지 않는다' 규칙 줄만 나옴. `.env` 파일 없음 | — | — |
