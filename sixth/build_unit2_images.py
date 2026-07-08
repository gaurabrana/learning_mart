#!/usr/bin/env python3
"""Concept diagrams for IT246 (sixth) Unit 2 — Ethics for IT Workers & Users (S6–S10).
Genuinely spatial concepts only (relationship web, standards map, insider iceberg, data-trail
flow, security-vs-privacy seesaw, opinion→defamation spectrum, verify-before-share flow);
all comparisons/examples are rendered as native PPTX tables in the deck (§7A). License-safe.
Output -> sixth/images/   Run: python3 build_unit2_images.py
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

def s6_web():
    fig,ax=canvas(10,5.6)
    ax.text(50,97,"The IT worker at the centre — six relationships, six duties",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    rbox(ax,38,43,24,15,"IT\nWORKER",fc=NAVY,fs=13)
    nodes=[("EMPLOYER\nloyalty · honesty",BLUE,50,84),
           ("CLIENT\nhonest advice · disclose risk",TEAL,86,66),
           ("SUPPLIERS\nfair dealing · no bribes",AMBER,86,28),
           ("SOCIETY\nsafe systems · no harm",CORAL,50,13),
           ("USERS\nsupport · don't exploit",TEAL,14,28),
           ("PEERS\nrespect · no poaching",BLUE,14,66)]
    for name,c,x,y in nodes:
        rbox(ax,x-13,y-7,26,14,name,fc=PALEB if c==BLUE else (PALET if c==TEAL else (PALEA if c==AMBER else PALEC)),tc=INK,ec=c,fs=8.3)
        arrow(ax,x,y,50,50.5,color=LGREY,lw=1.5)
    caption(ax,"Every arrow is a duty of care created by privileged access — 'can' does not mean 'should'.",y=1)
    save(fig,"s6_web.png")

def s7_map():
    fig,ax=canvas(10,4.8)
    ax.text(50,94,"Who keeps IT professional — three tools, two sources",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    rbox(ax,6,58,40,16,"PROFESSIONAL BODIES\nACM · IEEE-CS · ISACA · CAN-Nepal",fc=BLUE,fs=9.5)
    rbox(ax,58,58,36,16,"GOVERNMENT\nNMC · NEC (not IT, yet)",fc=NAVY,fs=9.5)
    rbox(ax,4,20,26,16,"CODES OF ETHICS\npublished standards",fc=TEAL,fs=9)
    rbox(ax,37,20,26,16,"CERTIFICATIONS\nprove a skill (CCNA…)",fc=AMBER,fs=9)
    rbox(ax,70,20,26,16,"LICENSING\nlegal right to practise",fc=CORAL,fs=9)
    arrow(ax,20,58,17,36,color=GREY,lw=1.8); arrow(ax,30,58,50,36,color=GREY,lw=1.8)
    arrow(ax,76,58,83,36,color=GREY,lw=1.8)
    caption(ax,"Bodies publish CODES and run CERTIFICATIONS (voluntary); only GOVERNMENT grants LICENSING (legal force). IT has the first two, not the third.",y=2,fs=9.8)
    save(fig,"s7_map.png")

def s8_insider():
    fig,ax=canvas(10,5.2)
    ax.text(50,96,"The insider iceberg — most incidents start with ordinary users",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    # waterline
    ax.plot([6,94],[64,64],color=BLUE,lw=1.4,ls="--",zorder=1)
    ax.text(93,66,"what people fear",ha="right",color=GREY,fontsize=8.5,style="italic")
    ax.text(93,60,"what actually happens",ha="right",color=GREY,fontsize=8.5,style="italic")
    # tip
    ax.add_patch(Polygon([(50,90),(38,64),(62,64)],closed=True,fc=PALEC,ec=CORAL,lw=1.6,zorder=2))
    ax.text(50,74,"HACKERS\n(rare)",ha="center",va="center",color=CORAL,fontsize=9.5,fontweight="bold",zorder=3)
    # submerged mass
    ax.add_patch(Polygon([(38,64),(62,64),(80,14),(20,14)],closed=True,fc=PALEB,ec=BLUE,lw=1.6,zorder=2))
    ax.text(50,40,"INSIDER / USER MISTAKES\ncracked apps · reused passwords · phishing clicks\npersonal USBs · misuse of resources",ha="center",va="center",color=NAVY,fontsize=9.3,fontweight="bold",zorder=3)
    caption(ax,"More security tools won't fix behaviour below the line — that's what AUPs, anti-piracy and use norms are for.",y=2)
    save(fig,"s8_insider.png")

def s9_trail():
    fig,ax=canvas(10,4.6)
    ax.text(50,92,"Your data trail — one action, many hands",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    rbox(ax,3,44,18,22,"YOU\nloan form · SIM\nQR scan",fc=TEAL,fs=9)
    rbox(ax,29,44,20,22,"COMPANY\nbank · telecom\ncollects data",fc=BLUE,fs=9)
    rbox(ax,57,44,20,22,"THIRD PARTIES\nmarketers · brokers\npartners",fc=AMBER,fs=9)
    rbox(ax,83,44,15,22,"SPAM\n& FRAUD\ncalls you never\nasked for",fc=CORAL,fs=8.5)
    for x1,x2 in [(21,29),(49,57),(77,83)]:
        arrow(ax,x1,55,x2,55,color=NAVY,lw=2.2)
    caption(ax,"Consent · purpose limitation · minimization break down at each hop — 'when did you agree to THIS?' is the privacy question.",y=12,fs=9.8)
    save(fig,"s9_trail.png")

def s9_seesaw():
    fig,ax=canvas(10,4.4)
    ax.text(50,92,"Surveillance: every gain in security costs some privacy",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    # fulcrum
    ax.add_patch(Polygon([(50,30),(43,16),(57,16)],closed=True,fc=GREY,ec="none",zorder=2))
    # tilted beam
    ax.add_patch(FancyBboxPatch((14,34),72,5,boxstyle="round,pad=0.1,rounding_size=1",fc=NAVY,ec="none",
        transform=ax.transData,zorder=3))
    rbox(ax,10,44,26,14,"SECURITY\ncatch fraud, deter crime",fc=TEAL,fs=9)
    rbox(ax,64,44,26,14,"PRIVACY\ncontrol over your data",fc=BLUE,fs=9)
    caption(ax,"The ethical work is deciding how much monitoring is PROPORTIONATE — and whether people were TOLD (transparency + consent).",y=6,fs=9.8)
    save(fig,"s9_seesaw.png")

def s10_spectrum():
    fig,ax=canvas(10,4.2)
    ax.text(50,90,"Opinion → criticism → defamation: where the line is",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    segs=[("OPINION\n'I didn't enjoy\nthe coffee'",TEAL,6),
          ("CRITICISM\n'service is slow\nand overpriced'",BLUE,36),
          ("DEFAMATION\n'the owner is a\nthief' (false fact)",CORAL,66)]
    for t,c,x in segs:
        rbox(ax,x,42,28,26,t,fc=c,fs=9.5)
    arrow(ax,6,36,94,36,color=GREY,lw=2.0)
    ax.text(20,30,"protected",ha="center",color=TEAL,fontsize=9,style="italic")
    ax.text(80,30,"legal risk (ETA 2063)",ha="center",color=CORAL,fontsize=9,style="italic")
    caption(ax,"Test: FACT vs OPINION, and TRUE vs FALSE. Opinion and honest criticism are NOT defamation — a false statement of fact is.",y=8,fs=9.8)
    save(fig,"s10_spectrum.png")

def s10_verify():
    fig,ax=canvas(10,4.8)
    ax.text(50,94,"Verify before you share — three checks",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    rbox(ax,8,64,84,12,"A shocking post lands in your feed",fc=NAVY,fs=10)
    checks=[("1  SOURCE\ncredible? who posted it?",BLUE,6),
            ("2  CORROBORATION\nreported anywhere reputable?",TEAL,37),
            ("3  EMOTION\njust fear / urgency? (red flag)",AMBER,68)]
    for t,c,x in checks:
        rbox(ax,x,38,26,16,t,fc=c,fs=8.6)
        arrow(ax,x+13,64,x+13,54,color=GREY,lw=1.6)
    rbox(ax,10,12,22,14,"SHARE\nall three pass",fc=TEAL,fs=9)
    rbox(ax,39,12,22,14,"HOLD\nunsure",fc=AMBER,fs=9)
    rbox(ax,68,12,22,14,"REPORT\nclearly false / harmful",fc=CORAL,fs=9)
    for x in [21,50,79]:
        arrow(ax,x,38,x,26,color=GREY,lw=1.6)
    caption(ax,"Manufactured urgency ('withdraw your money NOW') is the classic signature of disinformation and scams.",y=2,fs=9.6)
    save(fig,"s10_verify.png")

for fn in [s6_web,s7_map,s8_insider,s9_trail,s9_seesaw,s10_spectrum,s10_verify]:
    fn()
print("\nAll IT246 Unit 2 diagrams written to",OUT)
