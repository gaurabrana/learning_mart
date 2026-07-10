#!/usr/bin/env python3
"""Concept diagrams for IT250 (eighth) Unit 6 — Digitalization in the Nepalese Perspective (S42–S48).
Genuinely spatial concepts only (the 4 e-governance types around the state; the 4-layer e-gov
architecture stack; the Digital Nepal Framework's 8 sectors; the 4-step wallet flow with NRB/NTA
regulators; the 4-sector digital scorecard). All comparisons and concrete-example sets are native
PPTX tables in the deck (§7A). matplotlib (Agg) only, NO emoji / exotic glyphs. License-safe.
Output -> eighth/images/   Run: python3 build_unit6_images.py
"""
import os, math
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
def arrow(ax,x1,y1,x2,y2,color=NAVY,lw=2.0,style="-|>"):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle=style,mutation_scale=13,color=color,lw=lw,zorder=2))
def caption(ax,text,color=GREY,y=3,fs=9.4):
    ax.text(50,y,text,ha="center",fontsize=fs,style="italic",color=color)

def s42_egov_types():
    fig,ax=canvas(10,5.2)
    ax.text(50,95,"The four types of e-governance — who the state connects with",ha="center",color=NAVY,fontsize=12,fontweight="bold")
    cx,cy=50,52
    rbox(ax,cx-12,cy-8,24,16,"GOVERNMENT\n(the state)",fc=NAVY,fs=10.5)
    grp=[("G2C\nCITIZENS\nNagarik App",TEAL,18,80),
         ("G2B\nBUSINESS\nIRD e-VAT, PPMO",BLUE,82,80),
         ("G2G\nGOVT AGENCIES\nfederal-local data",AMBER,18,24),
         ("G2E\nEMPLOYEES\npayroll, records",CORAL,82,24)]
    for t,c,x,y in grp:
        rbox(ax,x-13,y-9,26,18,t,fc=c,fs=8.2)
        # two-way arrows between hub and each group
        arrow(ax,cx+(x-cx)*0.30,cy+(y-cy)*0.30,cx+(x-cx)*0.60,cy+(y-cy)*0.60,color=GREY,lw=1.6)
        arrow(ax,x+(cx-x)*0.30,y+(cy-y)*0.30,x+(cx-x)*0.60,y+(cy-y)*0.60,color=LGREY,lw=1.5)
    caption(ax,"E-governance links the state to four groups, both ways: Citizens (G2C), Business (G2B), other Government (G2G), Employees (G2E).",y=4)
    save(fig,"s42_egov_types.png")

def s43_egov_architecture():
    fig,ax=canvas(10,5.4)
    ax.text(50,96,"The 4-layer e-governance architecture (top = what you see; bottom = what runs it)",ha="center",color=NAVY,fontsize=11,fontweight="bold")
    layers=[("PRESENTATION  —  app / website / portal you use","Nagarik App screen, e-passport portal",BLUE,74),
            ("APPLICATION  —  business logic, rules, workflows","validates forms, applies rules, routes requests",TEAL,58),
            ("DATA  —  databases & registries","citizen, PAN, vehicle, land records",AMBER,42),
            ("INFRASTRUCTURE  —  servers, network, data centre","Govt Integrated Data Centre, fibre, cloud",NAVY,26)]
    for title,sub,c,y in layers:
        ax.add_patch(FancyBboxPatch((14,y),60,13,boxstyle="round,pad=0.1,rounding_size=1.5",fc=c,ec="none",zorder=3))
        ax.text(44,y+8.4,title,ha="center",va="center",color=WHITE,fontsize=9.2,fontweight="bold",zorder=4)
        ax.text(44,y+3.4,sub,ha="center",va="center",color="#E8F0F7",fontsize=7.8,zorder=4)
    for y in [72,56,40]:
        arrow(ax,44,y,44,y-2.6,color=GREY,lw=1.6,style="<|-|>")
    # security band on the right
    ax.add_patch(FancyBboxPatch((78,26),16,60,boxstyle="round,pad=0.2,rounding_size=2",fc=PALEC,ec=CORAL,lw=1.6,zorder=2))
    ax.text(86,80,"SECURITY\n(all layers)",ha="center",va="center",color=CORAL,fontsize=8.6,fontweight="bold")
    ax.text(86,52,"National-ID\nlogin\n\nEncryption\n\n2FA / OTP",ha="center",va="center",color=INK,fontsize=8.0)
    caption(ax,"A request flows down the layers and the result flows back up; security wraps every layer. 'Server down' usually means the infrastructure layer failed.",y=13)
    save(fig,"s43_egov_architecture.png")

def s44_digital_nepal():
    fig,ax=canvas(10,5.4)
    ax.text(50,95,"Digital Nepal Framework (2019): 8 sectors, ~80 initiatives (reported)",ha="center",color=NAVY,fontsize=11.5,fontweight="bold")
    sectors=[("DIGITAL\nFOUNDATION",NAVY),("AGRICULTURE",TEAL),("HEALTH",BLUE),("EDUCATION",AMBER),
             ("ENERGY",CORAL),("TOURISM",TEAL),("FINANCE",BLUE),("URBAN INFRA &\nCONNECTIVITY",AMBER)]
    xs=[5,29,53,77]; ys=[55,28]
    for i,(t,c) in enumerate(sectors):
        x=xs[i%4]; y=ys[i//4]
        rbox(ax,x,y,18,17,t,fc=c,fs=8.4)
    ax.text(50,82,"Foundation = the base (connectivity, digital ID, payment rails, data centres)",ha="center",color=GREY,fontsize=8.6,style="italic")
    caption(ax,"One 'Digital Foundation' underpins seven service sectors. Adopted 2019; implementation partial — verify current progress before quoting.",y=13)
    save(fig,"s44_digital_nepal.png")

def s45_fin_inclusion():
    fig,ax=canvas(10,5.0)
    ax.text(50,95,"Digital wallet flow, and who regulates it",ha="center",color=NAVY,fontsize=12,fontweight="bold")
    steps=[("USER\n(payer)",TEAL,6),("WALLET /\nPLATFORM\neSewa, Khalti",BLUE,29),
           ("BANK\n(holds money)",AMBER,52),("RECEIVER\nmerchant / family",CORAL,75)]
    for t,c,x in steps:
        rbox(ax,x,44,19,16,t,fc=c,fs=8.4)
    for x in [25,48,71]:
        arrow(ax,x,52,x+4,52,color=GREY,lw=2.0)
    # regulators band
    ax.add_patch(FancyBboxPatch((6,74),88,12,boxstyle="round,pad=0.2,rounding_size=2",fc=PALEB,ec=BLUE,lw=1.6,zorder=2))
    ax.text(50,80,"REGULATORS:  NRB  — licenses wallets/banks, Payment & Settlement Act 2075, National Payment Switch, NepalPay QR interoperability, KYC   |   NTA — the telecom/internet it rides on",
            ha="center",va="center",color=NAVY,fontsize=7.6,fontweight="bold")
    for x in [15,38,61,84]:
        arrow(ax,x,74,x,61,color=LGREY,lw=1.2,style="-|>")
    ax.text(50,33,"NepalPay QR lets any wallet pay any merchant's QR — one interoperable standard.",ha="center",color=INK,fontsize=8.4)
    caption(ax,"Money moves User -> wallet -> bank -> receiver in seconds; NRB governs the money side, NTA the connectivity side.",y=16)
    save(fig,"s45_fin_inclusion.png")

def s48_sme_scorecard():
    fig,ax=canvas(10,5.2)
    ax.text(50,95,"The 4-sector digital scorecard — each win has a matching gap",ha="center",color=NAVY,fontsize=11.5,fontweight="bold")
    cols=[("TRADE","Daraz, UPI-Nepal,\nno middleman","Cash-only beyond\ncities; LDC 2026"),
          ("TOURISM","Instagram, direct\nbooking, QR tickets","Seasonal; rural\ncash-only"),
          ("AGRICULTURE","TelePlantDoctor,\nmobile banking","2G, older farmers,\nlow literacy"),
          ("SMEs","QR + social\ncommerce","Collateral, skills\ngap, informal")]
    xs=[5,29,53,77]
    for (title,win,gap),x in zip(cols,xs):
        ax.add_patch(Rectangle((x,82),18,7,fc=NAVY,ec="none",zorder=3))
        ax.text(x+9,85.5,title,ha="center",va="center",color=WHITE,fontsize=9.2,fontweight="bold",zorder=4)
        ax.add_patch(FancyBboxPatch((x,52),18,26,boxstyle="round,pad=0.2,rounding_size=1.5",fc=PALET,ec=TEAL,lw=1.4,zorder=2))
        ax.text(x+9,74,"WIN",ha="center",color=TEAL,fontsize=8.4,fontweight="bold")
        ax.text(x+9,62,win,ha="center",va="center",color=INK,fontsize=7.6)
        ax.add_patch(FancyBboxPatch((x,22),18,26,boxstyle="round,pad=0.2,rounding_size=1.5",fc=PALEA,ec=AMBER,lw=1.4,zorder=2))
        ax.text(x+9,44,"GAP",ha="center",color=AMBER,fontsize=8.4,fontweight="bold")
        ax.text(x+9,32,gap,ha="center",va="center",color=INK,fontsize=7.6)
    caption(ax,"Every sector shows the same shape: a genuine digital win, held back by an access/infrastructure gap. Figures are reported — verify before quoting.",y=11)
    save(fig,"s48_sme_scorecard.png")

for fn in [s42_egov_types,s43_egov_architecture,s44_digital_nepal,s45_fin_inclusion,s48_sme_scorecard]:
    fn()
print("\nAll IT250 Unit 6 diagrams written to",OUT)
