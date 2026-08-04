#!/usr/bin/env python3
"""Concept diagrams for IT246 (sixth) Unit 5 — Fundamentals of Cybersecurity (S22–S27).
Genuinely SPATIAL concepts only (CIA triad, the five domains, attack-surface growth,
supply-chain trust chain, threat->vulnerability->asset chain, risk matrix, DoS flood,
man-in-the-middle relay, DNS-phonebook tampering, ARP-LAN trust, the white->black hat
spectrum); every comparison / concrete-example set is a native PPTX table in the deck (§7A).
DEFENSIVE / educational framing only — nothing here is an attack recipe. License-safe.
Output -> sixth/images/   Run: python3 build_unit5_images.py
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
def arrow(ax,x1,y1,x2,y2,color=NAVY,lw=2.0,style="-|>"):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle=style,mutation_scale=14,color=color,lw=lw,zorder=2))
def caption(ax,text,color=GREY,y=3,fs=10.5):
    ax.text(50,y,text,ha="center",fontsize=fs,style="italic",color=color)

def s22_ciatriad():
    fig,ax=canvas(10,5.4)
    ax.text(50,96,"The CIA triad — the three goals every control serves",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    # triangle vertices
    top=(50,78); left=(16,26); right=(84,26)
    ax.add_patch(Polygon([top,left,right],closed=True,fc=PALEB,ec=BLUE,lw=2.2,zorder=2))
    ax.text(50,46,"SECURITY",ha="center",va="center",color=NAVY,fontsize=12,fontweight="bold",zorder=4)
    ax.text(50,40,"(saw off any leg\nand the stool falls)",ha="center",va="center",color=GREY,fontsize=8.4,style="italic",zorder=4)
    # corner cards
    rbox(ax,34,74,32,13,"CONFIDENTIALITY\nkept secret / access-controlled",fc=BLUE,fs=8.8)
    ax.text(50,71,"NP: eSewa balance not leaked",ha="center",color=BLUE,fontsize=8,zorder=5)
    rbox(ax,2,12,30,14,"INTEGRITY\ndata unchanged &\ntrustworthy",fc=TEAL,fs=8.8)
    ax.text(17,9,"NP: land records not altered",ha="center",color=TEAL,fontsize=8,zorder=5)
    rbox(ax,68,12,30,14,"AVAILABILITY\nusable when\nneeded",fc=CORAL,fs=8.8)
    ax.text(83,9,"NP: e-banking stays online",ha="center",color=CORAL,fontsize=8,zorder=5)
    caption(ax,"Confidentiality = secrecy · Integrity = trustworthiness · Availability = uptime. Security needs all three at once.",y=2.5,fs=9.6)
    save(fig,"s22_ciatriad.png")

def s22_domains():
    fig,ax=canvas(10,4.4)
    ax.text(50,90,"Cyberspace = the 'fifth domain' (a place like land, sea, air, space)",ha="center",color=NAVY,fontsize=12,fontweight="bold")
    doms=[("LAND",GREY,7),("SEA",GREY,25),("AIR",GREY,43),("SPACE",GREY,61)]
    for t,c,x in doms:
        rbox(ax,x,50,15,16,t,fc=LGREY,tc=NAVY,fs=9.5)
    rbox(ax,79,50,17,16,"CYBER\nspace",fc=BLUE,fs=9.5)
    ax.text(87.5,44,"the 5th",ha="center",color=BLUE,fontsize=8,style="italic")
    # what it includes
    inc=["Public internet & websites","Private / bank networks","Cloud & data centres",
         "Mobile apps (eSewa, Nagarik App)","OT/ICS — NEA grid, water","Connected devices (CCTV, IoT)"]
    for i,t in enumerate(inc):
        x=6+(i%3)*31; y=30-(i//3)*11
        ax.add_patch(FancyBboxPatch((x,y),29,8,boxstyle="round,pad=0.15,rounding_size=1.5",fc=PALEB,ec=BLUE,lw=1.0,zorder=3))
        ax.text(x+14.5,y+4,t,ha="center",va="center",color=NAVY,fontsize=7.8,zorder=4)
    caption(ax,"Cyberspace is NOT just 'the websites I visit' — it includes back-end systems, infrastructure (OT/ICS) and offline-connected devices.",y=2,fs=9.3)
    save(fig,"s22_domains.png")

def s23_attacksurface():
    fig,ax=canvas(10,4.8)
    ax.text(50,95,"The attack surface keeps growing — more devices = more to defend",ha="center",color=NAVY,fontsize=12,fontweight="bold")
    # 2010 side
    ax.text(25,84,"~2010",ha="center",color=GREY,fontsize=11,fontweight="bold")
    rbox(ax,17,66,16,10,"Shop till\n+ 1 PC",fc=TEAL,fs=8.5)
    ax.text(25,60,"few entry points",ha="center",color=TEAL,fontsize=8,style="italic")
    # divider
    ax.plot([50,50],[10,80],color=LGREY,lw=1.2,ls="--")
    # 2026 side
    ax.text(75,84,"2026",ha="center",color=GREY,fontsize=11,fontweight="bold")
    cloud=["QR pay\n(fonepay)","Cloud DB","Mobile app","Smart CCTV","IoT sensors","Staff phones","Nagarik App","Wi-Fi router"]
    for i,t in enumerate(cloud):
        x=56+(i%4)*10.5; y=66-(i//4)*13
        ax.add_patch(Circle((x+3.5,y+3),5.6,fc=PALEC,ec=CORAL,lw=1.1,zorder=3))
        ax.text(x+3.5,y+3,t,ha="center",va="center",color=CORAL,fontsize=6.2,zorder=4)
    ax.text(75,34,"many entry points",ha="center",color=CORAL,fontsize=8,style="italic")
    caption(ax,"Cloud, mobile, IoT, QR payments and remote work each ADD entry points. New features usually arrive before their security does.",y=6,fs=9.4)
    save(fig,"s23_attacksurface.png")

def s23_supplychain():
    fig,ax=canvas(10,4.2)
    ax.text(50,90,"Supply-chain risk — you trust your vendor's vendor too",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    nodes=[("YOUR BANK\n/ ministry",BLUE,8),("SOFTWARE\nVENDOR",TEAL,38),("VENDOR'S\nSUB-VENDOR",AMBER,68)]
    for t,c,x in nodes:
        rbox(ax,x,45,24,18,t,fc=c,fs=9.2)
    arrow(ax,32,54,38,54,color=GREY); arrow(ax,62,54,68,54,color=GREY)
    ax.text(35,66,"grants access",ha="center",color=GREY,fontsize=7.6,style="italic")
    ax.text(65,66,"grants access",ha="center",color=GREY,fontsize=7.6,style="italic")
    # breach travels back
    arrow(ax,80,42,20,32,color=CORAL,lw=2.2,style="-|>")
    ax.text(50,25,"A breach anywhere in the chain becomes YOUR breach",ha="center",color=CORAL,fontsize=9.5,fontweight="bold")
    caption(ax,"You outsource the work, not the accountability: a vendor's carelessness lands in your system.",y=6,fs=9.5)
    save(fig,"s23_supplychain.png")

def s24_tva():
    fig,ax=canvas(10,4.8)
    ax.text(50,94,"Threat actor → threat → exploits a vulnerability → harms an asset",ha="center",color=NAVY,fontsize=11.6,fontweight="bold")
    rbox(ax,3,55,20,16,"THREAT ACTOR\nattacker",fc=NAVY,fs=8.6)
    rbox(ax,27,55,18,16,"THREAT\ne.g. a worm",fc=CORAL,fs=8.8)
    rbox(ax,49,55,22,16,"VULNERABILITY\nunpatched server",fc=AMBER,fs=8.6)
    rbox(ax,75,55,22,16,"ASSET\ncitizen data",fc=TEAL,fs=8.8)
    arrow(ax,23,63,27,63); arrow(ax,45,63,49,63); arrow(ax,71,63,75,63)
    ax.text(60,73,"exploits",ha="center",color=AMBER,fontsize=8,style="italic")
    ax.text(86,73,"harms",ha="center",color=TEAL,fontsize=8,style="italic")
    # no vuln => blocked
    ax.add_patch(FancyBboxPatch((14,20),72,16,boxstyle="round,pad=0.3,rounding_size=2",fc=PALET,ec=TEAL,lw=1.6,zorder=3))
    ax.text(50,31,"NO vulnerability  ⇒  the threat cannot land",ha="center",color=TEAL,fontsize=10.5,fontweight="bold",zorder=4)
    ax.text(50,24.5,"Patching removes the weakness, so the same threat has nothing to exploit.",ha="center",color=INK,fontsize=8.6,zorder=4)
    caption(ax,"A flood is a threat; living in a basement is the vulnerability; your belongings are the asset. Fix the weakness and the threat is blocked.",y=6,fs=9.2)
    save(fig,"s24_tva.png")

def s24_riskmatrix():
    fig,ax=canvas(10,5.0)
    ax.text(50,95,"Risk = threat × vulnerability × impact  (likelihood × consequence)",ha="center",color=NAVY,fontsize=11.8,fontweight="bold")
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
    caption(ax,"High threat but NO vulnerability ≈ low risk; a tiny weakness with catastrophic impact ≈ high risk. Spend defence on the top-right first.",y=6,fs=9.3)
    save(fig,"s24_riskmatrix.png")

def s25_dos():
    fig,ax=canvas(10,4.8)
    ax.text(50,94,"Denial-of-Service — flood the service so real users can't get in",ha="center",color=NAVY,fontsize=11.8,fontweight="bold")
    # bots
    for i in range(5):
        y=20+i*14
        ax.add_patch(Circle((12,y),4.2,fc=CORAL,ec=WHITE,lw=1.0,zorder=3))
        ax.text(12,y,"bot",ha="center",va="center",color=WHITE,fontsize=6.5,zorder=4)
        arrow(ax,17,y,44,50,color=CORAL,lw=1.3)
    rbox(ax,46,40,20,20,"SERVER\noverwhelmed",fc=AMBER,fs=9)
    # legit user blocked
    rbox(ax,78,58,18,12,"real user",fc=TEAL,fs=8.5)
    ax.add_patch(FancyArrowPatch((78,64),(67,54),arrowstyle="-|>",mutation_scale=14,color=TEAL,lw=1.8,zorder=2,ls="--"))
    ax.text(88,50,"✕ blocked",ha="center",color=CORAL,fontsize=9,fontweight="bold")
    ax.text(30,74,"many fake requests",ha="center",color=CORAL,fontsize=8,style="italic")
    caption(ax,"DoS/DDoS attacks AVAILABILITY. Defences (conceptual): rate-limiting, CDN/scrubbing, spare capacity, ISP/NPCERT coordination.",y=6,fs=9.2)
    save(fig,"s25_dos.png")

def s26_mitm():
    fig,ax=canvas(10,4.4)
    ax.text(50,90,"Man-in-the-Middle — attacker secretly relays (and can alter) traffic",ha="center",color=NAVY,fontsize=11.8,fontweight="bold")
    rbox(ax,5,48,20,16,"YOU\ncafé Wi-Fi",fc=TEAL,fs=9)
    rbox(ax,40,48,20,16,"ATTACKER\nin the middle",fc=CORAL,fs=9)
    rbox(ax,75,48,20,16,"BANK\nserver",fc=BLUE,fs=9)
    arrow(ax,25,56,40,56,color=GREY); arrow(ax,60,56,75,56,color=GREY)
    ax.text(32.5,64,"reads /",ha="center",color=CORAL,fontsize=7.8,style="italic")
    ax.text(67.5,64,"alters",ha="center",color=CORAL,fontsize=7.8,style="italic")
    ax.add_patch(FancyBboxPatch((12,20),76,14,boxstyle="round,pad=0.3,rounding_size=2",fc=PALET,ec=TEAL,lw=1.6,zorder=3))
    ax.text(50,27,"Defence: HTTPS/TLS everywhere + VPN on untrusted Wi-Fi + heed certificate warnings",ha="center",color=TEAL,fontsize=9,fontweight="bold",zorder=4)
    caption(ax,"MITM breaks Confidentiality AND Integrity. Encryption makes the relayed traffic unreadable and un-alterable.",y=6,fs=9.2)
    save(fig,"s26_mitm.png")

def s26_dns():
    fig,ax=canvas(10,4.6)
    ax.text(50,92,"DNS poisoning — the 'phonebook' is tampered with",ha="center",color=NAVY,fontsize=12,fontweight="bold")
    rbox(ax,6,55,22,14,"you type\nesewa.com.np",fc=TEAL,fs=8.6)
    rbox(ax,39,55,24,14,"DNS 'phonebook'\n(poisoned)",fc=CORAL,fs=8.6)
    rbox(ax,72,66,24,12,"REAL server",fc=BLUE,fs=8.8)
    rbox(ax,72,44,24,12,"FAKE look-alike",fc=CORAL,fs=8.8)
    arrow(ax,28,62,39,62,color=GREY)
    ax.add_patch(FancyArrowPatch((63,60),(72,72),arrowstyle="-|>",mutation_scale=13,color=LGREY,lw=1.6,ls="--",zorder=2))
    arrow(ax,63,60,72,50,color=CORAL,lw=2.2)
    ax.text(70,55,"right NAME,\nwrong server",ha="center",color=CORAL,fontsize=7.4,style="italic")
    ax.add_patch(FancyBboxPatch((10,20),80,13,boxstyle="round,pad=0.3,rounding_size=2",fc=PALET,ec=TEAL,lw=1.6,zorder=3))
    ax.text(50,26.5,"Defence: DNSSEC · trusted resolvers · HTTPS + certificate checks (the warning is the tell)",ha="center",color=TEAL,fontsize=8.8,fontweight="bold",zorder=4)
    caption(ax,"The address bar can show the RIGHT name while pointing at a FAKE server — a certificate warning is your clue.",y=6,fs=9.1)
    save(fig,"s26_dns.png")

def s26_arp():
    fig,ax=canvas(10,4.6)
    ax.text(50,92,"ARP poisoning — the LAN trusts address answers blindly",ha="center",color=NAVY,fontsize=12,fontweight="bold")
    rbox(ax,40,66,20,12,"SWITCH\n(local network)",fc=NAVY,fs=8.6)
    rbox(ax,8,42,18,12,"your PC",fc=TEAL,fs=8.6)
    rbox(ax,74,42,18,12,"gateway\n(router)",fc=BLUE,fs=8.6)
    rbox(ax,40,34,20,12,"ATTACKER\n'I am the gateway'",fc=CORAL,fs=8.0)
    arrow(ax,26,48,40,54,color=GREY); arrow(ax,74,48,60,54,color=GREY)
    arrow(ax,26,46,40,42,color=CORAL,lw=2.0)
    ax.text(30,38,"traffic diverted",ha="center",color=CORAL,fontsize=7.6,style="italic")
    ax.add_patch(FancyBboxPatch((8,15),84,12,boxstyle="round,pad=0.3,rounding_size=2",fc=PALET,ec=TEAL,lw=1.6,zorder=3))
    ax.text(50,21,"Defence: segmentation · dynamic ARP inspection · encrypted traffic (HTTPS/VPN) · monitoring",ha="center",color=TEAL,fontsize=8.6,fontweight="bold",zorder=4)
    caption(ax,"Even if the LAN is poisoned, HTTPS/VPN keeps the diverted traffic unreadable — encryption is the user's safety net.",y=5,fs=9.0)
    save(fig,"s26_arp.png")

def s27_hats():
    fig,ax=canvas(10,4.4)
    ax.text(50,90,"The hat is about AUTHORIZATION + INTENT, not skill",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    segs=[("WHITE HAT\nauthorized,\nethical (pen-tester)",TEAL,5),
          ("GREY HAT\nunauthorized but\nnot (always) malicious",AMBER,37),
          ("BLACK HAT\nmalicious &\nillegal",CORAL,69)]
    for t,c,x in segs:
        rbox(ax,x,44,26,22,t,fc=c,fs=8.6)
    arrow(ax,5,38,97,38,color=GREY,lw=2.0)
    ax.text(18,31,"legal · invited",ha="center",color=TEAL,fontsize=8.4,style="italic")
    ax.text(50,31,"still illegal",ha="center",color=AMBER,fontsize=8.4,style="italic")
    ax.text(82,31,"criminal",ha="center",color=CORAL,fontsize=8.4,style="italic")
    caption(ax,"Same skill, different intent: a bug-bounty researcher (white) and a ransomware operator (black) can use the same knowledge.",y=8,fs=9.3)
    save(fig,"s27_hats.png")

for fn in [s22_ciatriad,s22_domains,s23_attacksurface,s23_supplychain,s24_tva,s24_riskmatrix,
           s25_dos,s26_mitm,s26_dns,s26_arp,s27_hats]:
    fn()
print("\nAll IT246 Unit 5 diagrams written to",OUT)
