#!/usr/bin/env python3
"""Concept diagrams for IT246 (sixth) Unit 7 — Social Engineering and Cyber Terrorism
(S33–S37). Genuinely spatial concepts only (human-vs-firewall, cost/success quadrant,
credential chain-reaction, influence levers, the SE attack cycle, the attack-type
taxonomy, STOP-THINK-CLICK, intent-vs-severity map, cyber-terror types, infrastructure
cascade, the defence pyramid, the incident-response loop); all comparisons/examples are
native PPTX tables in the deck (§7A). DEFENSIVE / awareness framing only — no operational
attack steps. License-safe. Output -> sixth/images/   Run: python3 build_unit7_images.py
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

# ---------------------------------------------------------------- S33
def s33_human_firewall():
    fig,ax=canvas(10,5.0)
    ax.text(50,95,"Why humans break before machines do",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    # LEFT: the firewall the attacker never has to fight
    ax.text(26,86,"THE MACHINE",ha="center",color=BLUE,fontsize=10.5,fontweight="bold")
    # brick wall
    for r in range(5):
        for c in range(4):
            off=5 if r%2 else 0
            ax.add_patch(Rectangle((6+c*10+off,40+r*8),9,7,fc=BLUE,ec=WHITE,lw=1.2,zorder=3))
    ax.text(26,34,"Rs. 50,000 firewall + encryption\n(strong, expensive, patient)",ha="center",color=INK,fontsize=8.6)
    ax.text(26,26,"✗ never even gets a vote",ha="center",color=CORAL,fontsize=9,fontweight="bold")
    # RIGHT: the person who opens the gate
    ax.text(74,86,"THE PERSON",ha="center",color=CORAL,fontsize=10.5,fontweight="bold")
    ax.add_patch(Circle((74,72),5,fc=AMBER,ec=WHITE,lw=1.2,zorder=3))          # head
    ax.add_patch(FancyBboxPatch((69,52),10,15,boxstyle="round,pad=0.2,rounding_size=2",fc=AMBER,ec=WHITE,lw=1.2,zorder=3))  # body
    ax.text(74,44,'"Namaste, I\'m from your\nbank\'s head office…"',ha="center",color=INK,fontsize=8.4,style="italic")
    ax.text(74,34,"→ reads out the OTP",ha="center",color=CORAL,fontsize=9,fontweight="bold")
    ax.text(74,26,"✓ the gate opens willingly",ha="center",color=CORAL,fontsize=9,fontweight="bold")
    # attacker bypass arrow
    arrow(ax,50,74,66,72,color=CORAL,lw=2.4)
    ax.text(50,80,"attacker",ha="center",color=CORAL,fontsize=9,fontweight="bold")
    caption(ax,"Social engineering attacks the PERSON, not the PC. The strongest wall is useless if the gatekeeper opens the gate to the right uniform.",y=6,fs=9.4)
    save(fig,"s33_human_firewall.png")

def s33_cost_success():
    fig,ax=canvas(10,5.2)
    ax.text(50,96,"Why attackers choose it: cheap + high success",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    x0,y0,W,H=20,16,66,66
    ax.add_patch(Rectangle((x0,y0),W,H,fc=PALEB,ec=NAVY,lw=1.3,zorder=1))
    ax.plot([x0+W/2,x0+W/2],[y0,y0+H],color=GREY,lw=1.0,zorder=2)
    ax.plot([x0,x0+W],[y0+H/2,y0+H/2],color=GREY,lw=1.0,zorder=2)
    ax.text(x0+W/2,y0-6,"COST TO THE ATTACKER →",ha="center",color=NAVY,fontsize=9.5,fontweight="bold")
    ax.text(x0-6,y0+H/2,"SUCCESS RATE →",ha="center",color=NAVY,fontsize=9.5,fontweight="bold",rotation=90)
    ax.text(x0+3,y0+H-4,"low cost",ha="left",color=GREY,fontsize=8); ax.text(x0+W-3,y0+H-4,"high cost",ha="right",color=GREY,fontsize=8)
    rbox(ax,x0+3,y0+H-20,26,15,"SOCIAL\nENGINEERING\ncheap · high success",fc=CORAL,fs=8.8)
    rbox(ax,x0+W-30,y0+H-20,26,15,"zero-day exploit\ncostly · works",fc=BLUE,fs=8.4)
    rbox(ax,x0+3,y0+3,26,13,"random spam\ncheap · rarely works",fc=TEAL,fs=8.2)
    rbox(ax,x0+W-30,y0+3,26,13,"brute-force crypto\ncostly · rarely works",fc=GREY,fs=8.2)
    caption(ax,"Strong encryption/firewalls make direct attacks costly, so attackers pivot to the human — the path of least resistance.",y=5,fs=9.4)
    save(fig,"s33_cost_success.png")

# ---------------------------------------------------------------- S34
def s34_chain():
    fig,ax=canvas(10,4.6)
    ax.text(50,92,"One leaked OTP is never 'just one account'",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    links=[("1 OTP\nshared",CORAL),("EMAIL\ntaken over",AMBER),("BANK /\neSewa · Khalti",BLUE),
           ("SOCIAL\naccounts",TEAL),("CONTACTS\nscammed next",CORAL)]
    xs=[4,23,42,61,80]
    for (t,c),x in zip(links,xs):
        rbox(ax,x,44,17,22,t,fc=c,fs=8.8)
    for i in range(len(xs)-1):
        arrow(ax,xs[i]+17,55,xs[i+1],55,color=GREY,lw=2.0)
    ax.text(50,36,"chain reaction — the key unlocks a whole ring of linked accounts",ha="center",color=CORAL,fontsize=9.5,fontweight="bold")
    caption(ax,"Credentials are keys, not doors: impact cascades from one account to email, money, identity, and then your contacts.",y=12,fs=9.4)
    save(fig,"s34_chain.png")

def s34_levers():
    fig,ax=canvas(10,5.4)
    ax.text(50,96,"The psychology-of-influence levers (recognise, don't use)",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    levers=[("AUTHORITY",'"I\'m from the bank / police"',BLUE),
            ("LIKING / RAPPORT",'friendly chat before the ask',TEAL),
            ("SOCIAL PROOF",'"everyone has updated KYC"',AMBER),
            ("RECIPROCITY",'"I helped you — now help me"',BLUE),
            ("URGENCY",'"account blocks in 10 min"',CORAL),
            ("FEAR",'"a police case is filed"',CORAL)]
    xs=[6,37,68]; ys=[50,14]
    for i,(name,ex,c) in enumerate(levers):
        x=xs[i%3]; y=ys[i//3]
        rbox(ax,x,y+18,26,10,name,fc=c,fs=10)
        ax.add_patch(FancyBboxPatch((x,y),26,17,boxstyle="round,pad=0.2,rounding_size=2",fc=WHITE,ec=c,lw=1.4,zorder=3))
        ax.text(x+13,y+8.5,ex,ha="center",va="center",color=INK,fontsize=8.2,style="italic",zorder=4)
    caption(ax,"Spot the EMOTION a message is trying to trigger (trust, greed, fear, urgency) — naming the lever is the fastest way to catch a scam.",y=4,fs=9.3)
    save(fig,"s34_levers.png")

def s34_cycle():
    fig,ax=canvas(10,5.2)
    ax.text(50,95,"The social-engineering attack cycle",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    steps=[("1  RESEARCH\nname, bank, leaked list",BLUE),
           ("2  BUILD TRUST\nrapport + authority",TEAL),
           ("3  EXPLOIT\nurgency/fear → the ask",CORAL),
           ("4  EXIT\ntake value, vanish",AMBER)]
    cx,cy,r=50,46,25; pts=[]
    for i,(t,c) in enumerate(steps):
        ang=math.pi/2 - i*2*math.pi/len(steps)
        x=cx+r*math.cos(ang); y=cy+r*math.sin(ang); pts.append((x,y))
        rbox(ax,x-14,y-8,28,16,t,fc=c,fs=8.6)
    for i in range(len(pts)):
        x1,y1=pts[i]; x2,y2=pts[(i+1)%len(pts)]
        arrow(ax,x1+(x2-x1)*0.32,y1+(y2-y1)*0.32,x1+(x2-x1)*0.68,y1+(y2-y1)*0.68,color=GREY,lw=1.8)
    caption(ax,"The friendly chatter is misdirection (like a magician's patter); the 'trick' is the request that follows once trust is built.",y=4,fs=9.3)
    save(fig,"s34_cycle.png")

# ---------------------------------------------------------------- S35
def s35_taxonomy():
    fig,ax=canvas(10,5.2)
    ax.text(50,95,"Six attack types — one goal: make YOU the door",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    rbox(ax,36,80,28,11,"SOCIAL ENGINEERING",fc=NAVY,fs=10)
    rbox(ax,14,63,30,9,"DIGITAL CHANNELS",fc=BLUE,fs=9)
    rbox(ax,58,63,30,9,"HUMAN / PHYSICAL",fc=TEAL,fs=9)
    arrow(ax,44,80,32,72,color=GREY,lw=1.6); arrow(ax,56,80,70,72,color=GREY,lw=1.6)
    dig=[("PHISHING\nfake email + link",BLUE),("SMISHING\nfake SMS (KYC/lottery)",BLUE),("VISHING\nfake bank/police call",BLUE)]
    hum=[("PRETEXTING\ninvented backstory",TEAL),("BAITING\n'free' USB/download",TEAL),("TAILGATING\nfollow through a door",TEAL)]
    for i,(t,c) in enumerate(dig):
        rbox(ax,4+i*15.5,42,14.5,15,t,fc=c,fs=7.6); arrow(ax,29,63,11+i*15.5,57,color=LGREY,lw=1.2)
    for i,(t,c) in enumerate(hum):
        rbox(ax,54+i*15.0,42,14,15,t,fc=c,fs=7.6); arrow(ax,73,63,61+i*15.0,57,color=LGREY,lw=1.2)
    caption(ax,"Phishing is NOT only email: it spans SMS (smishing), calls (vishing), QR codes, and social media. Same con, different channel.",y=22,fs=9.2)
    save(fig,"s35_taxonomy.png")

def s35_stop_think_click():
    fig,ax=canvas(10,4.6)
    ax.text(50,92,"STOP · THINK · then CLICK — the pause is the protection",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    rbox(ax,4,52,24,20,"STOP\ndon't react to\nthe pressure",fc=CORAL,fs=9)
    rbox(ax,38,52,24,20,"THINK\nverify via the\nofficial number\nYOURSELF",fc=AMBER,fs=8.8)
    rbox(ax,72,52,24,20,"CLICK\nonly once you\nhave verified",fc=TEAL,fs=9)
    arrow(ax,28,62,38,62,color=GREY,lw=2.0); arrow(ax,62,62,72,62,color=GREY,lw=2.0)
    ax.text(50,40,"Never share OTP/PIN · hover/check links · slow down when rushed · report it",ha="center",color=NAVY,fontsize=9.4,fontweight="bold")
    caption(ax,"Like looking both ways before crossing a road: urgency is the attacker's weapon, so the deliberate pause is your best defence.",y=16,fs=9.3)
    save(fig,"s35_stop_think_click.png")

# ---------------------------------------------------------------- S36
def s36_intent_target():
    fig,ax=canvas(10,5.4)
    ax.text(50,96,"Where's the line? Motive × severity",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    x0,y0,W,H=20,16,66,66
    ax.add_patch(Rectangle((x0,y0),W,H,fc=PALEB,ec=NAVY,lw=1.3,zorder=1))
    ax.plot([x0+W/2,x0+W/2],[y0,y0+H],color=GREY,lw=1.0,zorder=2)
    ax.plot([x0,x0+W],[y0+H/2,y0+H/2],color=GREY,lw=1.0,zorder=2)
    ax.text(x0+W/2,y0-6,"MOTIVE:  profit  →  political / ideological",ha="center",color=NAVY,fontsize=9.3,fontweight="bold")
    ax.text(x0-6,y0+H/2,"SEVERITY / HARM →",ha="center",color=NAVY,fontsize=9.3,fontweight="bold",rotation=90)
    rbox(ax,x0+3,y0+3,27,14,"CYBERCRIME\nransomware for money",fc=BLUE,fs=8.2)
    rbox(ax,x0+3,y0+H-18,27,14,"CYBER WARFARE\nstate vs state",fc=AMBER,fs=8.4)
    rbox(ax,x0+W-30,y0+3,27,14,"HACKTIVISM\nprotest / a message",fc=TEAL,fs=8.2)
    rbox(ax,x0+W-30,y0+H-18,27,14,"CYBER TERRORISM\nideology + terror/harm",fc=CORAL,fs=8.2)
    caption(ax,"Most hacking is crime or vandalism. Terrorism needs political/ideological intent PLUS intent to terrorise or seriously harm.",y=5,fs=9.2)
    save(fig,"s36_intent_target.png")

def s36_types():
    fig,ax=canvas(10,4.8)
    ax.text(50,92,"Types of cyber terrorism (for awareness)",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    types=[("CRITICAL\nINFRASTRUCTURE\npower·water·telecom·finance",CORAL),
           ("DATA DESTRUCTION\n/ manipulation\nof public records",AMBER),
           ("SERVICE DENIAL\nlarge-scale DoS\non essential services",BLUE),
           ("PROPAGANDA &\nPSY-OPS\nrecruitment · disinformation",TEAL),
           ("FINANCING\nvia cyber means",GREY)]
    xs=[3,22.5,42,61.5,81]
    for (t,c),x in zip(types,xs):
        rbox(ax,x,40,17,26,t,fc=c,fs=7.4)
    ax.text(50,30,'"arson with a keyboard" — the goal is fear and damage, not theft',ha="center",color=CORAL,fontsize=9.6,fontweight="bold",style="italic")
    caption(ax,"Categories used for awareness: they target the systems a society depends on, or the public mind, to spread fear and disruption.",y=12,fs=9.2)
    save(fig,"s36_types.png")

# ---------------------------------------------------------------- S37
def s37_cascade():
    fig,ax=canvas(10,4.6)
    ax.text(50,92,"Cascading (domino) effects on infrastructure",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    doms=[("POWER\ngrid down",NAVY),("TELECOM\nmobile/net down",BLUE),("BANKING\nATM·eSewa frozen",TEAL),
          ("HOSPITALS\n& WATER hit",AMBER),("PUBLIC PANIC\n+ economic loss",CORAL)]
    xs=[3,22,41,60,79]
    for (t,c),x in zip(doms,xs):
        rbox(ax,x,44,17,22,t,fc=c,fs=8.2)
    for i in range(len(xs)-1):
        arrow(ax,xs[i]+17,55,xs[i+1],55,color=GREY,lw=2.2)
    ax.text(50,36,"one failure topples the next — real damage lands in the streets, not just on a screen",ha="center",color=CORAL,fontsize=9.3,fontweight="bold")
    caption(ax,"Attacks on industrial/control systems cause physical, economic, and human harm — not merely 'online' damage.",y=12,fs=9.2)
    save(fig,"s37_cascade.png")

def s37_defense_pyramid():
    fig,ax=canvas(10,5.0)
    ax.text(50,95,"Countering cyber terrorism — a layered defence",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    layers=[("NATIONAL — CERT/NPCERT · CI protection · cyber law · intl cooperation",NAVY,16,4,92,7.8),
            ("ORGANIZATIONAL — segmentation · IDS · IR + BCP/DR · backups",BLUE,34,16,68,7.6),
            ("PERSONAL — awareness · report · don't amplify",TEAL,52,30,40,7.4)]
    for text,c,y,x,w,fs in layers:
        ax.add_patch(Rectangle((x,y),w,16,fc=c,ec=WHITE,lw=1.6,zorder=3))
        ax.text(x+w/2,y+8,text,ha="center",va="center",color=WHITE,fontsize=fs,fontweight="bold",zorder=4)
    caption(ax,"No single layer is enough: the national base, the organizational middle, and the personal tip must all hold.",y=6,fs=9.3)
    save(fig,"s37_defense_pyramid.png")

def s37_ir_flow():
    fig,ax=canvas(10,5.0)
    ax.text(50,95,"Resilience: the incident-response cycle (assume it WILL happen)",ha="center",color=NAVY,fontsize=12,fontweight="bold")
    steps=[("PREPARE\nbackups · plan · drills",TEAL),("DETECT\nmonitoring/IDS",BLUE),("CONTAIN\nisolate · failover",AMBER),
           ("ERADICATE\nremove the threat",CORAL),("RECOVER\nrestore service",BLUE),("REVIEW\nlearn · coordinate CERT",TEAL)]
    cx,cy,r=50,45,27; pts=[]
    for i,(t,c) in enumerate(steps):
        ang=math.pi/2 - i*2*math.pi/len(steps)
        x=cx+r*math.cos(ang); y=cy+r*math.sin(ang); pts.append((x,y))
        rbox(ax,x-12,y-7,24,14,t,fc=c,fs=7.8)
    for i in range(len(pts)):
        x1,y1=pts[i]; x2,y2=pts[(i+1)%len(pts)]
        arrow(ax,x1+(x2-x1)*0.34,y1+(y2-y1)*0.34,x1+(x2-x1)*0.66,y1+(y2-y1)*0.66,color=GREY,lw=1.7)
    caption(ax,"Like earthquake preparedness: you can't stop every attack, but drills, backups, and a recovery plan decide scare vs catastrophe.",y=4,fs=9.1)
    save(fig,"s37_ir_flow.png")

for fn in [s33_human_firewall,s33_cost_success,s34_chain,s34_levers,s34_cycle,
           s35_taxonomy,s35_stop_think_click,s36_intent_target,s36_types,
           s37_cascade,s37_defense_pyramid,s37_ir_flow]:
    fn()
print("\nAll IT246 Unit 7 diagrams written to",OUT)
