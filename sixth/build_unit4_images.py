#!/usr/bin/env python3
"""Concept diagrams for IT246 (sixth) Unit 4 — Ethical Decisions in Software Development &
Ethics of IT Organizations (S17–S21). Genuinely spatial concepts only (cost-to-fix escalation,
testing pyramid, risk matrix, employment spectrum, whistle-blowing decision flow, IT lifecycle
loop); all comparisons/examples are native PPTX tables in the deck (§7A). License-safe.
Output -> sixth/images/   Run: python3 build_unit4_images.py
"""
import os, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, Polygon, FancyArrowPatch

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
def caption(ax,text,color=GREY,y=3,fs=10.5):
    ax.text(50,y,text,ha="center",fontsize=fs,style="italic",color=color)

def s17_costcurve():
    fig,ax=canvas(10,4.8)
    ax.text(50,94,"Cost to fix a defect rises ~10× at each later stage",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    stages=[("Requirements","1×",TEAL,14),("Design","10×",BLUE,32),("Code","100×",AMBER,52),
            ("Release","1000×",CORAL,74),("Post-release","10000×","#7a2317",92)]
    hs=[14,26,40,56,72]
    for (label,mult,c,x),h in zip(stages,hs):
        ax.add_patch(Rectangle((x-8,14),16,h,fc=c,ec=WHITE,lw=1.2,zorder=3))
        ax.text(x,14+h+4,mult,ha="center",color=c,fontsize=10,fontweight="bold")
        ax.text(x,10,label,ha="center",color=INK,fontsize=8.6)
    arrow(ax,6,14,98,14,color=GREY,lw=1.5)
    caption(ax,"A bug caught in requirements is cheap; the same bug found after release costs orders of magnitude more. Prevention beats cure.",y=2,fs=9.7)
    save(fig,"s17_costcurve.png")

def s18_pyramid():
    fig,ax=canvas(10,5.0)
    ax.text(50,95,"The testing pyramid — many small tests, few big ones",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    layers=[("UNIT tests — many, fast, cheap (each function)",TEAL,16,10,80),
            ("INTEGRATION — modules working together",BLUE,32,24,52),
            ("SYSTEM — the whole app end-to-end",AMBER,48,37,26),
            ("ACCEPTANCE (UAT) — user signs off",CORAL,64,45,10)]
    for text,c,y,x,w in layers:
        ax.add_patch(Rectangle((x,y),w,14,fc=c,ec=WHITE,lw=1.5,zorder=3))
        ax.text(50,y+7,text,ha="center",va="center",color=WHITE,fontsize=9,fontweight="bold",zorder=4)
    caption(ax,"'Testing shows the presence of bugs, not their absence.' Automate the base; a green demo is not a tested product.",y=4)
    save(fig,"s18_pyramid.png")

def s18_riskmatrix():
    fig,ax=canvas(10,5.0)
    ax.text(50,95,"Risk = likelihood × impact",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    # 3x3 grid
    colors=[["#E1F5EE","#FAEEDA","#FAECE7"],
            ["#FAEEDA","#FAECE7","#f2c9bb"],
            ["#FAECE7","#f2c9bb","#e39c86"]]
    labels=[["Low","Med","High"],["Med","High","High"],["High","High","Critical"]]
    x0,y0,cell=30,20,20
    for r in range(3):
        for c in range(3):
            ax.add_patch(Rectangle((x0+c*cell,y0+r*cell),cell,cell,fc=colors[r][c],ec=NAVY,lw=1.0,zorder=2))
            ax.text(x0+c*cell+cell/2,y0+r*cell+cell/2,labels[r][c],ha="center",va="center",color=INK,fontsize=9.5,fontweight="bold",zorder=3)
    ax.text(x0+1.5*cell,y0-7,"IMPACT →",ha="center",color=NAVY,fontsize=10,fontweight="bold")
    ax.text(x0-8,y0+1.5*cell,"LIKELIHOOD →",ha="center",color=NAVY,fontsize=10,fontweight="bold",rotation=90)
    caption(ax,"Prioritise the top-right (high likelihood × high impact) — especially any safety-critical risk. Log it, mitigate it, plan a rollback.",y=6,fs=9.7)
    save(fig,"s18_riskmatrix.png")

def s19_spectrum():
    fig,ax=canvas(10,4.2)
    ax.text(50,90,"The employment spectrum — security vs flexibility",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    segs=[("PERMANENT\nbenefits, security,\nloyalty",TEAL,4),
          ("CONTRACTOR\nfixed term, higher pay,\nno benefits",BLUE,29),
          ("FREELANCER\ngig-by-gig,\nno security",AMBER,54),
          ("OFFSHORE\nremote, cross-border,\ncost-driven",CORAL,79)]
    for t,c,x in segs:
        rbox(ax,x,44,20,24,t,fc=c,fs=8.4)
    arrow(ax,4,38,99,38,color=GREY,lw=2.0)
    ax.text(14,31,"most security",ha="center",color=TEAL,fontsize=9,style="italic")
    ax.text(88,31,"most flexible / cheapest",ha="center",color=CORAL,fontsize=9,style="italic")
    caption(ax,"Firms gain flexibility and cost moving right; workers lose benefits and security. The ethics is who carries that risk.",y=10,fs=9.7)
    save(fig,"s19_spectrum.png")

def s20_flow():
    fig,ax=canvas(10,5.2)
    ax.text(50,96,"Responsible whistle-blowing — a last-resort process",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    steps=[("1  Be sure of the FACTS — gather evidence, keep records",BLUE,80),
           ("2  Confirm the HARM is serious (illegal / dangerous)",TEAL,64),
           ("3  Report INTERNALLY — manager, ethics officer, audit",AMBER,48),
           ("4  Escalate — regulator (e.g. CIAA) if ignored",CORAL,32),
           ("5  Go EXTERNAL / public — only as a last resort",'#7a2317',16)]
    for text,c,y in steps:
        ax.add_patch(FancyBboxPatch((14,y),72,11,boxstyle="round,pad=0.2,rounding_size=2",fc=c,ec=WHITE,lw=1.4,zorder=3))
        ax.text(50,y+5.5,text,ha="center",va="center",color=WHITE,fontsize=9.3,fontweight="bold",zorder=4)
    for y in [80,64,48,32]:
        arrow(ax,50,y,50,y-5,color=GREY,lw=1.8)
    caption(ax,"Evidence-first, internal-first. External disclosure is the last step, not the first — and it carries real personal risk.",y=4,fs=9.7)
    save(fig,"s20_flow.png")

def s21_lifecycle():
    fig,ax=canvas(10,5.0)
    ax.text(50,95,"Green computing spans the whole IT lifecycle",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    steps=[("MANUFACTURE\nmaterials, energy",TEAL),("USE\npower, cooling",BLUE),
           ("DISPOSE\ne-waste, toxins",CORAL),("RECYCLE / REUSE\nrefurbish, recover",AMBER)]
    cx,cy,r=50,46,26
    pts=[]
    for i,(t,c) in enumerate(steps):
        ang=math.pi/2 - i*2*math.pi/len(steps)
        x=cx+r*math.cos(ang); y=cy+r*math.sin(ang); pts.append((x,y))
        rbox(ax,x-13,y-8,26,16,t,fc=c,fs=9)
    for i in range(len(pts)):
        x1,y1=pts[i]; x2,y2=pts[(i+1)%len(pts)]
        arrow(ax,x1+(x2-x1)*0.30,y1+(y2-y1)*0.30,x1+(x2-x1)*0.70,y1+(y2-y1)*0.70,color=GREY,lw=1.8)
    caption(ax,"'The cloud' is physical data centers burning real power. Green IT cuts energy at USE and closes the loop at DISPOSE.",y=4,fs=9.7)
    save(fig,"s21_lifecycle.png")

for fn in [s17_costcurve,s18_pyramid,s18_riskmatrix,s19_spectrum,s20_flow,s21_lifecycle]:
    fn()
print("\nAll IT246 Unit 4 diagrams written to",OUT)
