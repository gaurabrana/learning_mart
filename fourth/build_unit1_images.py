#!/usr/bin/env python3
"""Generate custom concept diagrams (PNG) for IT220 Unit 1.
License-safe, purpose-built teaching visuals. Output -> fourth/images/
Run: python3 build_unit1_images.py
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Polygon

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


# ---------- S1 ----------
def data_ladder():
    fig, ax = canvas(10, 4.6)
    steps = [("DATA", "raw facts\n9818000000  'Sita'  78", GREY),
             ("INFORMATION", "data + meaning\n'Sita scored 78'", BLUE),
             ("DATABASE", "organized · persistent\n· shared collection", TEAL)]
    x = 4
    for i, (head, sub, c) in enumerate(steps):
        box(ax, x, 30, 26, 34, "", fc=c)
        ax.text(x+13, 54, head, ha="center", va="center", color=WHITE, fontsize=15, fontweight="bold")
        ax.text(x+13, 41, sub, ha="center", va="center", color=WHITE, fontsize=10.5)
        if i < 2:
            arrow(ax, x+26, 47, x+32, 47, color=NAVY, lw=2.6)
        x += 32
    ax.text(50, 14, "Add organization + storage, and raw facts become a database.",
            ha="center", fontsize=11, style="italic", color=GREY)
    save(fig, "s1_data_ladder.png")


def users_dbms():
    fig, ax = canvas(10, 5.4)
    users = ["Teller", "Developer", "Analyst", "DBA"]
    for i, u in enumerate(users):
        box(ax, 4, 78 - i*19, 20, 13, u, fc=BLUE, fs=11)
        arrow(ax, 24, 84.5 - i*19, 40, 50, color=GREY, lw=1.8)
    box(ax, 40, 40, 26, 20, "DBMS\n(MySQL, Oracle…)", fc=NAVY, fs=13)
    arrow(ax, 66, 50, 78, 50, color=NAVY, lw=2.6)
    box(ax, 78, 38, 18, 24, "Database\n(the data)", fc=TEAL, fs=12)
    ax.text(50, 6, "Users never touch the data directly — the DBMS sits in between.",
            ha="center", fontsize=10.5, style="italic", color=GREY)
    save(fig, "s1_users_dbms.png")


def file_vs_dbms():
    fig, ax = canvas(10, 5.6)
    rows = [("File-based system", "DBMS"),
            ("Uncontrolled redundancy", "Controlled redundancy"),
            ("Data inconsistency", "Integrity constraints"),
            ("Hard to share safely", "Concurrent multi-user access"),
            ("Weak / no security", "Access control & permissions"),
            ("A crash can lose data", "Backup & recovery")]
    y = 86; h = 13
    for i, (a, b) in enumerate(rows):
        if i == 0:
            box(ax, 4, y, 45, h, a, fc=CORAL, fs=12)
            box(ax, 51, y, 45, h, b, fc=TEAL, fs=12)
        else:
            box(ax, 4, y, 45, h, a, fc=PALEC, tc=INK, fs=10.5, bold=False)
            box(ax, 51, y, 45, h, b, fc=PALET, tc=INK, fs=10.5, bold=False)
        y -= (h + 1.5)
    save(fig, "s1_file_vs_dbms.png")


def db_users():
    fig, ax = canvas(10, 4.8)
    items = [("Naive / end users", "ready-made screens\n(bank teller)", BLUE),
             ("App programmers", "build the apps\n(core-banking dev)", TEAL),
             ("Sophisticated users", "write own queries\n(data analyst)", AMBER),
             ("DBA", "design, security,\nbackups, tuning", CORAL)]
    x = 3
    for head, sub, c in items:
        box(ax, x, 34, 22, 40, "", fc=c)
        ax.text(x+11, 63, head, ha="center", color=WHITE, fontsize=11.5, fontweight="bold")
        ax.text(x+11, 46, sub, ha="center", color=WHITE, fontsize=9.8)
        x += 24.3
    ax.text(50, 20, "Four kinds of database user — from no SQL needed (left) to full control (right).",
            ha="center", fontsize=10.5, style="italic", color=GREY)
    save(fig, "s1_db_users.png")


# ---------- S2 ----------
def data_models():
    fig, ax = canvas(10, 5.0)
    levels = [("Conceptual / high-level", "close to how humans think — the ER model", BLUE),
              ("Representational", "the relational model (tables)", TEAL),
              ("Physical / low-level", "how data sits on disk (files, indexes)", NAVY)]
    y = 70
    for head, sub, c in levels:
        box(ax, 14, y, 72, 16, "", fc=c)
        ax.text(50, y+10.5, head, ha="center", color=WHITE, fontsize=13, fontweight="bold")
        ax.text(50, y+4.5, sub, ha="center", color=WHITE, fontsize=10)
        y -= 20
    ax.text(50, 6, "Blueprint (conceptual)  →  built house (physical)",
            ha="center", fontsize=10.5, style="italic", color=GREY)
    save(fig, "s2_data_models.png")


def schema_instance():
    fig, ax = canvas(10, 4.8)
    box(ax, 5, 30, 40, 46, "", fc=PALEB, ec=BLUE, lw=1.5, tc=INK)
    ax.text(25, 70, "SCHEMA", ha="center", color=BLUE, fontsize=14, fontweight="bold")
    ax.text(25, 60, "the design — changes rarely", ha="center", color=GREY, fontsize=9.5, style="italic")
    ax.text(25, 48, "Student(\n  roll, name, program\n)", ha="center", color=INK, fontsize=11, family="monospace")
    box(ax, 55, 30, 40, 46, "", fc=PALET, ec=TEAL, lw=1.5, tc=INK)
    ax.text(75, 70, "INSTANCE", ha="center", color=TEAL, fontsize=14, fontweight="bold")
    ax.text(75, 60, "the data now — changes constantly", ha="center", color=GREY, fontsize=9.0, style="italic")
    rows = ["101  Sita   BIM", "102  Hari   BIM", "103  Gita   BIM"]
    for i, r in enumerate(rows):
        ax.text(75, 50 - i*6, r, ha="center", color=INK, fontsize=10, family="monospace")
    ax.text(50, 20, "One schema  →  infinitely many instances over time.",
            ha="center", fontsize=10.5, style="italic", color=GREY)
    save(fig, "s2_schema_instance.png")


def three_schema():
    fig, ax = canvas(10, 6.0)
    # external views
    for i, t in enumerate(["Student\nview", "Teacher\nview", "Admin\nview"]):
        box(ax, 10 + i*28, 80, 24, 13, t, fc=BLUE, fs=10.5)
    ax.text(50, 74, "↕   external / conceptual mapping", ha="center", fontsize=9.5, style="italic", color=GREY)
    box(ax, 12, 54, 76, 16, "CONCEPTUAL SCHEMA\nwhole logical database — all students, subjects, marks", fc=TEAL, fs=12)
    ax.text(50, 48, "↕   conceptual / internal mapping", ha="center", fontsize=9.5, style="italic", color=GREY)
    box(ax, 12, 28, 76, 16, "INTERNAL SCHEMA\nphysical storage — files, blocks, indexes", fc=NAVY, fs=12)
    box(ax, 40, 10, 20, 13, "disk", fc=GREY, fs=11)
    arrow(ax, 50, 28, 50, 24, color=GREY)
    ax.text(50, 3, "External = many user views · Conceptual = one logical whole · Internal = storage",
            ha="center", fontsize=10, style="italic", color=GREY)
    save(fig, "s2_three_schema.png")


def data_independence():
    fig, ax = canvas(10, 4.8)
    box(ax, 8, 56, 84, 16, "LOGICAL data independence\nchange the conceptual schema (add a column/table) — views & apps unaffected", fc=BLUE, fs=11.5)
    box(ax, 8, 30, 84, 16, "PHYSICAL data independence\nchange storage (SSDs, indexes) — conceptual schema unaffected", fc=TEAL, fs=11.5)
    ax.text(50, 18, "Logical = change the DESIGN safely   ·   Physical = change STORAGE safely",
            ha="center", fontsize=11, style="italic", color=GREY)
    save(fig, "s2_data_independence.png")


# ---------- S3 ----------
def languages():
    fig, ax = canvas(10, 4.8)
    items = [("DDL", "define structure\nCREATE / ALTER / DROP", BLUE),
             ("DML", "query & modify data\nSELECT / INSERT / UPDATE", TEAL),
             ("DCL", "permissions\nGRANT / REVOKE", AMBER),
             ("TCL", "transactions\nCOMMIT / ROLLBACK", CORAL)]
    x = 3
    for head, sub, c in items:
        box(ax, x, 36, 22, 38, "", fc=c)
        ax.text(x+11, 63, head, ha="center", color=WHITE, fontsize=15, fontweight="bold")
        ax.text(x+11, 47, sub, ha="center", color=WHITE, fontsize=9.3)
        x += 24.3
    ax.text(50, 20, "SQL bundles all four sub-languages into one.",
            ha="center", fontsize=11, style="italic", color=GREY)
    save(fig, "s3_languages.png")


def interfaces():
    fig, ax = canvas(10, 4.6)
    ifs = ["Menu-based", "Form-based", "GUI", "Natural language", "API / embedded SQL"]
    x = 2.5
    for t in ifs:
        box(ax, x, 50, 18, 16, t, fc=BLUE, fs=9.5)
        arrow(ax, x+9, 50, 50, 33, color=LGREY, lw=1.4)
        x += 19.2
    box(ax, 38, 16, 24, 16, "Same\nDATABASE", fc=TEAL, fs=12)
    ax.text(50, 8, "Many doors into the same data — match the interface to the user.",
            ha="center", fontsize=10.5, style="italic", color=GREY)
    save(fig, "s3_interfaces.png")


def dbms_components():
    fig, ax = canvas(10, 5.6)
    box(ax, 32, 82, 36, 12, "Users / Applications", fc=BLUE, fs=12)
    arrow(ax, 50, 82, 50, 76)
    box(ax, 32, 63, 36, 12, "Query Processor / Optimizer", fc=NAVY, fs=11.5)
    arrow(ax, 50, 63, 50, 57)
    box(ax, 32, 44, 36, 12, "Storage + Buffer Manager", fc=TEAL, fs=11.5)
    arrow(ax, 50, 44, 50, 38)
    box(ax, 38, 24, 24, 13, "Database on disk", fc=GREY, fs=11)
    box(ax, 74, 63, 22, 12, "Catalog /\nMetadata", fc=CORAL, fs=10.5)
    box(ax, 74, 44, 22, 12, "Transaction\nManager (ACID)", fc=AMBER, fs=10)
    arrow(ax, 68, 69, 74, 69, color=LGREY, lw=1.6, style="-")
    arrow(ax, 68, 50, 74, 50, color=LGREY, lw=1.6, style="-")
    save(fig, "s3_dbms_components.png")


def data_dictionary():
    fig, ax = canvas(10, 4.4)
    box(ax, 26, 50, 48, 26, "DATA DICTIONARY\n(system catalog)", fc=NAVY, fs=13)
    ax.text(50, 40, "'a database about the database' — metadata", ha="center", fontsize=11, style="italic", color=GREY)
    tags = ["table names", "column types", "constraints", "users", "indexes"]
    x = 4
    for t in tags:
        box(ax, x, 18, 17.5, 12, t, fc=PALEB, tc=INK, fs=9, bold=False, ec=BLUE, lw=1)
        x += 18.6
    save(fig, "s3_data_dictionary.png")


# ---------- S4 ----------
def centralized():
    fig, ax = canvas(10, 4.6)
    box(ax, 34, 46, 32, 24, "CENTRAL MACHINE\nData + DBMS + App", fc=NAVY, fs=12)
    for i in range(3):
        box(ax, 8 + i*30, 16, 18, 12, "Terminal", fc=LGREY, tc=INK, fs=10, bold=False)
        arrow(ax, 17 + i*30, 28, 50, 46, color=GREY, lw=1.5)
    ax.text(50, 80, "Everything on one machine — simple, but a single point of failure.",
            ha="center", fontsize=11, style="italic", color=CORAL)
    save(fig, "s4_centralized.png")


def client_server():
    fig, ax = canvas(10, 5.0)
    ax.text(25, 92, "Two-tier", ha="center", fontsize=13, fontweight="bold", color=BLUE)
    box(ax, 12, 64, 26, 14, "Client\nUI + logic", fc=BLUE, fs=10.5)
    arrow(ax, 25, 64, 25, 54)
    box(ax, 12, 38, 26, 14, "Database Server", fc=TEAL, fs=10.5)
    ax.text(75, 92, "Three-tier", ha="center", fontsize=13, fontweight="bold", color=TEAL)
    box(ax, 62, 70, 26, 12, "Client (UI)", fc=BLUE, fs=10.5)
    arrow(ax, 75, 70, 75, 64)
    box(ax, 62, 50, 26, 13, "Application Server\n(business logic)", fc=AMBER, fs=10)
    arrow(ax, 75, 50, 75, 44)
    box(ax, 62, 30, 26, 13, "Database Server", fc=TEAL, fs=10.5)
    ax.text(50, 12, "Daraz ≈ three-tier:  phone app → app servers → database servers.",
            ha="center", fontsize=10.5, style="italic", color=GREY)
    save(fig, "s4_client_server.png")


def classification():
    fig, ax = canvas(10, 4.8)
    box(ax, 38, 80, 24, 13, "Classify a\nDBMS by…", fc=NAVY, fs=11.5)
    branches = [("Data model", "relational · object ·\nNoSQL · legacy", BLUE, 6),
                ("Number of users", "single-user vs\nmulti-user", TEAL, 38),
                ("Distribution", "centralized vs\ndistributed", AMBER, 70)]
    for head, sub, c, x in branches:
        box(ax, x, 30, 24, 26, "", fc=c)
        ax.text(x+12, 48, head, ha="center", color=WHITE, fontsize=11, fontweight="bold")
        ax.text(x+12, 38, sub, ha="center", color=WHITE, fontsize=9.2)
        arrow(ax, 50, 80, x+12, 56, color=LGREY, lw=1.6)
    save(fig, "s4_classification.png")


def synthesis():
    fig, ax = canvas(10, 5.6)
    cx, cy = 50, 50
    box(ax, 38, 42, 24, 16, "DATABASE\nSYSTEM", fc=NAVY, fs=13)
    nodes = [("Users", BLUE, 12, 82), ("Languages &\nInterfaces", BLUE, 70, 82),
             ("DBMS\nComponents", TEAL, 4, 46), ("Three-Schema\nArchitecture", TEAL, 78, 46),
             ("Deployment\nArchitecture", AMBER, 40, 12)]
    for t, c, x, y in nodes:
        arrow(ax, cx, cy, x+11, y+6, color=LGREY, lw=1.6, style="-")
        box(ax, x, y, 22, 13, t, fc=c, fs=10)
    save(fig, "s4_synthesis.png")


for fn in [data_ladder, users_dbms, file_vs_dbms, db_users,
           data_models, schema_instance, three_schema, data_independence,
           languages, interfaces, dbms_components, data_dictionary,
           centralized, client_server, classification, synthesis]:
    fn()

print("\nAll images written to", OUT)
