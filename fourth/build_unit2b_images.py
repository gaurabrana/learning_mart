#!/usr/bin/env python3
"""Concept diagrams for IT220 Unit 2 — S9–S12 batch (ER diagrams, ternary,
specialization/generalization, ER→table mapping). Chen / EER notation.
License-safe, purpose-built. Output -> fourth/images/
Run: python3 build_unit2b_images.py
"""
import os, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Ellipse, Polygon, FancyArrowPatch, Circle

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

def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=150, bbox_inches="tight",
                facecolor="white", pad_inches=0.15)
    plt.close(fig); print("wrote", name)

def rbox(ax, x, y, w, h, text, fc=BLUE, tc=WHITE, fs=12, round=True, ec="none", bold=True):
    style = "round,pad=0.02,rounding_size=2.2" if round else "square,pad=0.02"
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=style, fc=fc, ec=ec,
                                lw=1.4, mutation_aspect=0.5, zorder=3))
    ax.text(x+w/2, y+h/2, text, ha="center", va="center", color=tc, fontsize=fs,
            fontweight="bold" if bold else "normal", zorder=4)

def entity(ax, cx, cy, w, h, text, weak=False, fc=BLUE, fs=12):
    if weak:
        ax.add_patch(Rectangle((cx-w/2-1.6, cy-h/2-2.6), w+3.2, h+5.2, fc=fc, ec=NAVY, lw=1.4, zorder=2))
    ax.add_patch(Rectangle((cx-w/2, cy-h/2), w, h, fc=fc, ec=(WHITE if weak else "none"),
                           lw=1.6 if weak else 0, zorder=3))
    ax.text(cx, cy, text, ha="center", va="center", color=WHITE, fontsize=fs, fontweight="bold", zorder=4)

def diamond(ax, cx, cy, w, h, text, dbl=False, fc=TEAL, fs=10.5):
    pts = [(cx-w/2, cy), (cx, cy+h/2), (cx+w/2, cy), (cx, cy-h/2)]
    if dbl:
        o = [(cx-w/2-2.2, cy), (cx, cy+h/2+2.2), (cx+w/2+2.2, cy), (cx, cy-h/2-2.2)]
        ax.add_patch(Polygon(o, closed=True, fc=fc, ec=NAVY, lw=1.3, zorder=2))
    ax.add_patch(Polygon(pts, closed=True, fc=fc, ec=(WHITE if dbl else "none"),
                         lw=1.4 if dbl else 0, zorder=3))
    ax.text(cx, cy, text, ha="center", va="center", color=WHITE, fontsize=fs, fontweight="bold", zorder=4)

def oval(ax, cx, cy, w, h, text, dashed=False, dbl=False, key=False, fs=10):
    ec = BLUE; ls = (0, (4, 3)) if dashed else "solid"
    if dbl:
        ax.add_patch(Ellipse((cx, cy), w+4, h+4, fc=PALEB, ec=ec, lw=1.3, zorder=2))
    ax.add_patch(Ellipse((cx, cy), w, h, fc=PALEB, ec=ec, lw=1.4, ls=ls, zorder=3))
    ax.text(cx, cy, text, ha="center", va="center", color=INK, fontsize=fs, zorder=4,
            fontweight="bold" if key else "normal")
    if key:
        tw = 0.62 * w
        ax.plot([cx-tw/2, cx+tw/2], [cy-h*0.26, cy-h*0.26], color=INK, lw=1.3, zorder=5)

def link(ax, x1, y1, x2, y2, dbl=False, color=GREY, lw=1.6):
    if dbl:
        dx, dy = x2-x1, y2-y1; L = math.hypot(dx, dy) or 1
        ox, oy = -dy/L*0.8, dx/L*0.8
        ax.plot([x1+ox, x2+ox], [y1+oy, y2+oy], color=color, lw=lw, zorder=1)
        ax.plot([x1-ox, x2-ox], [y1-oy, y2-oy], color=color, lw=lw, zorder=1)
    else:
        ax.plot([x1, x2], [y1, y2], color=color, lw=lw, zorder=1)

def arrow(ax, x1, y1, x2, y2, color=GREY, lw=2.2):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=16,
                                 color=color, lw=lw, zorder=1))

def caption(ax, text, color=GREY, y=5, fs=11):
    ax.text(50, y, text, ha="center", fontsize=fs, style="italic", color=color)


# ================= S9 =================
def s9_legend():
    fig, ax = canvas(10, 6.4)
    ax.text(50, 96, "Chen / EER notation — one legend", ha="center", color=NAVY, fontsize=13, fontweight="bold")
    def lab(x, y, t): ax.text(x, y, t, ha="left", va="center", color=INK, fontsize=10)
    # left column (short labels so they don't reach the right column)
    entity(ax, 10, 84, 14, 8, "", fc=BLUE); lab(20, 84, "Entity (rectangle)")
    entity(ax, 10, 70, 14, 8, "", weak=True, fc=CORAL); lab(20, 70, "Weak entity (double)")
    oval(ax, 10, 56, 14, 8, ""); lab(20, 56, "Attribute (oval)")
    oval(ax, 10, 42, 14, 8, "", dashed=True); lab(20, 42, "Derived (dashed oval)")
    oval(ax, 10, 28, 14, 8, "", dbl=True); lab(20, 28, "Multivalued (double oval)")
    oval(ax, 10, 14, 14, 8, "id", key=True); lab(20, 14, "Key (underlined)")
    # right column
    diamond(ax, 60, 84, 15, 11, "", fc=TEAL); lab(70, 84, "Relationship (diamond)")
    diamond(ax, 60, 68, 15, 11, "", dbl=True, fc=TEAL); lab(70, 68, "Identifying (double diamond)")
    link(ax, 53, 52, 67, 52); lab(70, 52, "Partial participation (single)")
    link(ax, 53, 38, 67, 38, dbl=True); lab(70, 38, "Total participation (double)")
    ax.text(60, 22, "pkey", ha="center", va="center", color=INK, fontsize=10)
    ax.plot([54, 66], [18.5, 18.5], color=INK, lw=1.2, ls=(0, (3, 2))); lab(70, 20, "Partial key (dashed underline)")
    save(fig, "s9_legend.png")

def s9_naming():
    fig, ax = canvas(10, 4.6)
    rbox(ax, 6, 30, 40, 46, "", fc=PALEC, tc=INK, ec=CORAL)
    ax.text(26, 70, "✗  POOR", ha="center", color=CORAL, fontsize=13, fontweight="bold")
    for i, t in enumerate(["STUDENTS  (plural)", "TBL1 / REL1  (meaningless)", "student_course  (not a verb)"]):
        ax.text(26, 60-i*9, t, ha="center", color=INK, fontsize=10.5)
    rbox(ax, 54, 30, 40, 46, "", fc=PALET, tc=INK, ec=TEAL)
    ax.text(74, 70, "✓  GOOD", ha="center", color=TEAL, fontsize=13, fontweight="bold")
    for i, t in enumerate(["STUDENT  (singular noun)", "ENROLLS / TEACHES  (verb)", "reads as a sentence L→R"]):
        ax.text(74, 60-i*9, t, ha="center", color=INK, fontsize=10.5)
    caption(ax, "Entities = singular nouns · relationships = verbs · names a stakeholder can verify.", y=18)
    save(fig, "s9_naming.png")

def s9_attr_vs_entity():
    fig, ax = canvas(10, 4.8)
    ax.text(50, 92, "Attribute or its own entity?", ha="center", color=NAVY, fontsize=13, fontweight="bold")
    rbox(ax, 30, 70, 40, 12, "Does 'X' have its OWN attributes\nor relationships?", fc=BLUE, fs=10)
    arrow(ax, 40, 68, 24, 54, color=NAVY); arrow(ax, 60, 68, 76, 54, color=NAVY)
    ax.text(20, 58, "NO", ha="center", color=CORAL, fontsize=11, fontweight="bold")
    ax.text(80, 58, "YES", ha="center", color=TEAL, fontsize=11, fontweight="bold")
    rbox(ax, 6, 34, 34, 16, "Model as an\nATTRIBUTE", fc=CORAL, fs=11)
    rbox(ax, 60, 34, 34, 16, "Model as its own\nENTITY", fc=TEAL, fs=11)
    ax.text(23, 24, "e.g. product 'colour'", ha="center", color=GREY, fontsize=9.5)
    ax.text(77, 24, "e.g. Daraz 'CATEGORY'\n(has name, parent, icon…)", ha="center", color=GREY, fontsize=9.5)
    caption(ax, "Over-modelling adds needless complexity — model only what the requirements need.", y=6)
    save(fig, "s9_attr_vs_entity.png")


# ================= S10 =================
def s10_ternary():
    fig, ax = canvas(10, 5.0)
    diamond(ax, 50, 46, 26, 24, "SUPPLIES", fc=TEAL, fs=10)
    entity(ax, 18, 78, 26, 13, "SUPPLIER", fs=11)
    entity(ax, 82, 78, 24, 13, "PART", fs=11)
    entity(ax, 50, 12, 26, 13, "PROJECT", fs=11)
    link(ax, 40, 54, 26, 72); link(ax, 60, 54, 74, 72); link(ax, 50, 34, 50, 18)
    caption(ax, "Ternary (degree 3): 'Supplier S supplies Part P for Project J' — one three-way fact.", y=2)
    save(fig, "s10_ternary.png")

def s10_ternary_vs_binary():
    fig, ax = canvas(10, 4.8)
    entity(ax, 20, 74, 24, 12, "SUPPLIER", fs=10.5)
    entity(ax, 80, 74, 20, 12, "PART", fs=10.5)
    entity(ax, 50, 30, 24, 12, "PROJECT", fs=10.5)
    diamond(ax, 50, 78, 16, 12, "sup?", fc=CORAL, fs=8.5)
    diamond(ax, 32, 50, 16, 12, "works", fc=CORAL, fs=8.5)
    diamond(ax, 68, 50, 16, 12, "uses", fc=CORAL, fs=8.5)
    link(ax, 32, 74, 42, 78); link(ax, 58, 78, 68, 74)
    link(ax, 24, 68, 30, 56); link(ax, 44, 36, 36, 46)
    link(ax, 76, 68, 70, 56); link(ax, 56, 36, 64, 46)
    ax.text(50, 10, "✗  Three binaries can't say WHICH supplier supplied WHICH part TO WHICH project.",
            ha="center", color=CORAL, fontsize=10.5, fontweight="bold")
    save(fig, "s10_ternary_vs_binary.png")

def s10_associative():
    fig, ax = canvas(10, 4.6)
    entity(ax, 16, 74, 24, 12, "CUSTOMER", fs=10)
    entity(ax, 84, 74, 26, 12, "RESTAURANT", fs=9.5)
    entity(ax, 84, 24, 20, 12, "RIDER", fs=10)
    rbox(ax, 38, 42, 24, 16, "DELIVERY", fc=TEAL, fs=12)
    ax.text(50, 34, "(associative entity)", ha="center", color=GREY, fontsize=9, style="italic")
    arrow(ax, 28, 70, 40, 54, color=NAVY); arrow(ax, 72, 70, 60, 54, color=NAVY); arrow(ax, 74, 28, 60, 46, color=NAVY)
    caption(ax, "When a ternary gets its own attributes (time, fee, status) → make it an associative ENTITY.", y=6)
    save(fig, "s10_associative.png")


# ================= S11 =================
def s11_specialization():
    fig, ax = canvas(10, 5.0)
    entity(ax, 50, 82, 30, 13, "EMPLOYEE", fc=NAVY, fs=12)
    ax.add_patch(Circle((50, 60), 5.5, fc=WHITE, ec=NAVY, lw=1.6, zorder=3))
    ax.text(50, 60, "d", ha="center", va="center", color=NAVY, fontsize=12, fontweight="bold", zorder=4)
    link(ax, 50, 75.5, 50, 65.5)
    ax.text(58, 68, "is-a", color=GREY, fontsize=9, style="italic")
    subs = [("ENGINEER", 18), ("SECRETARY", 50), ("TECHNICIAN", 82)]
    for name, x in subs:
        link(ax, 50, 55, x, 40); entity(ax, x, 32, 26, 12, name, fc=TEAL, fs=10)
    caption(ax, "Specialization (top-down) — superclass EMPLOYEE splits into subclasses; 'd' = disjoint.", y=8)
    save(fig, "s11_specialization.png")

def s11_constraints_2x2():
    fig, ax = canvas(10, 5.0)
    ax.text(50, 95, "The 4 combinations", ha="center", color=NAVY, fontsize=13, fontweight="bold")
    ax.text(32, 84, "TOTAL", ha="center", color=BLUE, fontsize=11, fontweight="bold")
    ax.text(72, 84, "PARTIAL", ha="center", color=BLUE, fontsize=11, fontweight="bold")
    ax.text(8, 62, "DISJOINT (d)", ha="center", color=BLUE, fontsize=10, fontweight="bold", rotation=90)
    ax.text(8, 26, "OVERLAP (o)", ha="center", color=BLUE, fontsize=10, fontweight="bold", rotation=90)
    cells = [(16, 52, PALET, "d, total", "every account is\nSAVINGS or CURRENT"),
             (56, 52, PALEB, "d, partial", "employee may be\nneither subclass"),
             (16, 16, PALEA, "o, total", "person is STUDENT\nand/or STAFF (all)"),
             (56, 16, PALEC, "o, partial", "may belong to\nmany, or none")]
    for x, y, c, t1, t2 in cells:
        rbox(ax, x, y, 36, 26, "", fc=c, ec=GREY)
        ax.text(x+18, y+18, t1, ha="center", color=NAVY, fontsize=11, fontweight="bold")
        ax.text(x+18, y+8, t2, ha="center", color=INK, fontsize=9)
    save(fig, "s11_constraints_2x2.png")

def s11_inheritance():
    fig, ax = canvas(10, 4.8)
    rbox(ax, 32, 74, 36, 20, "", fc=NAVY, ec="none")
    ax.text(50, 88, "ACCOUNT", ha="center", color=WHITE, fontsize=12, fontweight="bold")
    ax.text(50, 79, "acc_no, holder, balance", ha="center", color=WHITE, fontsize=9)
    arrow(ax, 42, 72, 24, 50, color=NAVY); arrow(ax, 58, 72, 76, 50, color=NAVY)
    rbox(ax, 4, 26, 40, 22, "", fc=TEAL); ax.text(24, 42, "SAVINGS", ha="center", color=WHITE, fontsize=11, fontweight="bold")
    ax.text(24, 32, "+ interest_rate", ha="center", color=WHITE, fontsize=9.5)
    rbox(ax, 56, 26, 40, 22, "", fc=TEAL); ax.text(76, 42, "CURRENT", ha="center", color=WHITE, fontsize=11, fontweight="bold")
    ax.text(76, 32, "+ overdraft_limit", ha="center", color=WHITE, fontsize=9.5)
    caption(ax, "Each subclass INHERITS the superclass attributes, and adds its own specific ones.", y=10)
    save(fig, "s11_inheritance.png")


# ================= S12 =================
def s12_mapping_table():
    fig, ax = canvas(10, 6.0)
    ax.text(50, 96, "ER construct  →  relational result", ha="center", color=NAVY, fontsize=13, fontweight="bold")
    rows = [("Strong entity", "table + its simple attributes; pick primary key"),
            ("Weak entity", "table incl. owner's PK  (owner PK + partial key)"),
            ("1:1 relationship", "FK on one side (prefer the total side)"),
            ("1:N relationship", "FK on the  N (many)  side"),
            ("M:N relationship", "NEW junction table with both PKs"),
            ("Multivalued attr.", "separate table (entity key + value)"),
            ("n-ary relationship", "table with keys of ALL participants")]
    y = 82
    for i, (a, b) in enumerate(rows):
        c = PALEB if i % 2 == 0 else WHITE
        ax.add_patch(Rectangle((4, y-9.5), 92, 10.5, fc=c, ec=LGREY, lw=0.8, zorder=1))
        ax.text(7, y-4, a, ha="left", va="center", color=NAVY, fontsize=10.5, fontweight="bold")
        ax.text(42, y-4, b, ha="left", va="center", color=INK, fontsize=10)
        y -= 11
    caption(ax, "Composite attrs → flatten to components. Derived attrs → not stored.", y=2)
    save(fig, "s12_mapping_table.png")

def s12_1n_fk():
    fig, ax = canvas(10, 4.4)
    entity(ax, 16, 74, 26, 12, "DEPARTMENT", fs=10)
    diamond(ax, 50, 74, 18, 14, "has", fs=9)
    entity(ax, 84, 74, 24, 12, "EMPLOYEE", fs=10)
    link(ax, 29, 74, 41, 74); link(ax, 59, 74, 72, 74)
    ax.text(35, 84, "1", color=NAVY, fontsize=12, fontweight="bold"); ax.text(66, 84, "N", color=NAVY, fontsize=12, fontweight="bold")
    rbox(ax, 8, 30, 34, 20, "", fc=PALEB, tc=INK, ec=BLUE)
    ax.text(25, 44, "DEPARTMENT", ha="center", color=NAVY, fontsize=10, fontweight="bold")
    ax.text(25, 36, "dept_id (PK), name", ha="center", color=INK, fontsize=9)
    rbox(ax, 54, 30, 40, 20, "", fc=PALET, tc=INK, ec=TEAL)
    ax.text(74, 44, "EMPLOYEE", ha="center", color=NAVY, fontsize=10, fontweight="bold")
    ax.text(74, 36, "emp_id (PK), name, dept_id (FK)", ha="center", color=INK, fontsize=8.5)
    caption(ax, "1:N  →  the foreign key goes on the  N (many)  side (EMPLOYEE gets dept_id).", y=8)
    save(fig, "s12_1n_fk.png")

def s12_junction():
    fig, ax = canvas(10, 4.6)
    entity(ax, 16, 78, 24, 11, "STUDENT", fs=10)
    diamond(ax, 50, 78, 20, 14, "ENROLLS", fc=TEAL, fs=8.5)
    entity(ax, 84, 78, 22, 11, "COURSE", fs=10)
    link(ax, 28, 78, 40, 78); link(ax, 60, 78, 73, 78)
    ax.text(34, 87, "M", color=NAVY, fontsize=11, fontweight="bold"); ax.text(66, 87, "N", color=NAVY, fontsize=11, fontweight="bold")
    rbox(ax, 4, 28, 26, 18, "", fc=PALEB, ec=BLUE)
    ax.text(17, 40, "STUDENT", ha="center", color=NAVY, fontsize=9.5, fontweight="bold"); ax.text(17, 33, "roll_no (PK)", ha="center", color=INK, fontsize=8.5)
    rbox(ax, 37, 28, 26, 18, "", fc=PALEA, ec=AMBER)
    ax.text(50, 40, "ENROLLS", ha="center", color=NAVY, fontsize=9.5, fontweight="bold"); ax.text(50, 32, "roll_no (FK) +\ncourse_id (FK)", ha="center", color=INK, fontsize=8)
    rbox(ax, 70, 28, 26, 18, "", fc=PALET, ec=TEAL)
    ax.text(83, 40, "COURSE", ha="center", color=NAVY, fontsize=9.5, fontweight="bold"); ax.text(83, 33, "course_id (PK)", ha="center", color=INK, fontsize=8.5)
    caption(ax, "M:N  →  a NEW junction table whose PK is the pair of both foreign keys.", y=8)
    save(fig, "s12_junction.png")


for fn in [s9_legend, s9_naming, s9_attr_vs_entity,
           s10_ternary, s10_ternary_vs_binary, s10_associative,
           s11_specialization, s11_constraints_2x2, s11_inheritance,
           s12_mapping_table, s12_1n_fk, s12_junction]:
    fn()
print("\nAll S9-S12 images written to", OUT)
