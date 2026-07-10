#!/usr/bin/env python3
"""Concept diagrams for IT250 (eighth) Unit 5 — Economics of Information (S34-S41).
Genuinely spatial concepts only (physical vs information good, the market-for-lemons
adverse-selection cascade, signaling vs screening, AI shrinking the info gap, labor-market
polarization, the four IP types); every comparison / concrete-example set is a native PPTX
table in the deck (§7A). No emoji or exotic glyphs in matplotlib text (ASCII only). License-safe.
Output -> eighth/images/   Run: python3 build_unit5_images.py
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

def s34_info_good():
    fig,ax=canvas(10,5.2)
    ax.text(27,95,"PHYSICAL GOOD",ha="center",color=NAVY,fontsize=12,fontweight="bold")
    ax.text(75,95,"INFORMATION GOOD",ha="center",color=NAVY,fontsize=12,fontweight="bold")
    ax.plot([50,50],[8,90],color=LGREY,lw=1.2,ls="--")
    # physical: one owner, used up, costly to copy
    rbox(ax,8,66,20,14,"1 sack of rice\n(Bhaktapur)",fc=AMBER,fs=8.6)
    rbox(ax,8,44,20,12,"RIVAL:\nif I use it,\nyou cannot",fc=CORAL,fs=8.4)
    rbox(ax,8,24,20,12,"Costly to make\nEACH new copy",fc=GREY,fs=8.4)
    ax.text(18,16,"Give it away ->\nyou LOSE it",ha="center",color=INK,fontsize=8.2,fontweight="bold")
    # information: reusable, non-rival, ~0 copy cost
    rbox(ax,62,66,26,14,"1 song / PDF / app\n(a Nepali track)",fc=BLUE,fs=8.6)
    rbox(ax,62,44,26,12,"NON-RIVAL:\nmillions use it\nat the same time",fc=TEAL,fs=8.4)
    rbox(ax,62,24,26,12,"~0 cost to make\nthe NEXT copy",fc=TEAL,fs=8.4)
    ax.text(75,16,"Give it away ->\nyou STILL have it",ha="center",color=INK,fontsize=8.2,fontweight="bold")
    caption(ax,"A physical good is used up and rival; information is non-rival, reusable, and near-free to copy - so it needs different economics.",y=4,fs=9.2)
    save(fig,"s34_info_good.png")

def s35_lemons():
    fig,ax=canvas(10,5.4)
    ax.text(50,96,"The market for lemons: how average pricing drives out good cars",ha="center",color=NAVY,fontsize=11.5,fontweight="bold")
    # step boxes going down (the cascade)
    steps=[("Good used bikes worth Rs 120k  +  'lemons' (bad ones) worth Rs 40k",BLUE),
           ("Buyer cannot tell them apart -> offers the AVERAGE:  Rs 80k",AMBER),
           ("Good sellers refuse (Rs 80k < Rs 120k value) -> they EXIT the market",CORAL),
           ("Mostly lemons left -> buyers learn -> offer drops toward Rs 40k",CORAL),
           ("Good bikes gone; only lemons trade: ADVERSE SELECTION, market shrinks",NAVY)]
    y=80
    for i,(t,c) in enumerate(steps):
        rbox(ax,10,y,80,9,t,fc=c,fs=8.8)
        if i<len(steps)-1:
            arrow(ax,50,y,50,y-5.5,color=GREY,lw=2.0)
        y-=15.5
    caption(ax,"Because buyers pay only an average price, sellers of good quality withdraw - the bad drives out the good (Akerlof, 1970).",y=2.5,fs=9.0)
    save(fig,"s35_lemons.png")

def s36_signal_screen():
    fig,ax=canvas(10,5.2)
    ax.text(50,96,"Two fixes for asymmetric information: who acts?",ha="center",color=NAVY,fontsize=12,fontweight="bold")
    # SIGNALING (top): informed side sends a signal
    ax.text(50,86,"SIGNALING - the INFORMED side proves quality",ha="center",color=TEAL,fontsize=10,fontweight="bold")
    rbox(ax,6,68,24,12,"SELLER / WORKER\n(knows quality)",fc=TEAL,fs=8.4)
    rbox(ax,70,68,24,12,"BUYER / EMPLOYER\n(uninformed)",fc=GREY,fs=8.4)
    arrow(ax,30,74,70,74,color=TEAL,lw=2.4)
    ax.text(50,78,"sends a costly signal:",ha="center",color=INK,fontsize=8.2,fontweight="bold")
    ax.text(50,64,"warranty, brand, degree, certification, verified badge",ha="center",color=GREY,fontsize=8.2,style="italic")
    ax.plot([4,96],[58,58],color=LGREY,lw=1.0,ls="--")
    # SCREENING (bottom): uninformed side sets a test
    ax.text(50,52,"SCREENING - the UNINFORMED side sorts",ha="center",color=BLUE,fontsize=10,fontweight="bold")
    rbox(ax,6,32,24,12,"SELLER / WORKER\n(knows quality)",fc=GREY,fs=8.4)
    rbox(ax,70,32,24,12,"BUYER / EMPLOYER\n(uninformed)",fc=BLUE,fs=8.4)
    arrow(ax,70,38,30,38,color=BLUE,lw=2.4)
    ax.text(50,42,"offers a menu / test -> others self-select:",ha="center",color=INK,fontsize=8.2,fontweight="bold")
    ax.text(50,26,"insurance forms, test drive, deductibles, reviews, probation",ha="center",color=GREY,fontsize=8.2,style="italic")
    caption(ax,"Signaling: the side WITH the information proves it. Screening: the side WITHOUT it designs a test so quality reveals itself.",y=4,fs=9.0)
    save(fig,"s36_signal_screen.png")

def s38_ai_info():
    fig,ax=canvas(10,5.0)
    ax.text(50,95,"AI shrinks the information gap between the two sides",ha="center",color=NAVY,fontsize=12,fontweight="bold")
    rbox(ax,6,55,22,16,"BUYER\nknows little",fc=GREY,fs=8.8)
    rbox(ax,72,55,22,16,"SELLER\nknows a lot",fc=NAVY,fs=8.8)
    # AI engine in the middle narrowing the gap
    rbox(ax,38,54,24,18,"A I",fc=TEAL,fs=15)
    arrow(ax,28,63,38,63,color=TEAL,lw=2.2)
    arrow(ax,72,63,62,63,color=TEAL,lw=2.2)
    tools=["fraud detection","verified reviews","price comparison","recommendation match","transparency / ratings"]
    y=40
    for t in tools:
        ax.text(50,y,"- "+t,ha="center",color=INK,fontsize=8.6); y-=6
    caption(ax,"AI reads data both sides could not process alone - detecting fraud, verifying reviews, matching - so buyers face less hidden information.",y=3,fs=9.0)
    save(fig,"s38_ai_info.png")

def s40_polarization():
    fig,ax=canvas(10,5.2)
    ax.text(50,95,"Labor-market polarization: the middle hollows out",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    # baseline
    ax.plot([12,92],[22,22],color=GREY,lw=1.4)
    bars=[("LOW-skill\n(hard to automate)",22,26,TEAL,"STABLE / slight rise","riders, cleaners, care"),
          ("MIDDLE-skill\n(routine)",50,20,CORAL,"SHRINKS  (~40% at risk)","clerks, tellers, data entry"),
          ("HIGH-skill\n(analysis, creative)",78,30,BLUE,"GROWS","data, design, engineering")]
    for label,cx,ht,c,tag,eg in bars:
        ax.add_patch(Rectangle((cx-11,22),22,ht*1.6,fc=c,ec="none",zorder=3))
        ax.text(cx,22+ht*1.6+4,tag,ha="center",color=c,fontsize=8.4,fontweight="bold")
        ax.text(cx,18,label,ha="center",va="top",color=INK,fontsize=8.4,fontweight="bold")
        ax.text(cx,10,eg,ha="center",va="top",color=GREY,fontsize=7.6,style="italic")
    # arrows showing direction
    arrow(ax,50,60,50,50,color=CORAL,lw=2.6)   # middle down
    arrow(ax,78,72,78,80,color=BLUE,lw=2.6)     # high up
    caption(ax,"Automation replaces ROUTINE middle-skill jobs; high-skill and non-routine low-skill jobs grow - the workforce splits in two (OECD-style estimate: ~40% of routine tasks automatable).",y=2,fs=8.6)
    save(fig,"s40_polarization.png")

def s41_ip_types():
    fig,ax=canvas(10,5.2)
    ax.text(50,96,"The four types of intellectual property",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    cards=[("COPYRIGHT",BLUE,"protects: creative works\n(songs, films, code, books)","life + 50 yrs","Nepali music, movies"),
           ("PATENT",TEAL,"protects: inventions\n(new process / device)","~20 years","a new machine / drug"),
           ("TRADEMARK",AMBER,"protects: brand identity\n(name, logo, mark)","renewable forever","Wai Wai, eSewa logo"),
           ("TRADE SECRET",CORAL,"protects: secret know-how\n(recipe, algorithm)","as long as secret","recipe, ranking formula")]
    xs=[6,52]; ys=[50,10]
    i=0
    for row in range(2):
        for col in range(2):
            title,c,body,dur,eg=cards[i]; x=xs[col]; y=ys[row]
            ax.add_patch(FancyBboxPatch((x,y),42,34,boxstyle="round,pad=0.3,rounding_size=2",fc=WHITE,ec=c,lw=2.2,zorder=2))
            ax.add_patch(Rectangle((x,y+26),42,8,fc=c,ec="none",zorder=3))
            ax.text(x+21,y+30,title,ha="center",va="center",color=WHITE,fontsize=10.5,fontweight="bold",zorder=4)
            ax.text(x+21,y+17,body,ha="center",va="center",color=INK,fontsize=8.4,zorder=4)
            ax.text(x+21,y+8,"Term: "+dur,ha="center",va="center",color=c,fontsize=8.2,fontweight="bold",zorder=4)
            ax.text(x+21,y+3,"e.g. "+eg,ha="center",va="center",color=GREY,fontsize=7.8,style="italic",zorder=4)
            i+=1
    save(fig,"s41_ip_types.png")

for fn in [s34_info_good,s35_lemons,s36_signal_screen,s38_ai_info,s40_polarization,s41_ip_types]:
    fn()
print("\nAll IT250 Unit 5 diagrams written to",OUT)
