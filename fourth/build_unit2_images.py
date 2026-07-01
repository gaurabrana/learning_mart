#!/usr/bin/env python3
"""Custom concept diagrams for IT220 Unit 2 (ER modelling, Chen notation).
License-safe, purpose-built. Output -> fourth/images/  (S5–S8 batch)
Run: python3 build_unit2_images.py
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Ellipse, Polygon, FancyArrowPatch

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
os.makedirs(OUT, exist_ok=True)

NAVY="#0C2B4A"; BLUE="#185FA5"; TEAL="#0F6E56"; AMBER="#B07A1E"; CORAL="#993C1D"
GREY="#55606B"; LGREY="#C7CFD6"; PALEB="#E6F1FB"; PALET="#E1F5EE"; PALEA="#FAEEDA"
WHITE="#FFFFFF"; INK="#1A1A1A"
plt.rcParams["font.family"] = "DejaVu Sans"


def canvas(w=10, h=5.6):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")
    return fig, ax


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=150, bbox_inches="tight",
                facecolor="white", pad_inches=0.15)
    plt.close(fig); print("wrote", name)


def rbox(ax, x, y, w, h, text, fc=BLUE, tc=WHITE, fs=12, round=True, ec="none"):
    style = "round,pad=0.02,rounding_size=2.2" if round else "square,pad=0.02"
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=style, fc=fc, ec=ec,
                                lw=1.4, mutation_aspect=0.5, zorder=3))
    ax.text(x+w/2, y+h/2, text, ha="center", va="center", color=tc, fontsize=fs,
            fontweight="bold", zorder=4)


# ---- Chen primitives ----
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
        import math
        dx, dy = x2-x1, y2-y1
        L = math.hypot(dx, dy) or 1
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


# ================= S5 =================
def s5_what_vs_how():
    fig, ax = canvas(10, 4.8)
    rbox(ax, 6, 40, 40, 34, "", fc=PALEB, tc=INK, ec=BLUE)
    ax.text(26, 66, "CONCEPTUAL — the WHAT", ha="center", color=BLUE, fontsize=13, fontweight="bold")
    for i, t in enumerate(["'A Customer places Orders'", "boxes, lines, plain words", "no DBMS chosen yet"]):
        ax.text(26, 57-i*7, "• "+t, ha="center", color=INK, fontsize=10.5)
    rbox(ax, 54, 40, 40, 34, "", fc=PALET, tc=INK, ec=TEAL)
    ax.text(74, 66, "PHYSICAL — the HOW", ha="center", color=TEAL, fontsize=13, fontweight="bold")
    for i, t in enumerate(["CREATE TABLE, indexes", "files & storage on disk", "MySQL / Oracle specifics"]):
        ax.text(74, 57-i*7, "• "+t, ha="center", color=INK, fontsize=10.5)
    arrow(ax, 46, 57, 54, 57, color=NAVY, lw=2.4)
    caption(ax, "Model the WHAT first (ER), decide the HOW later — like a floor plan before bricks.", y=22)
    save(fig, "s5_what_vs_how.png")


def s5_design_pipeline():
    fig, ax = canvas(10, 4.4)
    steps = [("Requirements", "collection\n& analysis", GREY),
             ("Conceptual", "design → ER\ndiagram", BLUE),
             ("Logical", "map to\nrelational tables", TEAL),
             ("Physical", "storage,\nindexes", NAVY)]
    x = 3; w = 21
    for i, (h, s, c) in enumerate(steps):
        rbox(ax, x, 40, w, 30, "", fc=c)
        ax.text(x+w/2, 60, h, ha="center", color=WHITE, fontsize=12.5, fontweight="bold")
        ax.text(x+w/2, 49, s, ha="center", color=WHITE, fontsize=9.5)
        if i < 3:
            arrow(ax, x+w, 55, x+w+3.5, 55, color=NAVY, lw=2.4)
        x += w+3.5
    caption(ax, "Each stage feeds the next. ER sits at 'conceptual'; ER→tables (S12) is 'logical'.", y=24)
    save(fig, "s5_design_pipeline.png")


def s5_data_vs_functional():
    fig, ax = canvas(10, 4.6)
    rbox(ax, 6, 30, 40, 44, "", fc=PALEB, tc=INK, ec=BLUE)
    ax.text(26, 68, "DATA requirements", ha="center", color=BLUE, fontsize=13, fontweight="bold")
    ax.text(26, 61, "WHAT to store", ha="center", color=GREY, fontsize=10, style="italic")
    for i, t in enumerate(["Users, accounts", "Transactions", "Balances"]):
        ax.text(26, 52-i*7, "• "+t, ha="center", color=INK, fontsize=10.5)
    rbox(ax, 54, 30, 40, 44, "", fc=PALET, tc=INK, ec=TEAL)
    ax.text(74, 68, "FUNCTIONAL requirements", ha="center", color=TEAL, fontsize=13, fontweight="bold")
    ax.text(74, 61, "WHAT it must DO", ha="center", color=GREY, fontsize=10, style="italic")
    for i, t in enumerate(["'Send money'", "'View statement'", "'Top-up wallet'"]):
        ax.text(74, 52-i*7, "• "+t, ha="center", color=INK, fontsize=10.5)
    caption(ax, "Khalti example — capture BOTH the data and the operations, or you rebuild later.", y=20)
    save(fig, "s5_data_vs_functional.png")


# ================= S6 =================
def s6_type_vs_set():
    fig, ax = canvas(10, 4.8)
    entity(ax, 22, 60, 30, 14, "STUDENT", fc=BLUE, fs=14)
    ax.text(22, 76, "Entity TYPE (design-time)", ha="center", color=BLUE, fontsize=11, fontweight="bold")
    arrow(ax, 40, 55, 52, 45, color=GREY, lw=2)
    ax.text(78, 76, "Entity SET (instance-time)", ha="center", color=TEAL, fontsize=11, fontweight="bold")
    rows = ["101  Sita   BIM", "102  Hari   BIM", "103  Gita   BIM"]
    for i, r in enumerate(rows):
        rbox(ax, 56, 56-i*13, 40, 11, r, fc=PALET, tc=INK, ec=TEAL, fs=11)
    caption(ax, "One entity type (the category) → an entity set = all its members right now.", y=8)
    save(fig, "s6_type_vs_set.png")


def s6_attributes():
    fig, ax = canvas(10, 6.2)
    entity(ax, 50, 50, 24, 12, "STUDENT", fc=BLUE, fs=13)
    # key
    oval(ax, 16, 78, 22, 12, "roll_no", key=True); link(ax, 27, 74, 42, 55)
    # derived
    oval(ax, 84, 78, 20, 12, "age", dashed=True); link(ax, 74, 74, 60, 55)
    # multivalued
    oval(ax, 88, 46, 22, 12, "phone", dbl=True); link(ax, 76, 47, 62, 49)
    # composite name with children
    oval(ax, 16, 46, 22, 12, "name"); link(ax, 27, 46, 38, 49)
    for i, sub in enumerate(["first", "middle", "last"]):
        oval(ax, 6+i*13, 24, 12, 9, sub, fs=8.5); link(ax, 6+i*13, 28.5, 16, 40)
    # composite address
    oval(ax, 50, 22, 22, 11, "address"); link(ax, 50, 44, 50, 27.5)
    caption(ax, "Chen ovals: underline=key · dashed=derived · double=multivalued · sub-ovals=composite", y=4, fs=10.5)
    save(fig, "s6_attributes.png")


def s6_keys():
    fig, ax = canvas(10, 4.8)
    rbox(ax, 6, 62, 42, 14, "Candidate keys", fc=AMBER, fs=12)
    ax.text(27, 54, "citizenship_no · email · roll_no", ha="center", color=INK, fontsize=10.5)
    rbox(ax, 6, 30, 42, 14, "Primary key (chosen one)", fc=TEAL, fs=12)
    ax.text(27, 22, "citizenship_no  (underlined in ER)", ha="center", color=INK, fontsize=10.5)
    rbox(ax, 54, 46, 40, 20, "Composite key", fc=BLUE, fs=12)
    ax.text(74, 39, "(roll_no + program)\ntwo columns together = unique", ha="center", color=INK, fontsize=10)
    caption(ax, "A key is unique per entity. Names repeat → never a key; IDs/roll numbers do.", y=8)
    save(fig, "s6_keys.png")


# ================= S7 =================
def s7_relationship():
    fig, ax = canvas(10, 4.2)
    entity(ax, 16, 50, 24, 14, "STUDENT", fs=12)
    diamond(ax, 50, 50, 26, 26, "ENROLLS", fs=11)
    entity(ax, 84, 50, 24, 14, "COURSE", fs=12)
    link(ax, 28, 50, 37, 50); link(ax, 63, 50, 72, 50)
    caption(ax, "Relationship type = an association between entity types (degree 2 = binary).", y=14)
    save(fig, "s7_relationship.png")


def s7_recursive():
    fig, ax = canvas(10, 4.6)
    entity(ax, 50, 40, 28, 14, "EMPLOYEE", fs=13)
    diamond(ax, 50, 74, 26, 22, "SUPERVISES", fs=10)
    link(ax, 40, 44, 44, 66); link(ax, 60, 44, 56, 66)
    ax.text(30, 60, "supervisor", ha="center", color=CORAL, fontsize=10, fontweight="bold")
    ax.text(70, 60, "supervisee", ha="center", color=CORAL, fontsize=10, fontweight="bold")
    caption(ax, "Recursive relationship: same entity type on both ends — role names are essential.", y=12)
    save(fig, "s7_recursive.png")


def s7_cardinality():
    fig, ax = canvas(10, 4.6)
    trios = [("1 : 1", "CITIZEN — PASSPORT", 78), ("1 : N", "DEPARTMENT — EMPLOYEE", 50), ("M : N", "STUDENT — COURSE", 22)]
    for label, ex, y in trios:
        rbox(ax, 6, y-6, 18, 12, label, fc=TEAL, fs=14)
        ax.text(60, y, ex, ha="center", color=INK, fontsize=12)
    caption(ax, "Cardinality ratio = max instances an entity joins. M:N needs a junction table (S12).", y=6)
    save(fig, "s7_cardinality.png")


def s7_participation():
    fig, ax = canvas(10, 4.4)
    # total
    entity(ax, 16, 68, 22, 12, "LOAN", fc=BLUE, fs=11)
    diamond(ax, 56, 68, 20, 18, "belongs", fs=9)
    entity(ax, 88, 68, 22, 12, "CUSTOMER", fc=BLUE, fs=10.5)
    link(ax, 27, 68, 46, 68, dbl=True); link(ax, 66, 68, 77, 68)
    ax.text(37, 78, "TOTAL (double line):\nevery loan must have a customer", ha="center", color=TEAL, fontsize=9)
    # partial
    entity(ax, 16, 28, 22, 12, "CUSTOMER", fc=BLUE, fs=10.5)
    diamond(ax, 56, 28, 20, 18, "has", fs=9)
    entity(ax, 88, 28, 22, 12, "LOAN", fc=BLUE, fs=11)
    link(ax, 27, 28, 46, 28); link(ax, 66, 28, 77, 28)
    ax.text(37, 15, "PARTIAL (single line):\nnot every customer has a loan", ha="center", color=CORAL, fontsize=9)
    save(fig, "s7_participation.png")


# ================= S8 =================
def s8_weak_vs_strong():
    fig, ax = canvas(10, 4.4)
    entity(ax, 26, 50, 30, 16, "CUSTOMER", fc=BLUE, fs=13)
    ax.text(26, 30, "STRONG entity\n(single rectangle) — has its own key", ha="center", color=BLUE, fontsize=10.5)
    entity(ax, 74, 50, 30, 16, "ORDER_ITEM", weak=True, fc=CORAL, fs=12)
    ax.text(74, 28, "WEAK entity\n(double rectangle) — no key of its own", ha="center", color=CORAL, fontsize=10.5)
    caption(ax, "'Weak' = identity-dependent, NOT unimportant.", y=8)
    save(fig, "s8_weak_vs_strong.png")


def s8_identifying():
    fig, ax = canvas(10, 4.2)
    entity(ax, 16, 50, 22, 14, "LOAN", fc=BLUE, fs=12)
    diamond(ax, 50, 50, 24, 24, "HAS", dbl=True, fs=11)
    entity(ax, 85, 50, 26, 14, "INSTALLMENT", weak=True, fc=CORAL, fs=11)
    link(ax, 27, 50, 38, 50)
    link(ax, 62, 50, 71, 50, dbl=True)
    caption(ax, "Identifying relationship = double diamond; double line = total participation on the weak side.", y=14)
    save(fig, "s8_identifying.png")


def s8_partial_key():
    fig, ax = canvas(10, 4.6)
    entity(ax, 30, 52, 28, 14, "INSTALLMENT", weak=True, fc=CORAL, fs=11)
    oval(ax, 78, 66, 30, 13, "installment_no", dashed=True, fs=10)
    ax.plot([66, 90], [62.3, 62.3], color=INK, lw=1.2, ls=(0, (3, 2)), zorder=5)
    link(ax, 44, 55, 63, 64)
    ax.text(50, 26, "Full identity  =  owner key  +  partial key\n= LOAN_id 4521  +  installment_no 3",
            ha="center", color=NAVY, fontsize=12, fontweight="bold")
    caption(ax, "Partial key (dashed underline) is unique only WITHIN one owner.", y=8)
    save(fig, "s8_partial_key.png")


for fn in [s5_what_vs_how, s5_design_pipeline, s5_data_vs_functional,
           s6_type_vs_set, s6_attributes, s6_keys,
           s7_relationship, s7_recursive, s7_cardinality, s7_participation,
           s8_weak_vs_strong, s8_identifying, s8_partial_key]:
    fn()
print("\nAll S5-S8 images written to", OUT)
