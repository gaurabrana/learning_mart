#!/usr/bin/env python3
"""Concept diagrams for IT220 Unit 4 — Database Normalization (S18–S21).
Running example: ENROLL(StudentRoll, StudentName, StudentPhone[multi], CourseCode,
CourseTitle, InstructorID, InstructorName, InstructorDept, Grade) decomposed 1NF→BCNF/4NF.
License-safe, purpose-built. Output -> fourth/images/   Run: python3 build_unit4_images.py
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch

OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"images"); os.makedirs(OUT,exist_ok=True)
NAVY="#0C2B4A"; BLUE="#185FA5"; TEAL="#0F6E56"; AMBER="#B07A1E"; CORAL="#993C1D"
GREY="#55606B"; LGREY="#C7CFD6"; PALEB="#E6F1FB"; PALET="#E1F5EE"; PALEA="#FAEEDA"; PALEC="#FAECE7"
WHITE="#FFFFFF"; INK="#1A1A1A"
plt.rcParams["font.family"]="DejaVu Sans"

def canvas(w=10,h=5.6):
    fig,ax=plt.subplots(figsize=(w,h)); ax.set_xlim(0,100); ax.set_ylim(0,100); ax.axis("off"); return fig,ax
def save(fig,name):
    fig.savefig(os.path.join(OUT,name),dpi=150,bbox_inches="tight",facecolor="white",pad_inches=0.15)
    plt.close(fig); print("wrote",name)
def rbox(ax,x,y,w,h,text,fc=BLUE,tc=WHITE,fs=11,ec="none",bold=True):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.02,rounding_size=2",fc=fc,ec=ec,lw=1.4,mutation_aspect=0.5,zorder=3))
    ax.text(x+w/2,y+h/2,text,ha="center",va="center",color=tc,fontsize=fs,fontweight="bold" if bold else "normal",zorder=4)
def arrow(ax,x1,y1,x2,y2,color=NAVY,lw=2.0):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle="-|>",mutation_scale=14,color=color,lw=lw,zorder=2))
def caption(ax,text,color=GREY,y=4,fs=10.5):
    ax.text(50,y,text,ha="center",fontsize=fs,style="italic",color=color)
def table(ax,x,y,headers,rows,colw,rowh=6.5,fs=8.5,hl=None,title=None,fc_hdr=NAVY,tcol=None):
    """hl: set of (row,col) to shade coral (redundant); tcol title color."""
    hl=hl or set()
    if title: ax.text(x+sum(colw)/2,y+rowh+2.5,title,ha="center",color=tcol or NAVY,fontsize=fs+2,fontweight="bold")
    cx=x
    for j,h in enumerate(headers):
        ax.add_patch(Rectangle((cx,y),colw[j],rowh,fc=fc_hdr,ec=WHITE,lw=1,zorder=3))
        ax.text(cx+colw[j]/2,y+rowh/2,h,ha="center",va="center",color=WHITE,fontsize=fs,fontweight="bold",zorder=4)
        cx+=colw[j]
    for i,row in enumerate(rows):
        ry=y-(i+1)*rowh; cx=x
        for j,val in enumerate(row):
            fc=PALEC if (i,j) in hl else WHITE
            ax.add_patch(Rectangle((cx,ry),colw[j],rowh,fc=fc,ec=LGREY,lw=0.7,zorder=2))
            ax.text(cx+colw[j]/2,ry+rowh/2,str(val),ha="center",va="center",color=INK,fontsize=fs,zorder=3)
            cx+=colw[j]
    return sum(colw),(len(rows)+1)*rowh

# ---------- S18 ----------
def s18_anomalies():
    fig,ax=canvas(10,5.6)
    ax.text(50,96,"ENROLL — everything in one table → redundancy",ha="center",color=NAVY,fontsize=12,fontweight="bold")
    H=["Roll","Name","Course","Title","Instr","Dept","Grade"]
    R=[["101","Sita","DBMS","Database","I5","CSIT","A"],
       ["101","Sita","Java","Prog-I","I7","CSIT","B"],
       ["102","Hari","DBMS","Database","I5","CSIT","A"],
       ["103","Gita","DBMS","Database","I5","CSIT","C"]]
    # redundant cells: DBMS/Database/I5/CSIT repeated in rows 0,2,3
    hl={(0,2),(0,3),(0,4),(0,5),(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4),(3,5)}
    table(ax,6,78,H,R,colw=[9,12,12,15,9,10,10],hl=hl)
    ax.text(50,30,"Repeated (pink) cells = redundancy → three anomalies:",ha="center",color=CORAL,fontsize=10,fontweight="bold")
    rbox(ax,4,10,29,15,"INSERTION\ncan't add a course\nuntil someone enrolls",fc=CORAL,fs=9)
    rbox(ax,36,10,28,15,"DELETION\ndrop the last student →\ncourse facts vanish",fc=AMBER,fs=9)
    rbox(ax,67,10,29,15,"UPDATE\ninstructor's dept changes →\nfix many rows or go inconsistent",fc=BLUE,fs=9)
    save(fig,"s18_anomalies.png")

def s18_fd():
    fig,ax=canvas(10,4.8)
    ax.text(50,94,"Functional dependencies:  X → Y  ('X determines exactly one Y')",ha="center",color=NAVY,fontsize=12,fontweight="bold")
    fds=[("StudentRoll","StudentName",78),
         ("CourseCode","CourseTitle",62),
         ("InstructorID","InstructorName, InstructorDept",46),
         ("{StudentRoll, CourseCode}","Grade   (the whole key → Grade)",30)]
    for x,y_ in [(0,0)]: pass
    for lhs,rhs,y in fds:
        rbox(ax,6,y-5,34,10,lhs,fc=TEAL,fs=9.5)
        arrow(ax,40,y,52,y,color=NAVY)
        rbox(ax,52,y-5,44,10,rhs,fc=BLUE,fs=9.5)
    ax.text(50,14,"Key = {StudentRoll, CourseCode} — together they determine every attribute.",ha="center",color=NAVY,fontsize=10,fontweight="bold")
    caption(ax,"FDs come from real-world rules, not today's data — and they are one-directional (Roll→Name, not Name→Roll).",y=5)
    save(fig,"s18_fd.png")

# ---------- S19 ----------
def s19_1nf():
    fig,ax=canvas(10,4.6)
    table(ax,4,80,["Roll","Name","Phone"],[["101","Sita","9801, 9842, 9818"]],colw=[10,14,26],fs=9,
          title="✗ NOT 1NF — a list in one cell",fc_hdr=CORAL,tcol=CORAL,hl={(0,2)})
    arrow(ax,54,64,64,64)
    table(ax,66,80,["Roll","Phone"],[["101","9801"],["101","9842"],["101","9818"]],colw=[10,16],fs=9,
          title="✓ 1NF — atomic, one per row",fc_hdr=TEAL,tcol=TEAL)
    caption(ax,"1NF: every cell holds ONE atomic value — no lists, no repeating groups. Split the multivalued phone into its own rows/table.",y=14,fs=10)
    save(fig,"s19_1nf.png")

# ---------- S20 ----------
def s20_2nf():
    fig,ax=canvas(10,5.0)
    ax.text(50,95,"2NF — remove PARTIAL dependencies on the composite key {Roll, Course}",ha="center",color=NAVY,fontsize=11.5,fontweight="bold")
    table(ax,4,84,["Roll","Name","Course","Title","Grade"],[["101","Sita","DBMS","Database","A"]],colw=[9,12,11,14,9],fs=8.5,
          title="ENROLL_1NF (key = Roll+Course)")
    ax.text(24,60,"Roll → Name   (½ key)",ha="center",color=CORAL,fontsize=9,fontweight="bold")
    ax.text(52,60,"Course → Title  (½ key)",ha="center",color=CORAL,fontsize=9,fontweight="bold")
    arrow(ax,50,54,50,46)
    table(ax,4,40,["Roll","Name"],[["101","Sita"]],colw=[10,14],fs=8.5,title="STUDENT",fc_hdr=TEAL,tcol=TEAL)
    table(ax,34,40,["Course","Title"],[["DBMS","Database"]],colw=[12,16],fs=8.5,title="COURSE",fc_hdr=TEAL,tcol=TEAL)
    table(ax,70,40,["Roll","Course","Grade"],[["101","DBMS","A"]],colw=[9,11,9],fs=8.5,title="ENROLL",fc_hdr=TEAL,tcol=TEAL)
    caption(ax,"A non-key attribute must depend on the WHOLE key, not half of it. (Single-column keys are automatically 2NF.)",y=6,fs=10)
    save(fig,"s20_2nf.png")

def s20_3nf():
    fig,ax=canvas(10,4.8)
    ax.text(50,95,"3NF — remove TRANSITIVE dependencies through a non-key",ha="center",color=NAVY,fontsize=11.5,fontweight="bold")
    table(ax,4,82,["Course","Title","InstrID","InstrName","InstrDept"],[["DBMS","Database","I5","Sharma","CSIT"]],
          colw=[11,13,10,12,10],fs=8.5,title="COURSE (before)")
    ax.text(38,58,"Course → InstrID → InstrName, InstrDept   (transitive!)",ha="center",color=AMBER,fontsize=9.5,fontweight="bold")
    arrow(ax,50,52,50,44)
    table(ax,10,38,["Course","Title","InstrID"],[["DBMS","Database","I5"]],colw=[11,13,10],fs=8.5,title="COURSE",fc_hdr=TEAL,tcol=TEAL)
    table(ax,54,38,["InstrID","InstrName","InstrDept"],[["I5","Sharma","CSIT"]],colw=[10,13,11],fs=8.5,title="INSTRUCTOR",fc_hdr=TEAL,tcol=TEAL)
    caption(ax,"A non-key attribute must not depend on another non-key attribute. Break the key→non-key→non-key chain.",y=8,fs=10)
    save(fig,"s20_3nf.png")

def s20_final():
    fig,ax=canvas(10,4.4)
    ax.text(50,94,"Final 3NF design — five clean tables, anomalies gone",ha="center",color=NAVY,fontsize=12,fontweight="bold")
    boxes=[("STUDENT","Roll (PK), Name",6,64),
           ("STUDENT_PHONE","Roll (FK), Phone",38,64),
           ("COURSE","Course (PK), Title, InstrID (FK)",70,64),
           ("INSTRUCTOR","InstrID (PK), Name, Dept",6,34),
           ("ENROLL","Roll (FK), Course (FK), Grade",44,34)]
    for name,cols,x,y in boxes:
        rbox(ax,x,y,26,16,"",fc=PALET,ec=TEAL); ax.text(x+13,y+11,name,ha="center",color=NAVY,fontsize=9.5,fontweight="bold")
        ax.text(x+13,y+4,cols,ha="center",color=INK,fontsize=7.5)
    caption(ax,"Add a course with no students ✓  ·  drop last student, keep the course ✓  ·  change instructor's dept in ONE place ✓",y=12,fs=9.5)
    save(fig,"s20_final.png")

# ---------- S21 ----------
def s21_bcnf():
    fig,ax=canvas(10,4.8)
    ax.text(50,95,"BCNF — every determinant must be a SUPERKEY (stricter than 3NF)",ha="center",color=NAVY,fontsize=11.5,fontweight="bold")
    table(ax,4,82,["Course","Instructor","Room"],[["DBMS","Sharma","R1"],["Java","Sharma","R1"],["OS","Gurung","R2"]],
          colw=[12,15,10],fs=8.5,title="SECTION — 3NF-OK but…")
    ax.text(30,44,"Instructor → Room, but Instructor\nis NOT a superkey → BCNF violation",ha="center",color=CORAL,fontsize=9.5,fontweight="bold")
    arrow(ax,52,40,62,40)
    table(ax,64,74,["Instructor","Room"],[["Sharma","R1"],["Gurung","R2"]],colw=[15,10],fs=8.5,title="ROOM_OF",fc_hdr=TEAL,tcol=TEAL)
    table(ax,64,42,["Course","Instructor"],[["DBMS","Sharma"],["OS","Gurung"]],colw=[12,15],fs=8.5,title="TEACHES",fc_hdr=TEAL,tcol=TEAL)
    caption(ax,"3NF can tolerate a non-superkey determinant; BCNF does not. Split so every determinant is a key.",y=6,fs=10)
    save(fig,"s21_bcnf.png")

def s21_mvd():
    fig,ax=canvas(10,4.8)
    ax.text(50,95,"MVD & 4NF — independent multivalued facts explode into rows",ha="center",color=NAVY,fontsize=11.5,fontweight="bold")
    table(ax,4,82,["Roll","Course","Hobby"],
          [["1","DBMS","Music"],["1","DBMS","Football"],["1","Java","Music"],["1","Java","Football"]],
          colw=[8,14,14],fs=8.5,title="✗ courses × hobbies (redundant)",fc_hdr=CORAL,tcol=CORAL)
    arrow(ax,50,60,60,60)
    table(ax,62,80,["Roll","Course"],[["1","DBMS"],["1","Java"]],colw=[8,14],fs=8.5,title="STU_COURSE",fc_hdr=TEAL,tcol=TEAL)
    table(ax,62,52,["Roll","Hobby"],[["1","Music"],["1","Football"]],colw=[8,15],fs=8.5,title="STU_HOBBY",fc_hdr=TEAL,tcol=TEAL)
    caption(ax,"Courses and hobbies are INDEPENDENT — one table forces every pairing (2×2=4). 4NF splits the two MVDs apart.",y=8,fs=10)
    save(fig,"s21_mvd.png")

def s21_lossless():
    fig,ax=canvas(10,4.8)
    ax.text(50,95,"Lossless join — rejoining must give back EXACTLY the original",ha="center",color=NAVY,fontsize=11.5,fontweight="bold")
    rbox(ax,4,74,44,14,"✓ LOSSLESS",fc=TEAL,fs=11)
    ax.text(26,66,"shared attribute is a KEY of one table →\nSTUDENT ⋈ ENROLL rebuilds the original",ha="center",color=INK,fontsize=9)
    rbox(ax,52,74,44,14,"✗ LOSSY",fc=CORAL,fs=11)
    ax.text(74,66,"careless split loses the link →\nre-join invents SPURIOUS extra rows",ha="center",color=INK,fontsize=9)
    ax.text(50,44,"Rule: a binary decomposition is lossless if the shared attribute is a\nsuperkey of at least one of the two resulting tables.",ha="center",color=NAVY,fontsize=10,fontweight="bold")
    ax.text(50,22,"Dependency preservation: every original FD can still be checked WITHOUT re-joining.\nSometimes we keep 3NF (not BCNF) to preserve a dependency — a real trade-off.",
            ha="center",color=GREY,fontsize=9.5,style="italic")
    save(fig,"s21_lossless.png")

def s21_ladder():
    fig,ax=canvas(10,5.2)
    ax.text(50,96,"The normalization ladder",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    rungs=[("1NF","atomic values · no repeating groups / lists in a cell",TEAL),
           ("2NF","1NF + no PARTIAL dependency on a composite key",TEAL),
           ("3NF","2NF + no TRANSITIVE dependency through a non-key",BLUE),
           ("BCNF","every determinant is a superkey (stricter 3NF)",BLUE),
           ("4NF","BCNF + no independent multivalued dependency",AMBER)]
    y=80
    for nf,desc,c in rungs:
        rbox(ax,8,y-7,16,12,nf,fc=c,fs=12)
        ax.text(28,y-1,desc,ha="left",va="center",color=INK,fontsize=10)
        if y>20: arrow(ax,16,y-7,16,y-13,color=GREY,lw=1.8)
        y-=15
    caption(ax,"Each rung removes a specific class of anomaly. Final gate: is the decomposition LOSSLESS (and dependency-preserving)?",y=3,fs=10)
    save(fig,"s21_ladder.png")

for fn in [s18_anomalies,s18_fd,s19_1nf,s20_2nf,s20_3nf,s20_final,s21_bcnf,s21_mvd,s21_lossless,s21_ladder]:
    fn()
print("\nAll Unit 4 images written to",OUT)
