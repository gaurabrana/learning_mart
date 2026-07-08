# Course Material Authoring Standard

> **This is the single source of truth for every deck in this repo.** Any conversation or
> script that generates or edits course material (`fourth/`, `sixth/`, `eighth/`, future
> semesters) MUST follow this document. When in doubt, this file wins. If you change the
> house style, change it *here first*, then propagate.

---

## 0. The one-line brief

**Every slide must teach the whole concept on its own face — a student who never attended
the lecture, reading a flat PDF with no speaker notes, should still get the complete picture.**

We are building *study material that happens to be slides*, not presenter cue-cards. It is
fine — expected — for a deck to have many slides. It is never fine for a slide to be
understandable only if a teacher is talking over it.

---

## 1. The PDF-Safety Rule (the golden rule)

Decks get exported to PDF. **PDF export drops speaker notes.** Therefore:

> **No fact, definition, example, diagram label, answer, or reasoning may live *only* in
> speaker notes. If losing the notes would lose understanding, the content is in the wrong
> place — put it on the slide face.**

### What speaker notes ARE allowed to contain (teacher-only, non-load-bearing)
- Timing cues: `[~12 min]`, pacing reminders.
- Delivery choreography: "ask the class before revealing", "have two pairs draw at the board".
- "How to run this activity" logistics.
- Optional deeper tangents the teacher *may* mention but that are not required to understand the slide.

### What must NEVER be notes-only (move to the slide face)
- Definitions, mechanisms, "how it works".
- Worked examples and their answers.
- 🎯 Model exam answers.
- Analogies and memory hooks that carry the intuition.
- Misconception corrections.
- Anything a student would need to revise from.

**Test before shipping:** delete every speaker note in your head. Can a student still fully
learn from the slides? If no, you violated the golden rule.

---

## 2. What "self-contained" means — required content per concept

Your `UnitX_material.md` files already contain all of this. The build script's job is to get
it **onto the slide face**, not to summarise it into 4 bullets. For every concept, the slide(s)
must carry:

| Element | Required? | Purpose |
|---|---|---|
| **Definition** — plain English, one tight sentence | Always | What it is |
| **Mechanism / how it works** — 2–4 points | Always | Why/how it behaves |
| **Worked real example** — a system students use (Daraz, eSewa, Khalti, Nagarik App…) | Always | Makes it concrete |
| **Visual** — diagram, table, or comparison | When it clarifies (most concepts) | Dual-coding |
| **⚠️ Common trap / misconception + correction** | Always | Pre-empts errors |
| **🎯 Exam-ready answer** — the crisp answer a student would write | Always | Revision + assessment |
| **🧠 Analogy / memory hook** | Always | Retention |
| **🔑 Key terms** | When new terms appear | Glossary in place |

If all of that cannot fit legibly on one slide, **split the concept across two slides** (see §4).
Do not shrink to fit.

---

## 3. Legibility floor (never trade readability for cramming)

- **Body text ≥ 14 pt. Never below 12 pt** for anything a student must read.
- Headline 24–28 pt, sub/kicker 12–14 pt.
- Line length: keep text columns ≤ ~7.5" wide so lines stay readable.
- High contrast only (see palette). No text over busy image areas.
- Leave breathing room — a wall of tiny text is as useless as an empty slide.

**If it doesn't fit at ≥14 pt, that's the signal to split, not to shrink.**

---

## 4. Density & splitting policy

More slides is good. Cramming is bad. When a concept is too rich for one readable slide, use
the **two-slide concept pair**:

- **Slide A — "Understand it":** definition + mechanism + the visual.
- **Slide B — "Use it":** worked example + ⚠️ misconception + 🎯 exam-ready answer + 🔑 key terms.

Each slide of the pair is independently readable, and together they are fully self-contained.
Prefer a clean pair over one crammed slide every time.

A single dense slide (§6, "Concept slide") is fine when the concept is small enough to stay ≥14 pt.

---

## 5. The visual system (canonical — all decks share this so they look like one course)

Pulled from the existing build scripts. Do not invent new palettes per deck.

### Canvas
- 16:9, `13.333in × 7.5in`.
- Blank layout (`slide_layouts[6]`); every element positioned manually.

### Palette (RGB hex)
| Name | Hex | Use |
|---|---|---|
| NAVY | `0C2B4A` | Titles, headings, dark backgrounds |
| BLUE | `185FA5` | Section dividers, accent bars, kickers |
| TEAL | `0F6E56` | Positive/answer accents, activity theme, memory-hook band |
| AMBER | `854F0B` | Quiz theme, "caution"/attention accents |
| CORAL | `993C1D` | Misconception / warning accents |
| LIGHT | `F2F5F8` | Quiz slide background |
| PALE-TEAL | `E1F5EE` | Activity slide background |
| WHITE | `FFFFFF` | Content background, text on dark |
| DARK | `1A1A1A` | Primary body text |
| GREY | `55606B` | Secondary body text |

### Type
- Single sans family (PowerPoint default Calibri is fine; if a script sets a font, set it once, globally).
- Bold for headings and the lead line of each block; regular for elaboration.

### Slide-type themes (keep consistent across every unit)
| Slide type | Background | Accent |
|---|---|---|
| Title | NAVY | AMBER bar |
| Section divider | BLUE | white text |
| Concept | WHITE | BLUE header bar, NAVY heading |
| In-class activity | PALE-TEAL | TEAL |
| Quiz / check | LIGHT | AMBER |
| Panels (see §6) | tinted card on WHITE | per meaning: TEAL=answer, CORAL=trap, BLUE=example |

---

## 6. Slide layouts

### 6.1 Title slide
Course + unit, session range, context line (e.g. "Nepal / South Asia context"), notation note.

### 6.2 Section divider
Kicker (session + lecture hour) + big title. The **hook goes on the slide face here** (as a
line/question students can read), not only in notes.

### 6.3 Concept slide (the workhorse — redesigned for self-containment)
Zones on one WHITE slide:

```
┌──────────────────────────────────────────────────────────┐
│ ▂ BLUE bar   KICKER · [THEORY] · ~12 min                   │  header
│ Heading (NAVY, 26pt)                                       │
├───────────────────────────────┬──────────────────────────┤
│ DEFINITION (lead line, bold)   │                          │
│ How it works:                  │        VISUAL            │
│  • mechanism point             │      (diagram / table)   │
│  • mechanism point             │                          │
│  • mechanism point             │                          │
├───────────────────────────────┴──────────────────────────┤
│ ┌─ 🌍 Real example ─┐ ┌─ ⚠️ Common trap ─┐ ┌─ 🎯 Exam answer ─┐ │  panel row
│ │ Daraz: …          │ │ "X means Y" — no,│ │ crisp written    │ │
│ │                   │ │ actually …       │ │ answer …         │ │
│ └───────────────────┘ └──────────────────┘ └──────────────────┘ │
│ 🧠 Hook: one-liner        🔑 term = def · term = def            │  footer band
└──────────────────────────────────────────────────────────┘
```

Rules:
- The three bottom **panels are colored cards** (BLUE example / CORAL trap / TEAL answer) so
  meaning is readable at a glance and survives PDF.
- If the panel row + columns won't fit ≥14 pt → use the two-slide pair (§4). Slide A = header +
  columns + visual; Slide B = the panels blown up larger + key terms.
- The 🧠 memory hook stays as a visible band (it already is), never notes-only.

### 6.4 In-class activity slide
Task + steps on the face. Expected answer / what it rehearses may be brief on-face; detailed
facilitation is the one legitimate notes use.

### 6.5 Quiz / check-for-understanding slide
Questions AND answers on the face (this is study material — students revise from the answers).
Mark correct options clearly (✅). Include the discussion prompt.

### 6.6 Summary slide (end of each session)
3 takeaways + "next session" — **on the face**, not buried in the last quiz's notes (current
decks hide the summary in notes; stop doing that — give each session a real summary slide).

### 6.7 Solved-problem slide (REQUIRED for procedural units)
For anything procedural — SQL, relational algebra, normalization, ER-to-table mapping — a
definition is not enough; students learn by watching a problem worked. Use a **Problem → numbered
steps (with the reasoning shown) → Answer** layout. Include at least one capstone solved problem
per unit that synthesises the whole unit. Concept units (like ER) should still carry one capstone
solved problem that ties the concepts together.

### 6.8 Unit roadmap slide (near the front)
A "where am I" slide listing all sessions of the unit, with the current batch highlighted and the
rest greyed as upcoming. Gives the PDF reader a map and reinforces how the pieces connect.

### 6.9 End-of-unit cheat sheet + glossary
- **Cheat sheet:** one dense slide of compact reference blocks/tables (every rule, ratio, and
  signature in one place) — what students revise from the night before an exam.
- **Glossary:** the per-concept 🔑 key terms collected into a two-column reference at unit end.

### 6.10 Slide numbers & navigation (all slides)
Every slide carries a **slide number** (auto-contrast: light on dark backgrounds, grey on light),
added in a final pass so numbering stays correct as slides are inserted. Kickers already carry the
session/concept, so a separate running footer is optional — never let a footer collide with
bottom-edge content (hook bands, key-term cards).

---

## 7. Visualization standard

**Prefer a picture/table over prose whenever a relationship is spatial, comparative, sequential,
or hierarchical.** We already generate diagrams as PNGs via `build_unitX_images.py` (matplotlib).

Reach for a visual when the content is:
- **Comparison** → two-column table or side-by-side cards (e.g. data vs functional requirements).
- **Process / pipeline** → left-to-right arrow flow (e.g. Requirements→Conceptual→Logical→Physical).
- **Hierarchy / classification** → tree (e.g. attribute types).
- **Structure / relationship** → the domain diagram (e.g. Chen ER diagrams).
- **Before/after or right/wrong** → paired panels.

Rules:
- Every diagram must have **on-image labels** (they survive PDF; a caption in notes does not).
- Keep one visual style across the course: same fonts, same palette as §5, generous whitespace,
  no chart-junk.
- A visual supplements the text; it does not replace the required definition/answer.

---

## 7A. Depth through tables — MANDATORY (the "no abstraction without instances" rule)

> Learned from a real gap: a generated IT 246 deck stated each idea as 4–6 abstract bullets and
> stopped; the lecturer had to hand-add 10 tables (~89 example rows) to make Session 1 teachable.
> See `sixth/GAP_ANALYSIS_Unit1.md`. That work is now a rule, not an option.

**Abstraction alone is a defect. Every concept must be grounded in concrete, contrasted,
localised instances — and the correct form for that is almost always a table.** A student reading
the flat PDF must see enough real cases to *recognise the concept in the wild*, not just recite its
definition. When you write a concept, ask "what table makes this concrete?" and build it.

The four required table types (use whichever fit the concept; most concepts need at least one):

1. **Comparison table** — REQUIRED whenever ≥3 related/confusable terms are taught by contrast
   (ethics/morals/law/etiquette; 1NF/2NF/3NF/BCNF; theta/equi/natural join; centralized vs
   client/server). Put the terms as rows and the **shared dimensions as columns** (e.g. meaning ·
   source · who decides · consequence · example). **Never** teach a confusable set as parallel
   bullet lists — that is the exact anti-pattern this rule bans.
2. **Concrete-example table** — REQUIRED for every "X vs not-X" idea (ethical vs unethical, legal vs
   illegal, lossless vs lossy). Give **≥6 rows** of real instances, **localised to Nepal / IT** where
   possible, and add a **consequence/benefit column** where it adds meaning (law → penalty,
   etiquette → social cost, ethical practice → business benefit).
3. **Scaffolding table** — any claim of the form "involves many parties / two forces / several
   parts" gets a table that enumerates them (stakeholders → what they want; short-term profit vs
   long-term trust). Don't assert a breakdown in prose — show it.
4. **Payoff table** — where a concept motivates behaviour, show the concrete return
   (practice → benefit; good design → anomaly avoided).

Rules for tables:
- Tables are **generated, never hand-pasted.** Author them in `build_unitX_images.py` (rendered PNG)
  or via the shared pptx table helper in `deckkit.py` — one engine, `add_table_slide()`, with the
  semantic aliases `add_comparison_table()` / `add_examples_table()` (use whichever reads clearest at
  the call site; both auto-paginate onto their own slides). So they live in the build and can be
  regenerated. A deck that needed manual table-pasting has failed this standard.
- Tables live **on the slide face** (they are load-bearing study content — never notes-only).
- Long example tables may span two slides or scroll; keep body text ≥ 12 pt (§3) — split rather than shrink.
- **Label concepts to match the material's concept list** — never collapse a distinct concept into a
  bare "Diagram" slide (that hides that a concept is being taught).

**Depth test (run per concept):** *If a student who skipped the lecture can't point to concrete
examples of this concept after reading the slide, it is too abstract — add the table.*

---

## 8. Teaching techniques — rotate, don't default to bullets

Do not teach every concept the same "definition + 3 bullets" way. Pick the technique that fits
the concept, and vary it across a session so the deck has rhythm:

- **Feynman** — explain as if to a smart 18-year-old who's never heard the term; no unexplained jargon.
- **Analogy / dual-coding** — pair each abstract idea with an everyday one (food, money, sport, social media) *and* a picture.
- **Compare & contrast** — put two confusable things in a table (type vs set, weak vs strong, total vs partial).
- **Worked example** — walk one real scenario end to end, showing the reasoning, not just the result.
- **Misconception-first ("common trap")** — state the wrong belief students hold, then correct it.
- **Concrete → abstract** — start from a system they use (eSewa), then name the general principle.
- **Decision aid** — a small "if this → then that" rule or mini decision tree (e.g. M:N → junction table).
- **Retrieval practice** — quick questions *with answers shown*, so revision is active.
- **Spaced callback** — explicitly link back to a prior session's idea ("this is schema vs instance from S2, at the ER level").
- **Scenario / story** — a 2–3 sentence situation students can reason about (the 🔮 hypotheticals in the material — put them on the face, not just notes).

Localise every example (Nepal / South Asia) and, where useful, add one global example too.

---

## 9. Per-session skeleton (50 min)

Keep the timing model, but ensure **every part leaves a visible slide**:

1. **Divider + hook** — hook question visible on the face `[~5 min]`.
2. **Concept slides** — one concept per slide or per two-slide pair, each fully self-contained `[~35 min]`.
3. **In-class activity** — task + steps on the face `[~5 min]`.
4. **Quiz / check** — questions + answers on the face `[~5 min]`.
5. **Real-life application** — "this matters because…" as a visible line/panel `[~3 min]`.
6. **Summary slide** — 3 takeaways + next session, on its own slide `[~2 min]`.

Pace tags `[THEORY] [EXAMPLE] [ACTIVITY] [QUIZ]` go in the kicker line (visible), not just notes.

---

## 10. Source pipeline & file conventions (don't break these)

Per unit, per semester folder:
1. `IT###_session_plan.md` — week/session plan (planning only).
2. `UnitN_content_outline.md` — the content map (what fills each slot).
3. `UnitN_material.md` — **full lecturer + student material** (already self-contained; this is the
   source of truth for *content*). Slides are built FROM this.
4. `build_unitN_images.py` — generates diagram PNGs into `images/`.
5. `build_unitN_pptx.py` — builds `IT###_UnitN.pptx` from the material.

Naming: `s{session}_{concept}.png` for images (e.g. `s6_attributes.png`).

**Output path:** the build script's `prs.save(...)` path must point at the *current* repo
location. (Note: existing scripts hardcode `/Users/inventechg1/Desktop/2083_SEM/...` — update
to the actual path, `/Users/rshah/Documents/2083_SEM/...`, or derive it relative to the script.)

**Build → verify loop:** after building, sanity-check slide count and spot-check that no required
element (§2) ended up notes-only.

---

## 11. Pre-ship checklist (run for every deck)

- [ ] **Golden rule:** mentally delete all speaker notes — slides still teach the full concept?
- [ ] Every concept has: definition, mechanism, real example, misconception, 🎯 exam answer, 🧠 hook — **on the face**.
- [ ] Visuals have on-image labels; comparisons/processes/hierarchies are drawn, not just described.
- [ ] **Depth (§7A):** every confusable set is a comparison table; every "X vs not-X" concept has a
      concrete-example table (≥6 localised rows, + consequence/benefit column); claims have scaffolding
      tables; tables are generated (not hand-pasted) and on the slide face.
- [ ] **Depth test:** no concept is left abstract — a student can point to concrete examples from the face.
- [ ] All body text ≥ 14 pt; nothing crammed below the legibility floor (else split into a pair).
- [ ] Each session has a visible **summary slide** and a visible **hook**.
- [ ] Quiz slides show the **answers**.
- [ ] Palette, fonts, and slide-type themes match §5 (looks like the same course).
- [ ] Examples localised (Nepal / South Asia); global example added where helpful.
- [ ] Teaching technique varies across the session (not all "definition + bullets").
- [ ] `prs.save()` path is correct for this machine.

---

## 12. Editing & uniformity

- Small text fix → edit the material `.md` and the build script's block; rebuild.
- New example → follow the existing situation→action→result shape and the local-context rule.
- Restructure for time → cut to self-study, keep the self-contained requirement for whatever stays.
- **Never** introduce a new visual style, palette, or slide type without updating §5/§6 here first.

---

## 13. Reference implementation

`fourth/build_unit2_pptx.py` → `fourth/IT220_Unit2.pptx` is the **canonical example** of this
standard. It builds each concept as a two-slide pair (`concept_understand` + `concept_apply`),
puts the real example / common trap / exam-ready answer / key terms in colored `_card` panels on
the slide face, shows the hook on divider slides, gives every session a real summary slide, and
keeps speaker notes to timing cues only. **Copy its helpers and structure** when building any new
deck rather than reinventing the layout. Content is distilled from `fourth/Unit2_material.md`.

The **S9–S12 batch** (`fourth/build_unit2b_pptx.py` → `IT220_Unit2b.pptx`, from
`fourth/Unit2b_material.md` + `fourth/build_unit2b_images.py`) completes Unit 2 and adds the
`add_reference` helper (a full-width slide for the notation legend) and a `compact` mode on
`add_quiz` for dense consolidated-revision slides. Diagrams are generated with matplotlib into
`images/` before the deck is built.

---

## 14. Rollout & scope (what is done, what still needs depth)

The depth rule (§7A) and the self-contained standard apply to **every deck in this repo — IT 220
(fourth) and IT 246 (sixth)**. Status and marching orders:

### IT 220 (fourth)
- **Units 1–4 are DONE and FROZEN — do not touch them.** They were rebuilt to the self-contained
  standard (`IT220_Unit1.pptx`, `IT220_Unit2.pptx`, `IT220_Unit2b.pptx`, `IT220_Unit3.pptx`,
  `IT220_Unit4.pptx`). Leave these decks, their `build_*` scripts, and their `images/` as they are
  unless the user explicitly asks for a change.
- **Units 5–7 (and anything built from here on) MUST include the §7A depth tables** in addition to
  everything else in this standard.

### IT 246 (sixth)
- **Rebuild from the start (Unit 1 onward).** The existing sixth decks predate this standard
  (terse bullets, notes-heavy, zero tables). Every unit is to be regenerated to the full standard
  **including §7A depth tables**, using the same pipeline and helpers as the rebuilt IT 220 units.
- Unit 1 is the reference rebuild for sixth; then Units 2–9 one at a time.

### Everywhere, going forward
- New material is not "done" until it passes the §11 checklist, **including the two depth lines.**
- Import the shared toolkit `deckkit.py` (`from deckkit import *`) rather than copy-pasting helpers,
  and reuse its generated table helpers (`add_table_slide()` / its aliases `add_comparison_table()` /
  `add_examples_table()`) so depth tables are never hand-pasted again (the failure documented in
  `sixth/GAP_ANALYSIS_Unit1.md`).

---

*Last updated: 2026-07-08. Keep this file current — it governs every future deck.*
