# Gap Analysis & Rewrite Plan — IT 246 (sixth) Unit 1: An Overview of Ethics

**Compared:** `IT246_Unit1.pptx` (generated, 39 slides, 0 tables) vs `IT246_Unit1 2.pptx`
(your manually-enriched copy, 49 slides, 10 tables) · source `Unit1_material.md`.
**Method:** slide-by-slide text + table + notes extraction of both decks, aligned against the
source material and `COURSE_MATERIAL_STANDARD.md`.

---

## 1. Verdict in one line

The generated deck wasn't *wrong* — it was **too abstract and too sparse to study from**. You
filled the gap by hand with **10 comparison / concrete-example tables (~89 example rows)** in
Session 1. Every addition is exactly what the course standard now demands: **self-contained,
concrete, visualized-as-tables** content a student can learn from with no teacher. The sixth-sem
decks were built **before** `COURSE_MATERIAL_STANDARD.md` existed, so none of them have it yet.

---

## 2. What you added, slide by slide (Session 1)

You inserted 10 slides; all are tables. The generated deck had none.

| Your slide | Table added | Rows | Purpose it served |
|---|---|---|---|
| 5 | Ethics/Morals/Law/Etiquette × (Meaning, Source, Who decides, Consequence, Example) | 4 | Turned 4 abstract bullets into a **6-dimension comparison** |
| 6 | Ethical vs Unethical behaviour by profession (doctor, engineer, AI dev…) | 9 | Concrete grounding of "ethical vs unethical" |
| 7 | Ethical vs Unethical behaviour (more domains) | 11 | More coverage, incl. Nepal-relevant (bribery, nepotism) |
| 8 | Moral vs Immoral behaviour (personal-belief examples) | 15 | Made "morals" tangible |
| 9 | Lawful vs Illegal behaviour **+ consequence** | 15 | Made "law" tangible; added the penalty column |
| 10 | Good vs Poor Etiquette **+ consequence** | 15 | Made "etiquette" tangible |
| 11 | 4 concepts × (Main focus, Example question it answers) | 4 | A crisp **recall/summary** table |
| 14 | Stakeholders × what they want | 6 | The "many stakeholders conflict" claim, made concrete |
| 15 | Short-term profit vs long-term trust | 3 | The central tension, as a side-by-side |
| 16 | Ethical practice → business benefit | 7 | "Why ethics pays" — the payoff, concretely |

**Pattern:** every abstract claim in the generated deck ("law is enforced by the state",
"business serves many stakeholders", "profit vs trust") you re-expressed as a **table of concrete
instances**. That is the single consistent move.

---

## 3. The gaps, categorized

### Gap A — Depth / concreteness (the big one)
The generated slides stated each concept as **4–6 one-line bullets** and stopped. A student reading
the flat PDF gets the *definition* but not enough *instances* to actually recognise the concept in
the wild. You supplied ~89 worked instances. **Root issue: abstraction without enough examples.**

### Gap B — No comparison tables
The four core ideas (Ethics / Morals / Law / Etiquette) are *inherently comparative* — they're
taught by contrast. The generated deck listed them as separate bullets; you laid them side by side
across shared dimensions (source, who decides, consequence, example). A comparison **table** is the
correct visual form for confusable-set content, and it was missing.

### Gap C — Thin "how it works" scaffolding
Claims like "a business serves many stakeholders" and "profit vs trust" had **no supporting
breakdown**. You added the stakeholder table and the profit/trust table — the scaffolding that turns
a claim into something learnable.

### Gap D — Missing the "why it pays" payoff
The deck argued ethics matters but didn't show the concrete **benefit** side. Your ethical-practice
→ benefit table closes the "so what?" loop.

### Gap E — Style: predates the standard (structural)
The sixth decks use the **old** style: terse kicker + bullets, concept content leaning on speaker
notes, no self-contained "understand / apply" pairs, no on-face 🎯 exam answers / 🔑 key terms, no
page numbers, no cheat-sheet/glossary. Under `COURSE_MATERIAL_STANDARD.md` (written after these
decks), that's a fail on the **PDF-safety** and **self-contained** rules. The IT220 units already
rebuilt fix this; sixth has not been touched yet.

### Non-gap (worth noting)
No topic was actually dropped. The material's **Concept 2 (the Legal/Ethical 2×2 grid)** *is*
present — but it was mislabeled "S1 · Concept 1 · Diagram", which hides that a distinct concept is
being taught. Numbering/labelling should match the material's concept list.

---

## 4. Root cause

Two compounding causes:
1. **The generator optimised for slide-count brevity, not study-completeness.** It compressed rich
   material into minimal bullets — the exact anti-pattern the standard was later written to ban.
2. **These decks predate the standard.** They were built 14 Jun; `COURSE_MATERIAL_STANDARD.md` and
   the self-contained/table-rich pattern came afterward (and are already applied to IT220 Units 1–4).

Your manual edits are, in effect, a **worked specification** of what the rewrite must produce.

---

## 5. Lessons to fold into the standard

Your edits generalise into rules that should govern every future deck (add to
`COURSE_MATERIAL_STANDARD.md` §7 "Visualization"):

1. **Confusable sets → one comparison table.** Whenever ≥3 related terms are taught by contrast
   (ethics/morals/law/etiquette; 1NF/2NF/3NF; theta/equi/natural join), render a single table with
   the shared dimensions as columns — never parallel bullet lists.
2. **Every abstract concept earns a concrete-example table.** For each "X vs not-X" idea, give a
   table of real instances (≥6 rows, localised to Nepal where possible), plus a consequence column
   where it adds meaning (law → penalty, etiquette → social cost).
3. **Claims get scaffolding.** "Serves many stakeholders", "profit vs trust" → a table that
   enumerates the parties / the two sides.
4. **Show the payoff.** Where the concept motivates behaviour, add a practice → benefit table.
5. **Label concepts to match the material's concept list** (don't collapse a distinct concept into
   a "Diagram" slide).

---

## 6. Rewrite plan — sixth, starting with Unit 1

Bring IT 246 to the **same standard and pipeline** as the rebuilt IT220 units, *and* bake in your
table pattern. Deliverables per unit: enriched `UnitN_material.md` → `build_unitN_images.py`
(comparison/example tables + diagrams) → `build_unitN_pptx.py` (self-contained deck) → verify.

### 6.1 Unit 1 concretely (S1–S5)
For **each session**, produce self-contained understand/apply concept pairs **plus** the missing
tables. Minimum table set to author (S1 shown; replicate the pattern for S2–S5):

- **S1:** (a) 4-concept 6-dimension comparison table; (b) ethical-vs-unethical example table
  (≥10 rows, Nepal/IT-localised); (c) legal-vs-illegal + consequence; (d) etiquette good-vs-poor +
  consequence; (e) stakeholder table; (f) profit-vs-trust table; (g) ethical-practice → benefit
  table; (h) the Legal/Ethical 2×2 grid (keep — relabel as Concept 2). All on the slide face.
- **S2 (CSR):** Carroll's pyramid (already a diagram) + a **CSR-vs-greenwashing** example table +
  a stakeholder-expectations table.
- **S3 (Improving business ethics):** components-of-an-ethics-program table (component → what it does
  → example) + a "value vs enforceable rule" contrast table.
- **S4 (Ethical decision making):** the 5-step process as a numbered flow + the **four ethical
  lenses** as a comparison table (lens → question it asks → verdict on a shared scenario).
- **S5 (Ethics in IT):** an IT-specific ethical-issue table (issue → example → who's harmed →
  mitigation).

### 6.2 Apply the full standard while rewriting
- Two-slide **understand / apply** pairs; 🌍 example / ⚠️ trap / 🎯 exam-ready answer / 🔑 key terms
  **on the slide face** (not notes).
- Speaker notes = **timing/delivery only** (PDF-safe).
- Add **roadmap, per-session summary slides, cheat-sheet, glossary, page numbers** (as in IT220).
- Reuse the IT220 build helpers, and add a first-class **`add_comparison_table()` / `add_examples_table()`**
  helper so these tables are generated, not hand-pasted, next time.

### 6.3 Order of work
1. **Unit 1** (this analysis) — rebuild first; it's the reference for the pattern.
2. Units 2–9 of IT 246, one at a time (they already have content outlines; Units 1–2 also have full
   `material.md`).

### 6.4 Acceptance criteria (per session)
- [ ] Every confusable set is a comparison table (not parallel bullets).
- [ ] Every "X vs not-X" concept has a concrete-example table (≥6 rows, localised).
- [ ] Delete all speaker notes in your head → slides still teach fully.
- [ ] 🎯 exam answer + 🔑 key terms present on the face.
- [ ] Concept labels match `Unit1_material.md`'s concept list.
- [ ] Page numbers, summary slide, and unit cheat-sheet/glossary present.

---

## 7. Bottom line
Your manual Session-1 edits are the template: **replace abstraction with tables of concrete,
contrasted, localised examples.** The rewrite = (1) enrich the material with those tables for every
session, (2) convert the deck to the self-contained standard already proven on IT220, and (3) add a
reusable table-builder so this never has to be done by hand again. Recommend starting the rebuild
with **IT 246 Unit 1**.
