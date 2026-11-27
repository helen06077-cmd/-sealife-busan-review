# BM 캔버스 9줄 초안 — 어데GO (GREEN ROUTE BUSAN) · 2026-11-27 · sunghan

> **읽은 파일:** AX Top 3 = `sunghan/12일차_매트릭스_이성한.md`, `sunghan/12일차_어데GO_AX매트릭스.md`, 팀 공용 `ax-risk-check.md` · 손님 불편 Top 3 = `sunghan/journey/pain-top3.md` · 서비스 단계 = `sunghan/valuechain/steps.md`(남포 걸음 7단계)와 `sunghan/journey/map.md` 70줄부터(어데GO 11단계).
> **바꿔 읽은 것:** 부탁문의 AX 세 가지(① 외국인 관광객이 추천 경로대로 다니는지 확인 ② 추천 경로가 지도에 제대로 그려지는지 확인 ③ 지도에서 부산 밖 시를 노이즈로 빼기)는 위 12일차 파일에 **그대로 적힌 줄이 없습니다.** 12일차 파일의 아이디어는 시장 셋 고르기 · 영상 댓글 세기 · 안내 한 장 에이전트(`12일차_어데GO_AX매트릭스.md:9`~`:11`)입니다. 그래서 세 가지는 부탁문을 기준으로 삼고, 각 줄에서 팀 파일에 닿는 근거만 붙였습니다.
> **먼저 알 것:** 팀 파일은 손님을 "외국인이 아니라 국내 여행자"로 적었습니다(`sunghan/brand/persona.md:84`, `sunghan/brand/one-page.md:40`). 이번 초안은 부탁문을 따라 외국인 · 타지인을 고객으로 놓았으니, 팀과 이 차이를 맞춰야 합니다.
> **테스트 대상 파일:** `test-features.ps1`이 여는 `busan-routes_초안_v27.html`(`sunghan/busan-routes_tools/test-features.ps1:2`)은 저장소에 없습니다. 지도 화면 근거는 테스트 스크립트의 항목 이름까지만입니다.

| # | 줄 (쉬운 말) | 초안 | 근거 (파일 이름:줄 번호) |
|---|---|---|---|
| 1 | **고객 세그먼트** (누구에게) | 부산 밖에서 오는 여행자 — 외국인 관광객과 다른 시·도에서 온 국내 여행자. 부산 시민은 대상이 아닙니다. | 4개 언어 화면: `sunghan/busan-routes_tools/test-features.js:28` · 입장객 통계에 내/외국인 칸: `jaehee/notes/tour_stats_check.md:14` · 부산시민을 뺀 방문객 추정 자료: `jaehee/scenario.md:23` · 팀 기준 대상은 20~30대 여행자: `sunghan/CLAUDE.md:16` · 외국인 비중 · 숫자는 [확인 필요 — 외국인 입장객 수를 `tour_stats_check.md`의 내/외국인 칸에서 세기] |
| 2 | **가치 제안** (무엇을 약속) | 차 없이 부산 안에서만 다니는 경로를, 지도 위에 핀과 선으로 정확히 그려 주고 실제로 그 길을 따라갈 수 있게 합니다. 부산 밖 시는 지도와 추천에서 처음부터 뺍니다. | 상품 한 줄: `jaehee/scenario.md:7` · 지도에 핀 · 경로 선 · 길 안내 목록 확인 항목: `sunghan/busan-routes_tools/test-features.js:204`~`:206` · 추천 대상은 부산 16개 구·군만: `jaehee/data/processed/csv/부산_구군별_Top5_0_안내.csv:6` · '추천대로 실제 다녔는지'는 아직 잴 길이 없음 → [확인 필요] |
| 3 | **채널** (어떻게 만나) | 어데GO 웹 화면(한 · 영 · 중 · 일). 영상을 올릴 곳은 아직 정하지 않았습니다. | 어데GO 화면 · 4개 언어: `sunghan/busan-routes_tools/test-features.js:19`, `:28` · 채널 미정: `sunghan/valuechain/steps.md:10`, `:19` · 외국인이 화면을 어디서 처음 보는지(공항 · 부산역 · 비짓부산 등) [확인 필요] |
| 4 | **고객 관계** (어떻게 붙잡아) | 고른 조건을 저장해 다시 열어도 이어서 쓰게 합니다. 다녀온 뒤 "추천대로 다녔는지"를 손님이 직접 알려 주는 길을 새로 만듭니다(AX ①). | 조건 저장: `sunghan/busan-routes_tools/test-features.js:249` · 지금은 다녀온 뒤 알려 줄 길이 없음: `sunghan/journey/map.md:84` · 후기 자동 분류 아이디어와 개인정보 규칙: `sunghan/12일차_어데GO_AX매트릭스.md:15` · 위치 기록을 받을지, 손님 응답만 받을지 [확인 필요] |
| 5 | **수익원** (어떻게 돈을 받아) | **수수료** — 부산 안의 시장 가게 · 관광지가, 어데GO 추천 경로로 손님이 실제로 찾아왔다는 확인(AX ①)을 보고, 데려온 손님 한 팀마다 **[확인 필요] 원쯤**의 수수료를 우리에게 냅니다. | '손님을 데려다주는 값' 후보: `sunghan/valuechain/flows.md:67` · 지금 우리에게 들어오는 돈은 실선이 0개: `sunghan/valuechain/flows.md:81` · 7단계 돈 미정: `sunghan/valuechain/steps.md:13`, `:20` · 금액 · 내겠다는 가게: [확인 필요 — 팀 파일에 금액 없음, 가게 한 곳 이상에 물어보기] |
| 6 | **핵심 자원** (꼭 있어야 할 것) | 부산 16개 구·군 방문 수요 자료, OSM 지하철 출구 · 정류장 · 버스 노선 · 도로 경로 자료, 어데GO 화면과 기능 테스트 스크립트. | 데이터랩 22,080행 · 16개 구·군: `jaehee/data/processed/csv/부산_구군별_Top5_0_안내.csv:6`, `:17` · OSM 자료와 원자료 폴더: `sunghan/research/2026-11-19-data-license.md:31`~`:32` · 테스트 스크립트: `sunghan/busan-routes_tools/test-features.js:1` · 화면 원본 `busan-routes_초안_v27.html`이 저장소에 없음 → [확인 필요] |
| 7 | **핵심 활동** (꼭 해야 할 일) | AX ② 경로가 지도에 그려지는지 버튼을 눌러 자동 점검 · AX ③ 부산 밖 시와 노이즈를 추천 후보에서 빼기 · AX ① 추천대로 다녔는지 확인하는 질문 받기. | ② 지도 자동 점검: `sunghan/busan-routes_tools/test-features.js:204`~`:206` · 일반 · 위성 · 예비 지도 · 영어 화면을 헤드리스 Chrome으로 확인한 기록: `sunghan/research/2026-11-19-data-license.md:61` · ③ 대상 지역과 제외 기준: `jaehee/data/processed/csv/부산_구군별_Top5_0_안내.csv:6`, `:9` · ① 확인 방법은 팀 파일에 없음 → [확인 필요] · '부산 밖 시를 지도에서 가리는' 코드가 있는지 [확인 필요 — v27 화면에서 확인] |
| 8 | **핵심 파트너** (함께할 곳) | OpenStreetMap · FOSSGIS OSRM(지도 · 길찾기), 한국관광 데이터랩(수요 자료), 비짓부산패스(외국인 혜택), 수수료를 낼 부산 시장 가게 · 관광지. | OSM · OSRM: `sunghan/research/2026-11-19-data-license.md:32` · 데이터랩: `jaehee/data/processed/csv/부산_구군별_Top5_0_안내.csv:3` · 비짓부산패스(외국인 전용 여부): `jaehee/places/tag_criteria.md:44` · 시장 가게: `sunghan/valuechain/flows.md:67` · 맺은 협약은 하나도 없음 → [확인 필요] |
| 9 | **비용 구조** (돈이 드는 곳) | 자료 값은 무료입니다. 손님이 늘면 OSRM 공용 서버를 쓸 수 없어(대량 사용 금지) 길찾기 서버를 따로 둘 값이 듭니다. OSM 출처 표시 · ODbL 공개 같은 규칙을 지키는 품도 듭니다. | 자료 무료: `sunghan/valuechain/points.md:14` · OSRM 대량 사용 막음, 초당 1건: `sunghan/research/2026-11-19-data-license.md:32`, `:100` · ODbL 공개 방법: `sunghan/research/2026-11-19-data-license.md:89` · 서버 값 금액 [확인 필요] |

## 세어 보기

- **근거가 있는 줄 9 · [확인 필요]가 붙은 줄 9** — 9줄 모두 팀 파일 근거가 하나 이상 있지만, 9줄 모두 아직 확인할 것이 남았습니다.
- 근거만으로 채워져 [확인 필요]가 없는 줄: 0
- 가장 비어 있는 곳: **수익원 금액**(팀 파일에 원 단위 숫자 없음)과 **AX ① 추천대로 다녔는지 확인하는 방법**(지금 다녀온 뒤 알려 줄 길이 없음, `sunghan/journey/map.md:84`).

## 사람이 할 일

1. 수익원 줄을 소리 내어 읽고 "부산 시장 가게가 정말 이 수수료를 낼까?"에 내 답을 한 줄 붙이기.
2. 고객을 외국인 · 타지인으로 둘지, 팀 파일처럼 국내 여행자(최민재)로 둘지 팀과 맞추기 (`persona.md:84`).
3. AX ①에서 손님 위치를 받을 경우, 위치는 개인정보라 받기 전에 동의 · 지우는 때를 먼저 정하기 (`12일차_어데GO_AX매트릭스.md:15`의 규칙을 본보기로).
