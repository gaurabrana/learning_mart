#!/usr/bin/env python3
"""Concept diagrams for IT250 (eighth) Unit 4 — Digital Transformation (S26-S33).
Genuinely spatial concepts only (the 3-tier digitization ladder, driver categories, SDG
acceleration, traditional-vs-digital globalization contrast, the growth flow, the money-evolution
timeline, the three currency types); every comparison and concrete-example set is a native PPTX
table in the deck (see COURSE_MATERIAL_STANDARD.md §7A). Licence-safe, no emoji / exotic glyphs.
Output -> eighth/images/   Run: python3 build_unit4_images.py
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

def s26_three_tier():
    fig,ax=canvas(10,5.4)
    ax.text(50,95,"Three tiers of going digital: an ascending ladder",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    tiers=[("DIGITIZATION","turn paper into DATA\n(scan files, PDF forms)","fax -> PDF; ledger -> Excel",BLUE,8,30,26),
           ("DIGITALIZATION","improve a PROCESS with tech\n(automate a workflow)","online booking; e-payment",TEAL,37,44,26),
           ("DIGITAL TRANSFORMATION","new BUSINESS MODEL & culture\n(reinvent how value is made)","Daraz, Pathao, eSewa",AMBER,66,58,28)]
    for title,sub,ex,c,x,y,h in tiers:
        ax.add_patch(FancyBboxPatch((x,18),27,h,boxstyle="round,pad=0.3,rounding_size=2",fc=c,ec="none",zorder=3))
        ax.text(x+13.5,18+h-6,title,ha="center",va="center",color=WHITE,fontsize=9.4,fontweight="bold",zorder=4)
        ax.text(x+13.5,18+h-16,sub,ha="center",va="center",color=WHITE,fontsize=7.8,zorder=4)
        ax.text(x+13.5,22,ex,ha="center",va="center",color="#EAF2FA",fontsize=7.2,style="italic",zorder=4)
    arrow(ax,20,82,44,82,color=GREY,lw=2.0); arrow(ax,49,82,73,82,color=GREY,lw=2.0)
    ax.text(50,88,"increasing depth of change ->",ha="center",color=GREY,fontsize=8.6,style="italic")
    caption(ax,"Digitization = data; digitalization = process; transformation = the whole business model changes. Each tier builds on the one before.",y=6,fs=9.2)
    save(fig,"s26_three_tier.png")

def s27_drivers():
    fig,ax=canvas(10,5.2)
    ax.text(50,95,"What drives digital transformation",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    cx,cy=50,50
    rbox(ax,cx-14,cy-9,28,18,"DIGITAL\nTRANSFORMATION",fc=NAVY,fs=10)
    drv=[("TECHNOLOGICAL\ninternet, mobile,\ncloud, AI, IoT",BLUE,18,78),
         ("ECONOMIC\ncost, competition,\nproductivity",TEAL,82,78),
         ("SOCIAL\nuser behaviour,\nyouth, policy",AMBER,18,22),
         ("CRISIS\nCOVID-19 shock\n(accelerator)",CORAL,82,22)]
    for t,c,x,y in drv:
        rbox(ax,x-15,y-9,30,18,t,fc=c,fs=8.0)
        arrow(ax,x+(cx-x)*0.34,y+(cy-y)*0.34,x+(cx-x)*0.60,y+(cy-y)*0.60,color=GREY,lw=1.7)
    caption(ax,"Four forces push organisations to transform: technology makes it possible, economics makes it necessary, society expects it, and crisis accelerates it.",y=5,fs=9.0)
    save(fig,"s27_drivers.png")

def s28_sdg():
    fig,ax=canvas(10,5.2)
    ax.text(50,95,"How digital transformation accelerates the SDGs",ha="center",color=NAVY,fontsize=12.2,fontweight="bold")
    rbox(ax,4,42,20,18,"DIGITAL\nTRANSFORM-\nATION",fc=NAVY,fs=9)
    mechs=["speed","reach","efficiency","transparency","scalability"]
    ax.add_patch(FancyBboxPatch((30,30),20,44,boxstyle="round,pad=0.3,rounding_size=2",fc=PALET,ec=TEAL,lw=1.6,zorder=2))
    ax.text(40,70,"5 MECHANISMS",ha="center",color=TEAL,fontsize=8.6,fontweight="bold",zorder=4)
    for i,m in enumerate(mechs):
        ax.text(40,63-i*7,"- "+m,ha="center",color=INK,fontsize=8.2,zorder=4)
    arrow(ax,24,51,30,51,color=GREY,lw=1.8)
    sdgs=[("SDG 4\nEducation",BLUE,80),("SDG 8\nDecent work",TEAL,63),
          ("SDG 9\nInnovation",AMBER,46),("SDG 16\nGovernance",CORAL,29)]
    for t,c,y in sdgs:
        rbox(ax,72,y-6,24,12,t,fc=c,fs=8.2)
        arrow(ax,50,52,72,y,color=LGREY,lw=1.3)
    caption(ax,"DT speeds up, widens reach, cuts cost, adds transparency and scales services - so goals like SDG 4/8/9/16 are reached faster.",y=6,fs=9.0)
    save(fig,"s28_sdg.png")

def s30_globalization():
    fig,ax=canvas(10,5.0)
    ax.text(27,94,"TRADITIONAL globalization",ha="center",color=NAVY,fontsize=11,fontweight="bold")
    ax.text(75,94,"DIGITAL globalization",ha="center",color=NAVY,fontsize=11,fontweight="bold")
    ax.plot([50,50],[8,88],color=LGREY,lw=1.2,ls="--")
    # traditional: factory -> ship -> country, slow, big firms
    rbox(ax,4,62,18,13,"FACTORY\ngoods",fc=GREY,fs=8.2)
    rbox(ax,30,62,16,13,"SHIP /\nborder",fc=GREY,fs=8.2)
    arrow(ax,22,68,30,68,color=NAVY,lw=2.0)
    ax.text(27,52,"physical goods,\nslow, costly, big firms",ha="center",color=INK,fontsize=8.0)
    ax.text(27,38,"weeks/months\ncontainers, tariffs",ha="center",color=CORAL,fontsize=7.8,style="italic")
    # digital: laptop -> internet -> world, instant, anyone
    rbox(ax,55,62,17,13,"LAPTOP /\nskill",fc=BLUE,fs=8.2)
    rbox(ax,80,62,16,13,"INTERNET\n= world",fc=TEAL,fs=8.2)
    arrow(ax,72,68,80,68,color=BLUE,lw=2.0)
    ax.text(76,52,"services, data, software,\ninstant, low cost, anyone",ha="center",color=INK,fontsize=8.0)
    ax.text(76,38,"seconds\na freelancer in Nepal -> a client abroad",ha="center",color=TEAL,fontsize=7.6,style="italic")
    caption(ax,"Traditional globalization moves physical goods slowly across borders; digital globalization moves services, data and skills instantly - so a small player can go global.",y=6,fs=8.8)
    save(fig,"s30_globalization.png")

def s31_growth_flow():
    fig,ax=canvas(10,4.8)
    ax.text(50,94,"How digital transformation grows the economy",ha="center",color=NAVY,fontsize=12.2,fontweight="bold")
    steps=[("DIGITAL\nSKILLS",BLUE),("JOBS &\nBUSINESS",TEAL),("INCOME &\nEXPORTS",AMBER),("GDP\nGROWTH",CORAL)]
    xs=[6,30,54,78]
    for (t,c),x in zip(steps,xs):
        rbox(ax,x,48,18,20,t,fc=c,fs=9.0)
    for i in range(3):
        arrow(ax,xs[i]+18,58,xs[i+1],58,color=GREY,lw=2.0)
    # feedback loop
    ax.add_patch(FancyArrowPatch((87,48),(15,40),connectionstyle="arc3,rad=0.3",arrowstyle="-|>",mutation_scale=14,color=LGREY,lw=1.6,zorder=2))
    ax.text(50,30,"reinvest -> more skills, infrastructure (the loop repeats)",ha="center",color=GREY,fontsize=8.2,style="italic")
    caption(ax,"Digital skills create jobs and businesses; these raise income and exports (e.g. IT/freelancing); spending and reinvestment lift GDP - low marginal cost lets it scale.",y=8,fs=8.8)
    save(fig,"s31_growth_flow.png")

def s32_money_evolution():
    fig,ax=canvas(10,4.6)
    ax.text(50,94,"The evolution of money",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    steps=[("BARTER\ngoods for\ngoods",GREY),("COINS\nmetal, set\nvalue",AMBER),("PAPER\nnotes (NRB\nrupee)",BLUE),
           ("BANK /\nCARDS\naccount money",TEAL),("DIGITAL\nwallets\n(eSewa)",CORAL)]
    xs=[4,23,42,61,80]
    for (t,c),x in zip(steps,xs):
        rbox(ax,x,46,17,24,t,fc=c,fs=8.0)
    for i in range(4):
        arrow(ax,xs[i]+17,58,xs[i+1],58,color=GREY,lw=1.9)
    ax.text(50,36,"less physical, more convenient, faster to move ->",ha="center",color=GREY,fontsize=8.6,style="italic")
    caption(ax,"Money became steadily less physical - but a digital wallet still holds the SAME rupee the central bank issues. The form changed; the currency did not.",y=8,fs=8.9)
    save(fig,"s32_money_evolution.png")

def s33_currency_types():
    fig,ax=canvas(10,5.2)
    ax.text(50,95,"Three types of digital currency",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    cols=[("CRYPTOCURRENCY",CORAL,"issuer: NONE\n(decentralised)","backing: none\n- volatile","e.g. Bitcoin\nBANNED in Nepal"),
          ("STABLECOIN",AMBER,"issuer: private\ncompany","backing: pegged\nto USD / asset","e.g. USDT\nremittance use"),
          ("CBDC",TEAL,"issuer: CENTRAL\nBANK","backing: the\nstate (legal)","e.g. e-CNY, eNaira\nNRB studying")]
    xs=[6,38,70]
    for (title,c,a,b,d),x in zip(cols,xs):
        ax.add_patch(FancyBboxPatch((x,20),26,60,boxstyle="round,pad=0.4,rounding_size=2",fc=WHITE,ec=c,lw=2.2,zorder=2))
        ax.add_patch(Rectangle((x,71),26,9,fc=c,ec="none",zorder=3))
        ax.text(x+13,75.5,title,ha="center",va="center",color=WHITE,fontsize=9.2,fontweight="bold",zorder=4)
        ax.text(x+13,60,a,ha="center",va="center",color=INK,fontsize=8.0,zorder=4)
        ax.text(x+13,47,b,ha="center",va="center",color=INK,fontsize=8.0,zorder=4)
        ax.add_patch(FancyBboxPatch((x+2,24),22,12,boxstyle="round,pad=0.2,rounding_size=1",fc=c,ec="none",zorder=3))
        ax.text(x+13,30,d,ha="center",va="center",color=WHITE,fontsize=7.6,fontweight="bold",zorder=4)
    caption(ax,"Who issues it and what backs it is the key difference: nobody (crypto), a company (stablecoin), or the central bank (CBDC).",y=8,fs=9.0)
    save(fig,"s33_currency_types.png")

for fn in [s26_three_tier,s27_drivers,s28_sdg,s30_globalization,s31_growth_flow,s32_money_evolution,s33_currency_types]:
    fn()
print("\nAll IT250 Unit 4 diagrams written to",OUT)
