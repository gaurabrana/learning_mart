#!/usr/bin/env python3
"""Generate IT220 Unit 1 PowerPoint deck (with native-shape diagrams).
Run: python3 build_unit1_pptx.py  ->  IT220_Unit1.pptx
"""
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR

IMG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")

# Per-concept revision extras, keyed by the slide's image.
# (memory hook shown on the slide; exam Q + model answer added to speaker notes)
CONCEPT_EXTRAS = {
 "s1_data_ladder.png": ("Facts → meaning → organized store.",
   "Differentiate data, information & database with examples.",
   "Data = raw facts; information = data + context; database = organized, persistent, shared collection. eSewa: raw fields → 'you paid Hari Rs 500' → all transactions stored."),
 "s1_users_dbms.png": ("Data is the books; the DBMS is the librarian.",
   "What is a DBMS, and how does it differ from a database?",
   "DBMS = software that manages databases (MySQL, Oracle). Database = the actual data. The DBMS adds concurrency, integrity, querying, security. DB + DBMS + apps = a database system."),
 "s1_db_users.png": ("The DBA is air-traffic control for data.",
   "List the database users and the role of the DBA.",
   "Naive/end users, application programmers, sophisticated users, and the DBA. DBA duties: schema design, security/permissions, backup & recovery, performance tuning."),
 "s1_file_vs_dbms.png": ("One source of truth beats many drifting copies.",
   "State four advantages of a DBMS over a file-based system.",
   "Controlled redundancy, consistency/integrity, concurrent multi-user sharing, security/access control, backup & recovery (any four, one line each)."),
 "s2_data_models.png": ("Idea → tables → disk.",
   "What is a data model? Name its categories.",
   "A set of concepts describing structure + constraints + operations. Categories: conceptual (ER) → representational (relational/tables) → physical (storage)."),
 "s2_schema_instance.png": ("Schema = the mould; instance = what's in it now.",
   "Differentiate schema and instance with an example.",
   "Schema = stable design (e.g. Student(roll,name,program)); instance = the actual current rows, volatile. One schema has many instances over time."),
 "s2_three_schema.png": ("View → whole → storage.",
   "Explain the three-schema architecture.",
   "External (per-user views), conceptual (whole logical DB), internal (physical storage). Mappings between levels hide detail and give data independence."),
 "s2_data_independence.png": ("Logical = change the design safely; physical = change the storage safely.",
   "Define logical and physical data independence.",
   "Logical = change the conceptual schema without changing views/apps. Physical = change storage (indexes/disks) without changing the conceptual schema."),
 "s3_languages.png": ("Define, Manipulate, Control, Transact.",
   "Name the SQL sub-languages with one command each.",
   "DDL (CREATE), DML (SELECT/INSERT), DCL (GRANT), TCL (COMMIT). SQL bundles all four."),
 "s3_interfaces.png": ("Same data, many doors.",
   "List the types of DBMS interfaces.",
   "Menu-based, form-based, GUI, natural-language, and API/embedded-SQL. Principle: match the interface to the user."),
 "s3_dbms_components.png": ("A DBMS is a kitchen of cooperating roles.",
   "Name the main components of a DBMS and their roles.",
   "Query processor/optimizer, storage manager, buffer manager, transaction manager (ACID), and the catalog/data dictionary."),
 "s3_data_dictionary.png": ("Metadata = data about data.",
   "What is a data dictionary / system catalog?",
   "The system catalog stores metadata: table names, column types, constraints, users, indexes. It makes the database self-describing."),
 "s4_centralized.png": ("One machine = one point of failure.",
   "What is centralized architecture and its main drawback?",
   "Data + DBMS + app on one central machine; terminals only display. Simple, but a single point of failure with poor scalability."),
 "s4_client_server.png": ("Three tiers: face, logic, data.",
   "Differentiate two-tier and three-tier architecture.",
   "Two-tier: client (UI+logic) ↔ DB server. Three-tier: client (UI) ↔ application server (business logic) ↔ DB server. Three-tier scales better."),
 "s4_classification.png": ("Model · users · distribution.",
   "On what bases are DBMSs classified?",
   "By data model (relational/NoSQL/...), number of users (single vs multi), distribution (centralized vs distributed), and purpose."),
 "s4_synthesis.png": ("User → interface → DBMS → schema → architecture.",
   "How do the concepts of Unit 1 connect?",
   "Users reach a DBMS (components + catalog) via interfaces/languages; it manages a database described by a schema at 3 levels (data independence), on a centralized/client-server architecture; classified by model, users, distribution."),
}

# Short hypothetical ("imagine if…") prompts per concept — added to speaker notes.
HYPO = {
 "s1_data_ladder.png": "Given a file holding just '84,91,77,88' — is it data, info, or a database? Add context + structure to climb all three.",
 "s1_users_dbms.png": "If the college dropped its DBMS for per-department Excel, predict 3 failures within a month — each is a job the DBMS was doing.",
 "s1_db_users.png": "A startup with no DBA loses a table to a stray query — who notices, who restores it, and who should have set permissions?",
 "s1_file_vs_dbms.png": "A hospital keeps blood group in 3 files; only 1 is corrected before a transfusion — what's the risk, and which feature prevents it?",
 "s2_data_models.png": "Three teams describe one library (boxes / CREATE TABLE / disk files) — which abstraction level is each?",
 "s2_schema_instance.png": "Photograph the attendance register daily; on day 15 you add a column — did the schema or the instance change?",
 "s2_three_schema.png": "Hospital: patient / doctor / billing / DBA views — sort each onto external / conceptual / internal.",
 "s2_data_independence.png": "Add a biometric_id column — does the old portal break (logical)? Move data to SSD — which independence (physical)?",
 "s3_languages.png": "Four statements with keywords hidden (create / fetch / grant access / make permanent) — label each DDL/DML/DCL/TCL.",
 "s3_interfaces.png": "One library, three users (elderly member / busy librarian / developer) — design a fitting interface for each.",
 "s3_dbms_components.png": "A 0.1s query suddenly takes 30s — which component (optimizer / buffer / storage / transaction) do you suspect, and why?",
 "s3_data_dictionary.png": "Unknown database, no docs — list every table WITHOUT reading the data. (Query the catalog — it's self-describing.)",
 "s4_centralized.png": "Whole college on one server; the room loses power at result time — what's the blast radius? Now imagine 3 replicated servers.",
 "s4_client_server.png": "50,000 hit the portal in 5 min — which buckles, two-tier or three-tier, and where do you add machines in each?",
 "s4_classification.png": "Classify a laptop billing app, a bank core, and a social network on model / users / distribution.",
 "s4_synthesis.png": "eSewa's DB servers go down but app servers stay up — what still works, what breaks, and why?",
}

# ---- palette ----
NAVY   = RGBColor(0x0C, 0x2B, 0x4A)
BLUE   = RGBColor(0x18, 0x5F, 0xA5)
TEAL   = RGBColor(0x0F, 0x6E, 0x56)
AMBER  = RGBColor(0x85, 0x4F, 0x0B)
CORAL  = RGBColor(0x99, 0x3C, 0x1D)
LIGHT  = RGBColor(0xF2, 0xF5, 0xF8)
PALE   = RGBColor(0xE6, 0xF1, 0xFB)
PALET  = RGBColor(0xE1, 0xF5, 0xEE)
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
DARK   = RGBColor(0x1A, 0x1A, 0x1A)
GREY   = RGBColor(0x55, 0x60, 0x6B)
LGREY  = RGBColor(0xC7, 0xCF, 0xD6)

prs = Presentation()
prs.slide_width  = Inches(13.333)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]
SW, SH = prs.slide_width, prs.slide_height


def _bg(slide, color):
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = color


def _box(slide, l, t, w, h):
    return slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h)).text_frame


def _bar(slide, color, l, t, w, h):
    sp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(l), Inches(t), Inches(w), Inches(h))
    sp.fill.solid(); sp.fill.fore_color.rgb = color
    sp.line.fill.background(); sp.shadow.inherit = False
    return sp


def _notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text


def _settext(sp, text, font=WHITE, size=14, bold=True, align=PP_ALIGN.CENTER):
    tf = sp.text_frame; tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    for m in ("margin_left", "margin_right"):
        setattr(tf, m, Inches(0.06))
    tf.margin_top = Inches(0.03); tf.margin_bottom = Inches(0.03)
    lines = text.split("\n")
    p = tf.paragraphs[0]; p.alignment = align
    r = p.add_run(); r.text = lines[0]
    r.font.size = Pt(size); r.font.bold = bold; r.font.color.rgb = font
    for extra in lines[1:]:
        p2 = tf.add_paragraph(); p2.alignment = align
        r = p2.add_run(); r.text = extra
        r.font.size = Pt(size); r.font.bold = bold; r.font.color.rgb = font


def shp(slide, kind, l, t, w, h, text="", fill=BLUE, font=WHITE, size=14,
        bold=True, line=None, align=PP_ALIGN.CENTER):
    sp = slide.shapes.add_shape(kind, Inches(l), Inches(t), Inches(w), Inches(h))
    sp.fill.solid(); sp.fill.fore_color.rgb = fill
    if line is None:
        sp.line.fill.background()
    else:
        sp.line.color.rgb = line; sp.line.width = Pt(1.25)
    sp.shadow.inherit = False
    if text:
        _settext(sp, text, font, size, bold, align)
    return sp


def conn(slide, x1, y1, x2, y2, color=GREY, w=1.75):
    c = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    c.line.color.rgb = color; c.line.width = Pt(w); c.shadow.inherit = False
    return c


# ---------- standard slide scaffolds ----------
def add_title(title, subtitle, footer):
    s = prs.slides.add_slide(BLANK); _bg(s, NAVY)
    _bar(s, AMBER, 0.9, 3.05, 1.6, 0.10)
    tf = _box(s, 0.9, 2.0, 11.5, 1.0); tf.word_wrap = True
    r = tf.paragraphs[0].add_run(); r.text = title
    r.font.size = Pt(40); r.font.bold = True; r.font.color.rgb = WHITE
    tf2 = _box(s, 0.9, 3.25, 11.5, 1.2); tf2.word_wrap = True
    r = tf2.paragraphs[0].add_run(); r.text = subtitle
    r.font.size = Pt(20); r.font.color.rgb = RGBColor(0xCF, 0xDD, 0xEA)
    tf3 = _box(s, 0.9, 6.5, 11.5, 0.6)
    r = tf3.paragraphs[0].add_run(); r.text = footer
    r.font.size = Pt(13); r.font.color.rgb = RGBColor(0x9A, 0xB2, 0xC6)
    return s


def add_divider(kicker, title, notes=""):
    s = prs.slides.add_slide(BLANK); _bg(s, BLUE)
    tfk = _box(s, 0.9, 2.4, 11.5, 0.6)
    r = tfk.paragraphs[0].add_run(); r.text = kicker.upper()
    r.font.size = Pt(15); r.font.bold = True; r.font.color.rgb = RGBColor(0xBF, 0xDC, 0xF2)
    tft = _box(s, 0.9, 3.0, 11.5, 1.6); tft.word_wrap = True
    r = tft.paragraphs[0].add_run(); r.text = title
    r.font.size = Pt(34); r.font.bold = True; r.font.color.rgb = WHITE
    if notes: _notes(s, notes)
    return s


def _header(s, kicker, header, kicker_color=BLUE):
    _bar(s, kicker_color, 0, 0, SW.inches, 0.18)
    tfk = _box(s, 0.7, 0.32, 12.0, 0.45)
    r = tfk.paragraphs[0].add_run(); r.text = kicker.upper()
    r.font.size = Pt(12); r.font.bold = True; r.font.color.rgb = kicker_color
    tfh = _box(s, 0.7, 0.7, 12.0, 1.0); tfh.word_wrap = True
    r = tfh.paragraphs[0].add_run(); r.text = header
    r.font.size = Pt(28); r.font.bold = True; r.font.color.rgb = NAVY


def add_content(header, kicker, blocks, notes="", kicker_color=BLUE, image=None):
    s = prs.slides.add_slide(BLANK); _bg(s, WHITE)
    _header(s, kicker, header, kicker_color)
    txt_w = 6.0 if image else 11.9
    fs0, fs1 = (16, 14) if image else (19, 16)
    tf = _box(s, 0.7, 1.85, txt_w, 5.2); tf.word_wrap = True
    first = True
    for text, level in blocks:
        p = tf.paragraphs[0] if first else tf.add_paragraph(); first = False
        r = p.add_run(); r.text = text
        if level == 0:
            r.font.size = Pt(fs0); r.font.color.rgb = DARK; p.space_after = Pt(7); p.level = 0
        elif level == 1:
            r.font.size = Pt(fs1); r.font.color.rgb = GREY; p.space_after = Pt(3); p.level = 1
        else:
            r.font.size = Pt(fs1); r.font.color.rgb = TEAL; r.font.italic = True
            p.space_after = Pt(5); p.level = 1
    if image:
        path = os.path.join(IMG, image)
        if os.path.exists(path):
            pic = s.shapes.add_picture(path, Inches(6.95), Inches(2.0), width=Inches(6.0))
            band_top, band_h = 1.95, 4.6          # content band (inches; leave room for hook footer)
            h_in = pic.height / 914400.0          # EMU -> inches (all images are landscape, fits)
            pic.top = Inches(band_top + max(0.0, (band_h - h_in) / 2.0))
    # memory-hook footer + exam Q/A in notes (from the per-concept lookup)
    extra = CONCEPT_EXTRAS.get(image) if image else None
    if extra:
        hook, exam_q, exam_a = extra
        _bar(s, TEAL, 0, 6.95, SW.inches, 0.55)
        ftf = _box(s, 0.7, 6.99, 11.9, 0.5)
        p = ftf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        r = p.add_run(); r.text = "💡  Memory hook:  " + hook
        r.font.size = Pt(13); r.font.bold = True; r.font.color.rgb = WHITE
        notes = (notes + "\n\n" if notes else "") + "🎯 Likely exam Q: " + exam_q + "\n   Model answer: " + exam_a
        if image in HYPO:
            notes += "\n\n🔮 Hypothetical (pose to class): " + HYPO[image]
    if notes: _notes(s, notes)
    return s


def add_quiz(title, items, notes=""):
    s = prs.slides.add_slide(BLANK); _bg(s, LIGHT)
    _bar(s, AMBER, 0, 0, SW.inches, 0.18)
    tfk = _box(s, 0.7, 0.32, 12, 0.45)
    r = tfk.paragraphs[0].add_run(); r.text = "CHECK FOR UNDERSTANDING"
    r.font.size = Pt(12); r.font.bold = True; r.font.color.rgb = AMBER
    tfh = _box(s, 0.7, 0.7, 12, 0.9)
    r = tfh.paragraphs[0].add_run(); r.text = title
    r.font.size = Pt(26); r.font.bold = True; r.font.color.rgb = NAVY
    tf = _box(s, 0.7, 1.8, 11.9, 5.2); tf.word_wrap = True
    first = True
    for text, kind in items:
        p = tf.paragraphs[0] if first else tf.add_paragraph(); first = False
        r = p.add_run(); r.text = text
        if kind == "q":
            r.font.size = Pt(18); r.font.bold = True; r.font.color.rgb = NAVY; p.space_before = Pt(8)
        elif kind == "a":
            r.font.size = Pt(16); r.font.color.rgb = TEAL; r.font.bold = True; p.level = 1
        else:
            r.font.size = Pt(16); r.font.color.rgb = DARK; p.level = 1
    if notes: _notes(s, notes)
    return s


def add_activity(title, blocks, notes=""):
    s = prs.slides.add_slide(BLANK); _bg(s, PALET)
    _bar(s, TEAL, 0, 0, SW.inches, 0.18)
    tfk = _box(s, 0.7, 0.32, 12, 0.45)
    r = tfk.paragraphs[0].add_run(); r.text = "🛠  IN-CLASS ACTIVITY"
    r.font.size = Pt(12); r.font.bold = True; r.font.color.rgb = TEAL
    tfh = _box(s, 0.7, 0.7, 12, 0.9)
    r = tfh.paragraphs[0].add_run(); r.text = title
    r.font.size = Pt(26); r.font.bold = True; r.font.color.rgb = NAVY
    tf = _box(s, 0.7, 1.85, 11.9, 5.2); tf.word_wrap = True
    first = True
    for text, level in blocks:
        p = tf.paragraphs[0] if first else tf.add_paragraph(); first = False
        r = p.add_run(); r.text = text
        if level == 0:
            r.font.size = Pt(18); r.font.color.rgb = DARK; p.space_after = Pt(8)
        else:
            r.font.size = Pt(15.5); r.font.color.rgb = GREY; p.space_after = Pt(4); p.level = 1
    if notes: _notes(s, notes)
    return s


def diagram_slide(kicker, header, kicker_color=BLUE):
    s = prs.slides.add_slide(BLANK); _bg(s, WHITE)
    _header(s, kicker, header, kicker_color)
    return s


# =================== DIAGRAMS ===================
def diag_data_ladder():
    s = diagram_slide("S1 · Concept 1  ·  Diagram", "From Data to a Database")
    y, h, w = 3.0, 1.7, 4.3
    xs = [0.7, 4.55, 8.4]
    specs = [("DATA\nraw facts\n9818000000   'Sita'   78", GREY),
             ("INFORMATION\ndata + meaning\n'Sita scored 78 in DBMS'", BLUE),
             ("DATABASE\norganized · persistent · shared\ncollection of related data", TEAL)]
    for x, (txt, col) in zip(xs, specs):
        shp(s, MSO_SHAPE.PENTAGON, x, y, w, h, txt, fill=col, size=15)
    cap = _box(s, 0.7, 5.1, 11.9, 1.0); cap.word_wrap = True
    r = cap.paragraphs[0].add_run()
    r.text = "Add organization + storage and raw facts become a database — the asset every app depends on."
    r.font.size = Pt(15); r.font.italic = True; r.font.color.rgb = GREY
    _notes(s, "Walk left to right. Stress that the SAME facts gain value at each step. The kirana-notebook is a database too — just a fragile one.")


def diag_file_vs_dbms():
    s = diagram_slide("S1 · Concept 5  ·  Comparison", "File System vs DBMS")
    rows = [("File-based System", "DBMS"),
            ("Uncontrolled redundancy", "Controlled redundancy"),
            ("Data inconsistency", "Integrity constraints"),
            ("Hard to share safely", "Concurrent multi-user access"),
            ("Weak / no security", "Access control & permissions"),
            ("A crash can lose data", "Backup & recovery")]
    L, T, W, H = 1.4, 2.0, 10.5, 4.6
    tbl = s.shapes.add_table(len(rows), 2, Inches(L), Inches(T), Inches(W), Inches(H)).table
    tbl.columns[0].width = Inches(W/2); tbl.columns[1].width = Inches(W/2)
    for ri, (a, b) in enumerate(rows):
        for ci, val in enumerate((a, b)):
            cell = tbl.cell(ri, ci)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            cell.margin_left = Inches(0.15); cell.margin_top = Inches(0.04); cell.margin_bottom = Inches(0.04)
            p = cell.text_frame.paragraphs[0]; p.alignment = PP_ALIGN.LEFT if ri else PP_ALIGN.CENTER
            r = p.add_run(); r.text = val
            if ri == 0:
                cell.fill.solid(); cell.fill.fore_color.rgb = (CORAL if ci == 0 else TEAL)
                r.font.color.rgb = WHITE; r.font.bold = True; r.font.size = Pt(17)
            else:
                cell.fill.solid(); cell.fill.fore_color.rgb = (RGBColor(0xFA, 0xEC, 0xE7) if ci == 0 else PALET)
                r.font.color.rgb = DARK; r.font.size = Pt(15)
    _notes(s, "Read each pair: the file-system pain on the left, the DBMS fix on the right. Tie back to the 'address in 5 files' inconsistency example.")


def diag_three_schema():
    s = diagram_slide("S2 · Concept 3  ·  Diagram", "Three-Schema Architecture")
    # External views (top)
    vw = 3.3; vy = 1.95; gap = 0.35; total = 3*vw + 2*gap; x0 = (13.333-total)/2
    views = ["EXTERNAL VIEW\nStudent — own marks",
             "EXTERNAL VIEW\nTeacher — class marks",
             "EXTERNAL VIEW\nAdmin — all records"]
    for i, v in enumerate(views):
        shp(s, MSO_SHAPE.ROUNDED_RECTANGLE, x0 + i*(vw+gap), vy, vw, 0.95, v, fill=BLUE, size=12.5)
    lbl1 = _box(s, 1.0, 3.02, 11.3, 0.3)
    r = lbl1.paragraphs[0].add_run(); r.text = "↕  external / conceptual mapping"
    r.font.size = Pt(11); r.font.italic = True; r.font.color.rgb = GREY
    r.font.color.rgb = GREY; lbl1.paragraphs[0].alignment = PP_ALIGN.CENTER
    # Conceptual band
    cw = 10.2; cx = (13.333-cw)/2
    shp(s, MSO_SHAPE.ROUNDED_RECTANGLE, cx, 3.35, cw, 1.0,
        "CONCEPTUAL SCHEMA\nWhole logical database — all students, subjects & marks", fill=TEAL, size=14)
    lbl2 = _box(s, 1.0, 4.42, 11.3, 0.3)
    r = lbl2.paragraphs[0].add_run(); r.text = "↕  conceptual / internal mapping"
    r.font.size = Pt(11); r.font.italic = True; r.font.color.rgb = GREY
    lbl2.paragraphs[0].alignment = PP_ALIGN.CENTER
    # Internal band
    shp(s, MSO_SHAPE.ROUNDED_RECTANGLE, cx, 4.75, cw, 1.0,
        "INTERNAL SCHEMA\nPhysical storage — files, blocks & indexes", fill=NAVY, size=14)
    # Disk
    shp(s, MSO_SHAPE.CAN, 6.07, 5.95, 1.2, 1.05, "disk", fill=GREY, size=12)
    _notes(s, "Centrepiece of S2. Top = many user views; middle = one logical whole; bottom = physical storage. The mappings between levels are what give data independence.")


def diag_dbms_components():
    s = diagram_slide("S3 · Concept 3  ·  Diagram", "Inside the DBMS")
    cx, cw = 3.7, 4.6
    shp(s, MSO_SHAPE.ROUNDED_RECTANGLE, cx, 1.95, cw, 0.85, "Users / Applications", fill=BLUE, size=15)
    shp(s, MSO_SHAPE.DOWN_ARROW, cx+cw/2-0.18, 2.85, 0.36, 0.4, fill=LGREY)
    shp(s, MSO_SHAPE.ROUNDED_RECTANGLE, cx, 3.3, cw, 0.85, "Query Processor / Optimizer", fill=NAVY, size=15)
    shp(s, MSO_SHAPE.DOWN_ARROW, cx+cw/2-0.18, 4.2, 0.36, 0.4, fill=LGREY)
    shp(s, MSO_SHAPE.ROUNDED_RECTANGLE, cx, 4.65, cw, 0.85, "Storage Manager + Buffer Manager", fill=TEAL, size=14)
    shp(s, MSO_SHAPE.DOWN_ARROW, cx+cw/2-0.18, 5.55, 0.36, 0.4, fill=LGREY)
    shp(s, MSO_SHAPE.CAN, cx+cw/2-0.7, 6.0, 1.4, 1.0, "Database\non disk", fill=GREY, size=12)
    # side boxes
    sx, sw = 9.1, 3.5
    cat = shp(s, MSO_SHAPE.ROUNDED_RECTANGLE, sx, 3.3, sw, 0.85, "Catalog / Metadata", fill=CORAL, size=14)
    txn = shp(s, MSO_SHAPE.ROUNDED_RECTANGLE, sx, 4.65, sw, 0.85, "Transaction Manager (ACID)", fill=AMBER, size=14)
    conn(s, cx+cw, 3.72, sx, 3.72, color=LGREY)
    conn(s, cx+cw, 5.07, sx, 5.07, color=LGREY)
    _notes(s, "Restaurant analogy: waiter = query processor, kitchen = storage manager, manager = transaction manager, receipt book = catalog. Transactions detailed in Unit 6.")


def diag_architectures():
    s = diagram_slide("S4 · Concept 2  ·  Diagram", "Centralized vs Two-tier vs Three-tier")
    cols = [
        (0.7, "Centralized", NAVY, [("Central Machine\nData + DBMS + App", NAVY, 1.4),
                                     ("Terminal (display only)", GREY, 0.7)]),
        (4.75, "Two-tier", BLUE, [("Client\nUI + application logic", BLUE, 1.0),
                                   ("Database Server", TEAL, 0.9)]),
        (8.9, "Three-tier", TEAL, [("Client (UI)", BLUE, 0.8),
                                    ("Application Server\n(business logic)", AMBER, 0.95),
                                    ("Database Server", TEAL, 0.8)]),
    ]
    cw = 3.6
    for x, title, tcol, boxes in cols:
        cap = _box(s, x, 1.85, cw, 0.5)
        r = cap.paragraphs[0].add_run(); r.text = title
        r.font.size = Pt(17); r.font.bold = True; r.font.color.rgb = tcol
        cap.paragraphs[0].alignment = PP_ALIGN.CENTER
        y = 2.5
        for i, (txt, col, h) in enumerate(boxes):
            if i > 0:
                shp(s, MSO_SHAPE.DOWN_ARROW, x+cw/2-0.16, y, 0.32, 0.34, fill=LGREY); y += 0.4
            shp(s, MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, h, txt, fill=col, size=13); y += h
    note = _box(s, 0.7, 6.55, 11.9, 0.6)
    r = note.paragraphs[0].add_run()
    r.text = "Daraz ≈ three-tier:  phone app → application servers → database servers."
    r.font.size = Pt(14); r.font.italic = True; r.font.color.rgb = GREY
    _notes(s, "Left = simple but single point of failure. Right = the modern scalable standard. Use the 'why your phone doesn't hold the full ledger' case.")


def diag_mindmap():
    s = diagram_slide("S4 · Synthesis  ·  Diagram", "Unit 1 — The Whole Picture")
    center = (5.52, 3.25, 2.3, 1.0); ccx, ccy = 5.52+1.15, 3.25+0.5
    branches = [
        (1.1, 1.05, 2.7, 0.85, "Users\n(naive · programmer · DBA)", BLUE),
        (9.5, 1.05, 2.8, 0.85, "Languages & Interfaces\n(DDL/DML/DCL/TCL)", BLUE),
        (0.5, 3.3, 2.6, 0.9, "DBMS Components\n(+ catalog)", TEAL),
        (10.2, 3.3, 2.6, 0.9, "Three-Schema Architecture\n(data independence)", TEAL),
        (5.3, 5.75, 2.75, 0.9, "Deployment Architecture\n(centralized / client-server)", AMBER),
    ]
    for x, y, w, h, _, _c in branches:  # connectors first (behind)
        conn(s, ccx, ccy, x+w/2, y+h/2, color=LGREY, w=2)
    for x, y, w, h, txt, col in branches:
        shp(s, MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h, txt, fill=col, size=12.5)
    shp(s, MSO_SHAPE.OVAL, *center, "DATABASE\nSYSTEM", fill=NAVY, size=16)
    _notes(s, "Integration moment. Point to each branch and ask which session it came from. This is the slide to photograph for revision.")


# =================== BUILD DECK ===================
add_title(
    "Unit 1 — Database Concepts & Architecture",
    "IT 220: Database Management System  ·  BIM 4th Semester",
    "4 lecture hours (S1–S4)  ·  50 min each  ·  Nepal / South Asia context",
)
add_content(
    "Unit 1 — Learning Outcomes", "Overview",
    [("By the end of this unit, you will be able to:", 0),
     ("Define database, DBMS, and the roles around them; explain why a DBMS beats flat files", 1),
     ("Distinguish data models, schemas, and instances", 1),
     ("Explain the three-schema architecture and the two kinds of data independence", 1),
     ("Identify database languages/interfaces and DBMS components", 1),
     ("Compare centralized vs client/server architectures and classify DBMSs", 1)],
    notes="Set expectations: 4 sessions, one outcome cluster each. This unit is the foundation for the whole course.",
)

# ---------------- S1 (50 min: 5 hook + 35 content + 5 CFU + 3 app + 2 summary) ----------------
add_divider("Session 1 · Lecture hour 1", "What is a Database & DBMS?",
            "HOOK [~5 min]: 3 everyday facts — eSewa balance survives a dead phone; exam results survive the holidays; FB feed reloads where you left it. Land: none of it lives 'in the app' — it lives in a DATABASE. Show of hands: 'who checked eSewa/bank balance this week?' That number came out in under a second while thousands read theirs — nobody got the wrong balance. Cold-call: 'reinstall an app — why are you still logged in?' Agenda on board.")
add_content("Data → Information → Database", "S1 · Concept 1  [THEORY]  ·  ~7 min",
    [("Data = raw facts with no context yet:  9818000000,  'Sita',  78  (is 78 a mark? age? temp?)", 0),
     ("Information = data placed in context: 'Sita scored 78 in DBMS' — now 78 means something", 0),
     ("Database = an organized, RELATED collection of data, stored to be accessed/managed/updated", 0),
     ("The test — three properties must hold: persistent · shared · structured", 2),
     ("Global: a bank's account ledger  |  Nepal: TU/PU college exam database", 1)],
    image="s1_data_ladder.png",
    notes="Write DATA·INFORMATION·DATABASE on the board. Ask 'is 78 a mark, age, or house number?' to show data is raw. Three properties = persistent (survives shutdown), shared (many users/apps), structured. Mini case (~90s): a kirana shop's paper notebook IS a database — organized, persistent — but fragile (one reader, fire/tea risk, manual search). 'Hold that notebook — it's the problem the DBMS solves.'")
add_content("DBMS — Database Management System", "S1 · Concept 2  [THEORY]  ·  ~7 min",
    [("DBMS = the SOFTWARE that lets you define, create, query, update & administer databases", 0),
     ("Database = the DATA itself.  DBMS = the program that manages it.  Together = a database system", 2),
     ("'MySQL' is the DBMS (engine); the 'college' database is the data it manages — one engine, many DBs", 1),
     ("Examples: MySQL, MariaDB, PostgreSQL, Oracle, SQL Server", 1),
     ("Misconception: 'Excel is a database' — no real concurrency, integrity, querying at scale, or security", 2),
     ("Analogy: DBMS = librarian, data = books; no librarian = a pile on the floor", 2)],
    image="s1_users_dbms.png",
    notes="Separate the two ideas students confuse ALL semester. Deliver the librarian analogy: the librarian doesn't OWN the books, they MANAGE them — exactly the DBMS-vs-database relationship. Repeat the MySQL line twice. Excel is fine for 200 rows; it breaks at the point a DBMS begins.")
add_content("Database Users & the DBA", "S1 · Concepts 3–4  [EXAMPLE]  ·  ~7 min",
    [("Naive / end users — use ready-made screens (a bank teller)", 0),
     ("Application programmers — build the apps that talk to the DB (core-banking dev)", 0),
     ("Sophisticated users — write their own complex queries (data/MIS analyst)", 0),
     ("DBA — schema design, security/permissions, backups, performance tuning", 0),
     ("Case: exam-result server crawls the night before results — who do you call? The DBA.", 2)],
    image="s1_db_users.png",
    notes="Use ONE Nepali bank to populate all four roles (teller → naive; app team → programmers; risk/MIS → sophisticated; DBA). The DBA is accountable when the data layer misbehaves — make the role feel real and high-stakes.")
add_content("Why a Database beats a File System", "S1 · Concept 5  [THEORY]  ·  ~6 min",
    [("Redundant copies → inconsistency  ⇒  controlled redundancy", 0),
     ("Files out of sync  ⇒  consistency & integrity constraints", 0),
     ("Hard to share safely  ⇒  concurrent multi-user access", 0),
     ("Anyone can open a file  ⇒  security / access control", 0),
     ("A crash loses data  ⇒  backup & recovery", 0),
     ("Misconception: 'more copies = safer.' Uncontrolled redundancy breaks consistency.", 2)],
    image="s1_file_vs_dbms.png",
    notes="Walk the address-in-5-files example: store a student's address in 5 files, update 4, forget 1 — now the data is inconsistent and you can't tell which is right. This single example motivates 'controlled redundancy'.")
add_activity("S1 — 'File or DBMS?'  ·  ~6 min",
    [("Think–Pair–Share (2 min pairs, 4 min sharing)", 0),
     ("Give pairs 4 scenarios: a wedding guest list in Excel; a bank's accounts; a one-person diary; Daraz orders", 1),
     ("For each: file/spreadsheet or a DBMS — and WHICH property (concurrency, integrity, scale, security) decides it?", 1),
     ("Share aloud; build the file-vs-DBMS table from their answers", 1)],
    notes="Anchors the abstract advantages in concrete choices. The bank accounts + Daraz orders clearly need a DBMS (concurrency, integrity, scale); the diary/guest list don't — that contrast IS the lesson.")
add_quiz("S1 — Quick Check  ·  ~5 min",
    [("Q1. Which is NOT a function of a DBMS?", "q"),
     ("a) define data   b) print documents   c) query   d) control access", "o"),
     ("✅ b) Print formatted documents", "a"),
     ("Q2. Who grants/revokes user permissions?", "q"),
     ("✅ c) Database Administrator (DBA)", "a"),
     ("Discussion: name a phone app and guess what its database stores about you.", "o")],
    notes="APPLICATION [~3 min]: every fintech/e-commerce employer in Nepal (eSewa, Khalti, Daraz, IME Pay) runs on a DBMS — 'understands databases' is on almost every software/data/QA job ad. SUMMARY [~2 min]: database = organized shared persistent data; DBMS manages it; beats files on redundancy/integrity/sharing/security/recovery. Next: how we DESCRIBE data — models, schemas, instances.")

# ---------------- S2 ----------------
add_divider("Session 2 · Lecture hour 2", "Models, Schemas & the Three-Schema Architecture",
            "HOOK [~5 min]: last year the college stored results one way; this year IT moved everything to a faster server with a different internal layout. You — checking marks online — noticed NOTHING. That invisibility has a name: data independence. Ask 'why didn't the change break the student portal?' and hold it. Agenda: models → schema vs instance → three-schema → independence.")
add_content("Data Models", "S2 · Concept 1  [THEORY]  ·  ~7 min",
    [("Data model = concepts to describe STRUCTURE + CONSTRAINTS + OPERATIONS of a database", 0),
     ("High-level / conceptual — close to how humans think (the ER model, Unit 2)", 1),
     ("Representational — the relational model (tables)", 1),
     ("Low-level / physical — how data sits on disk (files, indexes)", 1),
     ("Analogy: conceptual = the architect's blueprint; physical = the built house (bricks, wiring)", 2)],
    image="s2_data_models.png",
    notes="Keep it light — models are previewed here, detailed in Unit 2. The takeaway is the IDEA of describing data at different abstraction levels; that sets up the three-schema architecture.")
add_content("Schema vs Instance", "S2 · Concept 2  [THEORY]  ·  ~8 min",
    [("Schema = the DESIGN / structure of the database. Defined once, changes RARELY.", 0),
     ("Instance (state) = the actual DATA at a moment. Changes CONSTANTLY.", 0),
     ("Schema:  Student(roll, name, program)  —  the definition / the mould", 1),
     ("Instance: today's actual 60 students with real roll numbers; tomorrow one drops out → new instance", 1),
     ("Misconception: 'schema and data are the same.' Schema = the mould; instance = what's poured in.", 2)],
    image="s2_schema_instance.png",
    notes="Hammer the mould/poured-in metaphor. Write Student(roll,name,program) on the board, then list 3 fake rows beside it — 'same schema, infinitely many instances over time.' The schema barely changes; the instance changes every enrolment.")
add_content("Three-Schema Architecture", "S2 · Concept 3  [THEORY]  ·  ~9 min",
    [("External level — per-user VIEWS (a student sees only their own marks)", 0),
     ("Conceptual level — the WHOLE logical database (all students, subjects, marks)", 0),
     ("Internal level — how data is PHYSICALLY stored & indexed on disk", 0),
     ("Mappings connect the levels, so each level HIDES detail from the one above", 2)],
    image="s2_three_schema.png",
    notes="This is the centrepiece. Walk the college exam DB through all three: external = student sees own marks; conceptual = the complete exam DB; internal = how it's stored/indexed on disk. The mappings between levels are exactly what give data independence (next concept).")
add_content("Data Independence — the payoff", "S2 · Concept 4  [THEORY]  ·  ~6 min",
    [("Logical data independence: change the CONCEPTUAL schema (add a column/table)…", 0),
     ("   …without changing external views or the apps that use them", 1),
     ("Physical data independence: change STORAGE (move to SSDs, add an index)…", 0),
     ("   …without changing the conceptual schema", 1),
     ("Memory hook: Logical = change the DESIGN safely · Physical = change STORAGE safely", 2)],
    image="s2_data_independence.png",
    notes="Resolve the hook here. Mini case: the admin moves the DB to SSDs + adds an index overnight; next morning every app and user works unchanged = PHYSICAL independence. Logical independence (changing the design without breaking views) is the harder one to achieve.")
add_activity("S2 — 'Draw your college's three schemas'  ·  ~5 min",
    [("In pairs (3 min), then 2 pairs share (2 min)", 0),
     ("For the college result system, write what lives at EACH level:", 1),
     ("External (what does a student see? a teacher? admin?) · Conceptual (the whole DB) · Internal (storage)", 1),
     ("Then: name one change at the internal level that students would NOT notice (data independence)", 1)],
    notes="Cements the architecture by making students place real examples at each level. The 'change students wouldn't notice' prompt directly rehearses physical data independence.")
add_quiz("S2 — Quick Check  ·  ~5 min",
    [("Q1. Adding a column without breaking user views is…", "q"),
     ("✅ a) Logical data independence", "a"),
     ("Q2. Which level is closest to physical storage?", "q"),
     ("✅ c) Internal", "a"),
     ("Discussion: an everyday 'change the inside without changing the outside' example.", "o")],
    notes="APPLICATION [~3 min]: data independence is WHY banks, Ntc/Ncell, and gov portals upgrade storage/infrastructure without rewriting every app — systems lacking it become unmaintainable. SUMMARY [~2 min]: models describe data at 3 levels; schema = structure, instance = current data; three-schema architecture gives logical + physical independence. Next: the languages & interfaces to talk to a DBMS.")

# ---------------- S3 ----------------
add_divider("Session 3 · Lecture hour 3", "Languages, Interfaces & the DBMS Environment",
            "HOOK [~5 min]: there's one language to BUILD a database, another to USE it day-to-day, another to PROTECT it. You've heard of SQL — but SQL is actually several languages wearing one name. Ask 'which SQL keywords have you already seen?' Agenda: languages → interfaces → DBMS components → data dictionary.")
add_content("Database Languages — four jobs", "S3 · Concept 1  [THEORY]  ·  ~8 min",
    [("DDL (Data Definition) — define/alter STRUCTURE (CREATE a Course table)", 0),
     ("DML (Data Manipulation) — query & modify DATA (enrol a student, fetch marks)", 0),
     ("DCL (Data Control) — PERMISSIONS (give a TA read access)", 0),
     ("TCL (Transaction Control) — COMMIT / ROLLBACK transactions (confirm or undo a transfer)", 0),
     ("Misconception: 'SQL is one language.' SQL BUNDLES DDL+DML+DCL+TCL.", 2)],
    image="s3_languages.png",
    notes="Full SQL syntax is Unit 5 — today just the four categories. Mini case (one college): register a new course = DDL; enrol a student = DML; grant a TA view access = DCL; commit the enrolment = TCL. CREATE/SELECT/GRANT/COMMIT — all 'SQL', different jobs.")
add_content("Interfaces to a DBMS", "S3 · Concept 2  [EXAMPLE]  ·  ~7 min",
    [("Menu-based · form-based · GUI · natural language · API / embedded SQL", 0),
     ("Bank teller → form-based screen (guided, safe, no SQL needed)", 1),
     ("Developer → talks to the same DB directly via SQL / an API", 1),
     ("Principle: match the interface to the user", 2)],
    image="s3_interfaces.png",
    notes="Same data, many doors. The teller and the developer touch the SAME database through totally different interfaces matched to their skill/role. Sets up the shopkeeper-interface discussion in the quiz.")
add_content("Inside the DBMS box", "S3 · Concept 3  [THEORY]  ·  ~8 min",
    [("Query processor / optimizer — finds the CHEAPEST way to run a query", 0),
     ("Storage manager — reads/writes data to disk", 0),
     ("Buffer manager — keeps hot data in memory for speed", 0),
     ("Transaction manager — keeps transactions safe (ACID, Unit 6)", 0),
     ("Catalog / metadata — info about the database itself", 0)],
    image="s3_dbms_components.png",
    notes="Restaurant analogy: waiter (query processor decides how to fulfil the order), kitchen (storage manager), manager (transaction manager ensures no half-done order), receipt book (catalog).")
add_content("Data Dictionary / Catalog", "S3 · Concept 4  [THEORY]  ·  ~6 min",
    [("Stores metadata: table names, columns, types, constraints, users, indexes", 0),
     ("'A database about the database'", 2),
     ("Nepal: the system table that knows every table in the college DB", 1),
     ("Line: metadata = data about data (phone book = data; 'sorted by surname' = metadata)", 1)],
    image="s3_data_dictionary.png",
    notes="Keep crisp. When you ask 'what columns does Student have?', the answer comes FROM the catalog. Then run the activity.")
add_activity("S3 — 'Sort the command'  ·  ~6 min",
    [("Rapid-fire as a class (or in pairs), ~6 min", 0),
     ("Show commands one at a time: CREATE TABLE · SELECT · GRANT · DROP · UPDATE · COMMIT · REVOKE · INSERT", 1),
     ("Class calls out DDL / DML / DCL / TCL for each", 1),
     ("Then: 'enrol a student in a new course and make it permanent' — which languages, in order?", 1)],
    notes="Fast, high-energy retrieval practice. The last prompt chains DDL (if creating)→DML (enrol)→TCL (commit), reinforcing that one task touches multiple sub-languages.")
add_quiz("S3 — Quick Check  ·  ~5 min",
    [("Q1. CREATE TABLE belongs to which sub-language?", "q"),
     ("✅ a) DDL", "a"),
     ("Q2. Which component decides the cheapest way to run a query?", "q"),
     ("✅ c) Query processor / optimizer", "a"),
     ("Discussion: which interface would you build for a non-technical shopkeeper, and why?", "o")],
    notes="APPLICATION [~3 min]: knowing DDL/DML/DCL is the literal day-one skill in any backend/data/QA role — 'SQL required' job ads mean exactly these. SUMMARY [~2 min]: DDL/DML/DCL/TCL each have a job (SQL bundles them); many interfaces for many users; a DBMS = cooperating components + a catalog. Next: WHERE the database runs.")

# ---------------- S4 ----------------
add_divider("Session 4 · Lecture hour 4 — CLOSES UNIT 1", "Architectures & Classifying DBMSs",
            "HOOK [~5 min]: results are out, 5,000 students hit refresh in the same 60 seconds. What stops the system collapsing? Architecture — WHERE the database and apps actually run. Agenda: centralized → client/server (2-tier/3-tier) → classification → Unit 1 synthesis.")
add_content("Centralized Architecture", "S4 · Concept 1  [THEORY]  ·  ~7 min",
    [("Data + DBMS + app all on ONE central machine; terminals just display results", 0),
     ("Pro: simple to set up and manage", 1),
     ("Con: SINGLE POINT OF FAILURE — if that machine dies, everything stops; doesn't scale", 2),
     ("Nepal: an old standalone office system — one PC in the corner holds everything", 1)],
    image="s4_centralized.png",
    notes="Set up the contrast with client/server. Emphasise the single point of failure — it's the weakness that motivates everything that follows.")
add_content("Client/Server Architecture", "S4 · Concept 2  [EXAMPLE]  ·  ~9 min",
    [("Two-tier: client (UI + logic) ↔ database server", 0),
     ("Three-tier: client (UI) ↔ application server (business logic) ↔ database server", 0),
     ("Daraz app (client) → app servers (logic/cart/login) → DB servers (products/orders)", 1),
     ("Case: a banking app doesn't store your full ledger on the phone — data lives SERVER-SIDE", 2)],
    image="s4_client_server.png",
    notes="Three-tier is the modern web/mobile standard. The 'why your phone doesn't hold the full ledger' case lands the server-side idea: security, consistency, access from any device.")
add_content("Classification of DBMSs", "S4 · Concept 3  [THEORY]  ·  ~7 min",
    [("By data model: relational, object, object-relational, legacy hierarchical/network, NoSQL", 0),
     ("By number of users: single-user vs multi-user", 0),
     ("By number of sites: centralized vs distributed", 0),
     ("Misconception: 'NoSQL = no SQL / SQL is dead.' It means 'NOT ONLY SQL.'", 2)],
    image="s4_classification.png",
    notes="NoSQL and distributed are previews of Unit 7. Stress that relational still DOMINATES business systems; NoSQL is an additional tool for specific needs (huge scale, flexible schemas).")
add_content("Unit 1 — The whole picture", "S4 · Synthesis  [THEORY]  ·  ~6 min",
    [("Users → Languages/Interfaces → DBMS (components + catalog) →", 0),
     ("…a database described by a schema at 3 levels (data independence) →", 0),
     ("…running on an architecture (centralized / client-server) →", 0),
     ("…classified by model, users, and distribution", 0),
     ("Every branch is one session of this unit — photograph this for revision", 2)],
    image="s4_synthesis.png",
    notes="Walk the mind-map slowly; ask students which session each branch came from. This is the integration moment and the slide to photograph for revision.")
add_activity("S4 — 'Classify a Nepali app'  ·  ~5 min",
    [("In pairs (3 min), then 2 pairs share (2 min)", 0),
     ("Pick a Nepali app (eSewa, Daraz, Nagarik App, a bank app)", 1),
     ("Sketch whether it's two-tier or three-tier and label what lives in each tier", 1),
     ("Then classify its likely DBMS on the 3 axes (model, users, distribution) with a one-line reason", 1)],
    notes="Synthesises the whole session AND the unit. Most modern Nepali apps are three-tier, multi-user, relational (often with some NoSQL) — let pairs justify their guess.")
add_quiz("S4 — Quick Check  ·  ~5 min",
    [("Q1. Main weakness of a purely centralized system?", "q"),
     ("✅ b) Single point of failure", "a"),
     ("Q2. Three-tier adds which layer between client and DB?", "q"),
     ("✅ c) An application / business-logic server", "a"),
     ("Discussion: pick a Nepali app — is it two-tier or three-tier, and why?", "o")],
    notes="APPLICATION [~3 min]: every scalable product (e-commerce, fintech, Nagarik App, gov portals) is client/server, usually three-tier — this frames the rest of the course. SUMMARY [~2 min]: centralized = simple but fragile; client/server (esp. 3-tier) = scalable standard; DBMSs classify by model/users/distribution. Next unit: modelling data with the ER model.")

# ---------------- End-of-unit ----------------
add_divider("Assessment", "Unit 1 — End-of-Unit Quiz",
            "12 MCQ + 5 short answer + 3 applied/diagramming + 1 discussion. Full questions and answer key are in Unit1_material.md.")
add_content("Exam pointers — what to master", "Unit 1 · Review",
    [("Database vs DBMS vs database system — never confuse them", 0),
     ("Schema vs instance; the three-schema architecture (be able to draw it)", 0),
     ("Logical vs physical data independence", 0),
     ("DDL / DML / DCL / TCL with one example command each", 0),
     ("Centralized vs two-tier vs three-tier; the three classification axes", 0)],
    notes="These five lines map to the most common exam questions.")
add_title("End of Unit 1",
          "Next: Unit 2 — Data Modelling with the Entity-Relationship (ER) Model",
          "Generated for IT 220 · diagrams are native shapes (editable) · speaker notes in each slide's Notes pane")

out = "/Users/inventechg1/Desktop/2083_SEM/fourth/IT220_Unit1.pptx"
prs.save(out)
print("Saved", out, "with", len(prs.slides._sldIdLst), "slides")
