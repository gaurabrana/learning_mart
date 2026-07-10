#!/usr/bin/env python3
"""Concept diagrams for IT250 (eighth) Unit 1 — Introduction to the Digital Economy (S1–S8).
Genuinely spatial concepts only (economy evolution, digital-economy ecosystem web, explicit/tacit
iceberg, digital+knowledge overlap & the WHAT/HOW/NEXT hook, the four industrial revolutions
timeline, 4IR three-legged fusion, Nepal 4IR SWOT, influence quadrant); all comparisons and
concrete-example sets are native PPTX tables in the deck (§7A). License-safe (matplotlib only).
Output -> eighth/images/   Run: python3 build_unit1_images.py
"""
import os, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, Polygon, FancyArrowPatch, Ellipse

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

def s1_evolution():
    fig,ax=canvas(10,4.6)
    ax.text(50,92,"How value shifted: three economies",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    stages=[("TRADITIONAL\nland · labour · goods\n(farm, trade)",TEAL,16),
            ("INFORMATION\ncomputers · data\n(records, PCs)",BLUE,50),
            ("DIGITAL\nplatforms · networks · AI\n(eSewa, Daraz)",CORAL,84)]
    for t,c,x in stages:
        rbox(ax,x-14,40,28,30,t,fc=c,fs=9.2)
    for x1,x2 in [(50-14+28,50-14),(84-14,50+14)]:
        pass
    arrow(ax,16+14,55,50-14,55,color=GREY,lw=2.2)
    arrow(ax,50+14,55,84-14,55,color=GREY,lw=2.2)
    ax.text(50,20,"each era keeps the last, but the SOURCE of value moves →",ha="center",color=NAVY,fontsize=10,style="italic")
    caption(ax,"The digital economy didn't erase farms or factories — it changed where new value comes from: data, platforms, and networks.",y=6,fs=9.6)
    save(fig,"s1_evolution.png")

def s2_ecosystem():
    fig,ax=canvas(10,5.4)
    ax.text(50,96,"The digital-economy ecosystem — four actors, one web",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    cx,cy=50,48
    rbox(ax,cx-13,cy-7,26,14,"DIGITAL\nECONOMY",fc=NAVY,fs=10.5)
    nodes=[("CONSUMERS\nusers, wallets, buyers",TEAL,20,78),
           ("BUSINESSES /\nPLATFORMS\nDaraz, eSewa, Pathao",BLUE,80,78),
           ("GOVERNMENT /\nREGULATORS\nNRB, Min. of Comm.",AMBER,20,16),
           ("TECH PROVIDERS\nISPs, Ntc/Ncell, cloud",CORAL,80,16)]
    for t,c,x,y in nodes:
        rbox(ax,x-15,y-9,30,18,t,fc=c,fs=8.6)
        arrow(ax,x+(cx-x)*0.28,y+(cy-y)*0.28,x+(cx-x)*0.66,y+(cy-y)*0.66,color=GREY,lw=1.6)
        arrow(ax,cx+(x-cx)*0.30,cy+(y-cy)*0.30,cx+(x-cx)*0.62,cy+(y-cy)*0.62,color=LGREY,lw=1.4)
    caption(ax,"Value flows both ways between all four. Take any one away — no smartphones, no NRB rules, no users — and the wallet economy stalls.",y=2,fs=9.4)
    save(fig,"s2_ecosystem.png")

def s3_iceberg():
    fig,ax=canvas(10,5.2)
    ax.text(50,95,"Knowledge is an iceberg: explicit vs tacit",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    # waterline
    ax.add_patch(Rectangle((6,10),88,44,fc="#DCEBF6",ec="none",zorder=1))
    ax.plot([6,94],[54,54],color=BLUE,lw=1.6,ls="--",zorder=2)
    ax.text(90,56,"waterline",ha="right",color=BLUE,fontsize=8.5,style="italic")
    # tip (explicit)
    ax.add_patch(Polygon([(50,88),(38,55),(62,55)],closed=True,fc=TEAL,ec=WHITE,lw=1.4,zorder=3))
    ax.text(50,68,"EXPLICIT",ha="center",color=WHITE,fontsize=10.5,fontweight="bold",zorder=4)
    ax.text(50,60,"written, recorded\nmanuals · docs · code",ha="center",color=WHITE,fontsize=8.2,zorder=4)
    # base (tacit)
    ax.add_patch(Polygon([(38,54),(62,54),(78,14),(22,14)],closed=True,fc=NAVY,ec=WHITE,lw=1.4,zorder=3))
    ax.text(50,44,"TACIT",ha="center",color=WHITE,fontsize=11,fontweight="bold",zorder=4)
    ax.text(50,34,"in people's heads · experience\nintuition · skill · 'know-how'",ha="center",color="#CFE0EE",fontsize=8.6,zorder=4)
    caption(ax,"Explicit knowledge is easy to store and share; the larger, tacit part walks out the door when an expert leaves — the K-economy's core challenge.",y=3,fs=9.4)
    save(fig,"s3_iceberg.png")

def s5_overlap():
    fig,ax=canvas(10,5.0)
    ax.text(50,95,"Two lenses on one modern economy",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    ax.add_patch(Circle((38,50),26,fc=BLUE,ec="none",alpha=0.75,zorder=2))
    ax.add_patch(Circle((62,50),26,fc=TEAL,ec="none",alpha=0.75,zorder=2))
    ax.text(26,66,"DIGITAL",ha="center",color=WHITE,fontsize=12,fontweight="bold",zorder=4)
    ax.text(26,58,"the HOW\ninfrastructure,\nplatforms, data",ha="center",color=WHITE,fontsize=8.4,zorder=4)
    ax.text(74,66,"KNOWLEDGE",ha="center",color=WHITE,fontsize=12,fontweight="bold",zorder=4)
    ax.text(74,58,"the WHAT\nskills, ideas,\ninnovation",ha="center",color=WHITE,fontsize=8.4,zorder=4)
    ax.text(50,50,"Digitized\nIntelligence",ha="center",va="center",color=NAVY,fontsize=9.6,fontweight="bold",zorder=5)
    ax.text(50,20,"4IR = the NEXT frontier (physical + digital + biological)",ha="center",color=CORAL,fontsize=10.5,fontweight="bold")
    caption(ax,"Knowledge workers BUILD the platforms; the platforms GENERATE data that powers more knowledge work. They reinforce each other.",y=4,fs=9.4)
    save(fig,"s5_overlap.png")

def s6_timeline():
    fig,ax=canvas(10,4.8)
    ax.text(50,93,"The four industrial revolutions",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    revs=[("1st  ~1760s","Steam &\nmechanization",TEAL,14),
          ("2nd  ~1870s","Electricity &\nmass production",BLUE,38),
          ("3rd  ~1970s","Electronics,\ncomputers, automation",AMBER,62),
          ("4th  2000s–","AI, data, IoT,\nsmart systems",CORAL,86)]
    arrow(ax,8,40,96,40,color=GREY,lw=2.2)
    for i,(era,desc,c,x) in enumerate(revs):
        y=58 if i%2==0 else 8
        rbox(ax,x-11,y,22,22,era+"\n"+desc,fc=c,fs=8.3)
        ax.add_patch(Circle((x,40),1.8,fc=c,ec=WHITE,lw=1.2,zorder=4))
        ax.plot([x,x],[40,y if y>40 else y+22],color=c,lw=1.3,zorder=2)
    caption(ax,"Each revolution rewired what an economy can do. The 4th is not 'more computers' — it fuses the physical, digital, and biological.",y=2,fs=9.4)
    save(fig,"s6_timeline.png")

def s6_fusion():
    fig,ax=canvas(10,5.0)
    ax.text(50,95,"4IR = fusion of three worlds",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    ax.add_patch(Circle((38,58),22,fc=BLUE,ec="none",alpha=0.72,zorder=2))
    ax.add_patch(Circle((62,58),22,fc=TEAL,ec="none",alpha=0.72,zorder=2))
    ax.add_patch(Circle((50,38),22,fc=CORAL,ec="none",alpha=0.72,zorder=2))
    ax.text(30,66,"PHYSICAL",ha="center",color=WHITE,fontsize=10.5,fontweight="bold",zorder=4)
    ax.text(30,60,"robots, 3D print,\nself-driving",ha="center",color=WHITE,fontsize=7.8,zorder=4)
    ax.text(70,66,"DIGITAL",ha="center",color=WHITE,fontsize=10.5,fontweight="bold",zorder=4)
    ax.text(70,60,"AI, IoT, cloud,\nbig data",ha="center",color=WHITE,fontsize=7.8,zorder=4)
    ax.text(50,30,"BIOLOGICAL",ha="center",color=WHITE,fontsize=10.5,fontweight="bold",zorder=4)
    ax.text(50,25,"genomics, biometrics,\ngene editing",ha="center",color=WHITE,fontsize=7.8,zorder=4)
    ax.text(50,50,"cyber-\nphysical\nsystems",ha="center",va="center",color=NAVY,fontsize=8.6,fontweight="bold",zorder=5)
    caption(ax,"A self-diagnosing factory (physical+digital) or AI-read gene test (digital+biological) is only possible when the three worlds merge.",y=3,fs=9.3)
    save(fig,"s6_fusion.png")

def s7_swot():
    fig,ax=canvas(10,5.2)
    ax.text(50,96,"Nepal's 4IR readiness — a SWOT",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    quad=[("STRENGTHS",TEAL,6,50,"• Young, tech-open population\n• Growing IT education\n• Fast digital-payment uptake"),
          ("WEAKNESSES",CORAL,52,50,"• Weak rural connectivity, power\n• Slow policy / regulation\n• Skill & R&D gaps"),
          ("OPPORTUNITIES",BLUE,6,8,"• IT/BPO outsourcing exports\n• Tourism-tech, agri-tech\n• Leapfrogging legacy stages"),
          ("THREATS",AMBER,52,8,"• Job loss without reskilling\n• Cyber & privacy risk\n• Widening digital divide")]
    for title,c,x,y,body in quad:
        ax.add_patch(FancyBboxPatch((x,y),42,38,boxstyle="round,pad=0.4,rounding_size=2",fc=WHITE,ec=c,lw=2.0,zorder=2))
        ax.add_patch(Rectangle((x,y+31),42,7,fc=c,ec="none",zorder=3))
        ax.text(x+21,y+34.5,title,ha="center",va="center",color=WHITE,fontsize=10,fontweight="bold",zorder=4)
        ax.text(x+2.5,y+27,body,ha="left",va="top",color=INK,fontsize=8.3,zorder=4)
    caption(ax,"Internal (strengths/weaknesses) vs external (opportunities/threats): readiness is real but uneven — reskilling decides the outcome.",y=2,fs=9.3)
    save(fig,"s7_swot.png")

def s8_quadrant():
    fig,ax=canvas(10,5.2)
    ax.text(50,96,"The digital economy's influence — four fronts",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    quad=[("SUSTAINABILITY",TEAL,6,50,"+ paperless, remote work, e-gov\n–  e-waste, data-centre energy"),
          ("PRIVACY",BLUE,52,50,"+ convenience, personalization\n–  tracking, consent gaps, misuse"),
          ("REGULATION",AMBER,6,8,"+ trust, consumer protection\n–  law lags tech (data-protection gap)"),
          ("STRATEGY",CORAL,52,8,"+ data-driven, digital-first edge\n–  disruption, constant adaptation")]
    for title,c,x,y,body in quad:
        ax.add_patch(FancyBboxPatch((x,y),42,38,boxstyle="round,pad=0.4,rounding_size=2",fc=WHITE,ec=c,lw=2.0,zorder=2))
        ax.add_patch(Rectangle((x,y+31),42,7,fc=c,ec="none",zorder=3))
        ax.text(x+21,y+34.5,title,ha="center",va="center",color=WHITE,fontsize=10,fontweight="bold",zorder=4)
        ax.text(x+2.5,y+26,body,ha="left",va="top",color=INK,fontsize=8.6,zorder=4)
    caption(ax,"Every front cuts both ways. 'Going digital' is not automatically green or safe — regulation and strategy decide who gains and who pays.",y=2,fs=9.3)
    save(fig,"s8_quadrant.png")

for fn in [s1_evolution,s2_ecosystem,s3_iceberg,s5_overlap,s6_timeline,s6_fusion,s7_swot,s8_quadrant]:
    fn()
print("\nAll IT250 Unit 1 diagrams written to",OUT)
