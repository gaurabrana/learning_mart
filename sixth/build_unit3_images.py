#!/usr/bin/env python3
"""Concept diagrams for IT246 (sixth) Unit 3 — Intellectual Property (S11–S16).
Genuinely spatial concepts only (four IP families, idea-vs-expression split, patentability funnel,
patent-process timeline, patent-vs-secret decision tree, plagiarism/infringement Venn, license
spectrum, cybersquatting flow); all comparisons/examples are native PPTX tables in the deck (§7A).
License-safe. Output -> sixth/images/   Run: python3 build_unit3_images.py
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

def s11_families():
    fig,ax=canvas(10,5.2)
    ax.text(50,96,"The four families of intellectual property",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    fam=[("COPYRIGHT","protects EXPRESSION\ncode · music · text · art\nauto on creation · life+50 yrs",BLUE,PALEB,4,52),
         ("PATENT","protects an INVENTION\nnew, useful, non-obvious\napply + disclose · ~20 yrs",TEAL,PALET,52,52),
         ("TRADE SECRET","protects SECRET INFO\nrecipes · algorithms · lists\nkeep secret · unlimited",AMBER,PALEA,4,8),
         ("TRADEMARK","protects BRAND IDENTITY\nname · logo · slogan\nregister · renew forever",CORAL,PALEC,52,8)]
    for title,body,ec,fc,x,y in fam:
        ax.add_patch(FancyBboxPatch((x,y),44,36,boxstyle="round,pad=0.3,rounding_size=2",fc=fc,ec=ec,lw=1.8,zorder=2))
        ax.text(x+22,y+29,title,ha="center",color=ec,fontsize=12,fontweight="bold")
        ax.text(x+22,y+13,body,ha="center",color=INK,fontsize=9.3)
    caption(ax,"Each protects a DIFFERENT thing, is acquired differently, and lasts a different length of time (full table in the deck).",y=1)
    save(fig,"s11_families.png")

def s11_idea_expr():
    fig,ax=canvas(10,4.4)
    ax.text(50,92,"Copyright protects EXPRESSION, not the IDEA",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    rbox(ax,6,44,40,26,"THE IDEA\n(a recipe; an algorithm;\na plot; 'an app that splits bills')",fc=PALEB,tc=INK,ec=BLUE,fs=10)
    rbox(ax,54,44,40,26,"THE EXPRESSION\n(your written code; your text;\nyour recorded song)",fc=PALET,tc=INK,ec=TEAL,fs=10)
    ax.text(28,38,"NOT protected — anyone may reuse",ha="center",color=BLUE,fontsize=9.5,style="italic")
    ax.text(74,38,"PROTECTED the instant it's fixed",ha="center",color=TEAL,fontsize=9.5,style="italic")
    caption(ax,"Others may cook the dish (the idea) — they may NOT photocopy and sell your cookbook (your expression).",y=12)
    save(fig,"s11_idea_expr.png")

def s12_funnel():
    fig,ax=canvas(10,5.0)
    ax.text(50,95,"Patentability — pass all three tests or no patent",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    tests=[("1  NOVELTY — is it genuinely NEW? (not already known)",BLUE,10,86,72),
           ("2  INVENTIVENESS — is it NON-OBVIOUS to an expert?",TEAL,28,68,52),
           ("3  INDUSTRIAL APPLICABILITY — is it USEFUL / can it be made?",AMBER,46,50,32)]
    for text,c,y,x,w in tests:
        ax.add_patch(FancyBboxPatch(((100-w)/2,y),w,14,boxstyle="round,pad=0.2,rounding_size=2",fc=c,ec=WHITE,lw=1.5,zorder=3))
        ax.text(50,y+7,text,ha="center",va="center",color=WHITE,fontsize=9.3,fontweight="bold",zorder=4)
    rbox(ax,38,18,24,12,"PATENT\nGRANTED",fc=NAVY,fs=11)
    arrow(ax,50,46,50,30,color=GREY,lw=2.0)
    caption(ax,"Pure ideas, discoveries, and laws of nature fail test 1/2 — only concrete, applicable inventions pass.",y=6)
    save(fig,"s12_funnel.png")

def s12_process():
    fig,ax=canvas(10,4.2)
    ax.text(50,90,"The patent process — slow, public, costly, territorial",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    steps=[("Prior-art\nsearch",BLUE),("File claims\n(DoI, Nepal)",TEAL),("Examination",AMBER),("Grant",BLUE),("Renewal\nfees (~20 yr)",CORAL)]
    x=2; w=17
    for i,(t,c) in enumerate(steps):
        rbox(ax,x,42,w,24,t,fc=c,fs=9.3)
        if i<4: arrow(ax,x+w,54,x+w+2.5,54,color=NAVY,lw=2.2)
        x+=w+2.5
    caption(ax,"A Nepal patent protects you only in Nepal (territorial). After ~20 years the invention becomes public.",y=16)
    save(fig,"s12_process.png")

def s13_tree():
    fig,ax=canvas(10,5.0)
    ax.text(50,95,"Patent or trade secret? — a decision tree",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    rbox(ax,32,80,36,12,"You have an invention",fc=NAVY,fs=10.5)
    rbox(ax,26,58,48,12,"Can rivals reverse-engineer it once sold?",fc=BLUE,fs=9.5)
    arrow(ax,50,80,50,70,color=GREY,lw=1.8)
    # yes branch -> patent
    rbox(ax,6,34,38,14,"YES → it will be visible\nPATENT it (disclose, ~20 yr monopoly)",fc=TEAL,fs=9)
    # no branch -> trade secret
    rbox(ax,56,34,38,14,"NO → hard to copy / long-term value\nTRADE SECRET (keep quiet, unlimited)",fc=AMBER,fs=9)
    arrow(ax,42,58,30,48,color=TEAL,lw=1.8); ax.text(28,53,"yes",color=TEAL,fontsize=9,fontweight="bold")
    arrow(ax,58,58,72,48,color=AMBER,lw=1.8); ax.text(74,53,"no",color=AMBER,fontsize=9,fontweight="bold")
    caption(ax,"Patent = shout it from the rooftop for 20 years' rent. Trade secret = whisper it and hope no one overhears — forever.",y=6)
    save(fig,"s13_tree.png")

def s14_venn():
    fig,ax=canvas(10,4.8)
    ax.text(50,95,"Plagiarism vs copyright infringement — overlap, not identity",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    ax.add_patch(Circle((36,46),27,fc=PALEB,ec=BLUE,lw=1.8,alpha=0.85,zorder=2))
    ax.add_patch(Circle((64,46),27,fc=PALEC,ec=CORAL,lw=1.8,alpha=0.6,zorder=2))
    ax.text(24,64,"PLAGIARISM",ha="center",color=BLUE,fontsize=11,fontweight="bold",zorder=4)
    ax.text(24,52,"ethical /\nacademic offence",ha="center",color=INK,fontsize=8.8,zorder=4)
    ax.text(24,40,"copying an idea\nwith no credit\n(even if uncopyrighted)",ha="center",color=INK,fontsize=8,zorder=4)
    ax.text(76,64,"INFRINGEMENT",ha="center",color=CORAL,fontsize=11,fontweight="bold",zorder=4)
    ax.text(76,52,"legal offence",ha="center",color=INK,fontsize=8.8,zorder=4)
    ax.text(76,40,"copying protected\nexpression\n(even if credited)",ha="center",color=INK,fontsize=8,zorder=4)
    ax.text(50,47,"BOTH\ncopy + no\npermission",ha="center",color=NAVY,fontsize=8.3,fontweight="bold",zorder=4)
    caption(ax,"Crediting the author avoids PLAGIARISM but not INFRINGEMENT — they are separate questions.",y=4)
    save(fig,"s14_venn.png")

def s15_licenses():
    fig,ax=canvas(10,4.2)
    ax.text(50,90,"The open-source licence spectrum — freedom vs obligation",ha="center",color=NAVY,fontsize=12.5,fontweight="bold")
    segs=[("PUBLIC DOMAIN\nno rights reserved",GREY,3),
          ("PERMISSIVE\nMIT · Apache\n(use freely, attribute)",TEAL,27),
          ("COPYLEFT\nGPL (derivatives\nmust stay open)",BLUE,51),
          ("PROPRIETARY\nall rights reserved",CORAL,75)]
    for t,c,x in segs:
        rbox(ax,x,44,22,24,t,fc=c,fs=8.6)
    arrow(ax,3,38,97,38,color=GREY,lw=2.0)
    ax.text(14,31,"most free",ha="center",color=TEAL,fontsize=9,style="italic")
    ax.text(86,31,"most restricted",ha="center",color=CORAL,fontsize=9,style="italic")
    caption(ax,"Open source = copyright PLUS a licence. Even 'free' code carries obligations (attribution, share-alike) — ignoring them is infringement.",y=10,fs=9.7)
    save(fig,"s15_licenses.png")

def s16_squat():
    fig,ax=canvas(10,4.2)
    ax.text(50,90,"Cybersquatting — and how a dispute is resolved",ha="center",color=NAVY,fontsize=13,fontweight="bold")
    steps=[("Squatter registers\nbrand's domain\n(bad faith)",CORAL),("Demands ransom\nor diverts traffic",AMBER),
           ("Brand files dispute\nUDRP (.com) /\n.np registry",BLUE),("Domain returned\nto rightful owner",TEAL)]
    x=3; w=21
    for i,(t,c) in enumerate(steps):
        rbox(ax,x,42,w,24,t,fc=c,fs=8.8)
        if i<3: arrow(ax,x+w,54,x+w+1.5,54,color=NAVY,lw=2.2)
        x+=w+1.5
    caption(ax,"Grabbing a famous name's domain to resell it is bad-faith cybersquatting — not legitimate domain investing.",y=14,fs=9.7)
    save(fig,"s16_squat.png")

for fn in [s11_families,s11_idea_expr,s12_funnel,s12_process,s13_tree,s14_venn,s15_licenses,s16_squat]:
    fn()
print("\nAll IT246 Unit 3 diagrams written to",OUT)
