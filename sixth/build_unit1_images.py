#!/usr/bin/env python3
"""Concept diagrams for IT246 (sixth) Unit 1 — An Overview of Ethics (S1–S5).
Genuinely spatial concepts only (grid, pyramid, radial map, process loop, flow, scale);
comparisons are rendered as native PPTX tables in the deck. License-safe, purpose-built.
Output -> sixth/images/   Run: python3 build_unit1_images.py
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

def s1_grid():
    fig,ax=canvas(10,5.4)
    ax.text(50,96,"The Legal / Ethical grid — two separate axes",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    # quadrants
    quads=[(8,50,PALET,TEAL,"LEGAL + ETHICAL","Paying taxes honestly\nKeeping a promise to a customer","the easy quadrant"),
           (54,50,PALEC,CORAL,"LEGAL + UNETHICAL","Exploiting a tax loophole\nQueue-jumping via 'source-force'","← most IT/business scandals live here"),
           (8,10,PALEB,BLUE,"ILLEGAL + ETHICAL","Justified civil disobedience\nWhistle-blowing that breaks an NDA","rare, debated"),
           (54,10,PALEA,AMBER,"ILLEGAL + UNETHICAL","Paying a bribe ('ghus')\nLeaking someone's private data","the obvious-wrong quadrant")]
    for x,y,fc,ec,title,body,tag in quads:
        ax.add_patch(FancyBboxPatch((x,y),38,34,boxstyle="round,pad=0.3,rounding_size=2",fc=fc,ec=ec,lw=1.6,zorder=2))
        ax.text(x+19,y+28,title,ha="center",color=ec,fontsize=11,fontweight="bold")
        ax.text(x+19,y+16,body,ha="center",color=INK,fontsize=9.5)
        ax.text(x+19,y+4,tag,ha="center",color=ec,fontsize=8.5,style="italic")
    caption(ax,"Legal and ethical are DIFFERENT questions. The dangerous quadrant is legal-but-unethical — only your judgment stops you.",y=1)
    save(fig,"s1_grid.png")

def s2_pyramid():
    fig,ax=canvas(10,5.2)
    ax.text(50,96,"Carroll's CSR Pyramid — build it bottom-up",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    layers=[("ECONOMIC — be profitable (survival funds everything above)",TEAL,10,8,84),
            ("LEGAL — obey the law (society's codified minimum)",BLUE,26,20,64),
            ("ETHICAL — do what's right beyond the law",AMBER,42,32,40),
            ("PHILANTHROPIC — give back to the community",CORAL,58,44,16)]
    for text,c,y,x,w in layers:
        ax.add_patch(Rectangle((x,y),w,14,fc=c,ec=WHITE,lw=1.5,zorder=3))
        ax.text(50,y+7,text,ha="center",va="center",color=WHITE,fontsize=9.5,fontweight="bold",zorder=4)
    caption(ax,"Lower layers must hold first: donating (top) while underpaying staff (failing ethical) is CSR done backwards.",y=2)
    save(fig,"s2_pyramid.png")

def s2_stakeholders():
    fig,ax=canvas(10,5.2)
    ax.text(50,96,"Stakeholders — everyone materially affected, not just owners",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    rbox(ax,38,42,24,14,"THE\nBUSINESS",fc=NAVY,fs=12)
    around=[("Customers",14,78),("Employees",50,82),("Owners /\nShareholders",84,78),
            ("Suppliers",88,42),("Government",84,10),("Society &\nCommunity",50,6),("Environment",14,10),("Local\nCommunity",10,42)]
    for name,x,y in around:
        rbox(ax,x-11,y-6,22,12,name,fc=PALEB,tc=INK,ec=BLUE,fs=9)
        arrow(ax,x,y,50,49,color=LGREY,lw=1.4)
    caption(ax,"Shareholder lens: profit = success. Stakeholder lens: harming any affected group is a failure, even if profit is up.",y=1)
    save(fig,"s2_stakeholders.png")

def s3_cycle():
    fig,ax=canvas(10,5.0)
    ax.text(50,95,"An ethics program is a CYCLE, not a poster",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    steps=[("Code of\nconduct",BLUE),("Training",TEAL),("Safe\nreporting",AMBER),("Audit",BLUE),("Consequences",CORAL)]
    cx,cy,r=50,45,30
    pts=[]
    for i,(t,c) in enumerate(steps):
        ang=math.pi/2 - i*2*math.pi/len(steps)
        x=cx+r*math.cos(ang); y=cy+r*math.sin(ang); pts.append((x,y))
        rbox(ax,x-11,y-6,22,12,t,fc=c,fs=9.5)
    for i in range(len(pts)):
        x1,y1=pts[i]; x2,y2=pts[(i+1)%len(pts)]
        arrow(ax,x1+(x2-x1)*0.28,y1+(y2-y1)*0.28,x1+(x2-x1)*0.72,y1+(y2-y1)*0.72,color=GREY,lw=1.6)
    caption(ax,"Each part feeds the next; enforcement + culture matter far more than the document itself.",y=2)
    save(fig,"s3_cycle.png")

def s4_5step():
    fig,ax=canvas(10,4.4)
    ax.text(50,92,"The 5-step ethical decision process",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    steps=[("1\nGet the\nfacts",TEAL),("2\nStakeholders\n& options",BLUE),("3\nEvaluate\n(4 lenses)",AMBER),
           ("4\nChoose\n& act",BLUE),("5\nReflect",TEAL)]
    x=3; w=17
    for i,(t,c) in enumerate(steps):
        rbox(ax,x,40,w,26,t,fc=c,fs=10)
        if i<4: arrow(ax,x+w,53,x+w+2.5,53,color=NAVY,lw=2.2)
        x+=w+2.5
    caption(ax,"Steps 1 and 2 are the ones people skip — and that's where most bad decisions are born.",y=14)
    save(fig,"s4_5step.png")

def s5_scale():
    fig,ax=canvas(10,4.4)
    ax.text(50,92,"Why IT ethics is different: impact at machine scale",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    rbox(ax,6,44,34,20,"OFFLINE wrong\na dishonest shopkeeper\ncheats ONE customer\nat a time",fc=PALEB,tc=INK,ec=BLUE,fs=10)
    arrow(ax,42,54,58,54,color=CORAL,lw=2.6)
    rbox(ax,60,44,34,20,"IT wrong\none bad line of code / policy\nharms MILLIONS in seconds —\nand the harm can be permanent",fc=PALEC,tc=INK,ec=CORAL,fs=10)
    ax.text(50,30,"Scale · Speed · Anonymity · Permanence · a capability–regulation gap",ha="center",color=NAVY,fontsize=11,fontweight="bold")
    caption(ax,"'A rumor in a village fades; a screenshot online is forever.' The law is often missing — your ethics is all that holds.",y=10)
    save(fig,"s5_scale.png")

for fn in [s1_grid,s2_pyramid,s2_stakeholders,s3_cycle,s4_5step,s5_scale]:
    fn()
print("\nAll IT246 Unit 1 diagrams written to",OUT)
