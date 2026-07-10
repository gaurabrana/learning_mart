#!/usr/bin/env python3
"""Concept diagrams for IT250 (eighth) Unit 3 — Digital Markets, Strategy & Innovation (S16-S25).
Genuinely spatial concepts only (digital-market ecosystem, co-opetition upstream/downstream, the
layered internet model, sustaining vs disruptive innovation trajectory, value chain/shop/network
configurations, strategic control points). All comparisons and concrete-example sets are native
PPTX tables in the deck (§7A). No emoji or exotic glyphs in matplotlib text (they render as tofu).
Output -> eighth/images/   Run: python3 build_unit3_images.py
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

def s16_digital_market():
    fig,ax=canvas(10,5.4)
    ax.text(50,95,"A digital market: buyers & sellers meet on a platform, on 5 components",
            ha="center",color=NAVY,fontsize=12,fontweight="bold")
    rbox(ax,6,64,20,16,"BUYERS\n(demand)",fc=BLUE,fs=9.2)
    rbox(ax,74,64,20,16,"SELLERS\n(supply)",fc=AMBER,fs=9.2)
    rbox(ax,38,63,24,18,"DIGITAL\nMARKET\n(platform)",fc=TEAL,fs=10)
    arrow(ax,26,74,38,74,color=BLUE,lw=2.2); arrow(ax,62,70,74,70,color=AMBER,lw=2.2)
    arrow(ax,74,66,62,66,color=GREY,lw=1.6); arrow(ax,38,68,26,68,color=GREY,lw=1.6)
    ax.text(50,58,"interactions matched, priced & settled online",ha="center",color=GREY,fontsize=8.6,style="italic")
    comps=[("PLATFORM",TEAL),("PAYMENTS",BLUE),("LOGISTICS",AMBER),("DATA &\nANALYTICS",CORAL),("SUPPORT",GREY)]
    x=4.5
    for t,c in comps:
        rbox(ax,x,24,17,14,t,fc=c,fs=8.4); x+=19
    ax.text(50,44,"THE 5 COMPONENTS (the foundation every digital market runs on)",
            ha="center",color=NAVY,fontsize=9,fontweight="bold")
    caption(ax,"A digital market is an online space where buyers & sellers interact; it needs a platform, payments, logistics, data and support to work.",y=13,fs=9.2)
    save(fig,"s16_digital_market.png")

def s19_coopetition():
    fig,ax=canvas(10,5.2)
    ax.text(50,95,"Co-opetition: cooperate upstream, compete downstream",
            ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    # upstream cooperation band
    ax.add_patch(FancyBboxPatch((8,70),84,14,boxstyle="round,pad=0.3,rounding_size=2",fc=PALET,ec=TEAL,lw=2,zorder=2))
    ax.text(50,77,"COOPERATE UPSTREAM  -  shared tech, infrastructure & standards\n(e.g. ConnectIPS / NCHL rails, QR interoperability, cloud, APIs)",
            ha="center",va="center",color=TEAL,fontsize=8.8,fontweight="bold",zorder=4)
    # two firms
    rbox(ax,14,44,26,16,"FIRM A\n(e.g. eSewa)",fc=BLUE,fs=9)
    rbox(ax,60,44,26,16,"FIRM B\n(e.g. Khalti)",fc=AMBER,fs=9)
    arrow(ax,40,52,60,52,color=GREY,lw=1.8); arrow(ax,60,48,40,48,color=GREY,lw=1.8)
    ax.text(50,55,"same rails",ha="center",color=GREY,fontsize=7.8,style="italic")
    # downstream competition band
    ax.add_patch(FancyBboxPatch((8,18),84,14,boxstyle="round,pad=0.3,rounding_size=2",fc=PALEC,ec=CORAL,lw=2,zorder=2))
    ax.text(50,25,"COMPETE DOWNSTREAM  -  customers, brand, price & experience\n(each still fights to win the same users)",
            ha="center",va="center",color=CORAL,fontsize=8.8,fontweight="bold",zorder=4)
    arrow(ax,27,44,40,34,color=CORAL,lw=1.8); arrow(ax,73,44,60,34,color=CORAL,lw=1.8)
    caption(ax,"Rivals share the pipes that grow the whole market, then compete for the customers on top - the Value-Net logic.",y=6,fs=9.2)
    save(fig,"s19_coopetition.png")

def s20_layers():
    fig,ax=canvas(10,5.4)
    ax.text(50,95,"The layered internet model (business view)",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    layers=[("USER  -  experiences the service","GREY","people, businesses, government",GREY,60,10),
            ("APPLICATION layer  -  the experience","AMBER","Foodmandu, Daraz app, Netflix, Facebook",AMBER,45,12),
            ("PLATFORM layer  -  the capability","BLUE","eSewa/Fonepay, Android/iOS, AWS services",BLUE,31,12),
            ("INFRASTRUCTURE layer  -  the technical base","TEAL","fibre, data centres, NTC/Ncell, cloud, devices",TEAL,17,12)]
    for title,_c,ex,c,y,h in layers:
        ax.add_patch(FancyBboxPatch((16,y),68,h-1.5,boxstyle="round,pad=0.2,rounding_size=1.5",fc=c,ec="none",zorder=3))
        ax.text(50,y+(h-1.5)*0.62,title,ha="center",va="center",color=WHITE,fontsize=9.2,fontweight="bold",zorder=4)
        ax.text(50,y+(h-1.5)*0.24,ex,ha="center",va="center",color=WHITE,fontsize=7.6,zorder=4)
    # value flows up (left), control flows down (right)
    ax.add_patch(FancyArrowPatch((10,18),(10,70),arrowstyle="-|>",mutation_scale=15,color=NAVY,lw=2.2))
    ax.text(6,44,"VALUE flows UP\n(technical -> capability\n-> experience)",ha="center",va="center",color=NAVY,fontsize=8,rotation=90,fontweight="bold")
    ax.add_patch(FancyArrowPatch((90,70),(90,18),arrowstyle="-|>",mutation_scale=15,color=CORAL,lw=2.2))
    ax.text(94,44,"CONTROL flows DOWN\n(own a lower layer =\npower over higher)",ha="center",va="center",color=CORAL,fontsize=8,rotation=90,fontweight="bold")
    caption(ax,"Each layer adds value on the one below; whoever controls a lower layer holds power over everyone above it.",y=6,fs=9.2)
    save(fig,"s20_layers.png")

def s21_innovation():
    fig,ax=canvas(10,5.2)
    ax.text(50,95,"Sustaining vs disruptive innovation",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    ax.add_patch(FancyArrowPatch((12,16),(12,86),arrowstyle="-|>",mutation_scale=13,color=GREY,lw=1.6))
    ax.add_patch(FancyArrowPatch((12,16),(94,16),arrowstyle="-|>",mutation_scale=13,color=GREY,lw=1.6))
    ax.text(7,52,"performance",ha="center",va="center",color=NAVY,fontsize=9,rotation=90,fontweight="bold")
    ax.text(53,9,"time ->",ha="center",color=NAVY,fontsize=9,fontweight="bold")
    xs=[12+i for i in range(0,80,2)]
    # incumbent sustaining line (starts high, climbs steeply, overshoots)
    inc=[38+0.62*(x-12) for x in xs]
    ax.plot(xs,inc,color=BLUE,lw=3,zorder=3)
    # customers-need band (moderate slope)
    need=[34+0.30*(x-12) for x in xs]
    ax.plot(xs,need,color=GREY,lw=1.6,ls="--",zorder=2)
    # disruptor: enters low, climbs, crosses the need line
    dis=[14+0.55*(x-12) for x in xs]
    ax.plot(xs,dis,color=CORAL,lw=3,zorder=3)
    ax.text(70,78,"incumbent\n(sustaining:\nbetter & pricier)",ha="left",color=BLUE,fontsize=8,fontweight="bold")
    ax.text(72,44,"what most\ncustomers need",ha="left",color=GREY,fontsize=7.6,style="italic")
    ax.text(58,30,"disruptor\n(cheaper, 'good enough',\nthen climbs up)",ha="left",color=CORAL,fontsize=8,fontweight="bold")
    ax.add_patch(Circle((63,42),1.8,fc=AMBER,ec=WHITE,lw=1.2,zorder=5))
    ax.text(46,50,"catches up ->\nlow end taken",ha="center",color=AMBER,fontsize=7.4,fontweight="bold")
    caption(ax,"Sustaining innovation improves the product for existing customers; disruptive innovation enters cheap at the bottom, then rises to overtake.",y=4,fs=9.0)
    save(fig,"s21_innovation.png")

def s23_value_creation():
    fig,ax=canvas(10,5.2)
    ax.text(50,95,"Three ways to create value: chain, shop, network",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    # VALUE CHAIN (linear)
    ax.text(17,84,"VALUE CHAIN",ha="center",color=BLUE,fontsize=9.5,fontweight="bold")
    ax.text(17,79,"transform inputs -> outputs",ha="center",color=GREY,fontsize=7.2,style="italic")
    for i,t in enumerate(["IN","MAKE","OUT"]):
        rbox(ax,7,64-i*13,20,9,t,fc=BLUE,fs=8.2)
        if i<2: arrow(ax,17,64-i*13,17,64-(i+1)*13+9,color=GREY,lw=1.6)
    ax.text(17,24,"factory, Daraz\nwarehouse, telecom\nhandset maker",ha="center",color=INK,fontsize=7.4)
    # VALUE SHOP (cyclical problem solving)
    ax.text(50,84,"VALUE SHOP",ha="center",color=TEAL,fontsize=9.5,fontweight="bold")
    ax.text(50,79,"diagnose -> solve a problem",ha="center",color=GREY,fontsize=7.2,style="italic")
    steps=["FIND\nPROBLEM","OPTIONS","SOLVE","CHECK"]
    cx,cy,r=47,52,13
    pts=[]
    for i,t in enumerate(steps):
        ang=math.pi/2 - i*2*math.pi/4
        x=cx+r*math.cos(ang); y=cy+r*math.sin(ang); pts.append((x,y))
        rbox(ax,x-8,y-5,16,10,t,fc=TEAL,fs=7.2)
    for i in range(4):
        x1,y1=pts[i]; x2,y2=pts[(i+1)%4]
        arrow(ax,x1+(x2-x1)*0.34,y1+(y2-y1)*0.34,x1+(x2-x1)*0.66,y1+(y2-y1)*0.66,color=GREY,lw=1.5)
    ax.text(50,24,"hospital, law/audit\nfirm, IT consultancy,\nrepair service",ha="center",color=INK,fontsize=7.4)
    # VALUE NETWORK (mediating hub)
    ax.text(83,84,"VALUE NETWORK",ha="center",color=AMBER,fontsize=9.5,fontweight="bold")
    ax.text(83,79,"connect members to each other",ha="center",color=GREY,fontsize=7.2,style="italic")
    hub=(85,55)
    rbox(ax,hub[0]-8,hub[1]-5,16,10,"HUB",fc=AMBER,fs=8)
    for ang in [42,90,142,318,270]:
        x=hub[0]+14*math.cos(math.radians(ang)); y=hub[1]+13*math.sin(math.radians(ang))
        ax.add_patch(Circle((x,y),3.0,fc=WHITE,ec=AMBER,lw=1.6,zorder=3))
        ax.add_patch(FancyArrowPatch((hub[0],hub[1]),(x,y),arrowstyle="-",color=GREY,lw=1.3,zorder=1))
    ax.text(83,24,"bank, telecom,\neSewa/Fonepay,\nPathao, marketplace",ha="center",color=INK,fontsize=7.4)
    caption(ax,"Chain makes things, shop solves problems, network connects people - most digital platforms are value networks.",y=6,fs=9.0)
    save(fig,"s23_value_creation.png")

def s25_control_points():
    fig,ax=canvas(10,5.2)
    ax.text(50,95,"Strategic control points: the chokepoints that confer power",
            ha="center",color=NAVY,fontsize=12.3,fontweight="bold")
    rbox(ax,37,45,26,16,"CONTROL\nPOINT\n(others must\npass through)",fc=NAVY,fs=8.6)
    pts=[("DATA","who owns the\nuser data","Google, Meta",BLUE,12,72),
         ("ALGORITHMS","who runs the\nmatching/ranking","TikTok, Uber",TEAL,64,72),
         ("STANDARDS","the format others\nmust adopt","Visa, Fonepay",AMBER,12,20),
         ("USER RELATIONSHIP","who owns the\ncustomer","Apple, Amazon",CORAL,64,20)]
    for t,d,ex,c,x,y in pts:
        ax.add_patch(FancyBboxPatch((x,y),24,15,boxstyle="round,pad=0.2,rounding_size=1.5",fc=c,ec="none",zorder=3))
        ax.text(x+12,y+11,t,ha="center",va="center",color=WHITE,fontsize=8.4,fontweight="bold",zorder=4)
        ax.text(x+12,y+6.5,d,ha="center",va="center",color=WHITE,fontsize=6.8,zorder=4)
        ax.text(x+12,y+2.5,ex,ha="center",va="center",color=WHITE,fontsize=6.8,style="italic",zorder=4)
        # connector to centre
        tx=50 if x<40 else 50;
        cxp=x+24 if x<40 else x
        arrow(ax,cxp if x<40 else x, y+7.5, 37 if x<40 else 63, 53 if y>40 else 50, color=GREY,lw=1.4)
    caption(ax,"Whoever controls the control point (data, algorithms, standards, or the user relationship) controls the market.",y=6,fs=9.2)
    save(fig,"s25_control_points.png")

for fn in [s16_digital_market,s19_coopetition,s20_layers,s21_innovation,s23_value_creation,s25_control_points]:
    fn()
print("\nAll IT250 Unit 3 diagrams written to",OUT)
