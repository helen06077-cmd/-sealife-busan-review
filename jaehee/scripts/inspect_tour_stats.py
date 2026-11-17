"""관광지식정보시스템 부산 주요관광지점 입장객(월별) 점검 스크립트.

- 원본(.xls)은 읽기만 한다.
- '합계' 행 + 월별 열만 사용 ('인원계'·'총계' 열은 값 계산에 쓰지 않고 검산에만 사용).
- 결측 = 공란 또는 0.
- 성격: 실측 입장객 (관광지점별). 부산 전체 관광객 수가 아님.

실행: jaehee/.venv/bin/python -I jaehee/scripts/inspect_tour_stats.py
출력: data/processed/busan_monthly_visitors.csv, data/processed/tour_stats_summary.csv
"""
import csv
import re
import sys
from pathlib import Path

import xlrd

BASE = Path(__file__).resolve().parent.parent  # jaehee/
RAW = BASE / "data/raw/관광지식정보시스템_부산주요관광지점입장객_월별_201501-202609_20261117.xls"
OUT_LONG = BASE / "data/processed/busan_monthly_visitors.csv"
OUT_SUM = BASE / "data/processed/tour_stats_summary.csv"

MIN_RUN = 36  # 예측 대상 후보 기준: 연속 36개월 이상

# 군구 → 권역
DISTRICT_REGION = {
    "중구": "원도심·영도", "서구": "원도심·영도", "동구": "원도심·영도", "영도구": "원도심·영도",
    "부산진구": "서면·동래", "동래구": "서면·동래", "연제구": "서면·동래", "금정구": "서면·동래",
    "수영구": "수영·남구", "남구": "수영·남구",
    "해운대구": "해운대·기장", "기장군": "해운대·기장",
    "사하구": "서부 낙동강", "강서구": "서부 낙동강",
}
# 군구 기준과 다르게 배정하는 장소 (근거: 1차 확정 계획안 예시)
PLACE_REGION = {"감천문화마을": "원도심·영도"}
REGIONS = ["원도심·영도", "서면·동래", "수영·남구", "해운대·기장", "서부 낙동강", "기타"]


def region_of(district, place):
    if place in PLACE_REGION:
        return PLACE_REGION[place], "계획안 예시 기준(군구와 다름)"
    if district in DISTRICT_REGION:
        return DISTRICT_REGION[district], "군구 기준"
    return "확인 필요", "군구가 권역표에 없음"


def is_valid(v):
    return isinstance(v, float) and v > 0


def runs(flags):
    """연속 True 구간 [(start, end)] 반환 (end 포함)."""
    out, start = [], None
    for i, f in enumerate(flags + [False]):
        if f and start is None:
            start = i
        elif not f and start is not None:
            out.append((start, i - 1))
            start = None
    return out


def main():
    sh = xlrd.open_workbook(str(RAW)).sheet_by_index(0)
    head1, head2 = sh.row_values(0), sh.row_values(1)

    # 월별 열 찾기
    months, month_cols, total_cols = [], [], {}
    year = None
    for c in range(5, sh.ncols):
        if str(head1[c]).strip():
            year = str(head1[c]).strip()
        h = str(head2[c]).strip()
        m = re.fullmatch(r"(\d{4})년 (\d{2})월", h)
        if m:
            months.append(f"{m.group(1)}-{m.group(2)}")
            month_cols.append(c)
        elif h == "인원계":
            total_cols[year] = c
    assert len(months) == 141, f"월 수가 141이 아님: {len(months)}"

    long_rows, summary = [], []
    check_msgs = []
    for r in range(2, sh.nrows):
        v = sh.row_values(r)
        if v[3] != "합계":
            continue
        district, place = v[1].strip(), v[2].strip()
        region, basis = region_of(district, place)
        vals = [v[c] for c in month_cols]
        flags = [is_valid(x) for x in vals]

        # 검산: 연도별 월 합계 == 인원계
        for y, tc in total_cols.items():
            ysum = sum(x for x, mo in zip(vals, months) if mo.startswith(y[:4]) and isinstance(x, float))
            tot = v[tc] if isinstance(v[tc], float) else 0.0
            if abs(ysum - tot) > 0.5:
                check_msgs.append(f"{place} {y}: 월합 {ysum:.0f} ≠ 인원계 {tot:.0f}")

        for mo, x in zip(months, vals):
            long_rows.append({
                "place_name": place, "district": district, "region": region,
                "year_month": mo, "visitors": int(x) if isinstance(x, float) else "",
            })

        idx = [i for i, f in enumerate(flags) if f]
        rs = runs(flags)
        best = max(rs, key=lambda t: t[1] - t[0]) if rs else None
        best_len = best[1] - best[0] + 1 if best else 0
        # 결측: 첫 값~끝 값 사이의 공란·0 (앞뒤 미수집 구간은 따로 표기)
        if idx:
            inner_missing = [months[i] for i in range(idx[0], idx[-1] + 1) if not flags[i]]
        else:
            inner_missing = []
        covid = [m for m, f in zip(months, flags) if m[:4] in ("2020", "2021") and not f]
        summary.append({
            "place_name": place, "district": district, "region": region, "region_basis": basis,
            "valid_months": len(idx), "total_months": len(months),
            "first": months[idx[0]] if idx else "", "last": months[idx[-1]] if idx else "",
            "longest_run": best_len,
            "longest_run_period": f"{months[best[0]]}~{months[best[1]]}" if best else "",
            "n_runs": len(rs),
            "inner_missing": " ".join(inner_missing),
            "covid_missing_count": len(covid),
            "covid_missing": " ".join(covid),
            "zero_months": " ".join(m for m, x in zip(months, vals) if x == 0.0),
            "candidate": "Y" if best_len >= MIN_RUN else "",
            "recent_12m_total": int(sum(x for x in vals[-12:] if isinstance(x, float))),
        })

    OUT_LONG.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_LONG, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=["place_name", "district", "region", "year_month", "visitors"])
        w.writeheader()
        w.writerows(long_rows)
    with open(OUT_SUM, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(summary[0].keys()))
        w.writeheader()
        w.writerows(summary)

    print(f"장소 {len(summary)}곳, 월 {len(months)}개 ({months[0]}~{months[-1]}), long 행 {len(long_rows)}")
    print("검산(월합=인원계) 불일치:", len(check_msgs))
    for m in check_msgs:
        print("  ", m)
    for s in summary:
        print(f"{s['candidate'] or '-'} | {s['region']} | {s['district']} {s['place_name']} | "
              f"유효 {s['valid_months']}/141 | {s['first']}~{s['last']} | 최장연속 {s['longest_run']} ({s['longest_run_period']}) "
              f"| 구간수 {s['n_runs']} | 코로나결측 {s['covid_missing_count']} | 최근12개월 {s['recent_12m_total']:,}")
        if s["inner_missing"]:
            print("     중간결측:", s["inner_missing"])
    print("후보 없는 권역:", [r for r in REGIONS if not any(s['region'] == r and s['candidate'] for s in summary)])


if __name__ == "__main__":
    sys.exit(main())
