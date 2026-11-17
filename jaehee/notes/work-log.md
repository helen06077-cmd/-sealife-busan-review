# 작업 로그 (B)

형식: 날짜 · 한 일 · 만든/바꾼 파일 · 다음 할 일

- 2026-11-17 · jaehee-week1 브랜치 생성, 작업 폴더 구조·인벤토리 틀·.gitignore 준비 · data/raw/.gitkeep, data/processed/.gitkeep, scripts/.gitkeep, data_inventory.md, notes/work-log.md, .gitignore · 주요관광지점 입장객·데이터랩 방문자수 샘플 내려받아 data/raw/에 저장
- 2026-11-17 · 주요관광지점 입장객(월별) 구조 확인·관광지 18곳 연속성/결측/권역 계산, 예측 대상 후보 16곳 중 4곳+조건부 1곳 추천(부산아쿠아리움·부산시립박물관·태종대·부네치아 선셋 전망대, 조건부 스포원) · scripts/inspect_tour_stats.py, data/processed/busan_monthly_visitors.csv, data/processed/tour_stats_summary.csv, notes/tour_stats_check.md, data_inventory.md, .gitignore(.venv 추가) · 2026년 상반기 공백(휴업/미입력) 확인, 북구 권역 팀 확인, 권역·장소 후보표와 태그 기준표 초안
- 2026-11-17 · 권역 5개·장소 후보 27곳(계획안 예시 16 + 입장객 통계 11) 선정, 태그 기준표 초안(방문단위 적합도 0~2점·실내·유모차·휠체어·체류시간·권역·비짓부산패스·도보 15분), 권역별 필수 유형 점검 · places/region_candidates.csv, places/tag_criteria.md, places/region_checklist.md · 팀 확인(북구 권역·스포원/렛츠런파크 포함 여부·서면·동래 아이 동반 실내 보완), 열린관광지·비짓부산패스 데이터 받기, C와 place_id 체계 맞추기, A와 보정 5곳 태깅
- 2026-11-17 · week1_prompts.md를 PDF로 변환(커밋 안 함), md→PDF 변환 스크립트 작성 · scripts/md_to_pdf.py, exports/week1_prompts.pdf(.gitignore 제외), .gitignore(exports/ 추가) · 필요 시 다른 md도 같은 스크립트로 변환
- 2026-11-17 · 구·군별 Top5 관광지 검색건수 수집(데이터랩, Claude in Chrome) 및 검증 · data/processed/부산_구군별_Top5_관광지_수요예측_202301-202610.xlsx, data_inventory.md(행 추가) · 금요일 회의에서 제외 기준·검증필요 항목·2026년 검색량 감소 처리 결정
- 2026-11-17 · 대표 사용자 3명(유모차 가족·해운대 / 어르신 동반·서면 / 혼자·해운대) 시나리오 작성 — 팀 자료 근거만 사용, 월별 입장객 배수 계산(2023~2025), 근거 없는 10개 항목은 현장 확인 목록으로 분리 · scenario.md · 팀과 시나리오 검토, 현장 확인 목록 중 열린관광지 목록·시간대별 방문 수요부터 확인
