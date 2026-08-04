#!/usr/bin/env python3
"""Generate custom concept diagrams (PNG) for IT220 Unit 5 — SQL (S22–S36).
Spatial teaching visuals only (comparisons/examples live in native PPTX tables).
Same house style as build_unit1_images.py (canvas/box/arrow/save). MySQL/MariaDB dialect.
Output -> fourth/images/
Run: python3 build_unit5_images.py
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
os.makedirs(OUT, exist_ok=True)

NAVY="#0C2B4A"; BLUE="#185FA5"; TEAL="#0F6E56"; AMBER="#B07A1E"; CORAL="#993C1D"
GREY="#55606B"; LGREY="#C7CFD6"; PALEB="#E6F1FB"; PALET="#E1F5EE"; PALEA="#FAEEDA"
PALEC="#FAECE7"; WHITE="#FFFFFF"; INK="#1A1A1A"

plt.rcParams["font.family"] = "DejaVu Sans"


def canvas(w=10, h=5.6):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")
    return fig, ax


def box(ax, x, y, w, h, text, fc=BLUE, tc=WHITE, fs=12, bold=True, round=True, ec="none", lw=0):
    style = "round,pad=0.02,rounding_size=2.2" if round else "square,pad=0.02"
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=style, fc=fc, ec=ec, lw=lw,
                                mutation_aspect=0.5, zorder=2))
    ax.text(x + w/2, y + h/2, text, ha="center", va="center", color=tc,
            fontsize=fs, fontweight="bold" if bold else "normal", zorder=3, wrap=True)


def arrow(ax, x1, y1, x2, y2, color=GREY, lw=2.2, style="-|>"):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style, mutation_scale=16,
                                 color=color, lw=lw, zorder=1))


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=150, bbox_inches="tight",
                facecolor="white", pad_inches=0.15)
    plt.close(fig)
    print("wrote", name)


# ---------- S22 · the running college-DB schema ----------
def schema():
    fig, ax = canvas(10, 5.8)
    box(ax, 4, 74, 30, 20, "Student\nroll (PK) · name · program\nsemester · dob · email", fc=BLUE, fs=9.5)
    box(ax, 66, 74, 30, 20, "Course\ncourse_id (PK) · title\ncredits · dept", fc=BLUE, fs=9.5)
    box(ax, 35, 42, 30, 22, "Enrollment\nroll (FK) · course_id (FK)\nsem · grade · marks\nPK(roll, course_id, sem)", fc=TEAL, fs=9)
    box(ax, 66, 42, 30, 20, "Instructor\ninst_id (PK) · name\ndept · salary", fc=BLUE, fs=9.5)
    box(ax, 35, 10, 30, 18, "Teaches\ninst_id (FK) · course_id (FK)\nsem", fc=TEAL, fs=9)
    arrow(ax, 34, 78, 50, 64, color=CORAL, lw=1.8)      # Student -> Enrollment
    arrow(ax, 76, 74, 60, 64, color=CORAL, lw=1.8)      # Course -> Enrollment
    arrow(ax, 81, 42, 62, 28, color=CORAL, lw=1.8)      # Instructor -> Teaches
    arrow(ax, 66, 52, 56, 28, color=CORAL, lw=1.8)      # Course -> Teaches
    ax.text(50, 2, "The running example for every session (S22–S36). Red arrows = foreign keys.",
            ha="center", fontsize=10, style="italic", color=GREY)
    save(fig, "s22_schema.png")


# ---------- S23 · SELECT/FROM/WHERE flow ----------
def query_flow():
    fig, ax = canvas(10, 4.6)
    box(ax, 4, 40, 24, 22, "FROM\nStudent\n(which table)", fc=NAVY, fs=11)
    box(ax, 38, 40, 24, 22, "WHERE\nprogram='BIM'\n(which ROWS)", fc=CORAL, fs=11)
    box(ax, 72, 40, 24, 22, "SELECT\nname, program\n(which COLUMNS)", fc=TEAL, fs=11)
    arrow(ax, 28, 51, 38, 51, color=GREY, lw=2.6)
    arrow(ax, 62, 51, 72, 51, color=GREY, lw=2.6)
    ax.text(50, 80, "SQL is written SELECT-first, but read it FROM → WHERE → SELECT.",
            ha="center", fontsize=11.5, fontweight="bold", color=NAVY)
    ax.text(16, 30, "pick the table", ha="center", fontsize=9.5, color=GREY)
    ax.text(50, 30, "keep matching rows", ha="center", fontsize=9.5, color=GREY)
    ax.text(84, 30, "keep chosen columns", ha="center", fontsize=9.5, color=GREY)
    ax.text(50, 12, "WHERE filters ROWS · SELECT projects COLUMNS — two different jobs.",
            ha="center", fontsize=10.5, style="italic", color=CORAL)
    save(fig, "s23_query_flow.png")


# ---------- S24 · self-join ----------
def selfjoin():
    fig, ax = canvas(10, 4.8)
    box(ax, 6, 55, 34, 26, "Student  s1\n101 Sita  BIM\n102 Hari  BIM\n103 Gita  BCA", fc=BLUE, fs=10)
    box(ax, 60, 55, 34, 26, "Student  s2\n101 Sita  BIM\n102 Hari  BIM\n103 Gita  BCA", fc=TEAL, fs=10)
    arrow(ax, 40, 68, 60, 68, color=CORAL, lw=2.2, style="<->")
    ax.text(50, 74, "same table,\ntwo aliases", ha="center", fontsize=9.5, color=CORAL, fontweight="bold")
    box(ax, 20, 20, 60, 20, "WHERE s1.program = s2.program\nAND s1.roll <> s2.roll\n→ classmates: (Sita, Hari)", fc=NAVY, fs=10.5)
    ax.text(50, 8, "Tuple variables (s1, s2) let one table be joined to itself.",
            ha="center", fontsize=10.5, style="italic", color=GREY)
    save(fig, "s24_selfjoin.png")


# ---------- S25 · set-operation Venns ----------
def setops():
    fig, ax = canvas(10, 4.2)
    def pair(cx, title, mode):
        r = 9
        a = Circle((cx-5, 55), r, fc=PALEB, ec=BLUE, lw=1.8, zorder=1)
        b = Circle((cx+5, 55), r, fc=PALET, ec=TEAL, lw=1.8, zorder=1)
        ax.add_patch(a); ax.add_patch(b)
        # highlight
        if mode == "union":
            ax.add_patch(Circle((cx-5, 55), r, fc=AMBER, ec="none", alpha=0.35, zorder=2))
            ax.add_patch(Circle((cx+5, 55), r, fc=AMBER, ec="none", alpha=0.35, zorder=2))
        elif mode == "inter":
            ax.add_patch(Circle((cx, 55), 4.6, fc=AMBER, ec="none", alpha=0.6, zorder=3))
        elif mode == "except":
            ax.add_patch(Circle((cx-5, 55), r, fc=AMBER, ec="none", alpha=0.35, zorder=2))
            ax.add_patch(Circle((cx+5, 55), r, fc=WHITE, ec="none", alpha=1.0, zorder=3))
            ax.add_patch(Circle((cx+5, 55), r, fc=PALET, ec=TEAL, lw=1.8, alpha=0.4, zorder=3))
        ax.text(cx, 40, title, ha="center", fontsize=11, fontweight="bold", color=NAVY)
    pair(18, "UNION\nA ∪ B (all)", "union")
    pair(50, "INTERSECT\nA ∩ B (both)", "inter")
    pair(82, "EXCEPT\nA − B (only A)", "except")
    ax.text(50, 82, "Set operations combine two union-compatible result sets (A = one query, B = another).",
            ha="center", fontsize=10.5, fontweight="bold", color=NAVY)
    ax.text(50, 26, "UNION removes duplicates · UNION ALL keeps them.",
            ha="center", fontsize=10, style="italic", color=CORAL)
    save(fig, "s25_setops.png")


# ---------- S26 · GROUP BY collapse + WHERE/HAVING ----------
def groupby():
    fig, ax = canvas(10, 5.2)
    ax.text(50, 94, "GROUP BY collapses many rows into one row per group.",
            ha="center", fontsize=11, fontweight="bold", color=NAVY)
    rows = ["IT dept  60000", "IT dept  80000", "MGT dept 50000", "MGT dept 70000", "IT dept  90000"]
    for i, r in enumerate(rows):
        box(ax, 6, 74 - i*8, 30, 6.5, r, fc=PALEB, tc=INK, fs=9, bold=False, ec=BLUE, lw=0.8)
    arrow(ax, 38, 55, 52, 55, color=GREY, lw=2.6)
    ax.text(45, 61, "GROUP BY dept", ha="center", fontsize=9, color=TEAL, fontweight="bold")
    box(ax, 54, 62, 40, 8, "IT   → AVG(salary)=76666", fc=TEAL, fs=9.5)
    box(ax, 54, 50, 40, 8, "MGT  → AVG(salary)=60000", fc=TEAL, fs=9.5)
    # pipeline placement
    box(ax, 6, 20, 20, 12, "WHERE\nfilters ROWS\n(before groups)", fc=CORAL, fs=9)
    box(ax, 30, 20, 20, 12, "GROUP BY\nmakes groups", fc=NAVY, fs=9)
    box(ax, 54, 20, 20, 12, "HAVING\nfilters GROUPS\n(after)", fc=AMBER, fs=9)
    arrow(ax, 26, 26, 30, 26, color=GREY, lw=2); arrow(ax, 50, 26, 54, 26, color=GREY, lw=2)
    ax.text(50, 10, "WHERE = bouncer at the door (per row) · HAVING = inspector of each seated group.",
            ha="center", fontsize=10, style="italic", color=GREY)
    save(fig, "s26_groupby.png")


# ---------- S27 · three-valued logic truth grid ----------
def three_valued():
    fig, ax = canvas(10, 5.0)
    ax.text(50, 95, "Any comparison with NULL → UNKNOWN. WHERE keeps only TRUE rows.",
            ha="center", fontsize=11, fontweight="bold", color=NAVY)
    # AND table
    def grid(x0, title, data):
        ax.text(x0+21, 82, title, ha="center", fontsize=11, fontweight="bold", color=BLUE)
        heads = ["", "T", "F", "U"]
        for j, h in enumerate(heads):
            box(ax, x0 + j*10.5, 70, 10, 8, h, fc=NAVY, fs=9.5)
        rows = ["T", "F", "U"]
        for i, rlab in enumerate(rows):
            box(ax, x0, 61 - i*9, 10, 8, rlab, fc=NAVY, fs=9.5)
            for j, val in enumerate(data[i]):
                c = TEAL if val == "T" else (CORAL if val == "F" else GREY)
                box(ax, x0 + (j+1)*10.5, 61 - i*9, 10, 8, val, fc=c, fs=9.5)
    grid(4, "AND", [["T","F","U"],["F","F","F"],["U","F","U"]])
    grid(54, "OR", [["T","T","T"],["T","F","U"],["T","U","U"]])
    ax.text(50, 12, "T = TRUE · F = FALSE · U = UNKNOWN.   Use  IS NULL / IS NOT NULL — never = NULL.",
            ha="center", fontsize=10.5, style="italic", color=CORAL)
    save(fig, "s27_three_valued.png")


# ---------- S28 · subquery nesting ----------
def subquery():
    fig, ax = canvas(10, 4.8)
    box(ax, 6, 12, 88, 76, "", fc=PALEB, ec=BLUE, lw=1.8, tc=INK)
    ax.text(50, 82, "OUTER query", ha="center", fontsize=12, fontweight="bold", color=BLUE)
    ax.text(50, 74, "SELECT name FROM Student WHERE roll IN (", ha="center", fontsize=10.5,
            color=INK, family="monospace")
    box(ax, 18, 34, 64, 30, "", fc=PALET, ec=TEAL, lw=1.6, tc=INK)
    ax.text(50, 58, "INNER subquery (runs FIRST)", ha="center", fontsize=11, fontweight="bold", color=TEAL)
    ax.text(50, 48, "SELECT roll FROM Enrollment\nWHERE course_id='IT220'", ha="center", fontsize=10,
            color=INK, family="monospace")
    ax.text(50, 40, "→ {101, 102, 105}", ha="center", fontsize=10, color=CORAL, fontweight="bold")
    ax.text(50, 27, ")", ha="center", fontsize=11, color=INK, family="monospace")
    arrow(ax, 50, 34, 50, 24, color=CORAL, lw=2.2)
    ax.text(64, 29, "inner result feeds the outer WHERE", ha="left", fontsize=9, style="italic", color=GREY)
    save(fig, "s28_subquery.png")


# ---------- S29 · correlated subquery loop ----------
def correlated():
    fig, ax = canvas(10, 4.6)
    box(ax, 6, 40, 40, 34, "OUTER row\nStudent s\n(roll = 101)", fc=BLUE, fs=11)
    box(ax, 54, 40, 40, 34, "EXISTS ( SELECT *\nFROM Enrollment e\nWHERE e.roll = s.roll )", fc=TEAL, fs=10)
    arrow(ax, 46, 64, 54, 64, color=CORAL, lw=2.2)
    ax.text(50, 70, "s.roll passed IN", ha="center", fontsize=9, color=CORAL, fontweight="bold")
    arrow(ax, 54, 48, 46, 48, color=NAVY, lw=2.2)
    ax.text(50, 42, "TRUE if ≥1 row found", ha="center", fontsize=9, color=NAVY, fontweight="bold")
    ax.text(50, 88, "Correlated subquery: the inner query re-runs for EACH outer row, using its values.",
            ha="center", fontsize=10.5, fontweight="bold", color=NAVY)
    ax.text(50, 24, "EXISTS only checks 'is there any row?' — SELECT * or SELECT 1 are equivalent.",
            ha="center", fontsize=10, style="italic", color=GREY)
    save(fig, "s29_correlated.png")


# ---------- S30 · view = window into base tables ----------
def view_window():
    fig, ax = canvas(10, 4.8)
    box(ax, 6, 20, 30, 30, "Student\n(base table)", fc=NAVY, fs=10.5)
    box(ax, 6, 54, 30, 26, "Enrollment\n(base table)", fc=NAVY, fs=10.5)
    box(ax, 62, 34, 32, 34, "MeritList\n(VIEW)\nsaved query —\nstores no data", fc=TEAL, fs=10.5)
    arrow(ax, 36, 60, 62, 55, color=BLUE, lw=2); arrow(ax, 36, 34, 62, 45, color=BLUE, lw=2)
    ax.text(49, 24, "re-runs the join\neach time you query it", ha="center", fontsize=9, style="italic", color=GREY)
    ax.text(50, 90, "A view is a WINDOW into base tables — you see through it, you don't copy the data.",
            ha="center", fontsize=10.5, fontweight="bold", color=NAVY)
    save(fig, "s30_view.png")


# ---------- S32 · view-updatability decision tree ----------
def updatable():
    fig, ax = canvas(10, 5.2)
    box(ax, 34, 84, 32, 12, "Is this view\nupdatable?", fc=NAVY, fs=11)
    box(ax, 34, 60, 32, 14, "Single base table?\nNo GROUP BY / aggregate?\nNo DISTINCT / derived cols?", fc=BLUE, fs=8.8)
    arrow(ax, 50, 84, 50, 74, color=GREY, lw=2)
    box(ax, 8, 30, 34, 16, "UPDATABLE\nsimple filter/subset view\n(e.g. BIMStudents)", fc=TEAL, fs=9.5)
    box(ax, 58, 30, 34, 16, "NOT updatable\njoin / GROUP BY / aggregate\n(e.g. DeptAvgSalary)", fc=CORAL, fs=9.5)
    arrow(ax, 42, 60, 25, 46, color=TEAL, lw=2); ax.text(30, 54, "YES", fontsize=9, color=TEAL, fontweight="bold")
    arrow(ax, 58, 60, 75, 46, color=CORAL, lw=2); ax.text(66, 54, "NO", fontsize=9, color=CORAL, fontweight="bold")
    ax.text(50, 18, "You can't 'un-bake the cake': an aggregate view can't be pushed back to individual rows.",
            ha="center", fontsize=10, style="italic", color=GREY)
    save(fig, "s32_updatable.png")


# ---------- S33 · the four JOIN Venns ----------
def joins():
    fig, ax = canvas(10, 4.4)
    def venn(cx, title, mode):
        r = 8
        ax.add_patch(Circle((cx-4.5, 58), r, fc=PALEB, ec=BLUE, lw=1.6, zorder=1))
        ax.add_patch(Circle((cx+4.5, 58), r, fc=PALET, ec=TEAL, lw=1.6, zorder=1))
        if mode in ("inner", "left", "full"):
            ax.add_patch(Circle((cx, 58), 3.8, fc=AMBER, ec="none", alpha=0.6, zorder=3))
        if mode in ("left", "full"):
            ax.add_patch(Circle((cx-4.5, 58), r, fc=AMBER, ec="none", alpha=0.32, zorder=2))
        if mode in ("right", "full"):
            ax.add_patch(Circle((cx+4.5, 58), r, fc=AMBER, ec="none", alpha=0.32, zorder=2))
        ax.text(cx-6.5, 70, "L", fontsize=9, color=BLUE, fontweight="bold")
        ax.text(cx+6, 70, "R", fontsize=9, color=TEAL, fontweight="bold")
        ax.text(cx, 44, title, ha="center", fontsize=10, fontweight="bold", color=NAVY)
    venn(15, "INNER\nmatches only", "inner")
    venn(38, "LEFT\nall L + matches", "left")
    venn(62, "RIGHT\nall R + matches", "right")
    venn(85, "FULL\neverything", "full")
    ax.text(50, 84, "JOIN types differ only in which unmatched rows they KEEP (filled = kept).",
            ha="center", fontsize=10.5, fontweight="bold", color=NAVY)
    ax.text(50, 32, "Unmatched rows kept by an OUTER join get NULLs on the missing side.",
            ha="center", fontsize=10, style="italic", color=GREY)
    save(fig, "s33_joins.png")


# ---------- S34 · stored-procedure sequence ----------
def procedure():
    fig, ax = canvas(10, 4.4)
    box(ax, 4, 46, 24, 18, "App\nCALL enroll(101,'IT220')", fc=BLUE, fs=9.5)
    box(ax, 38, 40, 26, 30, "DATABASE SERVER\nprocedure enroll()\nruns MANY statements", fc=NAVY, fs=9.5)
    box(ax, 74, 66, 22, 12, "check seats", fc=TEAL, tc=WHITE, fs=9)
    box(ax, 74, 50, 22, 12, "INSERT row", fc=TEAL, tc=WHITE, fs=9)
    box(ax, 74, 34, 22, 12, "UPDATE count", fc=TEAL, tc=WHITE, fs=9)
    arrow(ax, 28, 55, 38, 55, color=CORAL, lw=2.4)
    ax.text(33, 60, "one call", ha="center", fontsize=8.5, color=CORAL, fontweight="bold")
    for y in (72, 56, 40):
        arrow(ax, 64, 55, 74, y, color=LGREY, lw=1.6, style="-")
    ax.text(50, 88, "One CALL runs a stored block of many statements ON the server (one round-trip).",
            ha="center", fontsize=10.5, fontweight="bold", color=NAVY)
    ax.text(50, 22, "A saved recipe the kitchen runs on order — vs you dictating every step each time.",
            ha="center", fontsize=10, style="italic", color=GREY)
    save(fig, "s34_procedure.png")


# ---------- S35 · trigger event timeline ----------
def trigger():
    fig, ax = canvas(10, 4.2)
    box(ax, 4, 50, 20, 16, "UPDATE\non Enrollment\n(the event)", fc=BLUE, fs=9)
    box(ax, 30, 50, 18, 16, "BEFORE\ntrigger\n(optional)", fc=AMBER, fs=9)
    box(ax, 54, 50, 18, 16, "the row\nchanges", fc=NAVY, fs=9)
    box(ax, 78, 50, 18, 16, "AFTER\ntrigger fires\nauto-log", fc=TEAL, fs=9)
    for x1, x2 in ((24, 30), (48, 54), (72, 78)):
        arrow(ax, x1, 58, x2, 58, color=GREY, lw=2.2)
    ax.text(50, 82, "A trigger fires AUTOMATICALLY on INSERT/UPDATE/DELETE — you never CALL it.",
            ha="center", fontsize=10.5, fontweight="bold", color=NAVY)
    ax.text(50, 34, "OLD.grade → NEW.grade written to GradeAudit(...) with NOW() — an integrity trail.",
            ha="center", fontsize=10, style="italic", color=GREY)
    save(fig, "s35_trigger.png")


# ---------- S35 · table scan vs index lookup ----------
def index():
    fig, ax = canvas(10, 4.6)
    ax.text(25, 92, "No index → full table scan", ha="center", fontsize=10.5, fontweight="bold", color=CORAL)
    for i in range(6):
        box(ax, 6 + (i % 3)*14, 66 - (i//3)*11, 12, 8, "row", fc=PALEC, tc=INK, fs=8, bold=False, ec=CORAL, lw=0.8)
    ax.text(25, 40, "read EVERY row\n(slow on millions)", ha="center", fontsize=9, color=GREY)
    ax.text(75, 92, "With index → B-tree lookup", ha="center", fontsize=10.5, fontweight="bold", color=TEAL)
    box(ax, 68, 66, 16, 9, "root", fc=TEAL, fs=8.5)
    box(ax, 60, 52, 12, 8, "< M", fc=PALET, tc=INK, fs=8, bold=False, ec=TEAL, lw=0.8)
    box(ax, 80, 52, 12, 8, "≥ M", fc=PALET, tc=INK, fs=8, bold=False, ec=TEAL, lw=0.8)
    box(ax, 72, 38, 14, 8, "roll 101", fc=AMBER, fs=8.5)
    arrow(ax, 74, 66, 66, 60, color=TEAL, lw=1.6); arrow(ax, 78, 66, 86, 60, color=TEAL, lw=1.6)
    arrow(ax, 86, 52, 79, 46, color=TEAL, lw=1.6)
    ax.text(75, 30, "jump straight to the row\n(few hops)", ha="center", fontsize=9, color=GREY)
    ax.text(50, 14, "Index = the alphabetical index at the back of a textbook. Speeds reads; slows writes.",
            ha="center", fontsize=10, style="italic", color=NAVY)
    save(fig, "s35_index.png")


# ---------- S36 · full clause execution pipeline ----------
def pipeline():
    fig, ax = canvas(10, 4.6)
    stages = [("FROM", "tables + joins", NAVY),
              ("WHERE", "filter rows", CORAL),
              ("GROUP BY", "make groups", BLUE),
              ("HAVING", "filter groups", AMBER),
              ("SELECT", "pick columns", TEAL),
              ("ORDER BY", "sort output", GREY)]
    x = 2
    for i, (head, sub, c) in enumerate(stages):
        box(ax, x, 44, 14.5, 22, "", fc=c)
        ax.text(x+7.2, 58, head, ha="center", color=WHITE, fontsize=10, fontweight="bold")
        ax.text(x+7.2, 49, sub, ha="center", color=WHITE, fontsize=7.8)
        if i < 5:
            arrow(ax, x+14.5, 55, x+16, 55, color=NAVY, lw=2)
        x += 16
    ax.text(50, 82, "Logical execution ORDER — not the order you write it in.",
            ha="center", fontsize=11.5, fontweight="bold", color=NAVY)
    ax.text(50, 26, "You WRITE SELECT first, but the engine RUNS FROM first and SELECT almost last.",
            ha="center", fontsize=10.5, style="italic", color=CORAL)
    save(fig, "s36_pipeline.png")


for fn in [schema, query_flow, selfjoin, setops, groupby, three_valued,
           subquery, correlated, view_window, updatable, joins,
           procedure, trigger, index, pipeline]:
    fn()

print("\nAll images written to", OUT)
