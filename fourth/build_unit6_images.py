#!/usr/bin/env python3
"""Generate custom concept diagrams (PNG) for IT220 Unit 6 —
Transaction Processing, Concurrency Control & Recovery.
License-safe, purpose-built teaching visuals with on-image labels
(labels survive PDF export). Output -> fourth/images/
Run: python3 build_unit6_images.py
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


def circle(ax, x, y, r, text, fc=BLUE, tc=WHITE, fs=13):
    ax.add_patch(Circle((x, y), r, fc=fc, ec="none", zorder=2))
    ax.text(x, y, text, ha="center", va="center", color=tc, fontsize=fs, fontweight="bold", zorder=3)


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=150, bbox_inches="tight",
                facecolor="white", pad_inches=0.15)
    plt.close(fig)
    print("wrote", name)


# ---------- S37 : transaction state diagram ----------
def states():
    fig, ax = canvas(10, 5.4)
    box(ax, 3, 55, 20, 13, "ACTIVE\n(running ops)", fc=BLUE, fs=11)
    box(ax, 31, 55, 22, 13, "PARTIALLY\nCOMMITTED", fc=AMBER, fs=11)
    box(ax, 61, 55, 20, 13, "COMMITTED", fc=TEAL, fs=11.5)
    box(ax, 31, 22, 20, 13, "FAILED", fc=CORAL, fs=11.5)
    box(ax, 61, 22, 20, 13, "ABORTED\n(terminated)", fc=GREY, fs=10.5)
    arrow(ax, 23, 61.5, 31, 61.5, color=NAVY)          # active -> partially
    ax.text(27, 65, "end ops", ha="center", fontsize=8.5, color=GREY, style="italic")
    arrow(ax, 53, 61.5, 61, 61.5, color=NAVY)          # partially -> committed
    ax.text(57, 65, "commit\n(log flushed)", ha="center", fontsize=8, color=GREY, style="italic")
    arrow(ax, 13, 55, 26, 35, color=CORAL)             # active -> failed
    arrow(ax, 41, 55, 41, 35, color=CORAL)             # partially -> failed
    arrow(ax, 51, 28.5, 61, 28.5, color=GREY)          # failed -> aborted
    ax.text(56, 32, "rollback", ha="center", fontsize=8.5, color=GREY, style="italic")
    ax.text(50, 8, "Active → Partially committed → Committed  (success path)   ·   "
            "any failure → Failed → Aborted (rolled back)",
            ha="center", fontsize=10, style="italic", color=GREY)
    save(fig, "s37_states.png")


# ---------- S37 : the system log (journal) ----------
def log_timeline():
    fig, ax = canvas(10, 4.8)
    entries = [("[start, T]", BLUE),
               ("[write, T, RitaBal, 2000, 1500]", AMBER),
               ("[write, T, HariBal, 1000, 1500]", AMBER),
               ("[commit, T]", TEAL)]
    y = 78
    for txt, c in entries:
        box(ax, 12, y, 76, 12, txt, fc=c, fs=11.5)
        y -= 17
    ax.text(50, 10, "The log records every write (old + new value) BEFORE the data page changes —\n"
            "so a crash can UNDO (old value) or REDO (new value).",
            ha="center", fontsize=10, style="italic", color=GREY)
    save(fig, "s37_log.png")


# ---------- S38 : ACID four-quadrant ----------
def acid():
    fig, ax = canvas(10, 5.4)
    quad = [("A — Atomicity", "all operations happen,\nor none do", BLUE, 4, 52),
            ("C — Consistency", "valid state → valid state\n(sum of money preserved)", TEAL, 51, 52),
            ("I — Isolation", "concurrent txns don't\ninterfere (appear alone)", AMBER, 4, 6),
            ("D — Durability", "once committed, it\nsurvives any later crash", CORAL, 51, 6)]
    for head, sub, c, x, y in quad:
        box(ax, x, y, 45, 40, "", fc=c)
        ax.text(x+22.5, y+30, head, ha="center", color=WHITE, fontsize=14, fontweight="bold")
        ax.text(x+22.5, y+15, sub, ha="center", color=WHITE, fontsize=10.5)
    save(fig, "s38_acid.png")


# ---------- S39 : lost update timeline ----------
def lost_update():
    fig, ax = canvas(10, 5.2)
    ax.text(27, 94, "T1  (Rita +500)", ha="center", fontsize=12, fontweight="bold", color=BLUE)
    ax.text(73, 94, "T2  (Hari +300)", ha="center", fontsize=12, fontweight="bold", color=CORAL)
    ax.plot([50, 50], [4, 88], color=LGREY, lw=1.2, ls="--")
    steps = [("read bal = 1000", BLUE, 27, 80),
             ("read bal = 1000", CORAL, 73, 68),
             ("write 1500", BLUE, 27, 56),
             ("write 1300", CORAL, 73, 44)]
    for txt, c, x, y in steps:
        box(ax, x-18, y, 36, 9, txt, fc=c, fs=10.5)
    arrow(ax, 50, 84, 50, 8, color=GREY, lw=1.6)
    ax.text(52, 20, "time", fontsize=9, color=GREY)
    ax.text(50, 30, "Final balance = 1300  ✗   (T1's +500 is LOST)",
            ha="center", fontsize=11.5, fontweight="bold", color=CORAL)
    ax.text(50, 20, "Correct answer should be 1800. Both read the same old value → one update overwrites the other.",
            ha="center", fontsize=9, style="italic", color=GREY)
    save(fig, "s39_lost_update.png")


# ---------- S39 : precedence graphs (acyclic vs cyclic) ----------
def precedence():
    fig, ax = canvas(10, 4.8)
    ax.text(25, 92, "No cycle → SERIALIZABLE", ha="center", fontsize=12, fontweight="bold", color=TEAL)
    circle(ax, 12, 55, 6.5, "T1", fc=BLUE)
    circle(ax, 30, 55, 6.5, "T2", fc=BLUE)
    circle(ax, 21, 30, 6.5, "T3", fc=BLUE)
    arrow(ax, 18.5, 55, 23.5, 55, color=TEAL, lw=2.4)
    arrow(ax, 27, 49, 23, 36, color=TEAL, lw=2.4)
    ax.text(21, 12, "T1→T2→T3, no way back\n= equals a serial order", ha="center", fontsize=9, color=GREY, style="italic")
    ax.text(75, 92, "Cycle → NOT serializable", ha="center", fontsize=12, fontweight="bold", color=CORAL)
    circle(ax, 66, 55, 6.5, "T1", fc=CORAL)
    circle(ax, 84, 55, 6.5, "T2", fc=CORAL)
    arrow(ax, 72, 57, 78, 57, color=CORAL, lw=2.4)
    arrow(ax, 78, 53, 72, 53, color=CORAL, lw=2.4)
    ax.text(75, 12, "T1→T2 AND T2→T1\n= no equivalent serial order", ha="center", fontsize=9, color=GREY, style="italic")
    save(fig, "s39_precedence.png")


# ---------- S40 : 2PL growing / shrinking phase curve ----------
def phases():
    fig, ax = canvas(10, 4.8)
    ax.plot([8, 8], [15, 82], color=GREY, lw=1.4)   # y axis
    ax.plot([8, 92], [15, 15], color=GREY, lw=1.4)  # x axis
    ax.text(4, 50, "locks\nheld", ha="center", va="center", fontsize=10, color=GREY, rotation=90)
    ax.text(50, 7, "time  →", ha="center", fontsize=10, color=GREY)
    ax.plot([8, 45], [15, 75], color=BLUE, lw=3)    # growing
    ax.plot([45, 82], [75, 15], color=CORAL, lw=3)  # shrinking
    ax.plot(45, 75, "o", color=NAVY, ms=9)
    ax.text(45, 82, "LOCK POINT (one peak)", ha="center", fontsize=10, fontweight="bold", color=NAVY)
    ax.text(26, 40, "GROWING\nonly acquire locks", ha="center", fontsize=10.5, fontweight="bold", color=BLUE)
    ax.text(66, 40, "SHRINKING\nonly release locks", ha="center", fontsize=10.5, fontweight="bold", color=CORAL)
    ax.text(50, 1, "Once you release the first lock you may never acquire another — this single peak guarantees serializability.",
            ha="center", fontsize=8.8, style="italic", color=GREY)
    save(fig, "s40_phases.png")


# ---------- S40 : deadlock wait-for graph ----------
def deadlock():
    fig, ax = canvas(10, 4.6)
    circle(ax, 32, 55, 9, "T1", fc=BLUE)
    circle(ax, 68, 55, 9, "T2", fc=CORAL)
    arrow(ax, 41, 59, 59, 59, color=NAVY, lw=2.4)
    ax.text(50, 66, "waits for lock held by", ha="center", fontsize=9, color=GREY, style="italic")
    arrow(ax, 59, 51, 41, 51, color=NAVY, lw=2.4)
    ax.text(50, 42, "waits for lock held by", ha="center", fontsize=9, color=GREY, style="italic")
    ax.text(50, 22, "T1 holds Rita's row & wants Hari's; T2 holds Hari's row & wants Rita's.",
            ha="center", fontsize=10, color=INK)
    ax.text(50, 12, "CYCLE in the wait-for graph = DEADLOCK → abort one 'victim' to break it.",
            ha="center", fontsize=10.5, fontweight="bold", color=CORAL)
    save(fig, "s40_deadlock.png")


# ---------- S41 : timestamp ordering ----------
def timestamps():
    fig, ax = canvas(10, 4.8)
    box(ax, 33, 74, 34, 16, "Data item  X", fc=NAVY, fs=13)
    box(ax, 6, 44, 40, 15, "read_TS(X)\n= newest reader's TS", fc=BLUE, fs=10.5)
    box(ax, 54, 44, 40, 15, "write_TS(X)\n= newest writer's TS", fc=TEAL, fs=10.5)
    arrow(ax, 40, 74, 26, 59, color=GREY, lw=1.6)
    arrow(ax, 60, 74, 74, 59, color=GREY, lw=1.6)
    ax.text(50, 30, "Each txn gets a unique timestamp TS at start (older TS = higher priority).",
            ha="center", fontsize=10, color=INK)
    ax.text(50, 20, "An op that violates timestamp order  →  the txn is ABORTED & RESTARTED with a larger TS.",
            ha="center", fontsize=10.5, fontweight="bold", color=CORAL)
    ax.text(50, 9, "No locks, no waiting  →  no deadlock (but possible starvation from repeated restarts).",
            ha="center", fontsize=9.5, style="italic", color=GREY)
    save(fig, "s41_timestamps.png")


# ---------- S42 : deferred update + recovery ----------
def deferred():
    fig, ax = canvas(10, 5.0)
    ax.plot([6, 94], [70, 70], color=GREY, lw=1.6)
    for x, lbl in [(18, "[start,T1]"), (38, "checkpoint"), (58, "[commit,T1]"), (78, "CRASH")]:
        ax.plot([x, x], [67, 73], color=GREY, lw=1.4)
        ax.text(x, 78, lbl, ha="center", fontsize=8.5, color=(CORAL if lbl=="CRASH" else GREY),
                fontweight=("bold" if lbl=="CRASH" else "normal"))
    ax.text(50, 88, "Deferred update  (NO-UNDO / REDO)", ha="center", fontsize=13, fontweight="bold", color=NAVY)
    box(ax, 8, 40, 40, 16, "Has [start] AND [commit]\nbefore crash", fc=TEAL, fs=10.5)
    box(ax, 52, 40, 40, 16, "Has [start] but NO [commit]", fc=CORAL, fs=10.5)
    arrow(ax, 28, 40, 28, 30, color=TEAL, lw=2)
    arrow(ax, 72, 40, 72, 30, color=CORAL, lw=2)
    box(ax, 10, 14, 36, 14, "REDO from log\n(reapply new values)", fc=TEAL, fs=10.5)
    box(ax, 54, 14, 36, 14, "IGNORE — nothing to undo\n(DB never changed)", fc=GREY, fs=10)
    ax.text(50, 5, "Writes are deferred until AFTER commit → uncommitted txns never touched the DB (no undo needed).",
            ha="center", fontsize=8.8, style="italic", color=GREY)
    save(fig, "s42_deferred.png")


# ---------- S43 : immediate update recovery ----------
def immediate():
    fig, ax = canvas(10, 5.0)
    ax.text(50, 92, "Immediate update  (UNDO / REDO)", ha="center", fontsize=13, fontweight="bold", color=NAVY)
    box(ax, 20, 68, 60, 13, "DB is updated WHILE the txn is active (WAL enforced)", fc=BLUE, fs=10.5)
    box(ax, 6, 40, 40, 16, "Committed before crash", fc=TEAL, fs=11)
    box(ax, 54, 40, 40, 16, "Uncommitted at crash", fc=CORAL, fs=11)
    arrow(ax, 26, 40, 26, 30, color=TEAL, lw=2)
    arrow(ax, 74, 40, 74, 30, color=CORAL, lw=2)
    box(ax, 8, 12, 36, 15, "REDO\n(reapply new values,\nforward order)", fc=TEAL, fs=10)
    box(ax, 56, 12, 36, 15, "UNDO\n(restore old values,\nreverse order)", fc=CORAL, fs=10)
    ax.text(50, 3, "Writing early means a crash can leave half-done changes on disk → you MUST be able to UNDO.",
            ha="center", fontsize=8.8, style="italic", color=GREY)
    save(fig, "s43_immediate.png")


# ---------- S43 : shadow paging ----------
def shadow():
    fig, ax = canvas(10, 5.0)
    box(ax, 6, 70, 34, 14, "Shadow (old) page table", fc=GREY, fs=11)
    box(ax, 60, 70, 34, 14, "Current (new) page table", fc=BLUE, fs=11)
    box(ax, 6, 40, 16, 12, "Page 1", fc=PALEB, tc=INK, fs=10, ec=GREY, lw=1)
    box(ax, 24, 40, 16, 12, "Page 2", fc=PALEB, tc=INK, fs=10, ec=GREY, lw=1)
    box(ax, 60, 40, 16, 12, "Page 1", fc=PALEB, tc=INK, fs=10, ec=BLUE, lw=1)
    box(ax, 78, 40, 16, 12, "Page 2'", fc=PALET, tc=INK, fs=10, ec=TEAL, lw=1.4)
    arrow(ax, 23, 70, 14, 52, color=GREY, lw=1.5)
    arrow(ax, 31, 70, 32, 52, color=GREY, lw=1.5)
    arrow(ax, 76, 70, 68, 52, color=BLUE, lw=1.5)
    arrow(ax, 80, 70, 86, 52, color=TEAL, lw=1.8)
    ax.text(86, 34, "new copy\nof changed page", ha="center", fontsize=8.5, color=TEAL, style="italic")
    ax.text(50, 22, "COMMIT = atomically switch the pointer to the new page table.",
            ha="center", fontsize=11, fontweight="bold", color=TEAL)
    ax.text(50, 12, "ABORT = just discard the new pages and keep the shadow — no undo log needed.",
            ha="center", fontsize=10, color=INK)
    ax.text(50, 3, "Analogy: edit a photocopy; make it official on success, tear it up on abort.",
            ha="center", fontsize=8.8, style="italic", color=GREY)
    save(fig, "s43_shadow.png")


# ---------- S44 : 3-2-1 backup + RPO/RTO ----------
def backup():
    fig, ax = canvas(10, 5.0)
    ax.text(27, 92, "The 3-2-1 backup rule", ha="center", fontsize=12.5, fontweight="bold", color=NAVY)
    box(ax, 4, 66, 44, 13, "3  copies of the data", fc=BLUE, fs=11)
    box(ax, 4, 50, 44, 13, "2  different media/devices", fc=TEAL, fs=11)
    box(ax, 4, 34, 44, 13, "1  copy off-site (other city/cloud)", fc=AMBER, fs=10.5)
    ax.text(27, 24, "Survives a destroyed data-center:\nrestore backup + REDO archived log.",
            ha="center", fontsize=9.5, style="italic", color=GREY)
    ax.text(75, 92, "RPO vs RTO on a failure axis", ha="center", fontsize=12, fontweight="bold", color=NAVY)
    ax.plot([54, 96], [56, 56], color=GREY, lw=1.6)
    ax.plot([72, 72], [52, 60], color=CORAL, lw=2)
    ax.text(72, 64, "FAILURE", ha="center", fontsize=9, fontweight="bold", color=CORAL)
    ax.plot([62, 62], [53, 59], color=BLUE, lw=1.6)
    ax.text(62, 46, "last backup", ha="center", fontsize=8.5, color=BLUE)
    box(ax, 55, 30, 18, 10, "RPO\ndata lost", fc=BLUE, fs=9)
    box(ax, 76, 30, 18, 10, "RTO\ntime to restore", fc=TEAL, fs=9)
    ax.text(75, 18, "RPO = how much data you can afford to lose;\nRTO = how fast you must be back up.",
            ha="center", fontsize=9, style="italic", color=GREY)
    save(fig, "s44_backup.png")


for fn in [states, log_timeline, acid, lost_update, precedence, phases, deadlock,
           timestamps, deferred, immediate, shadow, backup]:
    fn()

print("\nAll images written to", OUT)
