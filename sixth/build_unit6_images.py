#!/usr/bin/env python3
"""Concept diagrams for IT246 (sixth) Unit 6 — Personal Cybersecurity (S28–S32).
Genuinely spatial concepts only (posture layers, 3-2-1 backup, IoT home map, OTP-scam
anatomy, theft attack-chain, delete-vs-wipe recoverability, home-network split, password
strength ladder, MFA factor pyramid, credential-stuffing domino). All comparisons/examples
are native PPTX tables in the deck (§7A). License-safe, no external assets.
Output -> sixth/images/   Run: python3 build_unit6_images.py
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

# ---------------------------------------------------------------- S28
def s28_posture():
    fig,ax=canvas(10,5.2)
    ax.text(50,95,"Security posture = four layers of defence",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    layers=[("① PATCH  — close known holes (auto-update OS, browser, apps)",TEAL,70),
            ("② PROTECT — one good antivirus + a firewall on",BLUE,54),
            ("③ BACK UP — 3-2-1 recoverable copies of your data",AMBER,38),
            ("④ CONTAIN — limit the damage if one layer fails",CORAL,22)]
    for text,c,y in layers:
        ax.add_patch(FancyBboxPatch((10,y),80,12,boxstyle="round,pad=0.2,rounding_size=2",fc=c,ec=WHITE,lw=1.6,zorder=3))
        ax.text(50,y+6,text,ha="center",va="center",color=WHITE,fontsize=9.6,fontweight="bold",zorder=4)
    for y in [70,54,38]:
        arrow(ax,50,y,50,y-4,color=GREY,lw=1.8)
    caption(ax,"Posture = patch + protect + back up + contain. No single wall is enough — most attacks are automated and hit whoever skipped a layer.",y=8,fs=9.6)
    save(fig,"s28_posture.png")

def s28_backup321():
    fig,ax=canvas(10,5.0)
    ax.text(50,95,"The 3-2-1 backup rule",ha="center",color=NAVY,fontsize=13.5,fontweight="bold")
    cols=[("3","COPIES","of every\nimportant file",TEAL,18),
          ("2","MEDIA TYPES","e.g. laptop disk\n+ external drive",BLUE,50),
          ("1","OFFSITE","cloud / a drive\nat another place",CORAL,82)]
    for num,head,sub,c,x in cols:
        ax.add_patch(Circle((x,64),9,fc=c,ec=WHITE,lw=2,zorder=3))
        ax.text(x,64,num,ha="center",va="center",color=WHITE,fontsize=22,fontweight="bold",zorder=4)
        ax.text(x,49,head,ha="center",color=c,fontsize=11,fontweight="bold")
        ax.text(x,40,sub,ha="center",va="top",color=INK,fontsize=9)
    ax.text(50,22,"Defeats ransomware · theft · disk failure · load-shedding surge",ha="center",color=NAVY,fontsize=10,fontweight="bold")
    caption(ax,"A backup is a spare key with a trusted neighbour — useless until the day you're locked out, then it is everything.",y=8,fs=9.6)
    save(fig,"s28_backup321.png")

# ---------------------------------------------------------------- S29
def s29_iot_home():
    fig,ax=canvas(10,5.2)
    ax.text(50,95,"An IoT home — every device is a door",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    ax.add_patch(FancyBboxPatch((30,44),40,22,boxstyle="round,pad=0.3,rounding_size=2",fc=NAVY,ec=WHITE,lw=1.6,zorder=3))
    ax.text(50,55,"ROUTER\n(WorldLink / Vianet)",ha="center",va="center",color=WHITE,fontsize=9.4,fontweight="bold",zorder=4)
    devs=[("CCTV / IP camera",CORAL,10,80,"default admin/admin"),
          ("Smart TV",BLUE,74,80,"rarely updated"),
          ("Smart bulb / plug",AMBER,10,20,"no updates, always on"),
          ("Phone / laptop",TEAL,74,20,"the one you DO lock")]
    for t,c,x,y,warn in devs:
        rbox(ax,x,y-6,22,12,t,fc=c,fs=8.8)
        ax.text(x+11,y-9,warn,ha="center",va="top",color=CORAL if c!=TEAL else TEAL,fontsize=7.6,style="italic")
        arrow(ax,x+11,y-6 if y>50 else y+6,50 if x<40 else 50,55,color=GREY,lw=1.4)
    caption(ax,"Default-password IoT = a house where the builder's master key still opens the door. Mirai enslaved millions this way.",y=5,fs=9.6)
    save(fig,"s29_iot_home.png")

def s29_otp_scam():
    fig,ax=canvas(10,5.2)
    ax.text(50,96,"Anatomy of an OTP / eSewa scam call",ha="center",color=NAVY,fontsize=12.8,fontweight="bold")
    steps=[('1  "I\'m from eSewa / your bank"  → fake authority',BLUE,80),
           ('2  "A wrong transfer hit your account"  → panic story',AMBER,64),
           ('3  "Read me the OTP to REVERSE it"  → the trap',CORAL,48),
           ('4  You share the 6-digit OTP  → the last key',"#7a2317",32),
           ('5  Money gone — the OTP authorised THEIR transfer',NAVY,16)]
    for text,c,y in steps:
        ax.add_patch(FancyBboxPatch((12,y),76,11,boxstyle="round,pad=0.2,rounding_size=2",fc=c,ec=WHITE,lw=1.4,zorder=3))
        ax.text(50,y+5.5,text,ha="center",va="center",color=WHITE,fontsize=9.3,fontweight="bold",zorder=4)
    for y in [80,64,48,32]:
        arrow(ax,50,y,50,y-5,color=GREY,lw=1.8)
    caption(ax,"RED FLAGS: unsolicited call · urgency · asks for OTP/MPIN. eSewa/Khalti/banks NEVER ask for your OTP. Refuse and hang up.",y=4,fs=9.4)
    save(fig,"s29_otp_scam.png")

# ---------------------------------------------------------------- S30
def s30_theft_chain():
    fig,ax=canvas(10,4.6)
    ax.text(50,92,"A stolen UNLOCKED phone → account takeover",ha="center",color=NAVY,fontsize=12.6,fontweight="bold")
    steps=[("Phone\nsnatched",GREY,10),("Still logged into\neSewa / Gmail / FB",CORAL,32),
           ("OTP SMS visible\non lock screen",AMBER,55),("Reset passwords,\ndrain wallet",NAVY,79)]
    for t,c,x in steps:
        rbox(ax,x,44,19,22,t,fc=c,fs=8.8)
    for x in [29,52,75]:
        arrow(ax,x,55,x+4,55,color=GREY,lw=2.0)
    ax.text(50,34,"The data, not the hardware, is the real loss",ha="center",color=CORAL,fontsize=10.5,fontweight="bold")
    caption(ax,"Break the chain: full-disk encryption + strong lock + remote wipe + hide OTP previews. Then a thief gets a brick, not your life.",y=10,fs=9.4)
    save(fig,"s30_theft_chain.png")

def s30_delete_wipe():
    fig,ax=canvas(10,4.8)
    ax.text(50,94,"Delete vs format vs wipe vs encrypt — how recoverable?",ha="center",color=NAVY,fontsize=12.4,fontweight="bold")
    bars=[("Delete / recycle bin",92,CORAL,"fully recoverable"),
          ("Quick format",70,AMBER,"mostly recoverable"),
          ("Factory reset (unencrypted)",45,AMBER,"often recoverable"),
          ("Encrypt-then-wipe",8,TEAL,"unrecoverable ✓")]
    y=72
    for label,length,c,verdict in bars:
        ax.text(3,y+3.2,label,ha="left",va="center",color=INK,fontsize=9.2,fontweight="bold")
        ax.add_patch(Rectangle((32,y),length*0.55,7,fc=c,ec=WHITE,lw=1.2,zorder=3))
        ax.text(32+length*0.55+2,y+3.5,verdict,ha="left",va="center",color=c,fontsize=8.6,style="italic")
        y-=18
    ax.text(50,6,"← less data left recoverable   ·   more data left recoverable →",ha="center",color=GREY,fontsize=9)
    save(fig,"s30_delete_wipe.png")

# ---------------------------------------------------------------- S31
def s31_network():
    fig,ax=canvas(10,5.0)
    ax.text(50,95,"Home network — split MAIN from GUEST/IoT",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    rbox(ax,40,58,20,14,"ROUTER\nWPA2/3 · firmware\nupdated · admin pw changed",fc=NAVY,fs=8.2)
    # main network
    ax.add_patch(FancyBboxPatch((6,20),40,30,boxstyle="round,pad=0.3,rounding_size=2",fc=PALET,ec=TEAL,lw=1.8,zorder=1))
    ax.text(26,45,"MAIN NETWORK",ha="center",color=TEAL,fontsize=10.5,fontweight="bold")
    for t,x in [("Work laptop",12),("Your phone",30)]:
        rbox(ax,x,26,15,9,t,fc=TEAL,fs=8)
    # guest network
    ax.add_patch(FancyBboxPatch((54,20),40,30,boxstyle="round,pad=0.3,rounding_size=2",fc=PALEA,ec=AMBER,lw=1.8,zorder=1))
    ax.text(74,45,"GUEST / IoT NETWORK",ha="center",color=AMBER,fontsize=10.5,fontweight="bold")
    for t,x in [("Visitors",58),("CCTV / TV / bulb",74)]:
        rbox(ax,x,26,15,9,t,fc=AMBER,fs=7.6)
    arrow(ax,45,58,30,50,color=TEAL,lw=1.8); arrow(ax,55,58,70,50,color=AMBER,lw=1.8)
    caption(ax,"The router is the front gate. A guest/IoT network keeps a hacked camera or a visitor's laptop off your work devices.",y=8,fs=9.4)
    save(fig,"s31_network.png")

# ---------------------------------------------------------------- S32
def s32_strength():
    fig,ax=canvas(10,4.8)
    ax.text(50,94,"Password strength — length beats complexity",ha="center",color=NAVY,fontsize=12.8,fontweight="bold")
    rows=[('"nepal123" / phone number',10,CORAL,"cracked instantly"),
          ('"P@ss123"  (short + symbols)',26,CORAL,"still weak — seconds"),
          ('"Kathmandu@2026"',52,AMBER,"better, but guessable"),
          ('"hariyo!gai-khana-25"  (passphrase)',94,TEAL,"strong — long + unique")]
    y=68
    for label,length,c,verdict in rows:
        ax.text(3,y+3.4,label,ha="left",va="center",color=INK,fontsize=9,fontweight="bold")
        ax.add_patch(Rectangle((40,y),length*0.5,7,fc=c,ec=WHITE,lw=1.2,zorder=3))
        ax.text(40+length*0.5+2,y+3.5,verdict,ha="left",va="center",color=c,fontsize=8.4,style="italic")
        y-=17
    caption(ax,"A long, unique passphrase beats a short symbolic one. Never reuse it — one leak then topples every account.",y=6,fs=9.4)
    save(fig,"s32_strength.png")

def s32_mfa():
    fig,ax=canvas(10,5.0)
    ax.text(50,95,"MFA factor pyramid — weakest to strongest",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    layers=[("PASSWORD ALONE — one factor, weakest",GREY,18,8,84),
            ("SMS OTP — better, but SIM-swap risk",AMBER,34,20,60),
            ("AUTHENTICATOR APP (TOTP) — strong",BLUE,50,32,36),
            ("HARDWARE KEY — strongest",TEAL,66,42,16)]
    for text,c,y,x,w in layers:
        ax.add_patch(Rectangle((x,y),w,14,fc=c,ec=WHITE,lw=1.5,zorder=3))
        ax.text(50,y+7,text,ha="center",va="center",color=WHITE,fontsize=8.8,fontweight="bold",zorder=4)
    caption(ax,"Turn on MFA for EMAIL first (it resets everything else), then banking + social. Authenticator app beats SMS; MFA blocks most takeovers even if your password leaks.",y=5,fs=9.0)
    save(fig,"s32_mfa.png")

def s32_domino():
    fig,ax=canvas(10,4.4)
    ax.text(50,92,"Credential stuffing — one leak topples many",ha="center",color=NAVY,fontsize=12.8,fontweight="bold")
    # the breached, already-fallen tile
    ax.add_patch(Polygon([(8,34),(26,34),(20,58),(2,58)],closed=True,fc=CORAL,ec=WHITE,lw=1.3,zorder=3))
    ax.text(14,72,"1 reused password\nleaks HERE",ha="center",color=CORAL,fontsize=9.2,fontweight="bold")
    arrow(ax,24,45,32,45,color=GREY,lw=2.2)
    # the accounts that fall with it
    sites=[("Facebook",42),("Gmail",58),("eSewa",74),("College\nportal",90)]
    for t,cx in sites:
        ax.add_patch(Rectangle((cx-7,34),14,24,fc=BLUE,ec=WHITE,lw=1.3,zorder=3))
        ax.text(cx,46,t,ha="center",va="center",color=WHITE,fontsize=8.6,fontweight="bold",zorder=4)
    ax.text(66,26,"attacker replays the same password across all of them",ha="center",color=NAVY,fontsize=9.2,fontweight="bold")
    caption(ax,"Reuse one password = one key for house, car, office, and locker. A manager gives every lock its own key so one leak stays contained.",y=8,fs=9.2)
    save(fig,"s32_domino.png")

for fn in [s28_posture,s28_backup321,s29_iot_home,s29_otp_scam,s30_theft_chain,
           s30_delete_wipe,s31_network,s32_strength,s32_mfa,s32_domino]:
    fn()
print("\nAll IT246 Unit 6 diagrams written to",OUT)
