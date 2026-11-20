# OSM 자료 · busan-routes v7 (조회 2026-11-20)

busan-routes_초안_v7.html 에 넣은 지하철 출구·버스 정류장·숨은 길·도로 경로를 만들 때 쓴 원자료와 스크립트.
지도 자료 출처: © OpenStreetMap contributors (https://www.openstreetmap.org/copyright), Overpass API로 조회. 도로·걷기 경로: FOSSGIS OSRM (https://routing.openstreetmap.de/about.html).

**라이선스: 이 폴더의 OSM 자료와 그것으로 만든 표(gen_exits.js, gen_bus.js, hidden_geo.json, road_new.json 등)는 Open Database License(ODbL 1.0)를 따른다 — https://opendatacommons.org/licenses/odbl/1-0/ .** 밖에 공개·배포할 때는 OpenStreetMap 출처 표시와 ODbL 링크를 함께 둔다.

| 파일 | 내용 |
|---|---|
| exits.json | 부산 지하철 출구(railway=subway_entrance) 785곳, 출구 번호 있는 곳 775곳 |
| stops.json | 부산 버스 정류장(highway=bus_stop) 2,610곳 |
| busrel_full.json | OSM에 올라온 부산 버스 노선 41개와 정류장 구성 (부산 전체 노선 아님) |
| busrel.json | 위 노선의 이름·번호만 (중복 자료) |
| hidden.json | 숨은 길 후보 이름 검색 결과 (흰여울·이바구·감천·문탠로드 등) |
| hidden_geo.json | 숨은 길 9곳의 걷기 경로(polyline)와 길이 |
| gen_exits.js | EXITS 표 **줄이기 전 원본** (역 → 출구 645곳). v7에는 2026-11-20 OSMF Geocoding 지침에 맞춰 일정에 쓰이는 출구 175곳(76역)만 넣었다 |
| gen_bus.js | 정류장 표 **첫 버전**(영문 이름 섞임, 버스 노선 번호 포함). v7에 들어간 최종본은 한글·영문 이름만 있고 노선 번호는 뺐다(2026-11-20, Geocoding 지침의 '이름·좌표만' 조건) |
| fetch_roads.ps1 | need.json의 빠진 구간을 OSRM에서 받아 road_new.json으로 만드는 스크립트 |
| need.json, road_new.json | **두 번째 실행분(79구간)만** 남아 있음. 첫 실행분 1,141구간은 v7 파일 안 ROAD 데이터에만 있음 |
| fetch.log | 첫 실행 로그 |

숨은 길 설명 근거: 168계단·이바구길 서울신문 2021-05-13, 감천문화마을 서울신문 2026-05-28. 나머지 7곳은 OSM 이름·지점만 근거라 [확인 필요].