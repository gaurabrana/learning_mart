#!/usr/bin/env python3
"""Concept diagrams for IT246 (sixth) Unit 9 — Cyber Law in the Context of Nepal
(S45–S48, the FINAL unit of the course). Genuinely spatial concepts only:
Nepal's cyber-law timeline, target-vs-tool grid, the complaint/enforcement flow,
the ETA's two halves, the digital-signature flow, the PKI trust pyramid, the CIA
triad, the policy→procedure hierarchy, and a course-on-a-page arc of all 9 units.
All comparisons/examples are native PPTX tables in the deck (§7A). License-safe.

⚠️ Legal note: dates/section numbers rendered here (ETA 2063/2008, ETR 2064, Cyber
Bureau 2018, "Section ~47") are ILLUSTRATIVE of the framework and its debate — verify
against the current official Nepali text before relying on specifics.
Output -> sixth/images/   Run: python3 build_unit9_images.py
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

# ---------------------------------------------------------------- S45
def s45_timeline():
    fig,ax=canvas(10,5.4)
    ax.text(50,95,"Nepal's cyber-law landscape — a timeline",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    ax.plot([6,94],[50,50],color=GREY,lw=2.5,zorder=1)
    # (x, label, colour, above?)
    marks=[(10,"Before 2004\nNo cyber statute\n(paper-era Muluki Ain)",CORAL,True),
           (30,"2063 BS / 2008 AD\nElectronic Transaction\nAct (ETA) — 1st cyber law",TEAL,False),
           (50,"2064 BS\nElectronic Transaction\nRules (ETR)",BLUE,True),
           (70,"2018\nNepal Police\nCyber Bureau set up",AMBER,False),
           (90,"Ongoing\nIT Bill / reform &\namendment proposals",GREY,True)]
    for x,label,c,above in marks:
        ax.add_patch(Circle((x,50),1.8,fc=c,ec=WHITE,lw=1.5,zorder=4))
        y=66 if above else 20
        rbox(ax,x-11,y,22,16,label,fc=c,fs=8.0)
        arrow(ax,x,50,x,(y+16 if above else y),color=c,lw=1.4) if above else arrow(ax,x,50,x,y+16,color=c,lw=1.4)
    caption(ax,"Nepal moved from NO digital-law era to the ETA 2063 — its primary cyber law — with reform still under debate. Dates illustrative: verify current law.",y=4,fs=9.3)
    save(fig,"s45_timeline.png")

def s45_targettool():
    fig,ax=canvas(10,5.2)
    ax.text(50,95,"Cybercrime: computer as TARGET vs computer as TOOL",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    ax.add_patch(FancyBboxPatch((5,18),42,66,boxstyle="round,pad=0.3,rounding_size=3",fc=PALEC,ec=CORAL,lw=2,zorder=1))
    ax.add_patch(FancyBboxPatch((53,18),42,66,boxstyle="round,pad=0.3,rounding_size=3",fc=PALEB,ec=BLUE,lw=2,zorder=1))
    ax.text(26,79,"TARGET",ha="center",color=CORAL,fontsize=12,fontweight="bold")
    ax.text(74,79,"TOOL",ha="center",color=BLUE,fontsize=12,fontweight="bold")
    ax.text(26,73,"the computer is attacked",ha="center",color=INK,fontsize=9,style="italic")
    ax.text(74,73,"the computer commits the crime",ha="center",color=INK,fontsize=9,style="italic")
    tgt=["Unauthorised access / hacking","Damage to computer source code","Data theft / breach","Denial-of-service attack"]
    tol=["Online financial fraud","Cyber-defamation","Harassment / cyberbullying","Fake profiles / identity theft"]
    for i,t in enumerate(tgt): ax.text(26,66-i*11,"•  "+t,ha="center",color=INK,fontsize=8.7)
    for i,t in enumerate(tol): ax.text(74,66-i*11,"•  "+t,ha="center",color=INK,fontsize=8.7)
    caption(ax,"If the computer is the victim → TARGET crime. If it is the weapon to harm a person → TOOL crime. Both are recognised under Nepali law.",y=6,fs=9.3)
    save(fig,"s45_targettool.png")

def s45_complaintflow():
    fig,ax=canvas(10,5.4)
    ax.text(50,96,"Reporting a cybercrime in Nepal — the enforcement path",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    steps=[("1  Incident — you are hacked, defamed, or defrauded online",CORAL,80),
           ("2  Preserve EVIDENCE — screenshots, URLs, dates, accounts",AMBER,64),
           ("3  File a complaint — Cyber Bureau (Bhotahiti) or local police",BLUE,48),
           ("4  Investigation — the Cyber Bureau traces & gathers proof",TEAL,32),
           ("5  Prosecution — case proceeds under the ETA in court / IT Tribunal",NAVY,16)]
    for text,c,y in steps:
        ax.add_patch(FancyBboxPatch((10,y),80,11,boxstyle="round,pad=0.2,rounding_size=2",fc=c,ec=WHITE,lw=1.4,zorder=3))
        ax.text(50,y+5.5,text,ha="center",va="center",color=WHITE,fontsize=9.4,fontweight="bold",zorder=4)
    for y in [80,64,48,32]:
        arrow(ax,50,y,50,y-5,color=GREY,lw=1.8)
    caption(ax,"Evidence first, then the Cyber Bureau. Knowing this path is practical citizenship. Procedure/venue illustrative — verify current law.",y=4,fs=9.3)
    save(fig,"s45_complaintflow.png")

# ---------------------------------------------------------------- S46
def s46_twohalves():
    fig,ax=canvas(10,5.0)
    ax.text(50,95,"The ETA 2063 has TWO halves — enable AND punish",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    ax.add_patch(FancyBboxPatch((5,20),42,64,boxstyle="round,pad=0.3,rounding_size=3",fc=PALET,ec=TEAL,lw=2,zorder=1))
    ax.add_patch(FancyBboxPatch((53,20),42,64,boxstyle="round,pad=0.3,rounding_size=3",fc=PALEC,ec=CORAL,lw=2,zorder=1))
    ax.text(26,78,"ENABLE  (most of the Act)",ha="center",color=TEAL,fontsize=10.5,fontweight="bold")
    ax.text(74,78,"PUNISH  (one chapter)",ha="center",color=CORAL,fontsize=10.5,fontweight="bold")
    en=["Legal recognition of e-records","Legal validity of digital signatures","Dispatch/receipt of e-records","Certificates, Controller & CAs","Enables e-commerce & e-governance"]
    pu=["Unauthorised access (hacking)","Damage to computer source code","Illegal/obscene e-publication","Computer fraud & forgery","Offences → fines + imprisonment"]
    for i,t in enumerate(en): ax.text(26,70-i*9.5,"•  "+t,ha="center",color=INK,fontsize=8.6)
    for i,t in enumerate(pu): ax.text(74,70-i*9.5,"•  "+t,ha="center",color=INK,fontsize=8.6)
    caption(ax,"Myth: 'the ETA is only about cybercrime.' Most of it ENABLES e-commerce; the offences chapter is just one part.",y=7,fs=9.3)
    save(fig,"s46_twohalves.png")

def s46_digsig():
    fig,ax=canvas(10,4.8)
    ax.text(50,93,"Digital signature — private key signs, public key verifies",ha="center",color=NAVY,fontsize=12,fontweight="bold")
    rbox(ax,4,52,20,20,"SENDER\nwrites the\ndocument",fc=BLUE,fs=8.6)
    rbox(ax,40,52,20,20,"SIGN with\nPRIVATE key",fc=TEAL,fs=8.6)
    rbox(ax,76,52,20,20,"VERIFY with\nPUBLIC key",fc=AMBER,fs=8.6)
    arrow(ax,24,62,40,62,color=GREY); arrow(ax,60,62,76,62,color=GREY)
    ax.text(84,46,"→ RECEIVER trusts it",ha="center",color=INK,fontsize=8.5,style="italic")
    props=[("Authentication","proves WHO signed"),("Integrity","proves it was NOT changed"),("Non-repudiation","signer can't later deny it")]
    for i,(t,d) in enumerate(props):
        x=10+i*30
        ax.add_patch(FancyBboxPatch((x,14),26,20,boxstyle="round,pad=0.2,rounding_size=2",fc=PALEB,ec=BLUE,lw=1.3,zorder=2))
        ax.text(x+13,28,t,ha="center",color=NAVY,fontsize=9,fontweight="bold")
        ax.text(x+13,20,d,ha="center",color=INK,fontsize=8.2)
    caption(ax,"Change one word and the signature breaks — like a wax seal that also fingerprints the message.",y=3,fs=9.3)
    save(fig,"s46_digsig.png")

# ---------------------------------------------------------------- S47
def s47_pki():
    fig,ax=canvas(10,5.0)
    ax.text(50,95,"Nepal's PKI trust chain — Controller → CAs → users",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    ax.add_patch(Polygon([(50,84),(24,20),(76,20)],closed=True,fc=PALEB,ec=BLUE,lw=1.6,zorder=1))
    tiers=[(72,NAVY,"CONTROLLER (OCC)","root authority — licenses & supervises CAs"),
           (50,BLUE,"Certifying Authorities (CAs)","licensed to issue digital-signature certificates"),
           (30,TEAL,"End-user certificates / subscribers","citizens, banks, businesses that sign & verify")]
    for y,c,t,d in tiers:
        ax.add_patch(FancyBboxPatch((30,y-4),40,8,boxstyle="round,pad=0.2,rounding_size=2",fc=c,ec=WHITE,lw=1.4,zorder=3))
        ax.text(50,y+0.5,t,ha="center",va="center",color=WHITE,fontsize=9.2,fontweight="bold",zorder=4)
        ax.text(50,y-6.5,d,ha="center",va="center",color=INK,fontsize=7.8,style="italic",zorder=4)
    caption(ax,"Trust flows down: the Controller (under MoCIT) is the root; a certificate is only as trustworthy as the chain above it.",y=5,fs=9.3)
    save(fig,"s47_pki.png")

# ---------------------------------------------------------------- S48
def s48_cia():
    fig,ax=canvas(10,5.0)
    ax.text(50,95,"Information security = the CIA triad",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    ax.add_patch(Polygon([(50,82),(16,22),(84,22)],closed=True,fc="none",ec=NAVY,lw=2.2,zorder=2))
    corners=[(50,82,TEAL,"CONFIDENTIALITY","only authorised eyes\nsee the data"),
             (16,20,BLUE,"INTEGRITY","data is accurate &\nunaltered"),
             (84,20,AMBER,"AVAILABILITY","data is there when\nneeded")]
    for x,y,c,t,d in corners:
        ax.add_patch(Circle((x,y),3,fc=c,ec=WHITE,lw=1.5,zorder=4))
        dy=6 if y>50 else -12
        ax.text(x,y+dy+6,t,ha="center",color=c,fontsize=10.5,fontweight="bold",zorder=5)
        ax.text(x,y+dy,d,ha="center",color=INK,fontsize=8.3,zorder=5)
    ax.text(50,46,"protect all three",ha="center",color=GREY,fontsize=9,style="italic")
    caption(ax,"Lose any one corner and the information is not secure. Law punishes AFTER; policy protects the triad BEFORE.",y=4,fs=9.3)
    save(fig,"s48_cia.png")

def s48_policyhierarchy():
    fig,ax=canvas(10,5.0)
    ax.text(50,95,"Policy → Standard → Procedure → Guideline",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    layers=[("POLICY — the rule & intent ('we protect customer data')",NAVY,70,18,64),
            ("STANDARD — the measurable requirement ('12-char passwords')",BLUE,54,26,48),
            ("PROCEDURE — the step-by-step how-to ('reset a password')",TEAL,38,33,34),
            ("GUIDELINE — recommended good practice (advisory)",AMBER,22,40,20)]
    for text,c,y,x,w in layers:
        ax.add_patch(Rectangle((x,y),w,14,fc=c,ec=WHITE,lw=1.5,zorder=3))
        ax.text(50,y+7,text,ha="center",va="center",color=WHITE,fontsize=8.6,fontweight="bold",zorder=4)
    caption(ax,"A policy states WHAT & WHY; standards make it measurable; procedures say HOW. Security is governance + people, not only firewalls.",y=6,fs=9.3)
    save(fig,"s48_policyhierarchy.png")

def s48_coursemap():
    fig,ax=canvas(10,5.2)
    ax.text(50,95,"The whole course as one arc — IT 246 on a page",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    phases=[("ETHICS\n(should)\nU1–U4",TEAL,16),("SECURITY\n(protect)\nU5–U7",BLUE,38),
            ("FORENSICS\n(investigate)\nU8",AMBER,60),("LAW\n(govern & punish)\nU9",CORAL,82)]
    for t,c,x in phases:
        rbox(ax,x-9,58,18,22,t,fc=c,fs=8.8)
    for x in [16,38,60]:
        arrow(ax,x+9,69,x+22-9,69,color=GREY,lw=2.0)
    units=["U1 Ethics overview","U2 IT workers & users","U3 Intellectual property","U4 Software & orgs",
           "U5 Cybersecurity","U6 Personal security","U7 Social engineering","U8 Digital forensics","U9 Cyber law — Nepal"]
    for i,u in enumerate(units):
        col=0 if i<5 else 1
        x=8 if col==0 else 54
        y=44-(i%5 if col==0 else i-5)*8
        ax.text(x,y,"•  "+u,ha="left",color=INK,fontsize=8.6)
    caption(ax,"Ethics says what you SHOULD do, security PROTECTS, forensics INVESTIGATES, and law GOVERNS — Nepal context binds Units 8–9.",y=3,fs=9.3)
    save(fig,"s48_coursemap.png")

for fn in [s45_timeline,s45_targettool,s45_complaintflow,s46_twohalves,s46_digsig,
           s47_pki,s48_cia,s48_policyhierarchy,s48_coursemap]:
    fn()
print("\nAll IT246 Unit 9 diagrams written to",OUT)
