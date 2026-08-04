#!/usr/bin/env python3
"""Concept diagrams for IT246 (sixth) Unit 8 — Digital Forensics (S38–S44).
Genuinely spatial concepts only (evolution timeline, the six-stage forensic process with a
chain-of-custody band, digital-evidence map, custody handoff chain, order of volatility,
write-blocker + hash match, bit-for-bit imaging, file carving, extraction-level pyramid,
Nepal cyber-forensics ecosystem + admissibility checklist). All comparisons/examples are
native PPTX tables in the deck (§7A). License-safe, on-image labels (survive PDF).
Output -> sixth/images/   Run: python3 build_unit8_images.py
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

def s38_timeline():
    fig,ax=canvas(10,4.8)
    ax.text(50,94,"From 'computer forensics' to 'digital forensics'",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    eras=[("1980s–90s\nCOMPUTER FORENSICS\nsingle PC, hard disks",TEAL,10),
          ("2000s\nnetworks, email,\nservers",BLUE,35),
          ("2010s\nMOBILE-DOMINANT\nphones, apps, cloud",AMBER,60),
          ("Today\nIoT, vehicles,\nmulti-device",CORAL,85)]
    for t,c,x in eras:
        rbox(ax,x-11,46,22,26,t,fc=c,fs=8.6)
        ax.add_patch(Circle((x,38),1.6,fc=c,ec=WHITE,lw=1.2,zorder=4))
    arrow(ax,6,38,96,38,color=GREY,lw=2.2)
    caption(ax,"The field broadened from one desktop hard disk to phones, cloud, IoT and networks. In Nepal most cases now hinge on mobiles & apps.",y=20,fs=9.6)
    save(fig,"s38_timeline.png")

def s39_process():
    fig,ax=canvas(10,5.2)
    ax.text(50,95,"The six-stage forensic process — scene to courtroom",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    stages=[("1\nIDENTIFY",TEAL),("2\nPRESERVE",BLUE),("3\nCOLLECT",AMBER),
            ("4\nEXAMINE",CORAL),("5\nANALYSE","#6C3A9E"),("6\nREPORT",NAVY)]
    x0=3.5; w=13.5; gap=2.3; y=52; h=20
    xs=[]
    for i,(t,c) in enumerate(stages):
        x=x0+i*(w+gap); xs.append(x)
        rbox(ax,x,y,w,h,t,fc=c,fs=9.5)
        if i<5: arrow(ax,x+w,y+h/2,x+w+gap,y+h/2,color=GREY,lw=1.8)
    # chain of custody band under all stages
    bx0=x0-0.5; bx1=xs[-1]+w+0.5
    ax.add_patch(FancyBboxPatch((bx0,30),bx1-bx0,12,boxstyle="round,pad=0.2,rounding_size=2",fc=PALEA,ec=AMBER,lw=1.6,zorder=2))
    ax.text((bx0+bx1)/2,36,"CHAIN OF CUSTODY & EVIDENCE INTEGRITY — documented, hashed, unbroken at EVERY stage",
            ha="center",va="center",color="#7a4a08",fontsize=9.4,fontweight="bold",zorder=3)
    caption(ax,"Preservation protects everything downstream; the report is written for a non-technical judge. A gap in custody can sink the whole case.",y=18,fs=9.5)
    save(fig,"s39_process.png")

def s40_evidence():
    fig,ax=canvas(10,5.2)
    ax.text(50,96,"What counts as digital evidence — the sources",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    cx,cy,r=50,48,30
    ax.add_patch(Circle((cx,cy),13,fc=NAVY,ec=WHITE,lw=2,zorder=5))
    ax.text(cx,cy,"DIGITAL\nEVIDENCE",ha="center",va="center",color=WHITE,fontsize=10.5,fontweight="bold",zorder=6)
    nodes=[("Files &\ndocuments",TEAL),("Metadata\n(hidden data)",BLUE),("Logs\n(system/router)",AMBER),
           ("Chats &\nemail",CORAL),("Images &\nvideo",TEAL),("Location /\nGPS",BLUE),
           ("Deleted /\nresidual data",AMBER),("Call records\n(CDRs)",CORAL)]
    n=len(nodes)
    for i,(t,c) in enumerate(nodes):
        ang=math.pi/2 - i*2*math.pi/n
        x=cx+r*math.cos(ang); y=cy+r*math.sin(ang)
        arrow(ax,cx+13*math.cos(ang),cy+13*math.sin(ang),x-8.5*math.cos(ang),y-6*math.sin(ang),color=LGREY,lw=1.5)
        rbox(ax,x-9,y-5,18,10,t,fc=c,fs=8.2)
    caption(ax,"Good evidence is admissible, authentic, complete, reliable & believable. A bare screenshot is weak — it is easily faked and lacks metadata.",y=3,fs=9.4)
    save(fig,"s40_evidence.png")

def s41_custody():
    fig,ax=canvas(10,4.8)
    ax.text(50,94,"Chain of custody — an unbroken, logged handoff",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    steps=[("SEIZURE\ntag, seal, photo",TEAL),("TRANSPORT\nsealed bag",BLUE),("LAB INTAKE\nlog + hash",AMBER),
           ("ANALYST\nwork on copy",CORAL),("STORAGE\nlocked locker","#6C3A9E"),("COURT\nexpert testimony",NAVY)]
    x0=3; w=14; gap=1.4; y=50; h=22
    for i,(t,c) in enumerate(steps):
        x=x0+i*(w+gap)
        rbox(ax,x,y,w,h,t,fc=c,fs=8.3)
        if i<5: arrow(ax,x+w,y+h/2,x+w+gap,y+h/2,color=GREY,lw=1.7)
        ax.text(x+w/2,y-5,"who·when\nwhy·how",ha="center",va="center",color=GREY,fontsize=6.6)
    caption(ax,"Every transfer records who handled it, when, why and how. Like a relay baton — any dropped handoff (a gap) can disqualify the evidence.",y=18,fs=9.4)
    save(fig,"s41_custody.png")

def s41_volatility():
    fig,ax=canvas(10,5.0)
    ax.text(50,95,"Order of volatility — collect the most fragile first",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    layers=[("CPU registers & cache — gone in an instant",CORAL,74,"MOST volatile"),
            ("RAM — running processes, open network connections, keys",AMBER,60,""),
            ("Network state — live connections, ARP, routing",BLUE,46,""),
            ("Disk files & swap — survive a running system",TEAL,32,""),
            ("Logs, archived & backup media — most durable","#2F5E4A",18,"LEAST volatile")]
    for text,c,y,tag in layers:
        ax.add_patch(FancyBboxPatch((16,y),68,11,boxstyle="round,pad=0.2,rounding_size=2",fc=c,ec=WHITE,lw=1.4,zorder=3))
        ax.text(50,y+5.5,text,ha="center",va="center",color=WHITE,fontsize=8.8,fontweight="bold",zorder=4)
        if tag: ax.text(88,y+5.5,tag,ha="left",va="center",color=INK,fontsize=7.6,style="italic")
    arrow(ax,10,80,10,20,color=GREY,lw=2.0)
    ax.text(7,50,"COLLECT IN THIS ORDER",rotation=90,ha="center",va="center",color=NAVY,fontsize=8.6,fontweight="bold")
    caption(ax,"Powering down first destroys RAM evidence (running processes, encryption keys). Capture the volatile layers before the durable ones.",y=4,fs=9.4)
    save(fig,"s41_volatility.png")

def s41_hashing():
    fig,ax=canvas(10,4.8)
    ax.text(50,94,"Write blocker + hashing — proof the copy is untouched",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    rbox(ax,4,52,20,20,"ORIGINAL\nseized drive\n(sealed)",fc=NAVY,fs=8.6)
    rbox(ax,40,52,22,20,"WRITE BLOCKER\nread-only\n(no writes back)",fc=CORAL,fs=8.4)
    rbox(ax,78,52,18,20,"FORENSIC\nIMAGE (copy)",fc=TEAL,fs=8.6)
    arrow(ax,24,62,40,62,color=GREY,lw=2.0)
    arrow(ax,62,62,78,62,color=GREY,lw=2.0)
    ax.text(50,47,"one-way: read the original, never write to it",ha="center",color=CORAL,fontsize=8.2,style="italic")
    # hash compare
    rbox(ax,8,20,36,14,"hash(original)\nSHA-256: a1b2c3…f9",fc=BLUE,fs=8.4)
    rbox(ax,56,20,36,14,"hash(copy)\nSHA-256: a1b2c3…f9",fc=BLUE,fs=8.4)
    ax.text(50,27,"=",ha="center",va="center",color=TEAL,fontsize=22,fontweight="bold")
    ax.text(50,12,"MATCH  →  the image is an exact, unaltered duplicate of the original",
            ha="center",color=TEAL,fontsize=9.6,fontweight="bold")
    caption(ax,"Change even one byte and the hash changes visibly — like a tamper-evident seal on a medicine bottle.",y=3,fs=9.2)
    save(fig,"s41_hashing.png")

def s42_imaging():
    fig,ax=canvas(10,4.6)
    ax.text(50,93,"Disk imaging — a bit-for-bit copy, then analyse the copy",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    # original disk with regions
    ax.add_patch(Rectangle((6,40),34,30,fc=WHITE,ec=NAVY,lw=1.6,zorder=3))
    ax.text(23,73,"ORIGINAL DISK (sealed)",ha="center",color=NAVY,fontsize=8.8,fontweight="bold")
    for i,(lab,c) in enumerate([("visible files",PALEB),("'free' space",PALEA),("slack",PALEC),("unallocated",PALET)]):
        ax.add_patch(Rectangle((6,40+i*7.5),34,7.5,fc=c,ec=NAVY,lw=0.8,zorder=4))
        ax.text(23,43.7+i*7.5,lab,ha="center",va="center",color=INK,fontsize=7.8)
    rbox(ax,66,45,28,20,"FORENSIC IMAGE\nevery bit, incl.\nslack + unallocated",fc=TEAL,fs=8.4)
    arrow(ax,40,55,66,55,color=GREY,lw=2.2)
    ax.text(53,60,"bit-for-bit",ha="center",color=GREY,fontsize=8,style="italic")
    ax.text(53,50,"+ hash check",ha="center",color=BLUE,fontsize=7.8,style="italic")
    caption(ax,"Image the WHOLE disk (not just visible files) so 'deleted' data in slack/unallocated space is preserved — then work only on the hashed copy.",y=14,fs=9.4)
    ax.text(50,4,"'Deleted' = the pointer/label is removed, but the bytes stay until overwritten.",ha="center",color=CORAL,fontsize=9,fontweight="bold")
    save(fig,"s42_imaging.png")

def s42_carving():
    fig,ax=canvas(10,4.4)
    ax.text(50,92,"File carving — rebuild files by signature, no index needed",ha="center",color=NAVY,fontsize=12.3,fontweight="bold")
    ax.text(50,80,"Raw unallocated space (file-system index is gone):",ha="center",color=GREY,fontsize=9)
    cells=["…","FF D8","JPEG","data","data","FF D9","…","89 50","PNG","…"]
    x0=6; cw=8.8; y=58
    for i,txt in enumerate(cells):
        c=PALET if txt in("FF D8","FF D9") else (PALEB if txt=="JPEG" else WHITE)
        ax.add_patch(Rectangle((x0+i*cw,y),cw,16,fc=c,ec=NAVY,lw=1.0,zorder=3))
        ax.text(x0+i*cw+cw/2,y+8,txt,ha="center",va="center",color=INK,fontsize=8.2,
                fontweight="bold" if txt in("FF D8","FF D9") else "normal",zorder=4)
    ax.annotate("header (FF D8)",xy=(x0+1*cw+cw/2,y),xytext=(x0+1*cw,y-14),
                arrowprops=dict(arrowstyle="->",color=TEAL,lw=1.4),ha="center",color=TEAL,fontsize=8,fontweight="bold")
    ax.annotate("footer (FF D9)",xy=(x0+5*cw+cw/2,y),xytext=(x0+5*cw,y-14),
                arrowprops=dict(arrowstyle="->",color=CORAL,lw=1.4),ha="center",color=CORAL,fontsize=8,fontweight="bold")
    caption(ax,"A JPEG always starts FF D8 and ends FF D9. Carving scans raw bytes for these signatures to rebuild a file even without the file-system index.",y=14,fs=9.3)
    ax.text(50,4,"Like reassembling a shredded document by its edges — the labelled folder is gone, the pieces are not.",ha="center",color=GREY,fontsize=8.6,style="italic")
    save(fig,"s42_carving.png")

def s43_extraction():
    fig,ax=canvas(10,5.0)
    ax.text(50,95,"Mobile extraction levels — more data, but harder & more invasive",ha="center",color=NAVY,fontsize=12,fontweight="bold")
    layers=[("MANUAL — scroll & photograph the screen",TEAL,66,52,10,"least data"),
            ("LOGICAL — via APIs / backups",BLUE,50,45,24,""),
            ("FILE-SYSTEM — app databases, more files",AMBER,34,38,38,""),
            ("PHYSICAL — full bit-for-bit image",CORAL,18,31,52,"most data")]
    for text,c,y,x,w,tag in layers:
        ax.add_patch(Rectangle((x,y),w,14,fc=c,ec=WHITE,lw=1.5,zorder=3))
        ax.text(50,y+7,text,ha="center",va="center",color=WHITE,fontsize=8.6,fontweight="bold",zorder=4)
        if tag: ax.text(85,y+7,tag,ha="left",va="center",color=INK,fontsize=7.8,style="italic")
    arrow(ax,15,74,15,20,color=GREY,lw=2.0)
    ax.text(11,47,"MORE DATA / MORE INVASIVE",rotation=90,ha="center",va="center",color=NAVY,fontsize=8,fontweight="bold")
    caption(ax,"App data often lives in SQLite databases; call logs, location history & media metadata add more. Cloud backups may hold what the phone 'deleted'.",y=5,fs=9.3)
    save(fig,"s43_extraction.png")

def s44_ecosystem():
    fig,ax=canvas(10,5.0)
    ax.text(50,95,"Cyber forensics in Nepal — complaint to admissible evidence",ha="center",color=NAVY,fontsize=12.3,fontweight="bold")
    flow=[("CITIZEN\ncomplaint",TEAL,7),("NEPAL POLICE\nCYBER BUREAU",BLUE,30),
          ("FORENSIC LAB\nimage · hash ·\ncustody",AMBER,53),("COURT\nadmissible under\nETA 2063",CORAL,76)]
    for t,c,x in flow:
        rbox(ax,x,58,18,20,t,fc=c,fs=8.3)
    for x in [7,30,53]:
        arrow(ax,x+18,68,x+23,68,color=GREY,lw=1.9)
    # admissibility checklist
    ax.add_patch(FancyBboxPatch((14,14),72,32,boxstyle="round,pad=0.3,rounding_size=2",fc=PALEB,ec=BLUE,lw=1.6,zorder=2))
    ax.text(50,41,"ADMISSIBILITY CHECKLIST",ha="center",color=NAVY,fontsize=9.6,fontweight="bold",zorder=3)
    checks=["✓ Relevant","✓ Authentic","✓ Integrity (custody + hash)","✓ Legally obtained (warrant)"]
    for i,ch in enumerate(checks):
        ax.text(18+(i%2)*36,33-(i//2)*9,ch,ha="left",va="center",color=TEAL,fontsize=8.8,fontweight="bold",zorder=3)
    caption(ax,"Genuine evidence is still rejected if illegally obtained or mishandled. Challenges: few trained staff, limited lab capacity, rising caseload.",y=6,fs=9.1)
    save(fig,"s44_ecosystem.png")

for fn in [s38_timeline,s39_process,s40_evidence,s41_custody,s41_volatility,
           s41_hashing,s42_imaging,s42_carving,s43_extraction,s44_ecosystem]:
    fn()
print("\nAll IT246 Unit 8 diagrams written to",OUT)
