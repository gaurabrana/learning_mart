#!/usr/bin/env python3
"""Concept diagrams for IT220 Unit 3 — Relational Algebra & Relational Calculus (S13–S17).
Running schema: Student(sid,name,program,city) · Enrollment(sid,course,grade) · Course(course,credit).
License-safe, purpose-built. Output -> fourth/images/   Run: python3 build_unit3_images.py
"""
import os, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, FancyArrowPatch

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
os.makedirs(OUT, exist_ok=True)
NAVY="#0C2B4A"; BLUE="#185FA5"; TEAL="#0F6E56"; AMBER="#B07A1E"; CORAL="#993C1D"
GREY="#55606B"; LGREY="#C7CFD6"; PALEB="#E6F1FB"; PALET="#E1F5EE"; PALEA="#FAEEDA"; PALEC="#FAECE7"
WHITE="#FFFFFF"; INK="#1A1A1A"
plt.rcParams["font.family"]="DejaVu Sans"

def canvas(w=10,h=5.6):
    fig,ax=plt.subplots(figsize=(w,h)); ax.set_xlim(0,100); ax.set_ylim(0,100); ax.axis("off"); return fig,ax
def save(fig,name):
    fig.savefig(os.path.join(OUT,name),dpi=150,bbox_inches="tight",facecolor="white",pad_inches=0.15)
    plt.close(fig); print("wrote",name)
def rbox(ax,x,y,w,h,text,fc=BLUE,tc=WHITE,fs=12,ec="none",bold=True):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.02,rounding_size=2.2",fc=fc,ec=ec,lw=1.4,mutation_aspect=0.5,zorder=3))
    ax.text(x+w/2,y+h/2,text,ha="center",va="center",color=tc,fontsize=fs,fontweight="bold" if bold else "normal",zorder=4)
def arrow(ax,x1,y1,x2,y2,color=NAVY,lw=2.2):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle="-|>",mutation_scale=16,color=color,lw=lw,zorder=2))
def caption(ax,text,color=GREY,y=4,fs=11):
    ax.text(50,y,text,ha="center",fontsize=fs,style="italic",color=color)

def table(ax,x,y,headers,rows,colw=None,rowh=7,fs=9,hl_rows=None,hl_cols=None,title=None,fc_hdr=NAVY):
    """Draw a relation table with top-left at (x,y). hl_rows/hl_cols highlight (0-based data index)."""
    n=len(headers); colw=colw or [16]*n
    if title: ax.text(x+sum(colw)/2,y+rowh+3,title,ha="center",color=NAVY,fontsize=fs+2,fontweight="bold")
    # header
    cx=x
    for j,htext in enumerate(headers):
        ax.add_patch(Rectangle((cx,y),colw[j],rowh,fc=fc_hdr,ec=WHITE,lw=1,zorder=3))
        ax.text(cx+colw[j]/2,y+rowh/2,htext,ha="center",va="center",color=WHITE,fontsize=fs,fontweight="bold",zorder=4)
        cx+=colw[j]
    # rows
    for i,row in enumerate(rows):
        ry=y-(i+1)*rowh; cx=x
        for j,val in enumerate(row):
            fc=WHITE
            if hl_cols and j in hl_cols: fc=PALEB
            if hl_rows and i in hl_rows: fc=PALET
            if hl_rows and hl_cols and i in hl_rows and j in hl_cols: fc="#CFE8DD"
            ax.add_patch(Rectangle((cx,ry),colw[j],rowh,fc=fc,ec=LGREY,lw=0.8,zorder=2))
            ax.text(cx+colw[j]/2,ry+rowh/2,str(val),ha="center",va="center",color=INK,fontsize=fs,zorder=3)
            cx+=colw[j]
    return sum(colw), (len(rows)+1)*rowh

STU_H=["sid","name","prog","city"]
STU=[["1","Sita","BIM","Pokhara"],["2","Hari","BIM","Kathmandu"],["3","Gita","BCA","Pokhara"],["4","Ram","BIM","Butwal"]]
ENR_H=["sid","course","grade"]
ENR=[["1","DBMS","A"],["1","Java","B"],["2","DBMS","A"],["3","Java","C"]]

# ---------- S13 ----------
def s13_closure():
    fig,ax=canvas(10,4.0)
    rbox(ax,4,42,20,20,"RELATION\n(input table)",fc=BLUE,fs=11)
    rbox(ax,40,44,20,16,"operation\nσ π ⋈ ∪ ...",fc=TEAL,fs=11)
    rbox(ax,76,42,20,20,"RELATION\n(output table)",fc=BLUE,fs=11)
    arrow(ax,24,52,40,52); arrow(ax,60,52,76,52)
    ax.text(86,32,"↺ output is a relation,\nso it can feed the next op",ha="center",color=GREY,fontsize=9)
    caption(ax,"Closure: every operation takes relation(s) in and gives a relation out — so operations chain.",y=12)
    save(fig,"s13_closure.png")

def s13_select_project():
    fig,ax=canvas(10,5.2)
    table(ax,3,86,STU_H,STU,colw=[7,12,9,13],title="σ  SELECT = rows (horizontal cut)",hl_rows=[0,2])
    table(ax,54,86,STU_H,STU,colw=[7,12,9,13],title="π  PROJECT = columns (vertical cut)",hl_cols=[1,2])
    ax.text(23,20,"σ_city='Pokhara'(Student)\nkeeps matching ROWS",ha="center",color=TEAL,fontsize=9.5,fontweight="bold")
    ax.text(74,20,"π_name,prog(Student)\nkeeps chosen COLUMNS",ha="center",color=BLUE,fontsize=9.5,fontweight="bold")
    ax.text(50,7,"⚠ Naming trap: SQL's keyword SELECT does π's job (columns), NOT σ.",ha="center",color=CORAL,fontsize=10,fontweight="bold")
    save(fig,"s13_select_project.png")

# ---------- S14 ----------
def venn(ax,cx,cy,r,mode,label):
    # two circles R (left), S (right)
    lx,rx=cx-r*0.55,cx+r*0.55
    if mode=="union":
        ax.add_patch(Circle((lx,cy),r,fc=PALET,ec=TEAL,lw=1.6,zorder=2,alpha=0.9))
        ax.add_patch(Circle((rx,cy),r,fc=PALET,ec=TEAL,lw=1.6,zorder=2,alpha=0.9))
    elif mode=="inter":
        ax.add_patch(Circle((lx,cy),r,fc=WHITE,ec=TEAL,lw=1.6,zorder=2))
        ax.add_patch(Circle((rx,cy),r,fc=WHITE,ec=TEAL,lw=1.6,zorder=2))
        # lens
        ax.add_patch(Circle((lx,cy),r,fc="none",ec="none"));
        from matplotlib.patches import Wedge
        ax.add_patch(Circle(((lx+rx)/2,cy),r*0.5,fc=PALET,ec="none",zorder=1,alpha=0.9))
    else: # diff R-S
        ax.add_patch(Circle((lx,cy),r,fc=PALEC,ec=CORAL,lw=1.6,zorder=1))
        ax.add_patch(Circle((rx,cy),r,fc=WHITE,ec=GREY,lw=1.4,zorder=2))
        ax.add_patch(Circle((lx,cy),r,fc="none",ec=CORAL,lw=1.6,zorder=3))
    ax.text(lx,cy,"R",ha="center",va="center",fontsize=11,color=NAVY,fontweight="bold",zorder=5)
    ax.text(rx,cy,"S",ha="center",va="center",fontsize=11,color=NAVY,fontweight="bold",zorder=5)
    ax.text(cx,cy-r-6,label,ha="center",fontsize=11,color=NAVY,fontweight="bold")

def s14_set_ops():
    fig,ax=canvas(10,4.2)
    venn(ax,18,58,13,"union","UNION  R ∪ S\n(in R or S)")
    venn(ax,50,58,13,"inter","INTERSECTION  R ∩ S\n(in both)")
    venn(ax,82,58,13,"diff","DIFFERENCE  R − S\n(in R, not S)")
    caption(ax,"∪ ∩ − need UNION-COMPATIBLE relations (same #columns, matching domains). − is order-sensitive: R−S ≠ S−R.",y=10,fs=10)
    save(fig,"s14_set_ops.png")

def s14_cartesian():
    fig,ax=canvas(10,4.8)
    ax.text(50,95,"CARTESIAN PRODUCT  ×  pairs EVERY row with EVERY row",ha="center",color=NAVY,fontsize=12,fontweight="bold")
    students=["Sita","Hari","Gita","Ram"]; courses=["DBMS","Java","OS"]
    x0,y0,cw,ch=20,72,20,11
    for j,c in enumerate(courses):
        ax.add_patch(Rectangle((x0+j*cw,y0),cw,ch,fc=BLUE,ec=WHITE,lw=1,zorder=3))
        ax.text(x0+j*cw+cw/2,y0+ch/2,c,ha="center",va="center",color=WHITE,fontsize=9,fontweight="bold",zorder=4)
    for i,s in enumerate(students):
        ry=y0-(i+1)*ch
        ax.add_patch(Rectangle((x0-cw,ry),cw,ch,fc=TEAL,ec=WHITE,lw=1,zorder=3))
        ax.text(x0-cw/2,ry+ch/2,s,ha="center",va="center",color=WHITE,fontsize=9,fontweight="bold",zorder=4)
        for j in range(len(courses)):
            ax.add_patch(Rectangle((x0+j*cw,ry),cw,ch,fc=WHITE,ec=LGREY,lw=0.8,zorder=2))
            ax.text(x0+j*cw+cw/2,ry+ch/2,"•",ha="center",va="center",color=GREY,fontsize=11,zorder=3)
    ax.text(50,6,"4 students × 3 courses = 12 pairings — most meaningless until you add a condition (→ JOIN, S15).",
            ha="center",color=CORAL,fontsize=10,fontweight="bold",style="italic")
    save(fig,"s14_cartesian.png")

# ---------- S15 ----------
def s15_join():
    fig,ax=canvas(10,5.0)
    ax.text(50,95,"JOIN  =  ×  then keep only rows where the condition matches",ha="center",color=NAVY,fontsize=12,fontweight="bold")
    # left: all pairs with match highlighted; right: result
    pairs=[["1","1 DBMS",True],["1","2 DBMS",False],["2","1 Java",False],["2","2 DBMS",True],["3","3 Java",True],["4","—",False]]
    table(ax,6,82,["Stu.sid","Enr(sid course)","keep?"],
          [[p[0],p[1],("✓" if p[2] else "✗")] for p in pairs],colw=[14,26,12],fs=9,
          hl_rows=[i for i,p in enumerate(pairs) if p[2]],title="Student × Enrollment  (σ on sid = sid)")
    arrow(ax,60,52,68,52)
    table(ax,70,74,["sid","course","grade"],[["1","DBMS","A"],["2","DBMS","A"],["3","Java","C"]],colw=[9,16,12],fs=9,
          title="Student ⋈ Enrollment")
    caption(ax,"Student ⋈_(sid=sid) Enrollment — the meaningless pairings drop away, matches remain.",y=8,fs=10)
    save(fig,"s15_join.png")

def s15_natural_join():
    fig,ax=canvas(10,4.6)
    table(ax,4,80,["sid","name","E.sid","course"],[["1","Sita","1","DBMS"],["2","Hari","2","DBMS"]],colw=[9,14,10,16],fs=9,
          title="EQUIJOIN — keeps BOTH sid columns",fc_hdr=CORAL)
    table(ax,58,80,["sid","name","course"],[["1","Sita","DBMS"],["2","Hari","DBMS"]],colw=[9,14,16],fs=9,
          title="NATURAL JOIN ⋈ — merges to ONE sid",fc_hdr=TEAL)
    caption(ax,"Natural join matches attributes with the SAME NAME (sid) and removes the duplicate column — like a zipper.",y=14,fs=10)
    save(fig,"s15_natural_join.png")

def s15_division():
    fig,ax=canvas(10,5.0)
    ax.text(50,95,"DIVISION  ÷  — 'related to ALL of a set'",ha="center",color=NAVY,fontsize=12,fontweight="bold")
    table(ax,4,84,["sid","course"],[["1","DBMS"],["1","Java"],["2","DBMS"],["3","DBMS"],["3","Java"]],colw=[10,16],fs=9,title="Enrollment(sid,course)")
    table(ax,40,84,["course"],[["DBMS"],["Java"]],colw=[16],fs=9,title="CoreCourses",fc_hdr=AMBER)
    arrow(ax,58,60,68,60)
    table(ax,70,72,["sid"],[["1"],["3"]],colw=[12],fs=10,title="÷ result",fc_hdr=TEAL)
    ax.text(50,10,"Which sid took EVERY core course? sid 1 and 3 (both DBMS and Java). sid 2 took only DBMS → excluded.",
            ha="center",color=CORAL,fontsize=10,fontweight="bold",style="italic")
    save(fig,"s15_division.png")

# ---------- S16 ----------
def s16_aggregate():
    fig,ax=canvas(10,4.6)
    table(ax,6,80,["course","grade→pts"],[["DBMS","4"],["Java","3"],["DBMS","4"],["Java","2"]],colw=[16,18],fs=9,title="Enrollment (raw)")
    arrow(ax,46,55,58,55)
    ax.text(52,63,"course ℱ AVG(pts)",ha="center",color=TEAL,fontsize=9.5,fontweight="bold")
    table(ax,62,74,["course","AVG(pts)"],[["DBMS","4.0"],["Java","2.5"]],colw=[16,18],fs=9,title="grouped result",fc_hdr=TEAL)
    caption(ax,"Aggregate ℱ (COUNT/SUM/AVG/MAX/MIN) groups rows, then summarizes each group — an EXTENDED operation.",y=12,fs=10)
    save(fig,"s16_aggregate.png")

def s16_outer_join():
    fig,ax=canvas(10,4.6)
    table(ax,4,82,["sid","name","course","grade"],[["1","Sita","DBMS","A"],["2","Hari","DBMS","A"]],colw=[9,13,15,11],fs=9,
          title="INNER JOIN — drops the unmatched",fc_hdr=CORAL)
    table(ax,56,82,["sid","name","course","grade"],[["1","Sita","DBMS","A"],["2","Hari","DBMS","A"],["4","Ram","NULL","NULL"]],colw=[9,13,15,13],fs=9,
          title="LEFT OUTER JOIN ⟕ — keeps Ram",fc_hdr=TEAL,hl_rows=[2])
    caption(ax,"Ram enrolled in nothing. Inner join hides him; LEFT outer join keeps him, padding missing values with NULL.",y=14,fs=10)
    save(fig,"s16_outer_join.png")

def s16_how_vs_what():
    fig,ax=canvas(10,4.4)
    rbox(ax,4,26,42,50,"",fc=PALET,tc=INK,ec=TEAL)
    ax.text(25,68,"ALGEBRA — the HOW",ha="center",color=TEAL,fontsize=12,fontweight="bold")
    ax.text(25,56,"step 1: σ_city='Pokhara'(Student)\nstep 2: π_name( result )",ha="center",color=INK,fontsize=10)
    ax.text(25,38,"procedural: you give\nthe step-by-step recipe",ha="center",color=GREY,fontsize=9,style="italic")
    rbox(ax,54,26,42,50,"",fc=PALEB,tc=INK,ec=BLUE)
    ax.text(75,68,"CALCULUS — the WHAT",ha="center",color=BLUE,fontsize=12,fontweight="bold")
    ax.text(75,56,"{ t.name | t ∈ Student\n            ∧ t.city='Pokhara' }",ha="center",color=INK,fontsize=10)
    ax.text(75,38,"declarative: you describe\nthe answer you want",ha="center",color=GREY,fontsize=9,style="italic")
    caption(ax,"Same result set. Algebra = turn-by-turn directions; calculus = give the destination address.",y=12,fs=10)
    save(fig,"s16_how_vs_what.png")

# ---------- S17 ----------
def s17_three_ways():
    fig,ax=canvas(10,4.8)
    ax.text(50,95,"'Names of students from Pokhara' — three equivalent ways",ha="center",color=NAVY,fontsize=12,fontweight="bold")
    rows=[("Relational algebra (procedural)","π_name( σ_city='Pokhara'(Student) )",TEAL,PALET),
          ("Tuple calculus TRC (declarative)","{ t.name | t ∈ Student ∧ t.city='Pokhara' }",BLUE,PALEB),
          ("Domain calculus DRC (declarative)","{ ⟨n⟩ | ∃ s,p ( ⟨s,n,p,'Pokhara'⟩ ∈ Student ) }",AMBER,PALEA)]
    y=74
    for lab,expr,ec,fc in rows:
        rbox(ax,6,y,88,16,"",fc=fc,ec=ec)
        ax.text(10,y+11,lab,ha="left",color=ec,fontsize=10,fontweight="bold")
        ax.text(10,y+4.5,expr,ha="left",color=INK,fontsize=10.5)
        y-=22
    caption(ax,"All three are relationally equivalent — same answer, different style.",y=6,fs=10)
    save(fig,"s17_three_ways.png")

def s17_synthesis():
    fig,ax=canvas(10,4.4)
    rbox(ax,6,44,38,26,"",fc=PALET,ec=TEAL)
    ax.text(25,63,"PROCEDURAL",ha="center",color=TEAL,fontsize=12,fontweight="bold")
    ax.text(25,52,"Relational Algebra\nσ π ∪ ∩ − × ⋈ ÷ ℱ",ha="center",color=INK,fontsize=9.5)
    rbox(ax,56,44,38,26,"",fc=PALEB,ec=BLUE)
    ax.text(75,63,"DECLARATIVE",ha="center",color=BLUE,fontsize=12,fontweight="bold")
    ax.text(75,52,"Calculus: TRC (tuples)\nDRC (domains)",ha="center",color=INK,fontsize=9.5)
    ax.annotate("",xy=(56,57),xytext=(44,57),arrowprops=dict(arrowstyle="<->",color=NAVY,lw=2))
    ax.text(50,60,"equivalent",ha="center",color=NAVY,fontsize=9,style="italic")
    rbox(ax,32,14,36,16,"SQL  (Unit 5)",fc=NAVY,fs=13)
    arrow(ax,25,44,40,30); arrow(ax,75,44,60,30)
    caption(ax,"Algebra, TRC and DRC are all relationally equivalent — and all underlie the SQL you'll write next.",y=4,fs=10)
    save(fig,"s17_synthesis.png")

for fn in [s13_closure,s13_select_project,s14_set_ops,s14_cartesian,
           s15_join,s15_natural_join,s15_division,
           s16_aggregate,s16_outer_join,s16_how_vs_what,s17_three_ways,s17_synthesis]:
    fn()
print("\nAll Unit 3 images written to",OUT)
