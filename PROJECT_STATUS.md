# PROJECT STATUS & HANDOFF — course-material rebuild

> **Purpose of this file.** A durable handoff so a fresh conversation can continue without
> re-deriving anything. Read this + [`COURSE_MATERIAL_STANDARD.md`](COURSE_MATERIAL_STANDARD.md)
> (the governing spec) + [`CLAUDE.md`](CLAUDE.md) (auto-loaded summary) and you're caught up.
> Last updated: 2026-07-09 (IT246 Units 1–4 done; **pivoting to a NEW semester: `eighth/` = IT 250 Digital Economy**).

---

## 0. ⭐ CURRENT FOCUS (start here)

**We are starting a new semester: `eighth/` = IT 250 Digital Economy (BIM 8th sem).**
It is at an EARLIER stage than the other courses: `eighth/` currently holds ONLY the instructor's
**raw lecture PDFs/PPTX** (see §1) — there is **no session plan, no content outline, no `material.md`,
and no build scripts yet.** So the eighth-sem workflow has an extra first step:

1. **Extract & organise content from the lecture PDFs** in each `eighth/unit N/` folder into a
   `UnitN_content_outline.md` (concepts, examples, the Nepal angle), the way `sixth/` outlines look.
2. Then the normal pipeline: `UnitN_material.md` → `build_unitN_images.py` → `build_unitN_pptx.py`,
   all to `COURSE_MATERIAL_STANDARD.md` incl. §7A depth tables.
3. **Reuse the toolkit:** copy `sixth/deckkit.py` into `eighth/` (it resolves `images/` relative to
   its own folder) and `from deckkit import *`, exactly like the IT246 Unit 2–4 scripts.

IT 250 is an **economics/management** course (digital markets, platforms, transformation), not a
technical one — so localise to Nepal's digital economy (eSewa/Khalti, NRB, e-governance/Nagarik App,
NTC/Ncell, Daraz, remittances, hydro/IT-export) and lean on comparison/example tables for the many
confusable concept pairs (digital vs knowledge economy, misinformation of markets, etc.).

---

## 1. What this project is

Three university courses, decks + study material, one folder per semester:
- **`fourth/` = IT 220: Database Management System** (BIM 4th sem), Units 1–7.
- **`sixth/` = IT 246: IT Ethics & Cybersecurity** (BIM 6th sem), Units 1–9.
- **`eighth/` = IT 250: Digital Economy** (BIM 8th sem, 3 cr, 48 LHs), Units 1–6. ⭐ NEW / current focus.
  Units: (1) Introduction — digital & K-economy, 4IR; (2) Fundamentals — multi-sided platforms,
  network effects, lock-in, monopolies, adoption indexes; (3) Digital Markets, Strategy & Innovation
  — co-opetition, layered internet model, business/value-creation models; (4) Digital Transformation
  — SDGs, globalization, digital currencies; (5) Economics of Information — asymmetric information,
  search/AI, IP & digitalization; (6) Digitalization in the Nepalese Perspective — e-governance,
  digital financial inclusion, sector impact. Source text: Øverby & Audestad (2021); Maheshwari (2019);
  Adhikari, *Digital Economics* (Kathmandu).

Each unit's pipeline: **`UnitN_material.md`** (source of truth, prose) → **`build_unitN_images.py`**
(matplotlib → PNGs in `images/`) → **`build_unitN_pptx.py`** (python-pptx → `IT###_UnitN.pptx`).
For `eighth/`, the source is currently the raw lecture PDFs, so an outline-extraction step comes first (§0).

## 2. The governing standard (read it)

`COURSE_MATERIAL_STANDARD.md` is the single source of truth for how decks are built. Non-negotiables:
- **Self-contained / PDF-safe (golden rule §1):** nothing load-bearing may live only in speaker
  notes (PDF export drops notes). Definitions, examples, 🎯 exam answers, key terms, misconception
  fixes all go **on the slide face**. Notes hold only timing/delivery cues.
- **Two-slide concept pairs (§6.3):** each concept = an **"understand"** slide (definition +
  how-it-works + optional diagram + memory hook) and an **"apply"** slide (4 colored panels:
  🌍 real example / ⚠️ common trap / 🎯 exam-ready answer / 🔑 key terms).
- **§7A Depth through tables (MANDATORY):** no abstraction without concrete instances. Every
  confusable set → a **comparison table**; every "X vs not-X" concept → a **concrete-example table**
  (≥6 rows, Nepal/IT-localised, + consequence/benefit column); claims → **scaffolding tables**;
  motivation → **payoff tables**. Tables are **generated, never hand-pasted**, and on the slide face.
- **Generous slide count:** NO rule about minimizing slides. Split freely; put each table on its own
  slide; never squeeze. (User instruction, 2026-07-08: "be full of heart… as many slides as needed.")
- **Also required:** solved-problem slides for procedural units; roadmap slide; per-session summary
  slide; end-of-unit cheat sheet + glossary; page numbers on every slide (auto-contrast).
- Shared **visual system** (palette/fonts/slide-types) in §5 so all decks look like one course.
- Run the §11 pre-ship checklist (incl. the two depth lines) before declaring a deck done.

## 3. Scope & rollout rules (§14 of the standard) — IMPORTANT

- **IT 250 (eighth): NEW — current focus.** Build all 6 units to the full standard + §7A depth. No prior
  scaffolding exists (raw lecture PDFs only) — extract outlines first (§0). This is where new work goes.
- **IT 220 (fourth) Units 1–4: DONE and FROZEN — do NOT touch** their decks / build scripts / images.
- **IT 220 Units 5–7: pending.** Must include §7A depth tables when built.
- **IT 246 (sixth): Units 1–4 DONE** (standard + §7A depth). **Units 5–9 pending** (outlines only).

## 4. Status by unit

| Course | Unit | Deck | Slides | State |
|---|---|---|---|---|
| IT220 | 1 (DB Concepts & Architecture) | `IT220_Unit1.pptx` | 58 | ✅ done, frozen |
| IT220 | 2 S5–S8 (ER model) | `IT220_Unit2.pptx` | 51 | ✅ done, frozen |
| IT220 | 2 S9–S12 (ER model) | `IT220_Unit2b.pptx` | 50 | ✅ done, frozen |
| IT220 | 3 (Relational Algebra & Calculus) | `IT220_Unit3.pptx` | 56 | ✅ done, frozen |
| IT220 | 4 (Normalization) | `IT220_Unit4.pptx` | 49 | ✅ done, frozen |
| IT220 | 5 (SQL, 15 sessions S22–S36) | — | — | ⏳ pending (has content outline only) |
| IT220 | 6 (Transactions/Concurrency/Recovery) | — | — | ⏳ pending (outline only) |
| IT220 | 7 (Advanced Topics) | — | — | ⏳ pending (outline only) |
| IT246 | 1 (An Overview of Ethics) | `IT246_Unit1.pptx` | 87 | ✅ rebuilt to standard + §7A depth |
| IT246 | 2 (Ethics for IT Workers & Users) | `IT246_Unit2.pptx` | 92 | ✅ rebuilt to standard + §7A depth |
| IT246 | 3 (Intellectual Property) | `IT246_Unit3.pptx` | 81 | ✅ built to standard + §7A depth |
| IT246 | 4 (Software Dev & IT Org Ethics) | `IT246_Unit4.pptx` | 80 | ✅ built to standard + §7A depth |
| IT246 | 5–9 | — | — | ⏳ pending build (5–9 have content outlines only) |
| **IT250** | **1 (Introduction — digital/K-economy, 4IR)** | `IT250_Unit1.pptx` | 107 | ✅ **built to standard + §7A depth (pending user review)** |
| IT250 | 2 (Fundamentals — platforms, network effects, monopolies) | `IT250_Unit2.pptx` | 100 | ✅ built to standard + §7A depth (pending user review) |
| IT250 | 3 (Digital Markets, Strategy & Innovation) | — | — | ⏳ lecture PDFs only |
| IT250 | 4 (Digital Transformation) | — | — | ⏳ lecture PDFs only |
| IT250 | 5 (Economics of Information) | — | — | ⏳ lecture PDFs only |
| IT250 | 6 (Digitalization — Nepalese Perspective) | — | — | ⏳ lecture PDFs only |

Notes:
- **IT250 (eighth) source inventory** — each `eighth/unit N/` folder holds the instructor's lecture
  PDFs/PPTX (the raw source to build from), no scaffolding yet. `eighth/course.txt` has the official
  syllabus. Rough contents: **U1** 7 files incl. `Question_Papers_Reconstructed.pdf` (useful for exam
  Qs); **U2** 6 (platforms, network effects, monopolies, adoption indexes); **U3** 10 (competition/
  co-opetition, layered internet, business & value-creation models, modeling); **U4** 8 (transformation,
  SDGs, globalization, digital currencies); **U5** 8 (asymmetric information, AI, consumer choice, IP);
  **U6** 6 (e-governance Nepal, digital financial inclusion, sector performance). There's a stray
  `.DS_Store` in `eighth/` — gitignore it. `eighth/` is currently **untracked in git** (not yet added).
- IT246 Unit 1 rebuild = **87 slides, 21 native tables** (was 39 slides, 0 tables). Diagrams:
  `sixth/build_unit1_images.py` → 6 PNGs (s1_grid, s2_pyramid, s2_stakeholders, s3_cycle, s4_5step, s5_scale).
  Its 21 §7A tables are now also backfilled into `Unit1_material.md` (was gap #1).
- IT246 Unit 2 rebuild = **92 slides, 23 native tables, 7 diagrams** (`sixth/build_unit2_images.py` →
  s6_web, s7_map, s8_insider, s9_trail, s9_seesaw, s10_spectrum, s10_verify). 20 concept pairs
  (5 sessions × 4). Quiz MCQs now carry a one-line "Why:" rationale (partially addresses old gap #5).
  Both the deck script and `Unit2_material.md` carry the tables (source kept in sync from the start).
- IT246 Unit 3 build = **81 slides, 16 native tables, 8 diagrams** (`sixth/build_unit3_images.py` →
  s11_families, s11_idea_expr, s12_funnel, s12_process, s13_tree, s14_venn, s15_licenses, s16_squat).
  16 concept pairs (S11–S16); capstone master 4-way IP comparison table in S16. Unit 3 had NO prior
  material.md — only a content outline — so the deck was authored from the outline, then `Unit3_material.md`
  was authored to match (lecturer-ready prose + the 16 tables), synced with the deck.
- IT246 Unit 4 build = **80 slides, 17 native tables, 6 diagrams** (`sixth/build_unit4_images.py` →
  s17_costcurve, s18_pyramid, s18_riskmatrix, s19_spectrum, s20_flow, s21_lifecycle). 17 concept pairs
  (S17–S21). Same outline-only recipe as Unit 3; `Unit4_material.md` authored to match the deck.
- All four IT246 build scripts now `from deckkit import *` — the shared toolkit `sixth/deckkit.py` (was gap #3).
- `sixth/IT246_Unit1 2.pptx` is the user's **manual** enrichment of the OLD deck — kept as reference,
  now superseded by the rebuild. `sixth/GAP_ANALYSIS_Unit1.md` is the analysis that drove the §7A rule.
- IT220 Unit 2 is split into two decks/scripts: `_unit2` (S5–S8) and `_unit2b` (S9–S12).

## 5. Build conventions / how to reproduce

- **Deps:** `python-pptx` (1.0.2) and `matplotlib` (3.9.4) are pip-installed on this machine.
- **Build a unit:** `cd <folder> && python3 build_unitN_images.py && python3 build_unitN_pptx.py`.
- **Save paths are relative** to the script (`os.path.dirname(os.path.abspath(__file__))`) — machine-independent.
  (The OLD scripts had a hardcoded `/Users/inventechg1/...` path; the rebuilt ones do NOT.)
- **Shared toolkit — `sixth/deckkit.py`.** IT246 build scripts now do `from deckkit import *` instead of
  copy-pasting helpers. deckkit exports: `_bg _box _bar _notes _header _card add_title add_outcomes
  add_roadmap add_divider concept_understand concept_apply add_activity add_quiz(compact=) add_summary
  add_cheatsheet add_glossary _add_page_numbers save`, plus the palette + `prs`/`SW`/`SH`/`BLANK`/`IMG`.
  Table helper: **`add_table_slide(kicker,title,headers,rows,per_page,widths,note,fs)`** — native PPTX
  table on its own slide, auto-paginating ("(cont.)"), navy header + alternating fills — with semantic
  aliases **`add_comparison_table` / `add_examples_table`** (§14). End a script with `_add_page_numbers();
  save("IT###_UnitN.pptx")`. **Reuse `sixth/build_unit4_pptx.py` as the template** — it's the newest and
  the model for outline-only units. **For `eighth/` (IT250):** copy `sixth/deckkit.py` → `eighth/deckkit.py`
  (it resolves `images/` next to itself, so one copy per course folder), then `from deckkit import *` in the
  eighth build scripts. (IT220 scripts still carry their own copied helpers; migrate only if/when touched —
  IT220 Units 1–4 are FROZEN.)
- **Palette (hex):** NAVY 0C2B4A, BLUE 185FA5, TEAL 0F6E56, AMBER 854F0B, CORAL 993C1D,
  card tints BLUE_T E6F1FB / CORAL_T FAECE7 / TEAL_T E1F5EE / AMBER_T FAEEDA. Slides 13.333×7.5in.
- **Verification snippet** (run after every build): check page numbers on all slides, every "apply"
  slide has 4 panels (🌍⚠️🎯🔑), no speaker note > 400 chars, longest card text < ~450 chars. A
  height-estimator for table overflow is in the last session's transcript (crude chars-per-line).

## 6. KNOWN GAPS

**Closed in the 2026-07-08 consolidation pass:**
- ✅ **#1 source/deck divergence.** Unit 1's 21 tables backfilled into `Unit1_material.md`; Unit 2 authored
  with tables in `Unit2_material.md` from the start. Go-forward rule: every rebuilt unit carries its §7A
  tables in BOTH the build script and the material.md.
- ✅ **#3 shared helper module.** `sixth/deckkit.py` extracted; both IT246 build scripts import it. Unit 1
  rebuilt through deckkit and byte-for-byte identical to before (87 slides, verified).
- ✅ **#4 standard wording vs code.** Standard §7A/§14 updated to name deckkit and the
  `add_table_slide` + `add_comparison_table`/`add_examples_table` alias set.
- ✅ **#5 quiz "why".** Unit 2 MCQs now carry a one-line rationale. (IT246 Unit 1 and IT220 not
  retrofitted — do so opportunistically if a deck is otherwise touched; not a regression.)

**Still open:**
1. **HIGH — visual rendering unverified.** No LibreOffice/`soffice` on this machine, so decks are verified
   programmatically only. Native PPTX **table styling** (borders/fills) is the least-proven part. **User
   should open Unit 1 & Unit 2 and eyeball the table slides**, or install a headless renderer for a PDF check.
2. **LOW — housekeeping.** `sixth/IT246_Unit1 2.pptx` is superseded (delete once the new decks are approved).
   The Unit 1/2 material.md "review copy" footers are now fixed; the old `build_unit2_pptx.py` was overwritten
   by the rebuild (its old-style helpers are gone).

**IT250 Unit 1 build (2026-07-09)** = **107 slides, 22 native §7A tables, 8 diagrams**
(`eighth/build_unit1_images.py` → s1_evolution, s2_ecosystem, s3_iceberg, s5_overlap, s6_timeline,
s6_fusion, s7_swot, s8_quadrant). 8 sessions S1–S8 (1 per LH), ~24 concept understand/apply pairs.
Workflow used: (1) `deckkit.py` copied into `eighth/`; (2) a reader agent distilled the `unit 1/`
lecture PDFs+PPTX into a source inventory; (3) `Unit1_content_outline.md` authored WITH a syllabus↔
old-material mapping (§0: match/gap/bonus) — the user's explicit ask; (4) deck + `Unit1_material.md`
(1791 lines, mirrors `sixth/Unit4_material.md`, carries the same tables) built to match. **Locked
decisions:** Nepal policy DEPTH held for Unit 6 (S8 keeps regulation introductory + forward-refs U6);
economics introductory only in U1 (mechanics → Unit 2); "regularity" read as "regulation". **Flag:**
`eighth/unit 1/Question_Papers_Reconstructed.pdf` is NOT an IT 250 paper — it's school-level
English/Social-Studies papers (a stray artifact); no genuine IT 250 past-paper exists, so 🎯 answers
are syllabus-derived. Structural verify passed (page numbers 107/107, 4-panel apply slides, notes
<400, cards <460); NOT visually rendered (no local soffice — same caveat as all decks).

**IT250 Unit 2 build (2026-07-09)** = **100 slides, 21 native §7A tables, 6 diagrams**
(`eighth/build_unit2_images.py` → s9_pipe_platform, s10_networkloop, s11_crosssubsidy, s12_flywheel,
s13_tipping, s15_dai_pillars). 7 sessions S9–S15 (1 per LH), 21 concept understand/apply pairs.
Same workflow as U1 (reader-agent inventory → `Unit2_content_outline.md` with §0 mapping → deck +
`Unit2_material.md`, 1753 lines). **S11 absorbs the platform economics deferred from Unit 1**
(two-sided cross-subsidy: money side vs subsidy side; zero-marginal-cost/economies of scale;
chicken-and-egg). Topics 1–3 (platforms/network effects/monopolies) were richly covered by the old
PDFs; the two-sided PRICING mechanics were the real gap and were built fresh. **Decisions:** syllabus
"OECD digital adoption government index" taught as the **OECD Digital Government Index (DGI)** — flag
to user in case they meant the UN EGDI (not in old material); an old L3 slide mislabelled an Amazon
example as "Uber" (corrected in build). Structural verify passed (100/100 page numbers, 4-panel apply,
notes <400, cards <460, tables ≤9 rows). Fixed a subagent artifact: the consolidated Section A answer
key in `Unit2_material.md` was all-"b" — repositioned to vary (key now 1-c,2-a,3-d,…). NOT visually
rendered (no local soffice).

**Recommended next action:** **PAUSE for user review of IT250 Unit 2**, then continue to **Unit 3
(Digital Markets, Strategy & Innovation — competition/co-opetition, the layered internet model,
digital business & value-creation models, modeling of digital markets; 10 LHs → ~10 sessions S16–S25,
`eighth/unit 3/` has 10 lecture PDFs)** using the same workflow. Then Units 4–6. Other still-open
tracks: IT246 Units 5–9 (outlines only); IT220 Units 5–7 (SQL Unit 5; MySQL/MariaDB locked) — lower priority.

**Established build recipe for an outline-only unit** (used for IT246 Units 3 & 4; reuse for all IT250):
0. **(IT250 only)** Extract a `UnitN_content_outline.md` from the unit's lecture PDFs first (no outline exists).
1. `build_unitN_images.py` — spatial diagrams only (comparisons → tables). Eyeball the tricky ones.
2. `build_unitN_pptx.py` — `from deckkit import *`; one understand+apply pair per concept, §7A depth
   table(s) per concept, per-session divider/activity/quiz/summary, cheat sheet, glossary, consolidated
   quiz, end title. Verify: page numbers, 4-panel apply slides, notes <400 chars, apply cards <~450.
3. `UnitN_material.md` — lecturer-ready prose mirroring `Unit4_material.md`, carrying the same tables
   (delegate to a subagent with the outline + deck + a prior material.md as template).

## 7. Working agreements with the user
- **Pause after each unit** for review (user's chosen cadence).
- **Generous slides, full depth** — never sacrifice depth for slide count.
- **Localise examples** to Nepal / South Asia (eSewa, Khalti, Daraz, Nagarik App, NRB, Ntc/Ncell, etc.).
- Persistent caveat to always state: decks are verified structurally, not visually (no local renderer).
- Decision locked for IT220 Unit 5 when built: **SQL examples target MySQL/MariaDB** (unless told otherwise).
