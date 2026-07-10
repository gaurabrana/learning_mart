#!/usr/bin/env python3
"""Concept diagrams for IT250 (eighth) Unit 2 — Fundamentals of Digital Economy (S9–S15).
Genuinely spatial concepts only (pipe vs platform, cross-side network-effect loop, two-sided
cross-subsidy, the flywheel, tipping / winner-take-most curve, DAI three-pillar + Nepal status);
all comparisons and concrete-example sets are native PPTX tables in the deck (§7A). License-safe.
Output -> eighth/images/   Run: python3 build_unit2_images.py
"""
import os, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, Polygon, FancyArrowPatch, Wedge

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

def s9_pipe_platform():
    fig,ax=canvas(10,5.0)
    ax.text(27,95,"PIPE (linear) business",ha="center",color=NAVY,fontsize=12,fontweight="bold")
    ax.text(75,95,"PLATFORM business",ha="center",color=NAVY,fontsize=12,fontweight="bold")
    # pipe: business -> customer, one way
    rbox(ax,6,60,18,14,"BUSINESS\nmakes the\nvalue",fc=BLUE,fs=8.6)
    rbox(ax,32,60,18,14,"CUSTOMER\nbuys it",fc=GREY,fs=8.6)
    arrow(ax,24,67,32,67,color=NAVY,lw=2.4)
    ax.text(28,52,"value flows ONE way",ha="center",color=GREY,fontsize=8.4,style="italic")
    ax.text(28,45,"e.g. Netflix originals,\nsoftware licence",ha="center",color=INK,fontsize=8.2)
    # divider
    ax.plot([52,52],[8,88],color=LGREY,lw=1.2,ls="--")
    # platform: hub with 3 groups around
    cx,cy=76,55
    rbox(ax,cx-9,cy-6,18,12,"PLATFORM\n(matches)",fc=TEAL,fs=8.6)
    grp=[("SELLERS /\nDRIVERS",BLUE,60,80),("BUYERS /\nRIDERS",AMBER,92,80),("PARTNERS /\nADS",CORAL,76,24)]
    for t,c,x,y in grp:
        rbox(ax,x-9,y-6,18,12,t,fc=c,fs=8.0)
        arrow(ax,x+(cx-x)*0.30,y+(cy-y)*0.30,x+(cx-x)*0.62,y+(cy-y)*0.62,color=GREY,lw=1.5)
        arrow(ax,cx+(x-cx)*0.32,cy+(y-cy)*0.32,cx+(x-cx)*0.64,cy+(y-cy)*0.64,color=LGREY,lw=1.3)
    ax.text(76,10,"value flows MANY ways — e.g. Daraz, Pathao",ha="center",color=INK,fontsize=8.2)
    caption(ax,"A pipe MAKES and sells value; a platform CONNECTS groups and lets them create value for each other.",y=2,fs=9.4)
    save(fig,"s9_pipe_platform.png")

def s10_networkloop():
    fig,ax=canvas(10,5.0)
    ax.text(50,95,"Cross-side network effect: the loop that feeds itself",ha="center",color=NAVY,fontsize=12,fontweight="bold")
    nodes=[("MORE\nRIDERS",BLUE,20,68),("SHORTER\nWAITS",TEAL,50,84),
           ("MORE\nDRIVERS JOIN",AMBER,80,68),("BETTER\nCOVERAGE",CORAL,50,44)]
    pts=[]
    for t,c,x,y in nodes:
        rbox(ax,x-11,y-8,22,16,t,fc=c,fs=8.8); pts.append((x,y))
    order=[0,1,2,3]
    for i in range(4):
        x1,y1=pts[order[i]]; x2,y2=pts[order[(i+1)%4]]
        arrow(ax,x1+(x2-x1)*0.26,y1+(y2-y1)*0.26,x1+(x2-x1)*0.74,y1+(y2-y1)*0.74,color=GREY,lw=1.9)
    ax.text(50,64,"↻",ha="center",va="center",color=NAVY,fontsize=26,fontweight="bold")
    caption(ax,"Each side makes the other more valuable (Pathao: riders ↔ drivers). Positive feedback — success breeds success.",y=6,fs=9.4)
    save(fig,"s10_networkloop.png")

def s11_crosssubsidy():
    fig,ax=canvas(10,4.8)
    ax.text(50,94,"Two-sided pricing: charge the right side",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    # subsidy side (free) left, platform middle, money side right
    rbox(ax,6,52,22,20,"SUBSIDY SIDE\n(free / cheap)\nusers, readers,\nriders",fc=TEAL,fs=8.8)
    rbox(ax,39,50,22,24,"PLATFORM",fc=NAVY,fs=11)
    rbox(ax,72,52,22,20,"MONEY SIDE\n(pays)\nadvertisers,\ncreators, merchants",fc=AMBER,fs=8.6)
    arrow(ax,28,62,39,62,color=TEAL,lw=2.2); ax.text(33.5,66,"attracts",ha="center",color=TEAL,fontsize=8,style="italic")
    arrow(ax,72,62,61,62,color=AMBER,lw=2.2); ax.text(66.5,66,"pays $",ha="center",color=AMBER,fontsize=8,style="italic")
    ax.text(50,40,"The free side is NOT charity — it is the bait that makes the paying side valuable.",ha="center",color=INK,fontsize=9)
    ax.text(50,32,"Google: users free · advertisers pay      |      Daraz: browsing free · sellers pay commission",ha="center",color=GREY,fontsize=8.4,style="italic")
    caption(ax,"Cross-subsidy: subsidise the side that attracts the side that pays. Who is free vs who pays is a design choice.",y=6,fs=9.4)
    save(fig,"s11_crosssubsidy.png")

def s12_flywheel():
    fig,ax=canvas(10,5.2)
    ax.text(50,95,"The platform flywheel — a DESIGNED feedback loop",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    steps=[("ACQUIRE\nnew users",TEAL),("ACTIVATE\nfirst value",BLUE),
           ("ENGAGE\nkeep using",AMBER),("RETAIN\nlock-in",CORAL)]
    cx,cy,r=50,48,26
    pts=[]
    for i,(t,c) in enumerate(steps):
        ang=math.pi/2 - i*2*math.pi/len(steps)
        x=cx+r*math.cos(ang); y=cy+r*math.sin(ang); pts.append((x,y))
        rbox(ax,x-12,y-8,24,16,t,fc=c,fs=8.8)
    for i in range(len(pts)):
        x1,y1=pts[i]; x2,y2=pts[(i+1)%len(pts)]
        arrow(ax,x1+(x2-x1)*0.32,y1+(y2-y1)*0.32,x1+(x2-x1)*0.68,y1+(y2-y1)*0.68,color=GREY,lw=1.9)
    ax.text(cx,cy,"more users\n→ more value\n→ more users",ha="center",va="center",color=NAVY,fontsize=8.4,fontweight="bold")
    caption(ax,"A network effect is natural; a flywheel is engineered. Retention (lock-in) feeds acquisition — the loop spins faster over time.",y=4,fs=9.3)
    save(fig,"s12_flywheel.png")

def s13_tipping():
    fig,ax=canvas(10,5.0)
    ax.text(50,95,"Tipping: why the digital leader takes (almost) all",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    ax.add_patch(FancyArrowPatch((10,14),(10,86),arrowstyle="-|>",mutation_scale=13,color=GREY,lw=1.6))
    ax.add_patch(FancyArrowPatch((10,14),(94,14),arrowstyle="-|>",mutation_scale=13,color=GREY,lw=1.6))
    ax.text(6,50,"market\nshare",ha="center",va="center",color=NAVY,fontsize=9,rotation=90,fontweight="bold")
    ax.text(52,7,"users / time →",ha="center",color=NAVY,fontsize=9,fontweight="bold")
    # S-curve tipping
    xs=[10+ i for i in range(0,84,2)]
    import math as m
    ys=[14+68/(1+m.exp(-0.22*(x-52))) for x in xs]
    ax.plot(xs,ys,color=BLUE,lw=3,zorder=3)
    # tipping point marker
    ax.add_patch(Circle((52,48),2.2,fc=CORAL,ec=WHITE,lw=1.4,zorder=5))
    ax.text(58,44,"TIPPING POINT\none platform becomes\nunstoppable",ha="left",color=CORAL,fontsize=8.6,fontweight="bold")
    ax.text(20,26,"contested:\nmany compete",ha="center",color=GREY,fontsize=8,style="italic")
    ax.text(82,74,"winner-\ntake-most",ha="center",color=BLUE,fontsize=8.4,style="italic",fontweight="bold")
    caption(ax,"Network effects + scale + lock-in create increasing returns: past the tipping point, users pile onto the leader (WhatsApp in Nepal).",y=3,fs=9.2)
    save(fig,"s13_tipping.png")

def s15_dai_pillars():
    fig,ax=canvas(10,5.0)
    ax.text(50,95,"World Bank Digital Adoption Index — 3 pillars (+ Nepal)",ha="center",color=NAVY,fontsize=12,fontweight="bold")
    cols=[("PEOPLE",TEAL,"internet, smartphones,\nsocial media, payments","Nepal: MODERATE–HIGH",TEAL),
          ("BUSINESS",BLUE,"cloud, e-commerce,\ndigital accounting","Nepal: LOW–MODERATE",AMBER),
          ("GOVERNMENT",AMBER,"e-services, digital ID,\ntax filing, open data","Nepal: EARLY STAGE",CORAL)]
    xs=[8,38,68]
    for (title,c,body,status,sc),x in zip(cols,xs):
        ax.add_patch(FancyBboxPatch((x,30),26,52,boxstyle="round,pad=0.4,rounding_size=2",fc=WHITE,ec=c,lw=2.0,zorder=2))
        ax.add_patch(Rectangle((x,74),26,8,fc=c,ec="none",zorder=3))
        ax.text(x+13,78,title,ha="center",va="center",color=WHITE,fontsize=10.5,fontweight="bold",zorder=4)
        ax.text(x+13,60,body,ha="center",va="center",color=INK,fontsize=8.4,zorder=4)
        ax.add_patch(FancyBboxPatch((x+2,34),22,10,boxstyle="round,pad=0.2,rounding_size=1",fc=sc,ec="none",zorder=3))
        ax.text(x+13,39,status,ha="center",va="center",color=WHITE,fontsize=7.8,fontweight="bold",zorder=4)
    caption(ax,"Adoption = effective USAGE, not just access. Nepal is strongest on People, weakest on Government (early-stage e-services).",y=16,fs=9.2)
    save(fig,"s15_dai_pillars.png")

for fn in [s9_pipe_platform,s10_networkloop,s11_crosssubsidy,s12_flywheel,s13_tipping,s15_dai_pillars]:
    fn()
print("\nAll IT250 Unit 2 diagrams written to",OUT)
