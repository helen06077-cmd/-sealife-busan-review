# 레드팀 · 어데GO BM 캔버스 공격 모음 · 2026-11-27 · sunghan

> **공격받은 파일:** `sunghan/bm/canvas-draft.md`(BM 캔버스 9줄)와 같은 폴더의 `sunghan/bm/value-proposition.md`(가치 제안 캔버스). `canvas.html`은 canvas-draft.md 9줄을 그대로 옮긴 화면본이라 따로 공격하지 않았습니다.
> **바꿔 읽은 것:** 부탁문의 [공격받을 캔버스 파일] 자리가 비어 있어 `canvas-draft.md`로 정했습니다. 부탁문의 '맨 위 bm/redteam.md'는 맨 위에 `bm/` 폴더가 없어서, 캔버스가 있는 `sunghan/bm/redteam.md`에 씁니다.
> **어떻게 했나:** `sunghan/agents/`의 redteam-investor · redteam-customer · redteam-competitor 지시를 각각 서브에이전트 셋에게 동시에 맡겼습니다. 셋은 서로의 답을 보지 않았고, 파일은 읽기만 했습니다. 셋이 든 파일:줄은 모아 쓰기 전에 원문과 다시 맞춰 봤고, 모두 맞았습니다.
> **근거 없음:** 15개 가운데 0개. 모든 지적이 팀 파일의 줄을 하나 이상 들었습니다.
> 캔버스와 다른 파일은 고치지 않았습니다. 판정 · 까닭 칸의 [초안]은 Claude가 쓰고 sunghan이 그대로 넣으라고 한 것입니다(2026-11-27). 팀이 정하면 [초안]을 지웁니다.
> **판정 기준:** 받아들임 = 지적한 사실이 팀 파일 원문과 맞고 캔버스가 지금 답하지 못함 · 반박 = 팀 파일에 지적과 반대되는 근거가 있음 · 보류 = 팀이 먼저 정하거나 더 확인해야 함.

## 셋이 같이 짚은 곳

| 묶음 | 짚은 곳 | 지적 번호 | 셋이 같이 든 근거 |
|---|---|---|---|
| A | **수익원 = 가게 수수료 하나뿐인데, 근거 없는 제안이고 맺은 관계도 없다.** 투자자는 "돈이 안 남는다", 경쟁사는 "지킬 관계가 없다", 고객은 "추천이 돈 내는 가게 편일 수 있다"로 읽었습니다. | 1 · 2 · 8 · 13 | `sunghan/industry/my-place.md:30`, `sunghan/valuechain/flows.md:67`, `sunghan/valuechain/flows.md:81` |
| B | **실제 이동은 카카오맵 · 네이버 · 구글 지도로 넘어간다.** 투자자는 "방문을 재지 못해 청구할 수 없다", 고객은 "쓰던 앱 대신 쓸 까닭이 없다", 경쟁사는 "손님이 옮겨 가는 값이 없다"로 읽었습니다. | 3 · 6 · 15 | `sunghan/journey/map.md:82` |
| C | **다녀온 뒤 손님이 알려 주는 길(AX ①)이 없다.** 투자자는 수수료 근거가 없다고, 경쟁사는 쌓인 고유 자료가 없다고, 고객은 그 확인에 내 정보가 어떻게 쓰이는지 정해지지 않았다고 짚었습니다. | 3 · 7 · 14 | `sunghan/journey/map.md:84`, `sunghan/bm/canvas-draft.md:13` |

둘만 같이 짚은 곳(참고):
- OSRM 공용 서버 한도(투자자 4 · 경쟁사 15) — `sunghan/research/2026-11-19-data-license.md:100`
- 고객이 외국인인지 국내 여행자인지 어긋남(투자자 5 · 고객 10) — `sunghan/brand/persona.md:84`

## 지적 모음

| 번호 | 관점 | 지적 | 근거로 든 칸 · 파일:줄 | 심각도(상 · 중 · 하) | 판정 | 까닭 |
|---|---|---|---|---|---|---|
| 1 | 투자자 | 수익원의 '가게 수수료'는 팀 파일에서 제안일 뿐이고, 내겠다는 가게도 금액도 없어 확인된 수익원이 0개다. | 수익원 · `sunghan/valuechain/flows.md:67`, `sunghan/industry/my-place.md:30`, `sunghan/valuechain/steps.md:13`, `sunghan/bm/canvas-draft.md:14` | 상 | [초안] 받아들임 | [초안] 수수료는 팀 파일에서 「[제안 · 파일에 근거 없음]」입니다(`sunghan/industry/my-place.md:30`). |
| 2 | 투자자 | 손님은 돈을 내지 않고, 들어오는 돈은 가게 한쪽이 내 주기로 하는 것에만 기댄다. 우리에게 들어오는 돈 화살표 가운데 실선은 0개다. | 수익원 · 고객 세그먼트 · `sunghan/valuechain/flows.md:81`, `sunghan/industry/my-place.md:16`, `sunghan/valuechain/flows.md:90` | 상 | [초안] 받아들임 | [초안] 들어오는 돈 실선이 0개라고 팀 파일이 직접 적었습니다(`sunghan/valuechain/flows.md:81`). |
| 3 | 투자자 | 수수료는 '추천 경로로 실제로 찾아왔다'는 확인이 있어야 받는데, 9단계부터 지도 앱에 링크만 건네고 11단계(다녀온 뒤 알려 주기)는 길이 없어 청구할 근거가 생기지 않는다. | 수익원 · 고객 관계 · 핵심 활동(AX ①) · `sunghan/journey/map.md:82`, `sunghan/journey/map.md:84`, `sunghan/brand/one-page.md:17`, `sunghan/bm/canvas-draft.md:16` | 상 | [초안] 받아들임 | [초안] 9단계는 링크만 건네고 11단계는 길이 없습니다(`sunghan/journey/map.md:82`, `:84`). 방문을 확인할 방법이 없습니다. |
| 4 | 투자자 | 손님이 늘면 길찾기 서버를 따로 둘 값과 상업 서비스용 법률 검토가 드는데, 비용 금액은 비어 있고 메울 수입도 없다. | 비용 구조 · 핵심 파트너(OSRM) · `sunghan/research/2026-11-19-data-license.md:32`, `:100`, `:91`, `sunghan/bm/canvas-draft.md:18` | 중 | [초안] 받아들임 | [초안] 서버 값이 [확인 필요]이고, 대량 사용을 막는다는 규칙은 원문에 있습니다(`sunghan/research/2026-11-19-data-license.md:100`). |
| 5 | 투자자 | 돈 근거는 다른 상품(남포 걸음 · 최민재 · 시장 셋) 파일에서 빌려 왔다. 캔버스 고객은 외국인 · 타지인이고, 가치 제안 캔버스의 불편과 짝이 맞는 해결은 0개다. | 수익원 · 고객 세그먼트 · 가치 제안 캔버스 짝 맞추기 · `sunghan/valuechain/steps.md:3`, `sunghan/industry/my-place.md:6`, `sunghan/brand/persona.md:84`, `sunghan/bm/value-proposition.md:98`, `:107` | 중 | [초안] 보류 | [초안] 고객을 외국인 · 타지인으로 할지 국내 여행자로 할지 팀이 먼저 정해야 합니다(`sunghan/bm/canvas-draft.md:5`, `sunghan/brand/persona.md:84`). |
| 6 | 고객 | "실제로 그 길을 따라갈 수 있게" 한다지만 이동 단계는 결국 카카오맵 · 네이버 · 구글 지도로 넘어가, 지금 쓰는 지도 앱 대신 쓸 까닭이 없다. | 가치 제안 · 가치 제안 캔버스 '불편 덜기' · `sunghan/journey/map.md:82`, `:86`, `sunghan/bm/canvas-draft.md:11` | 상 | [초안] 반박 | [초안] 우리 화면이 맡는 것은 길 찾기가 아니라 3~7단계 조건 고르기와 추천 일정입니다(`sunghan/journey/map.md:76`~`:80`). 다만 가치 제안 문장이 "길을 따라갈 수 있게"를 앞세운 점은 지적이 맞습니다. |
| 7 | 고객 | 돈이 "내가 실제로 찾아갔다는 확인"에 매여 있는데, 위치를 받는지 · 누구에게 넘기는지 · 언제 지우는지가 없다. 후기가 바깥 AI 서버로 가는 위험도 이미 적혀 있다. | 고객 관계 · 수익원 · `sunghan/bm/canvas-draft.md:13`, `:14`, `sunghan/12일차_어데GO_AX매트릭스.md:15`, `sunghan/valuechain/flows.md:89`, `sunghan/journey/map.md:92` | 상 | [초안] 받아들임 | [초안] 위치를 받을지 [확인 필요]이고, 개인정보 담당도 [확인 필요]입니다(`sunghan/bm/canvas-draft.md:13`, `sunghan/12일차_어데GO_AX매트릭스.md:15`). |
| 8 | 고객 | 추천 기준은 T map 검색 건수(추정)이고 돈은 수수료를 내는 가게에서 오니, 받는 추천이 나를 위한 것인지 돈 내는 가게를 위한 것인지 가릴 수 없다. | 수익원 · 가치 제안 · `sunghan/valuechain/flows.md:67`, `jaehee/data/processed/csv/부산_구군별_Top5_0_안내.csv:4`, `:5` | 중 | [초안] 반박 | [초안] 추천 순위는 T map 검색 건수로 정합니다(`jaehee/data/processed/csv/부산_구군별_Top5_0_안내.csv:4`). 수수료가 순위에 들어간다는 줄은 팀 파일에 없습니다. 수수료를 실제로 받기 시작하면 다시 살아나는 지적입니다. |
| 9 | 고객 | 가장 피하고 싶은 연휴 · 주말 인파(98건 중 7건)를 두고, 자료가 월별뿐이라 언제 덜 붐비는지 알려 주지 못한다. | 가치 제안 캔버스 '불편' 칸 불편 2 · 짝 '약함' · `jaehee/scenario.md:15`, `sunghan/12일차_어데GO_AX매트릭스.md:16`, `sunghan/journey/pain-top3.md:91`, `:94` | 중 | [초안] 받아들임 | [초안] 팀 파일이 날짜별 수요는 「보여 줄 수 없다」고 직접 적었습니다(`jaehee/scenario.md:15`). |
| 10 | 고객 | 외국인 손님이 이 화면을 어디서 처음 만나는지 정해진 곳이 없고, 외국인 혜택(비짓부산패스)도 확인되지 않았다. 팀 파일의 손님은 아예 국내 여행자다. | 고객 세그먼트 · 채널 · 핵심 파트너 · `sunghan/valuechain/steps.md:10`, `:19`, `jaehee/places/tag_criteria.md:44`, `sunghan/brand/persona.md:84`, `sunghan/brand/one-page.md:40` | 상 | [초안] 받아들임 | [초안] 채널이 「미정」입니다(`sunghan/valuechain/steps.md:10`). 비짓부산패스도 [확인 필요]입니다(`jaehee/places/tag_criteria.md:44`). |
| 11 | 경쟁사 | 수요 자료(데이터랩)와 지도 · 길 자료는 누구나 무료로 받는 공개 자료라 경쟁사도 같은 날 손에 넣는다. | 핵심 자원 · `jaehee/data/processed/csv/부산_구군별_Top5_0_안내.csv:3`, `:4`, `sunghan/research/2026-11-19-data-license.md:10`, `sunghan/valuechain/points.md:14` | 상 | [초안] 받아들임 | [초안] 데이터랩은 공개 화면에서 모은 자료이고 값은 무료입니다(`jaehee/data/processed/csv/부산_구군별_Top5_0_안내.csv:3`, `sunghan/research/2026-11-19-data-license.md:10`). |
| 12 | 경쟁사 | OSM으로 만든 출구표 · 정류장표는 공개하면 ODbL로 내놓아야 하고, 팀은 원자료와 스크립트까지 공개하는 길을 권한다. | 핵심 자원 · 비용 구조 · `sunghan/research/2026-11-19-data-license.md:67`, `:89` | 상 | [초안] 보류 | [초안] 지금은 내 PC에서만 써서 해당이 없고, 공개하거나 상업 서비스로 낼 때 변호사 의견을 받기로 했습니다(`sunghan/research/2026-11-19-data-license.md:67`, `:91`). |
| 13 | 경쟁사 | 시장 가게 · 관광지와의 관계는 협약 0개인 제안뿐이라, 경쟁사가 먼저 가게를 찾아가면 우리 자리는 남지 않는다. | 수익원 · 핵심 파트너 · `sunghan/industry/my-place.md:30`, `sunghan/valuechain/flows.md:67`, `:81`, `sunghan/valuechain/steps.md:13` | 상 | [초안] 받아들임 | [초안] 맺은 협약이 하나도 없습니다(`sunghan/bm/canvas-draft.md:17`). |
| 14 | 경쟁사 | 남이 갖지 못할 자료 후보(직접 걸은 기록 · 다녀온 뒤 손님 응답)는 둘 다 아직 한 건도 없다. | 핵심 활동 · 고객 관계 · `sunghan/valuechain/points.md:15`, `sunghan/valuechain/flows.md:73`, `sunghan/journey/map.md:84` | 중 | [초안] 받아들임 | [초안] 아직 아무도 걷지 않았고, 다녀온 뒤 알려 줄 길도 없습니다(`sunghan/valuechain/points.md:15`, `sunghan/journey/map.md:84`). |
| 15 | 경쟁사 | 길찾기는 남의 공용 서버(OSRM)에, 이동은 지도 앱에 기대고, 붙잡는 장치는 '조건 저장' 하나라 손님이 옮겨 가는 값이 거의 없다. 그 화면 원본(v27)도 저장소에 없다. | 핵심 파트너 · 고객 관계 · 가치 제안 캔버스 '상품과 서비스' · `sunghan/research/2026-11-19-data-license.md:100`, `sunghan/journey/map.md:82`, `sunghan/busan-routes_tools/test-features.js:249`, `sunghan/busan-routes_tools/test-features.ps1:2` | 중 | [초안] 받아들임 | [초안] 길찾기는 OSRM에 맡기고, 저장 기능은 조건 저장 하나뿐입니다(`sunghan/research/2026-11-19-data-license.md:100`, `sunghan/busan-routes_tools/test-features.js:249`). 6번과 겹칩니다. |

## 세어 보기

- 지적 15개: 투자자 5 · 고객 5 · 경쟁사 5.
- 심각도: 상 9 · 중 6 · 하 0.
- 셋이 같이 짚은 곳 3묶음(A 수수료 · B 지도 앱으로 넘김 · C 다녀온 뒤 알려 줄 길 없음).
- 근거 없음 0개.
- 판정 [초안]: 받아들임 11 · 반박 2(6 · 8) · 보류 2(5 · 12).

## 사람이 할 일

1. [초안] 판정을 팀이 읽고, 맞으면 [초안]을 지우고 다르면 고치기. 반박으로 둔 6 · 8번을 먼저 보기.
2. 보류로 둔 5번(고객을 누구로 둘지)과 12번(공개 · 상업 서비스 때 ODbL · 변호사 의견)은 정할 사람과 날짜를 적기.
