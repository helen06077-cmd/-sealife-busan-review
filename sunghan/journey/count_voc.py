# -*- coding: utf-8 -*-
"""리뷰를 여정 단계로 나누어 세고 journey/voc.md를 쓴다.

돌리는 법 (맨 위 폴더 -sealife-busan-review 에서):
    python sunghan/journey/count_voc.py
    python sunghan/journey/count_voc.py inputs/team_reviews.csv   # 다른 리뷰 파일

규칙을 고칠 때는 아래 STAGES · DISCOMFORT · SARCASM_* 를 고치고 다시 돌린다.
voc.md 맨 위의 규칙 표도 이 값들로 다시 써진다(voc.md를 손으로 고치면 다음 실행 때 덮인다).
"""
import csv
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent  # -sealife-busan-review
CSV_PATH = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "inputs" / "team_reviews.csv"
OUT_PATH = HERE / "voc.md"

# ── 여정 단계: sunghan/journey/map.md '여행자가 거치는 단계' 표의 1~11단계 ──
# 단계 이름은 map.md 그대로. 10단계는 이름에 든 세 말(구경하고 · 먹고 · 돈을 쓴다)로 나눴다.
# 말(정규식)이 리뷰 안에 하나라도 있으면 그 단계에 넣는다. 한 리뷰가 여러 단계에 들어갈 수 있다.
STAGES = [
    ("1", "갈 만한 곳과 밥집을 모은다", None, "우리 팀이 하는 일이라 리뷰가 닿지 않음"),
    ("2", "그 달에 많이 찾는 곳, 믿을 만한 집을 먼저 고른다", None, "우리 팀이 하는 일이라 리뷰가 닿지 않음"),
    ("3", "누구랑 떠나요?", [
        "아가", "아기", "애기", "아이", "아들", "자녀", "동생", "애들", "가족",
        "연인", "커플", "데이트", "혼자", r"\d+개월",
    ], "누구와 갔는지 말함"),
    ("4", "언제, 며칠 동안?", [
        "연휴", "추석", "휴가철", "여름철", "주말", "평일", "월요일", "토요일",
        "비 ?오는", "비맞", "더운 날", "더위", "추운 날씨", "예약", r"\d시까지",
        "쇼타임", "운영하는 시간", "시간은 정해져", "일찍",
    ], "언제 갔는지 · 미리 예약 · 운영 시간"),
    ("5", "어떻게 다닐까요?", [
        "자가용", "교통", "지하철", "버스", "택시",
    ], "무엇을 타고 갔는지"),
    ("6", "어떤 여행을 할까요? (테마 · 구 고르기)", None, "우리 화면에서 고르는 일이라 리뷰가 닿지 않음"),
    ("7", "추천 일정이 나왔어요", None, "우리 화면 일이라 리뷰가 닿지 않음"),
    ("8", "지도에서 길 따라가기", None, "우리 화면 일이라 리뷰가 닿지 않음"),
    ("9", "지도 앱으로 길을 찾아 이동한다", [
        "주차", "만차", "접근성", "해변 바로앞", "걸어서", "걸어가", "멀고",
        "저 멀리", "떨어져",
    ], "찾아가기 · 도착 · 주차"),
    ("10-구경", "구경하고 먹고 돈을 쓴다 — 구경하고", [
        "볼거리", "볼 ?거리", "볼 ?게", "볼것", "볼만", "구경", "둘러보",
        "물고기", "생물", "어류", "어종", "동물", "상어", "거북", "펭귄", "수달",
        "고래", "개구리", "자라", "수조", "수족관", "규모", "쇼", "공연", "인어",
        "연극", "먹이", "밥주", "체험", "보트", "동선", "시설", "사람이",
        "사람 ", "사람한테", "많은 사람", "직원", "친절", "안내", "깨끗",
        "비린내", "사진", "굿즈", "휠체어", "콜라보", "레고", "지하에",
        "작아", "작고", "작은", "작긴", "작지", "작을", "크지",
    ], "안에서 본 것 · 겪은 것(생물, 쇼, 시설, 직원, 사람 수)"),
    ("10-먹고", "구경하고 먹고 돈을 쓴다 — 먹고", [
        "식당", "카페", "음식", "먹었", "먹고", "간식",
    ], "먹은 것"),
    ("10-돈", "구경하고 먹고 돈을 쓴다 — 돈을 쓴다", [
        "입장료", "입장권", "요금", "비싸", "비쌈", "할인", "저렴", "공짜",
        "제가격", "결제", "인화", "상술", r"\d+원", "만원", "연간권", "환불",
        "주차비", "돈",
    ], "입장료 · 할인 · 결제 · 사진값 · 주차비"),
    ("11", "여행이 어땠는지 알려 준다", [
        "다시", "또 오", "재방문", "추천", "비추", "가볼 ?만", "꼭 가",
        "가지마", "안 ?가는", "오세요", "질릴", "back to here", "가고 ?샆",
        "가고 ?싶",
    ], "다시 가겠다 · 남에게 권한다 · 말린다"),
]

# ── 불편을 말한 것: 단계의 말과 같은 마디(문장 · 쉼표 사이) 안에 이 말이 있으면 그 단계의 불편 ──
DISCOMFORT = [
    "아쉽", "아쉬", "불편", "별로", "비싸", "비쌈", "실망", "힘들", "지칩",
    "최악", "불쾌", "불친절", "아까운", "아깝(?!지 않)", "좁", "협소", "만차",
    "부족", "낡", "열악", "허접", "상술", "볼 ?게 없", "볼 ?게 별로", "볼거리가 적",
    "적은 종", "적어서", "작아요", "작아서", "규모가 작", "작긴", "작은 느낌",
    "못하", "못 하", "못했", "안되", "안 되", "멀고", "너무 멀", "저 멀리",
    "떨어져", "사람이 너무 많", "사람 많", "사람 엄청 많", "치여", "많은 사람",
    "비린내", "짜증", "환장", "어이없", "잡치", "비추", "가지마", "깡패",
    "에휴", "단점", "그닥", "촉박", "짧아", "대기시간", "기다려", "비맞",
    "날렸", "줄었", "질릴", "hell", "돈에", "돈달라", "안 ?가는", "통제가 잘 안",
    "ㄱㅡ", ";;",
]

# ── 제외 ──
AD_WORDS = ["협찬", "광고", "체험단", "제공받", "원고료", "소정의"]

# ── 비꼬는 말일 수 있는 리뷰 (사람이 판단) ──
# 칭찬 말이 있으면서, 아래 '뒤집는 표시'가 하나 이상 있는 리뷰. 표시 수가 많은 순, 같으면 연번 순으로 다섯 개까지.
SARCASM_PRAISE = [
    "좋", "괜찮", "친절", "만족", "재밌", "재미", "귀엽", "귀여", "행복", "고향",
    "오세요", "최고", "대단",
]
SARCASM_MARKS = [
    "ㅋㅋ", ";;", "역설", "나름", "긴해", "긴 한데", "아무튼", "무슨", "대기중", "ㄱㅡ",
]
# 불편 말도 함께 있으면 표시 하나로 더 친다.

# 마디 자르기: 줄바꿈 · 문장 끝 뒤 공백 · 쉼표 · 이음말(그래도 · 그래서 · 근데 · 다만 · 그리고 · 하지만 · 그런데) 앞
UNIT_SPLIT = re.compile(r"\n|(?<=[.!?…~;])\s+|,\s*|\s+(?=그래도|그래서|근데|다만|그리고|하지만|그런데)")


def any_match(patterns, text):
    return [p for p in patterns if re.search(p, text)]


def units(text):
    return [u.strip() for u in UNIT_SPLIT.split(text) if u and u.strip()]


def main():
    with open(CSV_PATH, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    total = len(rows)

    # 1) 같은 글(공백만 다른 것 포함) → 처음 나온 것만 남김
    seen, dup, ads, kept = {}, [], [], []
    for r in rows:
        key = re.sub(r"\s+", "", r["리뷰"])
        if key in seen:
            dup.append((r["연번"], seen[key]))
            continue
        seen[key] = r["연번"]
        hit = any_match(AD_WORDS, r["리뷰"])
        if hit:
            ads.append((r["연번"], hit))
            continue
        kept.append(r)

    # 2) 단계 나누기
    result = {}
    no_stage = []
    for code, name, kws, _ in STAGES:
        result[code] = {"reviews": [], "discomfort": [], "low": [], "quotes": []}
    for r in kept:
        text = r["리뷰"]
        in_any = False
        for code, name, kws, _ in STAGES:
            if not kws or not any_match(kws, text):
                continue
            in_any = True
            st = result[code]
            st["reviews"].append(r["연번"])
            hit_units = [u for u in units(text) if any_match(kws, u) and any_match(DISCOMFORT, u)]
            if hit_units:
                st["discomfort"].append(r["연번"])
                st["quotes"].append((r["연번"], hit_units[0]))
                if r["별점"].strip() in ("1", "2"):
                    st["low"].append(r["연번"])
        if not in_any:
            no_stage.append(r["연번"])

    has_rating = any(r["별점"].strip() for r in kept)

    # 인용은 원문 그대로인지 확인
    by_no = {r["연번"]: r["리뷰"] for r in kept}
    for st in result.values():
        for no, q in st["quotes"]:
            assert q in by_no[no], f"인용이 원문과 다름: {no}"

    # 3) 비꼬는 말 후보
    sarcasm = []
    for r in kept:
        t = r["리뷰"]
        if not any_match(SARCASM_PRAISE, t):
            continue
        marks = any_match(SARCASM_MARKS, t)
        if marks:
            if any_match(DISCOMFORT, t):
                marks = marks + ["불편 말"]
            sarcasm.append((-len(marks), int(r["연번"]), r["연번"], marks, t))
    sarcasm.sort()
    sarcasm = sarcasm[:5]

    # 4) 쓰기
    def pat(p):
        return "`" + p.replace("|", "\\|") + "`"

    L = []
    L.append("# VOC · 씨라이프 부산아쿠아리움 리뷰를 여정 단계로 나누기")
    L.append("")
    L.append(f"> `count_voc.py`가 쓴 파일 · 리뷰 파일 `{CSV_PATH.relative_to(ROOT).as_posix()}` "
             "(카카오맵 후기, 2026-11-16 수집 · 출처는 `inputs/team_reviews_source.md`)")
    L.append("> **바꿔 읽은 것:** 부탁문의 `journey/stages.md`가 내 이름 폴더에 없어서, 같은 폴더 "
             "`sunghan/journey/map.md`의 '여행자가 거치는 단계' 표(1~11단계)를 여정 단계로 썼습니다. "
             "10단계는 이름에 든 세 말(구경하고 · 먹고 · 돈을 쓴다)로 나눴습니다.")
    L.append("")
    L.append("[1. 나의 기획 목적] 고객의 불편을 고객이 남긴 글로 근거를 세운다")
    L.append("[2. 최우선 판단 기준] 세는 것은 Python으로(이 파일의 숫자는 모두 `count_voc.py`가 셈). 인용은 원문 그대로")
    L.append("[3. 대상 / 제외] 대상: 이 파일의 리뷰 전부 / 제외: 같은 글이 두 번 이상 있는 리뷰(한 번만 셈), 광고 · 협찬이라고 밝힌 리뷰")
    L.append("")
    L.append("## 1. 단계를 고르는 규칙")
    L.append("")
    L.append("- 리뷰 안에 아래 '말' 가운데 하나라도 있으면 그 단계에 넣습니다. 한 리뷰가 여러 단계에 들어갈 수 있습니다.")
    L.append("- **불편을 말한 것:** 리뷰를 마디(줄바꿈 · 문장 끝 · 쉼표 · '그래도 · 그래서 · 근데 · 다만 · 그리고 · 하지만 · 그런데' 앞)로 자르고, 한 마디 안에 그 단계의 말과 아래 '불편 말'이 함께 있으면 그 단계의 불편으로 셉니다.")
    L.append("- 말은 글자가 들어 있는지만 봅니다(정규식). 뜻은 보지 않으므로 사람이 인용을 읽고 확인해야 합니다.")
    L.append("")
    L.append("| 단계 | 단계 이름 (map.md 그대로) | 무엇을 보나 | 이 말이 있으면 |")
    L.append("|---|---|---|---|")
    for code, name, kws, what in STAGES:
        words = " ".join(pat(k) for k in kws) if kws else "— (규칙 없음)"
        L.append(f"| {code} | {name} | {what} | {words} |")
    L.append("")
    L.append("**불편 말:** " + " ".join(pat(k) for k in DISCOMFORT))
    L.append("")
    L.append("**뺄 때 쓰는 말:** 같은 글 = 공백 · 줄바꿈을 빼고 글자가 똑같은 글(처음 나온 연번만 남김) · "
             "광고 · 협찬 = " + " ".join(pat(k) for k in AD_WORDS))
    L.append("")
    L.append("## 2. 단계별 건수")
    L.append("")
    L.append(f"건수는 모두 **이 파일 안에서 몇 건**입니다. 고객 전체의 비율이 아닙니다.")
    L.append("")
    L.append("| 여정 단계 | 리뷰 건수 | 그 가운데 불편을 말한 건수 | 그 가운데 별점 1 · 2점 건수 | 불편 인용 셋(연번과 원문 그대로) |")
    L.append("|---|---|---|---|---|")
    for code, name, kws, what in STAGES:
        st = result[code]
        if not kws:
            L.append(f"| {code}. {name} | — | — | — | {what} |")
            continue
        low = str(len(st["low"])) + "건" if has_rating else "[확인 필요]"
        qs = st["quotes"][:3]
        qtxt = "<br>".join(f"({no}) \"{q.replace('|', '¦')}\"" for no, q in qs) if qs else "—"
        L.append(f"| {code}. {name} | {len(st['reviews'])}건 | {len(st['discomfort'])}건 | {low} | {qtxt} |")
    L.append("")
    L.append("- 인용 셋은 불편 마디가 있는 리뷰 가운데 연번이 작은(최근에 쓴) 셋에서 그 마디를 글자 그대로 옮겼습니다. `count_voc.py`가 원문 안에 같은 글자가 있는지 확인했습니다.")
    L.append("- 인용 끝의 `... 더보기`는 카카오맵에서 잘린 채 복사된 표시입니다(원문 그대로 둠).")
    if not has_rating:
        L.append(f"- 별점: 리뷰 파일의 별점 칸이 남은 {len(kept)}건 모두 빈칸이라 셀 수 없습니다. [확인 필요] "
                 "(`inputs/team_reviews_source.md`: 복사한 글에 후기마다의 별점이 없음)")
    L.append("")
    L.append("**단계별 연번 (확인용)**")
    L.append("")
    for code, name, kws, _ in STAGES:
        if not kws:
            continue
        st = result[code]
        L.append(f"- {code} 리뷰: {', '.join(st['reviews']) or '없음'}")
        L.append(f"  - 불편: {', '.join(st['discomfort']) or '없음'}")
    L.append("")
    L.append("## 3. 분모와 뺀 것")
    L.append("")
    L.append(f"- **전체 리뷰 수(분모): {total}건** — 이 파일의 리뷰 전부")
    L.append(f"- **뺀 리뷰: {len(dup) + len(ads)}건**")
    if dup:
        L.append(f"  - 같은 글 {len(dup)}건: " + ", ".join(f"{a}(={b}와 같음)" for a, b in dup))
    else:
        L.append("  - 같은 글: 0건 (공백 · 줄바꿈을 빼고 글자가 똑같은 리뷰가 없음)")
    if ads:
        L.append(f"  - 광고 · 협찬 {len(ads)}건: " + ", ".join(f"{a}({'·'.join(h)})" for a, h in ads))
    else:
        L.append("  - 광고 · 협찬: 0건 (위 '뺄 때 쓰는 말'이 든 리뷰가 없음)")
    L.append(f"- **단계를 센 리뷰: {len(kept)}건** (분모 {total}건 − 뺀 {len(dup) + len(ads)}건)")
    L.append(f"- **어느 단계에도 들어가지 않은 리뷰: {len(no_stage)}건** — 연번 {', '.join(no_stage) or '없음'}")
    L.append("")
    L.append("## 4. 칭찬처럼 보이지만 비꼬는 말일 수 있는 리뷰 (판단은 사람이)")
    L.append("")
    L.append("칭찬 말(" + " ".join(pat(k) for k in SARCASM_PRAISE) + ")이 있으면서 뒤집는 표시("
             + " ".join(pat(k) for k in SARCASM_MARKS) + ")가 있는 리뷰를, 표시가 많은 순으로 다섯 개까지 골랐습니다. "
             "(불편 말도 함께 있으면 표시 하나로 더 칩니다.) Python은 후보만 골랐습니다. 정말 불편을 말한 것이면 옆에 '불편'이라고 적어 주세요.")
    L.append("")
    L.append("| 연번 | 원문 그대로 | 걸린 표시 | 사람 판단 |")
    L.append("|---|---|---|---|")
    for _, _, no, marks, t in sarcasm:
        cell = t.strip().replace("|", "¦").replace("\n", "<br>")
        L.append(f"| {no} | {cell} | {' '.join(m if m == '불편 말' else pat(m) for m in marks)} | |")
    L.append("")

    OUT_PATH.write_text("\n".join(L), encoding="utf-8")
    print(f"전체 {total} · 뺀 것 {len(dup) + len(ads)} · 센 것 {len(kept)} · 단계 없음 {len(no_stage)}")
    for code, name, kws, _ in STAGES:
        if kws:
            st = result[code]
            print(f"{code}\t리뷰 {len(st['reviews'])}\t불편 {len(st['discomfort'])}")
    print("비꼬기 후보:", [s[2] for s in sarcasm])
    print("썼음:", OUT_PATH)


if __name__ == "__main__":
    main()
