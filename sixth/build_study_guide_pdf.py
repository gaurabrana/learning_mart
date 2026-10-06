#!/usr/bin/env python3
"""Render IT246_Study_Guide.md to a print-ready PDF.

Why this exists: the study guide is table-heavy, and online md->PDF converters
either clip wide tables or blow the page count up with loose spacing. This
stylesheet is tuned for study material - compact leading, tables that never
split a row across a page, and every unit starting on a fresh page.

Usage
    cd sixth && /usr/bin/python3 build_study_guide_pdf.py
    /usr/bin/python3 build_study_guide_pdf.py path/to/other.md -o some/folder

Needs: the `markdown` package (present in /usr/bin/python3) and Google Chrome,
used headless to print the PDF.
"""

import argparse
import html
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import time

import markdown

ROOT = pathlib.Path(__file__).resolve().parent
DEFAULT_TARGETS = ["IT246_Study_Guide.md"]

CHROME_CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    shutil.which("google-chrome") or "",
    shutil.which("chromium") or "",
]

CSS = r"""
@page {
  size: A4;
  margin: 14mm 13mm 15mm 13mm;
  @bottom-center { content: counter(page); }
}

:root {
  --ink:    #16181d;
  --ink2:   #3d4350;
  --muted:  #6b7280;
  --rule:   #d6d9e0;
  --rule2:  #e8eaef;
  --accent: #1f4e79;
  --accent2:#2a6ea8;
  --thbg:   #eef3f8;
  --quote:  #f7f9fb;
}

* { box-sizing: border-box; }

body {
  font-family: "Charter", "Georgia", "Times New Roman", serif;
  font-size: 9.6pt;
  line-height: 1.42;
  color: var(--ink);
  margin: 0;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}

/* ---------- headings ---------- */
h1, h2, h3, h4 {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  color: var(--accent);
  line-height: 1.2;
  margin: 0 0 .3em;
  break-after: avoid-page;
  page-break-after: avoid;
}
h1 {
  font-size: 20pt;
  margin-top: 0;
  padding-bottom: .22em;
  border-bottom: 2.5px solid var(--accent);
  letter-spacing: -.01em;
}
h2 {
  font-size: 13.5pt;
  margin-top: 1.25em;
  padding-bottom: .14em;
  border-bottom: 1.2px solid var(--rule);
}
h3 {
  font-size: 11pt;
  margin-top: 1em;
  color: var(--accent2);
}
h4 { font-size: 9.8pt; margin-top: .85em; color: var(--ink2); }

/* each Unit starts on a fresh page; the title page does not get a break */
.newpage { break-before: page; page-break-before: always; }
h1.newpage { margin-top: 0; }

p, ul, ol { margin: 0 0 .5em; }
ul, ol { padding-left: 1.25em; }
li { margin-bottom: .16em; }
li > p { margin-bottom: .2em; }
strong { color: var(--ink); font-weight: 700; }

/* the "### BIM 8th Semester ..." standfirst right under the title */
h1 + h3 {
  margin-top: -.1em;
  font-size: 9.6pt;
  font-weight: normal;
  font-style: italic;
  color: var(--muted);
  border: 0;
}

/* ---------- tables: the backbone of this document ---------- */
table {
  border-collapse: collapse;
  width: 100%;
  margin: .5em 0 .75em;
  font-size: 8.7pt;
  line-height: 1.33;
  break-inside: auto;
}
th, td {
  border: 1px solid var(--rule);
  padding: 3.2pt 5pt;
  text-align: left;
  vertical-align: top;
  overflow-wrap: break-word;
  word-break: normal;
  hyphens: auto;
}
th {
  background: var(--thbg);
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 8.4pt;
  color: var(--accent);
}
/* a row must never be split across a page - half a definition is useless */
tr { break-inside: avoid; page-break-inside: avoid; }
thead { display: table-header-group; }
tbody tr:nth-child(even) { background: #fafbfc; }

/* ---------- callouts ---------- */
blockquote {
  margin: .5em 0 .75em;
  padding: 5pt 9pt;
  background: var(--quote);
  border-left: 2.5px solid var(--accent2);
  border-radius: 3px;
  color: var(--ink2);
  break-inside: avoid;
  page-break-inside: avoid;
}
blockquote > :last-child { margin-bottom: 0; }
blockquote p { margin-bottom: .3em; }

code {
  font-family: "SF Mono", "Menlo", "DejaVu Sans Mono", monospace;
  font-size: 8.6pt;
  background: #f4f4f1;
  border: 1px solid var(--rule2);
  border-radius: 3px;
  padding: .4pt 2.5pt;
}

hr {
  border: 0;
  border-top: 1px solid var(--rule);
  margin: 1em 0;
}

a { color: var(--accent); text-decoration: none; }
img { max-width: 100%; }

/* widow/orphan control so a heading never sits alone at a page foot */
p, li { orphans: 2; widows: 2; }
"""

PAGE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>{title}</title>
<style>{css}</style>
</head><body>
{body}
</body></html>
"""


def find_chrome() -> str:
    for c in CHROME_CANDIDATES:
        if c and pathlib.Path(c).exists():
            return c
    sys.exit("Could not find Google Chrome/Chromium - needed to write the PDF.")


# "# Unit 3 - ..." and "# Course-Wide Quick Revision" each open a new page.
NEWPAGE_RE = re.compile(r"<h1>(\s*(?:Unit\s+\d|Course-Wide))", re.I)


def mark_page_breaks(body: str) -> str:
    return NEWPAGE_RE.sub(r'<h1 class="newpage">\1', body)


def md_to_html(md_path: pathlib.Path) -> str:
    text = md_path.read_text(encoding="utf-8")
    # links to sibling .md files are dead in a PDF - show them as plain emphasis
    text = re.sub(r"\[([^\]]+)\]\((?!https?:)[^)]*\.md\)", r"*\1*", text)
    body = markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "sane_lists", "attr_list"],
    )
    body = mark_page_breaks(body)
    title = md_path.stem.replace("_", " ")
    m = re.search(r"<h1[^>]*>(.*?)</h1>", body, re.S)
    if m:
        title = html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip()
    return PAGE.format(title=html.escape(title), css=CSS, body=body)


def render(md_path: pathlib.Path, out_dir: pathlib.Path, chrome: str) -> pathlib.Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    pdf = out_dir / (md_path.stem + ".pdf")
    with tempfile.TemporaryDirectory() as tmp:
        htm = pathlib.Path(tmp) / (md_path.stem + ".html")
        htm.write_text(md_to_html(md_path), encoding="utf-8")
        cmd = [
            chrome,
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            "--no-first-run",
            "--no-default-browser-check",
            "--disable-extensions",
            "--disable-background-networking",
            "--disable-sync",
            "--hide-scrollbars",
            "--no-pdf-header-footer",
            "--virtual-time-budget=10000",
            f"--user-data-dir={tmp}/profile",
            f"--print-to-pdf={pdf}",
            htm.as_uri(),
        ]
        proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL)
        # headless Chrome sometimes writes the PDF and then refuses to exit, so
        # stop waiting once the file has held a steady size for a few checks
        last, steady, waited = -1, 0, 0.0
        while proc.poll() is None and waited < 180:
            time.sleep(0.5)
            waited += 0.5
            size = pdf.stat().st_size if pdf.exists() else -1
            steady = steady + 1 if size == last and size > 0 else 0
            last = size
            if steady >= 5:
                proc.terminate()
                break
        if proc.poll() is None:
            proc.kill()
        proc.wait()
        if not pdf.exists():
            sys.exit(f"Chrome did not produce {pdf}")
    return pdf


def collect(targets) -> list:
    files = []
    for t in targets:
        p = (ROOT / t) if not pathlib.Path(t).is_absolute() else pathlib.Path(t)
        if p.is_dir():
            files += sorted(p.glob("*.md"))
        elif p.is_file():
            files.append(p)
        else:
            sys.exit(f"No such file or folder: {p}")
    return files


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("targets", nargs="*", default=DEFAULT_TARGETS,
                    help="markdown files or folders (default: the study guide)")
    ap.add_argument("-o", "--out", default="docs",
                    help="output folder (default: eighth/docs)")
    args = ap.parse_args()

    chrome = find_chrome()
    for md_path in collect(args.targets or DEFAULT_TARGETS):
        out_dir = pathlib.Path(args.out)
        if not out_dir.is_absolute():
            out_dir = ROOT / out_dir
        pdf = render(md_path, out_dir, chrome)
        size = pdf.stat().st_size / 1024
        print(f"  {md_path.name}  ->  {pdf}  ({size:.0f} KB)")


if __name__ == "__main__":
    main()
