# PROJECT STATUS & HANDOFF — course-material rebuild

> **Purpose of this file.** A durable handoff so a fresh conversation can continue without
> re-deriving anything. Read this + [`COURSE_MATERIAL_STANDARD.md`](COURSE_MATERIAL_STANDARD.md)
> (the governing spec) + [`CLAUDE.md`](CLAUDE.md) (auto-loaded summary) and you're caught up.
> Last updated: 2026-07-08 (consolidation pass + IT246 Units 2, 3 & 4 built to standard).

---

## 1. What this project is

Two university courses, decks + study material, one folder per semester:
- **`fourth/` = IT 220: Database Management System** (BIM 4th sem), Units 1–7.
- **`sixth/` = IT 246: IT Ethics & Cybersecurity** (BIM 6th sem), Units 1–9.

Each unit's pipeline: **`UnitN_material.md`** (source of truth, prose) → **`build_unitN_images.py`**
(matplotlib → PNGs in `images/`) → **`build_unitN_pptx.py`** (python-pptx → `IT###_UnitN.pptx`).

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

- **IT 220 (fourth) Units 1–4: DONE and FROZEN — do NOT touch** their decks / build scripts / images.
- **IT 220 Units 5–7: pending.** Must include §7A depth tables when built.
- **IT 246 (sixth): rebuild from Unit 1 onward** to the full standard + depth. Unit 1 is done (below).

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

Notes:
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
  save("IT###_UnitN.pptx")`. **Reuse `sixth/build_unit2_pptx.py` as the template** — it's the newest.
  (IT220 scripts still carry their own copied helpers; migrate them to deckkit only if/when touched — but
  IT220 Units 1–4 are FROZEN, so in practice a future IT220 module could `from deckkit import *` too.)
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

**Recommended next action:** **PAUSE for user review of IT246 Units 2, 3 & 4** (user's cadence). On approval,
continue the IT246 track with **Unit 5 — Cybersecurity** (first of the security units 5–8; content outline
only — same recipe: images → deck via deckkit → material.md). NOTE: Units 5–8 shift from ethics to technical
security, so diagrams/tables will lean toward attack/defence mechanics (threats, controls, CIA triad, etc.).
IT220 Units 5–7 remain the other pending track (SQL Unit 5 is the big one; MySQL/MariaDB dialect locked).

**Established build recipe for an outline-only unit** (used for Unit 3, reuse for Units 4–9):
1. `build_unitN_images.py` — spatial diagrams only (comparisons → tables). Eyeball the tricky ones.
2. `build_unitN_pptx.py` — `from deckkit import *`; one understand+apply pair per concept, §7A depth
   table(s) per concept, per-session divider/activity/quiz/summary, cheat sheet, glossary, consolidated
   quiz, end title. Verify: page numbers, 4-panel apply slides, notes <400 chars, apply cards <~450.
3. `UnitN_material.md` — lecturer-ready prose mirroring `Unit2_material.md`, carrying the same tables
   (delegate to a subagent with the outline + deck + Unit2_material.md as template).

## 7. Working agreements with the user
- **Pause after each unit** for review (user's chosen cadence).
- **Generous slides, full depth** — never sacrifice depth for slide count.
- **Localise examples** to Nepal / South Asia (eSewa, Khalti, Daraz, Nagarik App, NRB, Ntc/Ncell, etc.).
- Persistent caveat to always state: decks are verified structurally, not visually (no local renderer).
- Decision locked for IT220 Unit 5 when built: **SQL examples target MySQL/MariaDB** (unless told otherwise).
