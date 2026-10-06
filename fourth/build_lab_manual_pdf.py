#!/usr/bin/env python3
"""Render docs/IT220_Lab_Manual.md to a print-ready PDF.

Why this exists: online markdown->PDF converters put code blocks in a <pre> that
does not wrap, so the long SQL lines are silently CUT OFF at the page edge. Here
the print stylesheet wraps code (with a hanging indent) so nothing is ever lost.

Usage
    cd fourth && python3 build_lab_manual_pdf.py
    python3 build_lab_manual_pdf.py path/to/other.md -o some/folder

Needs: python3 -m pip install markdown   (and Google Chrome, used headless).
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
DEFAULT_TARGETS = ["docs/IT220_Lab_Manual.md"]

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
  margin: 16mm 14mm 18mm 14mm;
  @bottom-center { content: counter(page); }
}

:root {
  --ink:    #1a1a2e;
  --ink2:   #44445f;
  --muted:  #6b6b85;
  --rule:   #d8d6ce;
  --rule2:  #ebe9e2;
  --accent: #1f4e79;
  --codebg: #f6f5f1;
  --warnbg: #fff8e6;
  --warnbd: #e0a800;
}

* { box-sizing: border-box; }

body {
  font-family: "Charter", "Georgia", "Times New Roman", serif;
  font-size: 10.5pt;
  line-height: 1.5;
  color: var(--ink);
  margin: 0;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}

/* ---------- headings ---------- */
h1, h2, h3, h4, h5, h6 {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  color: var(--accent);
  line-height: 1.25;
  margin: 0 0 .35em;
  break-after: avoid-page;
  page-break-after: avoid;
}
h1 { font-size: 19pt; margin-top: 0; }
h2 {
  font-size: 15pt;
  margin-top: 1.4em;
  padding-bottom: .18em;
  border-bottom: 2px solid var(--rule);
}
h3 { font-size: 12.5pt; margin-top: 1.2em; color: var(--ink); }
h4 { font-size: 11pt;  margin-top: 1em;   color: var(--ink2); }

/* each Lab / Part / Appendix starts on a fresh page - it is a workbook, not an
   essay. Ordinary headings just flow, so pages do not end up half empty. */
.newpage { break-before: page; page-break-before: always; }
.newpage:first-of-type { break-before: auto; page-break-before: auto; }
h1.newpage { margin-top: 0; }

p, ul, ol { margin: 0 0 .6em; }
li { margin-bottom: .2em; }
li > p { margin-bottom: .25em; }
strong { color: var(--ink); }

/* ---------- THE FIX: code blocks wrap instead of being clipped ---------- */
pre {
  background: var(--codebg);
  border: 1px solid var(--rule2);
  border-left: 3px solid var(--accent);
  border-radius: 4px;
  padding: 7pt 9pt;
  margin: .55em 0 .8em;
  /* wrap long lines; a PDF page has no scrollbar to reach them with */
  white-space: pre-wrap;
  overflow-wrap: break-word;
  word-break: break-word;
  overflow: visible;
  orphans: 2;
  widows: 2;
}
/* one source line = one block, so a line that is too wide for the page wraps
   with a hanging indent and still reads as a single SQL statement */
pre code .cl {
  display: block;
  padding-left: 2.4em;
  text-indent: -2.4em;
}
pre code {
  font-family: "SF Mono", "Menlo", "DejaVu Sans Mono", monospace;
  font-size: 9pt;
  line-height: 1.42;
  background: none;
  padding: 0;
  border: 0;
  white-space: inherit;
  overflow-wrap: inherit;
  word-break: inherit;
}
code {
  font-family: "SF Mono", "Menlo", "DejaVu Sans Mono", monospace;
  font-size: 9pt;
  background: var(--codebg);
  border: 1px solid var(--rule2);
  border-radius: 3px;
  padding: .5pt 3pt;
  overflow-wrap: break-word;
  word-break: break-word;
}

/* ---------- tables ---------- */
table {
  border-collapse: collapse;
  width: 100%;
  margin: .6em 0 .9em;
  font-size: 9.5pt;
  break-inside: auto;
}
th, td {
  border: 1px solid var(--rule);
  padding: 4pt 6pt;
  text-align: left;
  vertical-align: top;
  overflow-wrap: break-word;
  word-break: break-word;
}
th { background: #eef2f6; font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; }
tr { break-inside: avoid; page-break-inside: avoid; }
thead { display: table-header-group; }

/* ---------- callouts ---------- */
blockquote {
  margin: .6em 0 .9em;
  padding: 7pt 10pt;
  background: var(--warnbg);
  border-left: 3px solid var(--warnbd);
  border-radius: 4px;
  color: var(--ink2);
  break-inside: avoid;
  page-break-inside: avoid;
}
blockquote > :last-child { margin-bottom: 0; }

hr { border: 0; border-top: 1px solid var(--rule); margin: 1.1em 0; }

a { color: var(--accent); text-decoration: none; }

img { max-width: 100%; }

/* small caption line under the H1 */
h1 + h3 {
  margin-top: -.15em;
  font-size: 10.5pt;
  font-weight: normal;
  color: var(--muted);
}
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


# headings that deserve a fresh page: "Lab 7 (Week 7) - ...", "PART 2 - ...",
# "Appendix A - ..."
NEWPAGE_RE = re.compile(
    r"<h([12])>(\s*(?:Lab\s+\d|PART\s+\d|Appendix\s+[A-Z]))", re.I)


def mark_page_breaks(body: str) -> str:
    return NEWPAGE_RE.sub(r'<h\1 class="newpage">\2', body)


CODE_RE = re.compile(r"(<pre><code[^>]*>)(.*?)(</code></pre>)", re.S)


def wrap_code_lines(body: str) -> str:
    """Put every line of a code block in its own block-level span.

    A <pre> is one block, so a hanging indent on it would shift the whole
    listing. Per-line spans make each SQL line hang on its own instead.
    """
    def one(m):
        lines = m.group(2).split("\n")
        while lines and not lines[-1].strip():
            lines.pop()
        spans = "".join(
            '<span class="cl">%s</span>' % (ln if ln.strip() else "&#160;")
            for ln in lines
        )
        return m.group(1) + spans + m.group(3)

    return CODE_RE.sub(one, body)


def md_to_html(md_path: pathlib.Path) -> str:
    text = md_path.read_text(encoding="utf-8")
    # links between the docs point at .md files; in a PDF they are dead, so show
    # them as plain emphasised text instead of a broken link
    text = re.sub(r"\[([^\]]+)\]\((?!https?:)[^)]*\.md\)", r"*\1*", text)
    body = markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "sane_lists", "attr_list", "md_in_html"],
    )
    body = mark_page_breaks(body)
    body = wrap_code_lines(body)
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
            "--virtual-time-budget=5000",
            f"--user-data-dir={tmp}/profile",
            f"--print-to-pdf={pdf}",
            htm.as_uri(),
        ]
        proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL)
        # headless Chrome sometimes writes the PDF and then refuses to exit, so
        # stop waiting once the file has been there at a steady size
        last, steady, waited = -1, 0, 0.0
        while proc.poll() is None and waited < 120:
            time.sleep(0.5)
            waited += 0.5
            size = pdf.stat().st_size if pdf.exists() else -1
            steady = steady + 1 if size == last and size > 0 else 0
            last = size
            if steady >= 4:
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
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("targets", nargs="*", default=DEFAULT_TARGETS,
                    help="markdown files or folders (default: the lab manual)")
    ap.add_argument("-o", "--out", default=None,
                    help="output folder (default: beside the markdown file)")
    args = ap.parse_args()

    chrome = find_chrome()
    for md_path in collect(args.targets or DEFAULT_TARGETS):
        out_dir = pathlib.Path(args.out) if args.out else md_path.parent
        pdf = render(md_path, out_dir, chrome)
        size = pdf.stat().st_size / 1024
        print(f"  {md_path.name}  ->  {pdf}  ({size:.0f} KB)")


if __name__ == "__main__":
    main()
