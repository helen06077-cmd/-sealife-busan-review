# LOCAL · 어데GO (부산 구별 여행 경로) — 결과 안내 한 장

> 이 한 장만 열면 어데GO v27과 그 뒤에 있는 자료를 찾아갈 수 있습니다. 파일은 옮기거나 복사하지 않았습니다. (작성 2026-11-25, 브랜치 `sunghan/keyword-map` 기준)
> 형식은 맨 위 `LOCAL.md`(남포 걸음판)를 따랐습니다. 남포 걸음판은 그대로 두었습니다.

## 팀이 손으로 적을 두 칸

**서비스 한 줄:**
- 후보가 있는 곳: `sunghan/CLAUDE.md` 6줄(GREEN ROUTE BUSAN 기획 목적) · v27 한파일 2943줄(부산말로 '어디 가?') · 3103줄(버터 · 해리 · 나루와 떠나는 부산)

**대표 화면:**
- 후보가 있는 곳: v27 STEP 5 '추천 일정이 나왔어요'(한파일 3126줄) · '지도에서 길 따라가기' 버튼(3127줄) · 타고 내리기 미리 보기 `sunghan/busan-routes_assets/transfer-guide.gif`

> **먼저 알 것:** 'v27 한파일'은 `sunghan/busan-routes_초안_v27_한파일.html`(34MB, 그림을 파일 안에 넣은 판)입니다. 폴더판 `busan-routes_초안_v27.html`(1.1MB)은 `busan-routes_assets/` 폴더가 옆에 있어야 그림이 보입니다. **v26 · v27은 아직 Git에 안 올렸습니다.**

## 파일 표 (처음 읽을 순서대로)

| 처음 읽을 순서 | 파일 경로 (맨 위 기준) | 무엇인가 한 줄 | Git | main |
|---|---|---|---|---|
| 1 | `sunghan/busan-routes_초안_v27_한파일.html` | 어데GO 최신판. 누구와 → 언제 → 이동 → 테마·구 → 일정, 다섯 단계로 하루 일정을 짜 줌 | 안 올림 | — |
| 2 | `sunghan/journey/map.md` | v27을 보고 그린 밸류체인 맵(화살표 14개, 근거 파일 · 줄 번호) | 안 올림 | — |
| 3 | `jaehee/scenario.md` | 팀 기준 표. GREEN ROUTE BUSAN 기획 목적의 근거 | 추적 중 | 올라가 있음 |
| 4 | `jaehee/data_inventory.md` | 데이터 인벤토리. 실측(입장객)과 추정(T map 검색)을 나눠 적음 | 추적 중 | 올라가 있음 |
| 5 | `jaehee/data/raw/한국관광데이터랩_부산구군별_내비검색_Top30_월별_202301-202610_20261117.csv` | 구별 인기 관광지 Top 5와 달별 수요 지수의 원자료 | 추적 중 | 올라가 있음 |
| 6 | `hyebeen/부산_구별_맛집_카페_리스트.xlsx` | 구별 맛집 10 · 카페 5(카카오맵 별점 · 평가 수). v27이 적은 이름(`…맛집10_카페5_리스트.csv`)과 달라 [확인 필요] | 추적 중 | 올라가 있음 |
| 7 | `sunghan/research/2026-11-19-data-license.md` | 쓴 자료마다 이용 조건(OSM ODbL 출처 표시 등) | 추적 중 (고친 것 안 올림) | 올라가 있음 |
| 8 | `sunghan/research/2026-11-20-local-routes.md` | 부산 사람이 직접 쓴 글로 고른 현지인 추천 길(18건 중 3건 사용) | 안 올림 | — |
| 9 | `sunghan/research/osm-v7/README.md` | 지하철 출구 · 정류장 · 숨은 길 · 도로 선을 만든 원자료와 스크립트 | 안 올림 | — |
| 10 | `sunghan/busan-routes_tools/build-onefile.ps1` | 폴더판을 한파일판으로 묶는 스크립트(블로그 사진은 넣지 않음) | 안 올림 | — |
| 11 | `sunghan/busan-routes_tools/test-features.ps1` | v27 기능 테스트 실행기(Edge 헤드리스) | 안 올림 | — |
| 12 | `sunghan/busan-routes_tools/patch-v26-to-v27.ps1` | v26 → v27에서 바꾼 것(테마로 고르기 등) | 안 올림 | — |
| — | `sunghan/busan-routes_assets/img/` | 관광지 사진 202장. 위키미디어 공용의 자유 이용 사진만, 작가 · 라이선스를 화면에 표시(v27 한파일 2439줄) | 추적 중 | — |
| — | `sunghan/busan-routes_station-maps/` | 역 안내 그림 114장 | 추적 중 | zip으로 올라가 있음 |
| — | `sunghan/Sealife Busan Review - Report/` | 개발 과정 문서(`부산 구별 여행 경로 개발 과정 .hwpx`) · TourAPI 안내서 · API 주소 목록 | 안 올림 | — |
| — | 버스 번호 원본(부산버스정보시스템) | v27에 받은 날(2026-11-23)만 있고 원본 파일은 못 찾음 | — | [확인 필요] |
| — | 비짓부산패스 무료입장 34곳 원문 | v27에 목록만 있고 출처 파일은 못 찾음 | — | [확인 필요] |

- 'Git'은 지금 브랜치에서 추적 중인지, 'main'은 `origin/main`에 이미 올라가 있는지입니다.
- `origin/main`에 있는 어데GO는 v23까지입니다(`busan-routes_초안_v23.html`).

## 공개 점검 표

찾은 것만 적었습니다. 지우거나 고치지 않았습니다.

| 종류 | 파일 | 무엇이 있나 | Git | main |
|---|---|---|---|---|
| 닉네임 | `sunghan/busan-routes_초안_v27_한파일.html` 4289줄 · `busan-routes_초안_v27.html` | 맛집 사진 출처로 네이버 블로그 주소 182개. 주소 안에 블로그 아이디가 그대로 있음 | 안 올림 | — |
| 닉네임 | `sunghan/research/2026-11-20-local-routes.md` · v27 한파일 | 브런치 주소에 글쓴이 아이디가 들어 있음(본문에는 "닉네임은 적지 않음"이라고 적었지만 URL에 남음) | 안 올림 | — |
| 남의 사진 | `sunghan/busan-routes_assets/blog/` | 네이버 블로그에서 받은 맛집 사진 185장. `.gitignore`로 빠져 있고 한파일판에도 안 넣음(`build-onefile.ps1` 2줄). 폴더판을 폴더째 넘기면 같이 나감. 사람 얼굴이 있는지는 열어 보지 않음 [확인 필요] | 제외됨 | — |
| 남의 사진 | `sunghan/busan-routes_assets/img/` | 위키미디어 공용 사진 202장. 라이선스 표시가 있음 | 추적 중 | — |
| 원본 자료 | `jaehee/data/raw/` | 원본 두 파일이 이미 main에 올라가 있음. `sunghan/CLAUDE.md` 규칙("원본은 내 PC의 `raw/`에만")과 다름 [확인 필요] | 추적 중 | 올라가 있음 |
| 위치 | v27 '내 위치 찾기' | 화면 문구: "위치는 이 화면에서만 사용하며 저장하지 않아요." 고른 조건은 여행자 브라우저(localStorage)에만 저장 | — | — |
| 밖으로 나가는 요청 | v27 '지도에서 길 따라가기' | 출발 · 도착 좌표를 `routing.openstreetmap.de`(OSRM)로 보냄. '내 위치'에서 출발하면 그 좌표도 보냄 | — | — |
| 비밀값 | v27 한파일 · `busan-routes_tools/` · `research/osm-v7/` | `serviceKey` · `api_key` · `apikey` · `token=` · `인증키`를 찾음 → 나온 것 없음 | — | — |
| 비밀값 | `sunghan/Sealife Busan Review - Report/…/나머지 API 주소.txt` | API 문서 주소 목록(맨 위 `LOCAL.md`에 이미 적음) | 안 올림 | — |
