# -*- coding: utf-8 -*-
"""불편 후보마다 빈도 · 강도를 세고 journey/pain-top3.md를 쓴다.

돌리는 법 (맨 위 폴더 -sealife-busan-review 에서):
    python sunghan/journey/count_pain.py

- 대상: journey/voc.md '단계별 연번'의 '불편:' 줄에 있는 리뷰만 (voc.md를 읽어 가져옴)
- 후보마다 말(정규식)이 리뷰 안에 있으면 그 후보로 센다. 뜻은 보지 않으므로 사람이 연번을 읽고 확인한다.
- 빈도 분모 = voc.md의 '단계를 센 리뷰' 수, 강도 = 그 후보 리뷰 가운데 별점 1 · 2점 비율
- 해결 가능성은 사람이 매긴다(이 스크립트는 비워 둔다).
"""
import csv
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
CSV_PATH = ROOT / "inputs" / "team_reviews.csv"
VOC_PATH = HERE / "voc.md"
OUT_PATH = HERE / "pain-top3.md"

# (이름(손님 말투), 여정 단계, 정규식, 우리가 못 고치는가, 그 까닭)
CANDIDATES = [
    ("주차할 데가 없어서 멀리 대고 걸어가야 해요",
     "9. 지도 앱으로 길을 찾아 이동한다",
     r"만차|협소|주차하는 공간이 부족|주차가 너무 힘들|주차장이\.\.|주차면적 적|외부 ?주차장|다른 주차장|먼 곳으로 주차|주차를 (안쪽에 )?못|주차장이랑 본관이 아예 떨어져",
     "예", "주차장은 아쿠아리움 것. 차 없이 가는 길 안내는 우리 화면 일"),
    ("작아서 금방 끝나요, 볼 게 없어요",
     "10-구경. 구경하고",
     r"규모가 (너무 |매우 )?작|조금 규모가 작|작긴|작은 느낌|작아서 볼|볼 ?게 없(?!을까)|볼 ?게 별로|볼거리가 적|적은 종|5분이면 다 보고",
     "예", "전시 규모는 아쿠아리움 것"),
    ("입장료가 비싸요, 값만큼은 아니에요",
     "10-돈. 돈을 쓴다",
     r"(입장료|요금|돈도)[^.,/\n]{0,12}(비싸|비쌈|아까|에 비해|대비|저렴한 것도 아닌)",
     "예", "값은 아쿠아리움이 정함"),
    ("사람이 너무 많아서 제대로 못 봤어요",
     "10-구경. 구경하고 (연휴 · 주말 · 휴가철과 함께 나옴 → 4. 언제)",
     r"사람이 너무 많|사람 많|사람 엄청 많|치여서|많은 사람",
     "모름", "사람 수는 못 줄임. 덜 붐비는 때를 알려 줄 수 있는지는 수요 자료를 봐야 함"),
    ("공짜인 줄 알고 찍은 사진, 나갈 때 돈 내래요",
     "10-돈. 돈을 쓴다",
     r"인화|인쇄하면|사진 상술|돈달라",
     "예", "사진 판매는 아쿠아리움 것"),
    ("수조도 길도 좁고 낡았어요",
     "10-구경. 구경하고",
     r"좁(?!아터진 나라)|낡|열악|허접",
     "예", "시설은 아쿠아리움 것"),
    ("시간 · 예약을 미리 몰라서 다 못 봤어요",
     "4. 언제, 며칠 동안?",
     r"반납해야한다고해서 다 보지도 못|예약 마감이라 못",
     "모름", "쇼 · 체험 시간을 일정에 넣을 자료가 있는지 [확인 필요]"),
]


# 팀이 고른 셋 (2026-11-25 사용자가 알려 줌). 해결 가능성은 팀이 적으면 숫자로 바꾼다.
PICKS = [
    ("입장료가 비싸요, 값만큼은 아니에요", None),
    ("사람이 너무 많아서 제대로 못 봤어요", None),
    ("작아서 금방 끝나요, 볼 게 없어요", None),
]


def quote(text, rx):
    """말이 든 줄을 원문 그대로 돌려준다(원문 안에 같은 글자가 있는지 확인)."""
    for line in text.split("\n"):
        if rx.search(line):
            q = line.strip()
            assert q in text
            return q
    raise ValueError("인용을 못 찾음")


def write_definitions(detail, reviews, denom, stars_filled):
    by_name = {c[0]: c for c in CANDIDATES}
    hits = {d[0]: d[2] for d in detail}
    L = ["", "---", "", "## 4. 팀이 고른 셋 · 정의서", ""]
    L.append("> 고른 것은 팀입니다(2026-11-25). 이 절은 불편을 정의만 합니다. **해결 방법은 쓰지 않았습니다 — 12일차에 정합니다.**")
    L.append("> 인용은 그 후보의 말이 든 리뷰 가운데 연번이 작은(최근에 쓴) 셋에서, 말이 든 줄을 글자 그대로 옮겼습니다. `count_pain.py`가 원문 안에 같은 글자가 있는지 확인했습니다. `... 더보기`는 카카오맵에서 잘린 채 복사된 표시입니다.")
    L.append("")
    for n, (name, solv) in enumerate(PICKS, 1):
        _, stage, pat, cant, why = by_name[name]
        rx = re.compile(pat)
        ids = hits[name]
        L.append(f"### 4-{n}. {name}")
        L.append("")
        L.append(f"- **불편 한 줄:** \"{name}\"")
        L.append(f"- **여정 단계:** {stage}")
        L.append("- **근거 인용 셋:**")
        for i in ids[:3]:
            L.append(f"  - ({i}) \"{quote(reviews[i]['리뷰'], rx)}\"")
        L.append(f"- **건수와 분모:** {denom}건 중 {len(ids)}건 (이 파일 안의 건수 · 연번 {', '.join(map(str, ids))})")
        strength = "[확인 필요] (별점 칸이 비어 있음)" if not stars_filled else "위 표 참고"
        L.append(f"- **점수:** 빈도 {denom}건 중 {len(ids)}건 · 강도 {strength} · 해결 가능성 {solv if solv else '[확인 필요] (팀이 아직 안 매김)'}")
        L.append(f"- **우리가 못 고치는 것:** {cant} — {why}")
        L.append("")
    return L


def read_voc():
    text = VOC_PATH.read_text(encoding="utf-8")
    pain_ids = set()
    for m in re.finditer(r"^\s*- 불편: (.+)$", text, re.M):
        pain_ids |= {int(x) for x in re.findall(r"\d+", m.group(1))}
    denom = int(re.search(r"\*\*단계를 센 리뷰: (\d+)건\*\*", text).group(1))
    return pain_ids, denom


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    pain_ids, denom = read_voc()
    rows = list(csv.DictReader(open(CSV_PATH, encoding="utf-8-sig")))
    reviews = {int(r["연번"]): r for r in rows}
    stars_filled = [r for r in rows if r["별점"].strip()]

    out = []
    detail = []
    for name, stage, pat, cant, why in CANDIDATES:
        rx = re.compile(pat)
        hit = sorted(i for i, r in reviews.items() if rx.search(r["리뷰"]))
        inside = [i for i in hit if i in pain_ids]
        outside = [i for i in hit if i not in pain_ids]
        # 강도
        rated = [i for i in inside if reviews[i]["별점"].strip()]
        if not rated:
            strength = "[확인 필요] (별점 칸이 비어 있음)"
        else:
            low = sum(1 for i in rated if reviews[i]["별점"].strip() in ("1", "2"))
            strength = f"별점 있는 {len(rated)}건 중 {low}건"
        out.append(f"| {name} | {stage} | {len(inside)}건 / {denom}건 | {strength} |  | {cant} — {why} |")
        detail.append((name, pat, inside, outside))

    lines = []
    lines.append("# 불편 후보 견주기 · 빈도 · 강도 · 해결 가능성")
    lines.append("")
    lines.append("> `count_pain.py`가 쓴 파일 · 읽은 것: `journey/voc.md`(불편 연번 · 분모), 리뷰 원문 `inputs/team_reviews.csv`")
    lines.append("> **바꿔 읽은 것:** 부탁문의 `journey/stages.md`가 내 이름 폴더에 없어서, voc.md와 같이 `sunghan/journey/map.md`의 '여행자가 거치는 단계'(1~11단계, 10단계는 구경 · 먹고 · 돈으로 나눔)를 여정 단계로 썼습니다.")
    lines.append("")
    lines.append("[1. 나의 기획 목적] 불편 후보를 빈도 · 강도 · 해결 가능성으로 견줄 수 있게 한 표에 놓는다")
    lines.append("[2. 최우선 판단 기준] 빈도와 강도는 Python으로 센 숫자만. 해결 가능성은 사람이 매김")
    lines.append("[3. 대상 / 제외] 대상: voc.md의 불편 / 제외: 리뷰에 없는 불편, 숫자 없이 '많다'고 쓰기")
    lines.append("")
    lines.append("**세 개는 고르지 않았습니다. 고르는 것은 팀이 합니다.** 표의 차례는 순위가 아닙니다.")
    lines.append("")
    lines.append("## 1. 견주기 표")
    lines.append("")
    lines.append("| 후보 | 여정 단계 | 빈도(이 파일에서 몇 건 / 분모) | 강도(그 리뷰 가운데 별점 1 · 2점 비율) | 해결 가능성(1~5) | 우리가 못 고치는 것인가 |")
    lines.append("|---|---|---|---|---|---|")
    lines += out
    lines.append("")
    lines.append(f"- 빈도: voc.md에서 '불편'으로 잡힌 리뷰 가운데 그 후보의 말이 든 리뷰 수 / voc.md의 단계를 센 리뷰 {denom}건. 이 파일 안의 건수이고 고객 전체의 비율이 아닙니다.")
    lines.append("- 한 리뷰가 여러 후보에 들어갈 수 있습니다(예: 91은 주차 · 작음 · 낡음 셋 다).")
    lines.append(f"- 강도: 리뷰 파일의 별점 칸이 {len(rows)}건 가운데 {len(stars_filled)}건만 차 있어 셀 수 없습니다. [확인 필요] (`inputs/team_reviews_source.md`: 복사한 글에 후기마다의 별점이 없음). 33번은 본문에 '1점'이라고 썼지만 별점 칸이 아니라서 세지 않았습니다.")
    lines.append("- 해결 가능성: 비워 두었습니다. 팀이 1~5로 적어 주세요.")
    lines.append("- 우리가 못 고치는 것인가: Claude가 적은 첫 판단입니다. 팀이 고쳐 주세요.")
    lines.append("")
    lines.append("## 2. 후보마다 센 말과 연번 (확인용)")
    lines.append("")
    lines.append("말은 글자가 들어 있는지만 봅니다. 연번을 열어 정말 그 불편인지 사람이 확인해 주세요.")
    lines.append("")
    for name, pat, inside, outside in detail:
        lines.append(f"- **{name}** — 말: `{pat}`")
        lines.append(f"  - 센 연번: {', '.join(map(str, inside)) or '없음'}")
        if outside:
            lines.append(f"  - 말은 있지만 voc.md 불편이 아니라 세지 않은 연번: {', '.join(map(str, outside))}")
    lines.append("")
    lines.append("## 3. 후보로 만들지 않은 voc.md 불편")
    lines.append("")
    covered = set()
    for _, _, inside, _ in detail:
        covered |= set(inside)
    rest = sorted(pain_ids - covered)
    lines.append(f"voc.md 불편 리뷰 {len(pain_ids)}건 가운데 위 후보 어디에도 들지 않은 것 {len(rest)}건입니다. 원문 그대로:")
    lines.append("")
    lines.append("| 연번 | 원문 그대로 |")
    lines.append("|---|---|")
    for i in rest:
        t = reviews[i]["리뷰"].strip().replace("\n", "<br>").replace("|", "\\|")
        lines.append(f"| {i} | {t} |")
    lines.append("")

    lines += write_definitions(detail, reviews, denom, stars_filled)

    OUT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(out))
    for name, pat, inside, outside in detail:
        print(name, inside, "밖:", outside)
    print("남은 불편:", rest)


if __name__ == "__main__":
    main()
