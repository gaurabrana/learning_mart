#!/usr/bin/env python3
"""Render IT246_Study_Guide.md to a Word (.docx) study guide.

Companion to build_study_guide_pdf.py. Same markdown source, same visual system,
but a real Word file: proper Heading 1-4 styles (so the navigation pane and any
generated TOC work), tables with computed column widths, and page numbers in the
footer.

Why a hand-rolled parser instead of pandoc: pandoc is not installed here, and the
markdown this document uses is a small, fixed subset - headings, paragraphs,
bullet and numbered lists, pipe tables, blockquotes, rules, and inline
bold/italic/code. Parsing that directly keeps the repo free of a new toolchain.

Usage
    cd sixth && /usr/bin/python3 build_study_guide_docx.py
    /usr/bin/python3 build_study_guide_docx.py path/to/other.md -o some/folder

Needs: python-docx (present in /usr/bin/python3).
"""

import argparse
import pathlib
import re
import sys

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.shared import Mm, Pt, RGBColor, Emu

try:
    from PIL import Image
except ImportError:                                   # pragma: no cover
    Image = None

ROOT = pathlib.Path(__file__).resolve().parent
DEFAULT_TARGETS = ["IT246_Study_Guide.md"]

# ---- the shared visual system (same values as the PDF stylesheet) ----------
INK = RGBColor(0x16, 0x18, 0x1D)
INK2 = RGBColor(0x3D, 0x43, 0x50)
MUTED = RGBColor(0x6B, 0x72, 0x80)
ACCENT = RGBColor(0x1F, 0x4E, 0x79)
ACCENT2 = RGBColor(0x2A, 0x6E, 0xA8)
RULE = "D6D9E0"
THBG = "EEF3F8"
ZEBRA = "FAFBFC"
QUOTEBG = "F7F9FB"

BODY_FONT = "Georgia"
HEAD_FONT = "Helvetica Neue"
MONO_FONT = "Menlo"

BODY_PT = 9.5
TABLE_PT = 8.5
TABLE_HEAD_PT = 8.2
CAPTION_PT = 8.2

# print geometry: A4 with a wider inside margin, so the text does not vanish
# into the spine when the printed copy is stapled or spiral-bound
MARGIN_TOP = 15
MARGIN_BOTTOM = 16
MARGIN_INSIDE = 19      # the bound edge
MARGIN_OUTSIDE = 13
TEXT_W_MM = 210 - MARGIN_INSIDE - MARGIN_OUTSIDE
FIGURE_MAX_W_MM = 148   # a figure never runs the full measure - it reads better inset

# usable text width in DXA twips (1440 = 1 inch)
PAGE_W_DXA = int(TEXT_W_MM / 25.4 * 1440)


# --------------------------------------------------------------------------
# low-level OOXML helpers (python-docx has no public API for these)
# --------------------------------------------------------------------------
def _el(tag, **attrs):
    e = OxmlElement(tag)
    for k, v in attrs.items():
        e.set(qn("w:" + k), str(v))
    return e


def shade(cell_or_para, fill):
    """Solid background fill behind a table cell or a paragraph."""
    pr = cell_or_para._tc.get_or_add_tcPr() if hasattr(cell_or_para, "_tc") \
        else cell_or_para._p.get_or_add_pPr()
    pr.append(_el("w:shd", val="clear", color="auto", fill=fill))


def para_border(paragraph, edge="bottom", sz=8, color=RULE, space=2):
    """A rule under (or beside) a paragraph - used for heading underlines and
    the left bar on callouts. Cheaper and safer than faking it with a table."""
    pPr = paragraph._p.get_or_add_pPr()
    bdr = pPr.find(qn("w:pBdr"))
    if bdr is None:
        bdr = _el("w:pBdr")
        pPr.append(bdr)
    bdr.append(_el("w:" + edge, val="single", sz=sz, space=space, color=color))


def table_borders(table, color=RULE, sz=4):
    tbl_pr = table._tbl.tblPr
    borders = _el("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        borders.append(_el("w:" + edge, val="single", sz=sz, space=0, color=color))
    tbl_pr.append(borders)


def keep_row_together(row):
    """A table row must never split across a page - half a definition is
    useless to someone revising."""
    trPr = row._tr.get_or_add_trPr()
    trPr.append(_el("w:cantSplit"))


def repeat_header(row):
    trPr = row._tr.get_or_add_trPr()
    trPr.append(_el("w:tblHeader"))


def set_grid(table, widths):
    """Rewrite w:tblGrid to the computed widths and pin the layout to fixed.

    python-docx creates an even grid at add_table() time and never updates it,
    so without this every table comes out with equal columns however the cell
    widths are set."""
    tbl = table._tbl
    grid = tbl.find(qn("w:tblGrid"))
    if grid is not None:
        tbl.remove(grid)
    grid = _el("w:tblGrid")
    for w in widths:
        grid.append(_el("w:gridCol", w=w))
    # the grid must sit directly after tblPr
    tbl.insert(1, grid)

    tbl_pr = tbl.tblPr
    tbl_pr.append(_el("w:tblLayout", type="fixed"))
    tbl_pr.append(_el("w:tblW", w=sum(widths), type="dxa"))


def cell_margins(table, top=40, bottom=40, left=70, right=70):
    tbl_pr = table._tbl.tblPr
    mar = _el("w:tblCellMar")
    for edge, val in (("top", top), ("left", left), ("bottom", bottom), ("right", right)):
        mar.append(_el("w:" + edge, w=val, type="dxa"))
    tbl_pr.append(mar)


def add_page_number_footer(section):
    p = section.footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    for tag, attrs, text in (
        ("w:fldChar", {"fldCharType": "begin"}, None),
        ("w:instrText", {}, " PAGE "),
        ("w:fldChar", {"fldCharType": "end"}, None),
    ):
        e = OxmlElement(tag)
        for k, v in attrs.items():
            e.set(qn("w:" + k), v)
        if text is not None:
            e.set(qn("xml:space"), "preserve")
            e.text = text
        run._r.append(e)
    run.font.name = BODY_FONT
    run.font.size = Pt(8.5)
    run.font.color.rgb = MUTED


def add_running_header(section, text):
    """A running head so a loose printed page can still be placed."""
    hdr = section.header
    hdr.is_linked_to_previous = False
    p = hdr.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p.paragraph_format.space_after = Pt(2)
    for run in list(p.runs):
        run._r.getparent().remove(run._r)
    run = p.add_run(text)
    run.font.name = HEAD_FONT
    run.font.size = Pt(7.8)
    run.font.color.rgb = MUTED
    para_border(p, "bottom", sz=4, color=RULE, space=3)


def mirror_margins(doc):
    """Even/odd pages swap their inside and outside margins, so the binding
    edge is always the wide one in a double-sided print."""
    settings = doc.settings.element
    if settings.find(qn("w:mirrorMargins")) is None:
        settings.append(_el("w:mirrorMargins"))


def page_setup(section, first=False):
    section.page_width, section.page_height = Mm(210), Mm(297)
    section.top_margin, section.bottom_margin = Mm(MARGIN_TOP), Mm(MARGIN_BOTTOM)
    section.left_margin = Mm(MARGIN_INSIDE)     # "inside" once mirrored
    section.right_margin = Mm(MARGIN_OUTSIDE)
    section.header_distance = Mm(9)
    section.footer_distance = Mm(9)


def add_figure(doc, path, caption, number):
    """A centred diagram with a numbered caption, kept on one page."""
    width_mm = FIGURE_MAX_W_MM
    if Image is not None:
        with Image.open(path) as im:
            px_w, px_h = im.size
        # never upscale past the image's own 150-dpi natural size, and never
        # let a tall diagram push past half the text column's height
        natural_mm = px_w / 150 * 25.4
        width_mm = min(FIGURE_MAX_W_MM, natural_mm)
        height_mm = width_mm * px_h / px_w
        if height_mm > 150:
            width_mm *= 150 / height_mm

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pf = p.paragraph_format
    pf.space_before = Pt(7)
    pf.space_after = Pt(2)
    pf.keep_with_next = True
    pf.keep_together = True
    p.add_run().add_picture(str(path), width=Mm(width_mm))

    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cpf = cap.paragraph_format
    cpf.space_before = Pt(0)
    cpf.space_after = Pt(8)
    cpf.keep_together = True
    r = cap.add_run("Figure %d  " % number)
    r.font.name = HEAD_FONT
    r.font.size = Pt(CAPTION_PT)
    r.font.color.rgb = ACCENT2
    r.bold = True
    add_inline(cap, caption, size=CAPTION_PT, color=MUTED, base_italic=True)


# --------------------------------------------------------------------------
# OOXML element ordering
#
# The property elements below are schema *sequences*, not bags: Word rejects or
# silently drops a tblPr whose children are in the wrong order, even though
# LibreOffice renders it happily. python-docx places the properties it knows
# about correctly, but anything appended by hand (borders, shading, layout)
# lands at the end - so the whole document gets normalised before saving.
# --------------------------------------------------------------------------
ORDER = {
    "pPr": ["pStyle", "keepNext", "keepLines", "pageBreakBefore", "framePr",
            "widowControl", "numPr", "suppressLineNumbers", "pBdr", "shd",
            "tabs", "suppressAutoHyphens", "kinsoku", "wordWrap",
            "overflowPunct", "topLinePunct", "autoSpaceDE", "autoSpaceDN",
            "bidi", "adjustRightInd", "snapToGrid", "spacing", "ind",
            "contextualSpacing", "mirrorIndents", "suppressOverlap", "jc",
            "textDirection", "textAlignment", "textboxTightWrap",
            "outlineLvl", "divId", "cnfStyle", "rPr", "sectPr",
            "pPrChange"],
    "tblPr": ["tblStyle", "tblpPr", "tblOverlap", "bidiVisual",
              "tblStyleRowBandSize", "tblStyleColBandSize", "tblW", "jc",
              "tblCellSpacing", "tblInd", "tblBorders", "shd", "tblLayout",
              "tblCellMar", "tblLook", "tblCaption", "tblDescription",
              "tblPrChange"],
    "tcPr": ["cnfStyle", "tcW", "gridSpan", "hMerge", "vMerge", "tcBorders",
             "shd", "noWrap", "tcMar", "textDirection", "tcFitText", "vAlign",
             "hideMark", "tcPrChange"],
    "trPr": ["cnfStyle", "divId", "gridBefore", "gridAfter", "wBefore",
             "wAfter", "cantSplit", "trHeight", "tblHeader", "tblCellSpacing",
             "jc", "hidden", "trPrChange"],
}
# elements that may appear only once - a later one wins (it is the value we set)
SINGLETON = {"tblW", "tblLayout", "tblBorders", "tblCellMar", "shd", "pBdr",
             "jc", "tcW", "tblLook", "spacing", "ind"}


def normalise(root):
    """Sort each property element's children into schema order, dropping
    duplicate singletons (keeping the last value set)."""
    for tag, order in ORDER.items():
        for pr in root.iter(qn("w:" + tag)):
            kids = list(pr)
            seen, keep = set(), []
            for child in reversed(kids):
                name = child.tag.split("}")[1]
                if name in SINGLETON:
                    if name in seen:
                        continue
                    seen.add(name)
                keep.append(child)
            keep.reverse()
            keep.sort(key=lambda c: order.index(c.tag.split("}")[1])
                      if c.tag.split("}")[1] in order else len(order))
            for child in kids:
                pr.remove(child)
            for child in keep:
                pr.append(child)


# --------------------------------------------------------------------------
# markdown parsing
# --------------------------------------------------------------------------
INLINE_RE = re.compile(r"(\*\*.+?\*\*|(?<!\*)\*(?!\*).+?(?<!\*)\*(?!\*)|`[^`]+`)")


def add_inline(paragraph, text, size=BODY_PT, color=INK, font=BODY_FONT,
               base_bold=False, base_italic=False):
    """Write text into a paragraph, honouring **bold**, *italic* and `code`."""
    for part in INLINE_RE.split(text):
        if not part:
            continue
        bold, italic, mono = base_bold, base_italic, False
        if part.startswith("**") and part.endswith("**") and len(part) > 4:
            part, bold = part[2:-2], True
        elif part.startswith("`") and part.endswith("`") and len(part) > 2:
            part, mono = part[1:-1], True
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            part, italic = part[1:-1], True
        run = paragraph.add_run(part)
        run.font.name = MONO_FONT if mono else font
        run.font.size = Pt(size - 0.6 if mono else size)
        run.font.color.rgb = color
        run.bold = bold
        run.italic = italic


def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def is_sep(line):
    return bool(re.fullmatch(r"\|[\s:\-|]+\|", line.strip()))


def parse_blocks(lines):
    """Turn the markdown into a flat list of (kind, payload) blocks."""
    blocks, i, n = [], 0, len(lines)
    while i < n:
        raw = lines[i]
        line = raw.rstrip()

        if not line.strip():
            i += 1
            continue

        if re.fullmatch(r"-{3,}", line.strip()):
            blocks.append(("hr", None))
            i += 1
            continue

        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            blocks.append(("h%d" % len(m.group(1)), m.group(2).strip()))
            i += 1
            continue

        m = re.match(r"^!\[(.*?)\]\((.+?)\)\s*$", line.strip())
        if m:
            blocks.append(("img", (m.group(2).strip(), m.group(1).strip())))
            i += 1
            continue

        # pipe table: a header row followed by a |---|---| separator
        if line.startswith("|") and i + 1 < n and is_sep(lines[i + 1]):
            header = split_row(line)
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append(split_row(lines[i]))
                i += 1
            blocks.append(("table", (header, rows)))
            continue

        if line.lstrip().startswith(">"):
            buf = []
            while i < n and lines[i].lstrip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i]).rstrip())
                i += 1
            # blank lines inside a callout separate its paragraphs
            paras, cur = [], []
            for b in buf:
                if b.strip():
                    cur.append(b.strip())
                elif cur:
                    paras.append(" ".join(cur))
                    cur = []
            if cur:
                paras.append(" ".join(cur))
            blocks.append(("quote", paras))
            continue

        m = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)$", line)
        if m:
            items, ordered = [], bool(re.match(r"\d+\.", m.group(2)))
            while i < n:
                mm = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)$", lines[i].rstrip())
                if mm:
                    items.append(mm.group(3).strip())
                    i += 1
                elif (lines[i].strip() and lines[i].startswith(("  ", "\t"))
                      and items):
                    # an indented wrapped line belongs to the item above it
                    items[-1] += " " + lines[i].strip()
                    i += 1
                else:
                    break
            blocks.append(("ol" if ordered else "ul", items))
            continue

        # ordinary paragraph: consecutive plain lines join into one
        buf = []
        while i < n:
            cur = lines[i].rstrip()
            if (not cur.strip() or cur.startswith(("#", "|", ">"))
                    or re.fullmatch(r"-{3,}", cur.strip())
                    or re.match(r"^!\[.*?\]\(.+?\)\s*$", cur.strip())
                    or re.match(r"^(\s*)([-*]|\d+\.)\s+", cur)):
                break
            buf.append(cur.strip())
            i += 1
        if buf:
            blocks.append(("p", " ".join(buf)))
    return blocks


# --------------------------------------------------------------------------
# column widths
# --------------------------------------------------------------------------
def column_widths(header, rows, total=PAGE_W_DXA):
    """Share the page width out in proportion to how much text each column
    actually carries. Equal columns waste space on a 'Unit | Title | LH' table
    and crush the one column anybody reads."""
    ncol = len(header)
    weights, floors = [], []
    for c in range(ncol):
        texts = [re.sub(r"[*`]", "", r[c]) for r in rows if c < len(r)]
        texts.append(re.sub(r"[*`]", "", header[c]))
        lens = [len(x) for x in texts[:-1]] or [1]
        lens.append(len(texts[-1]) * 1.3)
        longest, mean = max(lens), sum(lens) / len(lens)
        weights.append(max(3.0, 0.45 * longest + 0.55 * mean))
        # a column must at least fit its longest single word, or Word
        # hyphen-breaks it mid-word ("Copyri / ght") and it reads as a typo
        word = max((len(w) for x in texts for w in x.split()), default=1)
        floors.append(min(0.26 * total, word * 95 + 170))

    lo, hi = 0.07 * total, 0.60 * total
    w = [max(lo, floors[i], min(hi, total * x / sum(weights)))
         for i, x in enumerate(weights)]
    # honouring the floors can overshoot the page; take the excess back from
    # the roomiest columns, never below their own floor
    for _ in range(40):
        over = sum(w) - total
        if over <= 1:
            break
        slack = [max(0.0, w[i] - floors[i]) for i in range(ncol)]
        if sum(slack) <= 0:
            break
        for i in range(ncol):
            w[i] -= over * slack[i] / sum(slack)
    w = [int(x * total / sum(w)) for x in w]
    w[-1] += total - sum(w)
    return w


# --------------------------------------------------------------------------
# document assembly
# --------------------------------------------------------------------------
def style_base(doc):
    normal = doc.styles["Normal"]
    normal.font.name = BODY_FONT
    normal.font.size = Pt(BODY_PT)
    normal.font.color.rgb = INK
    normal.paragraph_format.space_after = Pt(4)
    normal.paragraph_format.space_before = Pt(0)
    normal.paragraph_format.line_spacing = 1.08
    normal.paragraph_format.widow_control = True
    # east-asian font fallback, else Word substitutes something else entirely
    rpr = normal.element.get_or_add_rPr()
    rfonts = rpr.get_or_add_rFonts()
    for attr in ("w:ascii", "w:hAnsi", "w:cs"):
        rfonts.set(qn(attr), BODY_FONT)

    specs = {
        "Heading 1": (20, ACCENT, 0, 6),
        "Heading 2": (13.5, ACCENT, 14, 4),
        "Heading 3": (11, ACCENT2, 11, 3),
        "Heading 4": (9.8, INK2, 9, 2),
    }
    for name, (size, color, before, after) in specs.items():
        st = doc.styles[name]
        st.font.name = HEAD_FONT
        st.font.size = Pt(size)
        st.font.color.rgb = color
        st.font.bold = True
        st.font.italic = False
        pf = st.paragraph_format
        pf.space_before = Pt(before)
        pf.space_after = Pt(after)
        pf.keep_with_next = True
        pf.line_spacing = 1.0
        rpr = st.element.get_or_add_rPr()
        rfonts = rpr.get_or_add_rFonts()
        for attr in ("w:ascii", "w:hAnsi", "w:cs"):
            rfonts.set(qn(attr), HEAD_FONT)


def add_quote(doc, paras):
    for idx, text in enumerate(paras):
        p = doc.add_paragraph()
        pf = p.paragraph_format
        pf.left_indent = Mm(4)
        pf.right_indent = Mm(2)
        pf.space_before = Pt(4 if idx == 0 else 1)
        pf.space_after = Pt(4 if idx == len(paras) - 1 else 1)
        pf.keep_together = True
        shade(p, QUOTEBG)
        para_border(p, "left", sz=18, color="2A6EA8", space=6)
        add_inline(p, text, size=BODY_PT - 0.2, color=INK2)


def add_table(doc, header, rows):
    ncol = len(header)
    rows = [r + [""] * (ncol - len(r)) if len(r) < ncol else r[:ncol] for r in rows]
    table = doc.add_table(rows=1, cols=ncol)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table_borders(table)
    cell_margins(table)

    widths = column_widths(header, rows)
    set_grid(table, widths)
    # the grid lays the table out; the per-cell widths keep Word from
    # re-fitting the column when someone edits a cell
    for c, cell in enumerate(table.rows[0].cells):
        cell.width = Emu(widths[c] * 635)
    for c, text in enumerate(header):
        cell = table.rows[0].cells[c]
        shade(cell, THBG)
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.0
        add_inline(p, text, size=TABLE_HEAD_PT, color=ACCENT, font=HEAD_FONT,
                   base_bold=True)
    repeat_header(table.rows[0])
    keep_row_together(table.rows[0])

    for r, data in enumerate(rows):
        row = table.add_row()
        keep_row_together(row)
        for c, text in enumerate(data):
            cell = row.cells[c]
            cell.width = Emu(widths[c] * 635)
            if r % 2 == 1:
                shade(cell, ZEBRA)
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.0
            add_inline(p, text, size=TABLE_PT)

    doc.add_paragraph().paragraph_format.space_after = Pt(2)


def add_contents(doc, outline, course=""):
    """A plain-text detailed contents: every unit and every section, in order."""
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
    h = doc.add_paragraph(style="Heading 1")
    add_inline(h, "Detailed contents", size=20, color=ACCENT, font=HEAD_FONT,
               base_bold=True)
    para_border(h, "bottom", sz=18, color="1F4E79", space=3)

    note = doc.add_paragraph()
    note.paragraph_format.space_after = Pt(8)
    add_inline(note, "Every section of every unit, in the order it appears.",
               size=BODY_PT, color=MUTED, base_italic=True)

    for level, text in outline:
        if level == 1 and course and text.startswith(course):
            continue        # the cover title is not a destination
        if level == 2 and text.strip().lower() == "contents":
            continue        # the cover's own summary table, not a section
        p = doc.add_paragraph()
        pf = p.paragraph_format
        pf.space_before = Pt(6 if level == 1 else 0)
        pf.space_after = Pt(0.5)
        pf.line_spacing = 1.04
        pf.left_indent = Mm(0 if level == 1 else 7)
        pf.keep_with_next = level == 1
        add_inline(p, text, size=BODY_PT if level == 1 else BODY_PT - 0.5,
                   color=ACCENT if level == 1 else INK2,
                   font=HEAD_FONT if level == 1 else BODY_FONT,
                   base_bold=level == 1)


def build(md_path: pathlib.Path, out_dir: pathlib.Path) -> pathlib.Path:
    lines = md_path.read_text(encoding="utf-8").split("\n")
    blocks = parse_blocks(lines)

    doc = Document()
    sec = doc.sections[0]
    page_setup(sec)
    mirror_margins(doc)
    style_base(doc)
    add_page_number_footer(sec)

    # the detailed contents is generated from the headings themselves, as plain
    # text rather than a TOC field: a field prints blank unless the reader
    # happens to press F9 first, and this document is made to be printed
    outline = [(int(k[1]), v) for k, v in blocks if k in ("h1", "h2")]
    # the running head and the contents filter both need the course code; take
    # it from the title itself rather than hardcoding one course's number
    title = next((v for k, v in blocks if k == "h1"), "")
    m = re.match(r"\s*(IT\s*\d+)", title)
    course = m.group(1).strip() if m else ""
    figure_no = 0
    md_dir = md_path.parent

    first_heading = True
    first_unit = True
    standfirst = False   # the italic line that sits right under the title
    for kind, payload in blocks:
        if kind == "hr":
            continue  # the rules only separate units, and units already break

        if kind in ("h1", "h2", "h3", "h4"):
            level = int(kind[1])
            # each Unit and the revision section opens a fresh page - and its
            # own Word section, so it can carry its own running head
            if level == 1 and not first_heading:
                if first_unit:
                    add_contents(doc, outline, course)
                    first_unit = False
                sec = doc.add_section(WD_SECTION.NEW_PAGE)
                page_setup(sec)
                add_running_header(sec,
                                   (course + " · " if course else "") + payload)
            if level == 3 and standfirst:
                p = doc.add_paragraph()
                p.paragraph_format.space_after = Pt(7)
                add_inline(p, payload, size=BODY_PT, color=MUTED,
                           base_italic=True)
                standfirst = False
                continue
            p = doc.add_paragraph(style="Heading %d" % level)
            add_inline(p, payload,
                       size={1: 20, 2: 13.5, 3: 11, 4: 9.8}[level],
                       color={1: ACCENT, 2: ACCENT, 3: ACCENT2, 4: INK2}[level],
                       font=HEAD_FONT, base_bold=True)
            if level == 1:
                para_border(p, "bottom", sz=18, color="1F4E79", space=3)
                standfirst = first_heading
                first_heading = False
            elif level == 2:
                para_border(p, "bottom", sz=6, color=RULE, space=2)

        elif kind == "p":
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(4)
            add_inline(p, payload)

        elif kind in ("ul", "ol"):
            style = "List Bullet" if kind == "ul" else "List Number"
            for item in payload:
                p = doc.add_paragraph(style=style)
                pf = p.paragraph_format
                pf.space_after = Pt(1.5)
                pf.line_spacing = 1.06
                pf.left_indent = Mm(7)
                add_inline(p, item)

        elif kind == "img":
            rel, caption = payload
            path = (md_dir / rel).resolve()
            if not path.exists():
                sys.exit("Figure not found: %s" % path)
            figure_no += 1
            add_figure(doc, path, caption, figure_no)

        elif kind == "quote":
            add_quote(doc, payload)

        elif kind == "table":
            add_table(doc, *payload)

    normalise(doc.element.body)
    for s in doc.sections:
        for part in (s.footer, s.header):
            normalise(part._element)

    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / (md_path.stem + ".docx")
    doc.save(out)
    return out


def collect(targets):
    files = []
    for t in targets:
        p = (ROOT / t) if not pathlib.Path(t).is_absolute() else pathlib.Path(t)
        if p.is_dir():
            files += sorted(p.glob("*.md"))
        elif p.is_file():
            files.append(p)
        else:
            sys.exit("No such file or folder: %s" % p)
    return files


def main():
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("targets", nargs="*", default=DEFAULT_TARGETS)
    ap.add_argument("-o", "--out", default="docs")
    args = ap.parse_args()

    for md_path in collect(args.targets or DEFAULT_TARGETS):
        out_dir = pathlib.Path(args.out)
        if not out_dir.is_absolute():
            out_dir = ROOT / out_dir
        docx_path = build(md_path, out_dir)
        print("  %s  ->  %s  (%.0f KB)"
              % (md_path.name, docx_path, docx_path.stat().st_size / 1024))


if __name__ == "__main__":
    main()
