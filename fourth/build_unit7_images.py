#!/usr/bin/env python3
"""Generate custom concept diagrams (PNG) for IT220 Unit 7 — Advanced Topics.
License-safe, purpose-built teaching visuals with on-image labels (survive PDF).
Output -> fourth/images/  ·  Run: python3 build_unit7_images.py
Palette + helpers mirror build_unit1_images.py so all IT220 decks look like one course.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Polygon

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


# ---------- S45 · Performance tuning ----------
def index_vs_scan():
    fig, ax = canvas(10, 5.2)
    ax.text(50, 95, "Full table scan  vs  index lookup", ha="center",
            fontsize=14, fontweight="bold", color=NAVY)
    # left: full scan
    box(ax, 4, 78, 40, 8, "NO INDEX  —  full table scan", fc=CORAL, fs=11)
    for i in range(6):
        c = TEAL if i == 4 else LGREY
        box(ax, 6, 68 - i*9, 36, 7, f"row {i+1}" + ("   <- match!" if i == 4 else "  read..."),
            fc=PALEC if i != 4 else PALET, tc=INK, fs=9.5, bold=(i == 4), ec=c, lw=1.2)
    ax.text(24, 6, "read EVERY row to find one — slow on big tables",
            ha="center", fontsize=9.5, style="italic", color=CORAL)
    # right: index
    box(ax, 56, 78, 40, 8, "INDEX (B-tree)  —  jump to row", fc=TEAL, fs=11)
    box(ax, 66, 60, 20, 10, "citizenship_no\nindex", fc=BLUE, fs=10)
    arrow(ax, 76, 60, 76, 40, color=NAVY, lw=2.4)
    box(ax, 66, 30, 20, 9, "row 5  [hit]", fc=TEAL, fs=11)
    ax.text(76, 6, "go straight to the row — like a book's back-index",
            ha="center", fontsize=9.5, style="italic", color=TEAL)
    save(fig, "s45_index.png")


def query_plan():
    fig, ax = canvas(10, 4.8)
    ax.text(50, 94, "Read the execution plan (EXPLAIN), then tune", ha="center",
            fontsize=13.5, fontweight="bold", color=NAVY)
    box(ax, 4, 52, 44, 30, "", fc=PALEC, ec=CORAL, lw=1.6, tc=INK)
    ax.text(26, 76, "BEFORE", ha="center", color=CORAL, fontsize=12, fontweight="bold")
    ax.text(26, 66, "SELECT * FROM txn\n(no filter, no index)", ha="center",
            color=INK, fontsize=9.5, family="monospace")
    ax.text(26, 57, "Seq Scan · 2,000,000 rows · 4.0 s", ha="center", color=CORAL, fontsize=9.5)
    box(ax, 52, 52, 44, 30, "", fc=PALET, ec=TEAL, lw=1.6, tc=INK)
    ax.text(74, 76, "AFTER", ha="center", color=TEAL, fontsize=12, fontweight="bold")
    ax.text(74, 66, "SELECT amount FROM txn\nWHERE user_id=? AND date>=?", ha="center",
            color=INK, fontsize=9, family="monospace")
    ax.text(74, 57, "Index Scan · 42 rows · 0.2 s", ha="center", color=TEAL, fontsize=9.5)
    arrow(ax, 48, 67, 52, 67, color=NAVY, lw=2.8)
    ax.text(50, 34, "Fix: select only needed columns · filter on an indexed column · avoid scanning everything",
            ha="center", fontsize=10, color=GREY)
    ax.text(50, 20, "20× faster on the SAME hardware — measure with EXPLAIN before you change anything",
            ha="center", fontsize=10.5, style="italic", color=NAVY, fontweight="bold")
    save(fig, "s45_queryplan.png")


def security_model():
    fig, ax = canvas(10, 5.0)
    ax.text(50, 95, "The database access-control model", ha="center",
            fontsize=14, fontweight="bold", color=NAVY)
    box(ax, 3, 55, 20, 20, "USER\n(app / person)", fc=GREY, fs=10.5)
    arrow(ax, 23, 65, 29, 65, color=NAVY)
    box(ax, 29, 55, 22, 20, "AUTHENTICATION\nwho are you?\nlogin · OTP", fc=BLUE, fs=10)
    arrow(ax, 51, 65, 57, 65, color=NAVY)
    box(ax, 57, 55, 22, 20, "AUTHORIZATION\nwhat may you do?\nGRANT / REVOKE · roles", fc=TEAL, fs=9.5)
    arrow(ax, 79, 65, 85, 65, color=NAVY)
    box(ax, 85, 55, 13, 20, "DATA", fc=NAVY, fs=11)
    box(ax, 29, 25, 50, 16, "ENCRYPTION  —  at rest (stored data) + in transit (TLS/HTTPS)\na stolen dump is useless without the keys",
        fc=AMBER, fs=10)
    arrow(ax, 91, 55, 60, 41, color=CORAL, lw=1.8, style="-")
    ax.text(50, 10, "Authentication = ID at the gate · Authorization = which rooms your keycard opens · Encryption = locked safe",
            ha="center", fontsize=9.8, style="italic", color=GREY)
    save(fig, "s45_security.png")


# ---------- S46 · Parallel & distributed ----------
def parallel_vs_distributed():
    fig, ax = canvas(10, 5.0)
    ax.text(27, 95, "PARALLEL DB", ha="center", fontsize=13, fontweight="bold", color=BLUE)
    ax.text(27, 88, "one site · many CPUs/disks", ha="center", fontsize=9.5, style="italic", color=GREY)
    box(ax, 6, 30, 42, 50, "", fc=PALEB, ec=BLUE, lw=1.6, tc=INK)
    for i in range(2):
        for j in range(2):
            box(ax, 12 + j*20, 42 + i*22, 15, 14, f"CPU\ndisk", fc=BLUE, fs=9)
    ax.text(27, 35, "many cooks in ONE kitchen", ha="center", fontsize=9.5, style="italic", color=BLUE)

    ax.text(74, 95, "DISTRIBUTED DB", ha="center", fontsize=13, fontweight="bold", color=TEAL)
    ax.text(74, 88, "many sites · one logical DB", ha="center", fontsize=9.5, style="italic", color=GREY)
    sites = [("KTM", 56, 60), ("Pokhara", 82, 68), ("Biratnagar", 78, 40)]
    for name, x, y in sites:
        box(ax, x, y, 16, 10, name, fc=TEAL, fs=9.5)
    for a in range(len(sites)):
        for b in range(a+1, len(sites)):
            arrow(ax, sites[a][1]+8, sites[a][2]+5, sites[b][1]+8, sites[b][2]+5,
                  color=LGREY, lw=1.4, style="-")
    ax.text(74, 33, "branches of ONE restaurant\nin different cities", ha="center",
            fontsize=9.5, style="italic", color=TEAL)
    ax.plot([50, 50], [28, 84], color=LGREY, lw=1.2, ls="--")
    save(fig, "parallel_vs_distributed.png")


def fragmentation():
    fig, ax = canvas(10, 5.0)
    ax.text(50, 95, "Fragmentation — splitting one table across sites", ha="center",
            fontsize=13.5, fontweight="bold", color=NAVY)
    # horizontal
    ax.text(26, 84, "HORIZONTAL — split ROWS (by province)", ha="center",
            fontsize=10.5, fontweight="bold", color=BLUE)
    box(ax, 6, 58, 40, 20, "Bagmati rows  →  KTM server", fc=PALEB, tc=INK, fs=9.5, ec=BLUE, lw=1.3)
    box(ax, 6, 34, 40, 20, "Gandaki rows  →  Pokhara server", fc=PALEB, tc=INK, fs=9.5, ec=BLUE, lw=1.3)
    ax.text(26, 26, "each site keeps its own rows", ha="center", fontsize=9, style="italic", color=GREY)
    # vertical
    ax.text(74, 84, "VERTICAL — split COLUMNS", ha="center",
            fontsize=10.5, fontweight="bold", color=TEAL)
    box(ax, 54, 34, 18, 44, "id, name,\nphone\n\n(public\ncols)", fc=PALET, tc=INK, fs=9, ec=TEAL, lw=1.3)
    box(ax, 76, 34, 18, 44, "id,\nbalance,\nKYC\n\n(sensitive\ncols)", fc=PALET, tc=INK, fs=9, ec=TEAL, lw=1.3)
    ax.text(74, 26, "columns split; id repeated to re-join", ha="center", fontsize=9, style="italic", color=GREY)
    ax.text(50, 12, "Mixed = both together. Fragmentation SPLITS data; replication (next) COPIES it.",
            ha="center", fontsize=10, style="italic", color=NAVY)
    save(fig, "s46_fragmentation.png")


def replication_transparency():
    fig, ax = canvas(10, 5.0)
    ax.text(50, 95, "Replication + distribution transparency", ha="center",
            fontsize=13.5, fontweight="bold", color=NAVY)
    box(ax, 4, 60, 22, 12, "User in\nBiratnagar", fc=GREY, fs=10)
    arrow(ax, 26, 66, 33, 66, color=NAVY)
    box(ax, 33, 58, 30, 16, "TRANSPARENCY LAYER\n'find the data for me'", fc=BLUE, fs=10)
    ax.text(48, 52, "user never knows WHERE data lives or that it's copied", ha="center",
            fontsize=9, style="italic", color=GREY)
    sites = [(72, 78), (72, 58), (72, 38)]
    labels = ["KTM copy", "Pokhara copy", "Biratnagar copy"]
    for (x, y), lb in zip(sites, labels):
        box(ax, x, y, 24, 12, lb, fc=TEAL, fs=9.5)
        arrow(ax, 63, 66, x, y+6, color=LGREY, lw=1.5)
    ax.text(50, 22, "Replication = same data COPIED to many sites → faster reads + no single point of failure",
            ha="center", fontsize=10, color=NAVY, fontweight="bold")
    ax.text(50, 12, "Trade-off: every copy must be kept consistent on writes. Real systems use fragmentation AND replication.",
            ha="center", fontsize=9.5, style="italic", color=GREY)
    save(fig, "s46_replication.png")


# ---------- S47 · Warehousing / BigData / NoSQL ----------
def etl_warehouse():
    fig, ax = canvas(10, 4.8)
    ax.text(50, 95, "OLTP sources  →  ETL  →  Data Warehouse  →  OLAP", ha="center",
            fontsize=13, fontweight="bold", color=NAVY)
    srcs = ["eSewa\n(OLTP)", "Bank\n(OLTP)", "Telecom\n(OLTP)"]
    for i, s in enumerate(srcs):
        box(ax, 3, 66 - i*22, 16, 16, s, fc=BLUE, fs=9.5)
        arrow(ax, 19, 74 - i*22, 26, 55, color=GREY, lw=1.6)
    box(ax, 26, 44, 20, 22, "ETL\nExtract →\nTransform\n(clean) →\nLoad", fc=AMBER, fs=9.5)
    arrow(ax, 46, 55, 53, 55, color=NAVY, lw=2.4)
    box(ax, 53, 42, 20, 26, "DATA\nWAREHOUSE\nhistorical ·\nread-mostly", fc=NAVY, fs=10)
    arrow(ax, 73, 55, 80, 55, color=NAVY, lw=2.4)
    box(ax, 80, 44, 17, 22, "OLAP\ndashboards\n& reports", fc=TEAL, fs=10)
    ax.text(50, 22, "OLTP = run the business (fast, tiny writes)   ·   OLAP = analyze it (few big historical reads)",
            ha="center", fontsize=10, color=NAVY, fontweight="bold")
    ax.text(50, 12, "The hard part is TRANSFORM: cleaning & standardizing dates/phone formats across systems.",
            ha="center", fontsize=9.5, style="italic", color=GREY)
    save(fig, "s47_etl_warehouse.png")


def star_schema():
    fig, ax = canvas(10, 5.0)
    ax.text(50, 95, "Star schema — one fact table, many dimensions", ha="center",
            fontsize=13, fontweight="bold", color=NAVY)
    box(ax, 38, 42, 24, 18, "FACT\nSales\n(amount, qty)", fc=NAVY, fs=10.5)
    dims = [("Dim: Date", 38, 80), ("Dim: Customer", 6, 55),
            ("Dim: Product", 72, 55), ("Dim: Location", 38, 12)]
    for name, x, y in dims:
        box(ax, x, y, 22, 12, name, fc=TEAL, fs=9.5)
        arrow(ax, x+11, y + (0 if y < 42 else 12) + (12 if y < 42 else 0),
              50, 51, color=LGREY, lw=1.6, style="-")
    ax.text(50, 4, "Fact = the measured event; dimensions = the ways you slice it (by date, city, product…).",
            ha="center", fontsize=9.8, style="italic", color=GREY)
    save(fig, "s47_star_schema.png")


def nosql_landscape():
    fig, ax = canvas(10, 5.2)
    ax.text(50, 95, "The SQL vs NoSQL landscape", ha="center",
            fontsize=14, fontweight="bold", color=NAVY)
    quad = [
        ("KEY-VALUE\nRedis", "session / cart lookup", 6, 52, BLUE),
        ("DOCUMENT\nMongoDB", "flexible product catalog (JSON)", 54, 52, TEAL),
        ("COLUMN-FAMILY\nCassandra", "telecom CDRs at massive scale", 6, 12, AMBER),
        ("GRAPH\nNeo4j", "social / fraud networks", 54, 12, CORAL),
    ]
    for head, use, x, y, c in quad:
        box(ax, x, y, 40, 32, "", fc=c)
        ax.text(x+20, y+22, head, ha="center", color=WHITE, fontsize=12, fontweight="bold")
        ax.text(x+20, y+8, use, ha="center", color=WHITE, fontsize=9.5)
    ax.text(50, 4, "NoSQL COMPLEMENTS SQL — pick the tool for the job; most apps still keep a relational core.",
            ha="center", fontsize=9.8, style="italic", color=NAVY, fontweight="bold")
    save(fig, "s47_nosql_landscape.png")


# ---------- S48 · Course map ----------
def course_map():
    fig, ax = canvas(10, 5.4)
    ax.text(50, 96, "IT 220 in one picture — the database lifecycle", ha="center",
            fontsize=14, fontweight="bold", color=NAVY)
    # foundation
    box(ax, 6, 8, 88, 11, "UNIT 1 · Concepts & Architecture (the foundation everything rests on)",
        fc=NAVY, fs=11)
    steps = [
        ("U2\nDesign\n(ER→tables)", BLUE, 24),
        ("U3\nTheory\n(rel.\nalgebra)", BLUE, 34),
        ("U4\nNormalize\n(1NF→BCNF)", TEAL, 44),
        ("U5\nBuild/\nQuery\n(SQL)", TEAL, 54),
        ("U6\nProtect/\nRun (ACID)", AMBER, 64),
        ("U7\nScale/\nAdvanced", CORAL, 74),
    ]
    x = 6
    w = 13.5
    for i, (label, c, y) in enumerate(steps):
        box(ax, x, y, 13, 15, label, fc=c, fs=8.6)
        if i < len(steps) - 1:
            nx, ny = 6 + (i+1)*14.6, steps[i+1][2]
            arrow(ax, x+13, y+8, nx, ny+8, color=LGREY, lw=1.8)
        x += 14.6
    ax.text(50, 2.5, "Concepts → Design → Theory → Normalize → Build → Protect → Scale : one system, one lifecycle.",
            ha="center", fontsize=9.8, style="italic", color=GREY)
    save(fig, "s48_course_map.png")


for fn in [index_vs_scan, query_plan, security_model,
           parallel_vs_distributed, fragmentation, replication_transparency,
           etl_warehouse, star_schema, nosql_landscape, course_map]:
    fn()

print("\nAll Unit 7 images written to", OUT)
