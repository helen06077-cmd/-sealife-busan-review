"""md 파일을 PDF로 변환 (md → HTML → Chrome 'PDF로 저장').

실행: jaehee/.venv/bin/python -I jaehee/scripts/md_to_pdf.py jaehee/prompts/week1_prompts.md [더 많은 md ...]
출력: jaehee/exports/<파일이름>.pdf (exports/ 는 .gitignore 로 커밋 제외)
필요: markdown 패키지(.venv), Google Chrome
"""
import html
import subprocess
import sys
from pathlib import Path

import markdown

BASE = Path(__file__).resolve().parent.parent  # jaehee/
OUT_DIR = BASE / "exports"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

CSS = """
@page { size: A4; margin: 16mm 14mm; }
body { font-family: "Apple SD Gothic Neo", "Noto Sans KR", sans-serif; font-size: 10.5pt;
       line-height: 1.6; color: #1a1a1a; }
h1 { font-size: 18pt; border-bottom: 2px solid #333; padding-bottom: 4px; }
h2 { font-size: 14pt; border-bottom: 1px solid #ccc; padding-bottom: 3px; margin-top: 1.6em; }
h3 { font-size: 12pt; }
pre { background: #f5f5f5; border: 1px solid #ddd; border-radius: 4px; padding: 10px;
      white-space: pre-wrap; word-break: break-all; font-size: 9pt; }
code { font-family: Menlo, monospace; font-size: 9pt; }
table { border-collapse: collapse; width: 100%; font-size: 9pt; margin: 8px 0; }
th, td { border: 1px solid #bbb; padding: 4px 6px; vertical-align: top; }
th { background: #eee; }
tr, pre, blockquote { page-break-inside: avoid; }
blockquote { border-left: 3px solid #999; margin-left: 0; padding-left: 10px; color: #444; }
"""


def convert(md_path: Path) -> Path:
    text = md_path.read_text(encoding="utf-8")
    body = markdown.markdown(text, extensions=["tables", "fenced_code"])
    title = html.escape(md_path.stem)
    page = (f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>{title}</title>'
            f"<style>{CSS}</style></head><body>{body}</body></html>")
    OUT_DIR.mkdir(exist_ok=True)
    html_path = OUT_DIR / f"{md_path.stem}.html"
    pdf_path = OUT_DIR / f"{md_path.stem}.pdf"
    html_path.write_text(page, encoding="utf-8")
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf_path}", html_path.as_uri()],
                   check=True, capture_output=True)
    html_path.unlink()  # 중간 HTML 은 지움
    return pdf_path


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("사용법: md_to_pdf.py <md 파일> [...]")
    for arg in sys.argv[1:]:
        print("만듦:", convert(Path(arg).resolve()))
