# Repo: University course material (slide decks + study material)

This repo builds lecture decks (`.pptx`) and study material for university courses, one folder
per semester:
- `fourth/` = **IT 220 Database Management System** (Units 1–4 done & frozen; 5–7 pending).
- `sixth/` = **IT 246 IT Ethics & Cybersecurity** (Units 1–4 done to standard; 5–9 pending).
- `eighth/` = **IT 250 Digital Economy** ⭐ **current focus / new semester** — 6 units, all pending.

A finished unit has: a content outline, a full `material.md` (source of truth), and image-builder +
pptx-builder Python scripts. **`eighth/` is at an earlier stage — it currently holds only raw lecture
PDFs/PPTX, so its first step per unit is extracting a content outline from those PDFs.** See
`PROJECT_STATUS.md` §0 for the current focus and the exact eighth-sem workflow.

## READ THIS FIRST — the governing standard

**Before generating or editing ANY course material, read and follow
[`COURSE_MATERIAL_STANDARD.md`](COURSE_MATERIAL_STANDARD.md).** It is the single source of truth
for slide content, layout, the visual system, and the workflow. It wins over any default habit.

**For current status / where to continue, read [`PROJECT_STATUS.md`](PROJECT_STATUS.md)** — it has
the per-unit status table, build conventions, known open gaps, and the recommended next action.

### The rules that matter most
1. **Self-contained slides.** A student reading a flat PDF with no teacher and no speaker notes
   must still fully learn the concept. Slides are study material, not presenter cue-cards. Many
   slides is fine; a slide that only makes sense with a teacher talking is not.
2. **PDF-Safety / golden rule.** PDF export drops speaker notes, so **nothing load-bearing may
   live only in notes** — definitions, examples, 🎯 exam answers, analogies, misconception
   corrections all go on the slide face. Notes hold only timing/delivery cues.
3. **Visualize** comparisons, processes, hierarchies, and structures (labels on the image).
3a. **Depth through tables (§7A) — mandatory.** No abstraction without concrete instances. Every
   confusable set → a comparison table; every "X vs not-X" concept → a concrete-example table
   (≥6 localised rows, + consequence/benefit column); claims → scaffolding tables. Tables are
   *generated*, never hand-pasted, and live on the slide face.
   **Scope (§14):** IT 220 (fourth) Units 1–4 are DONE — do not touch; Units 5–7 onward add depth.
   IT 246 (sixth) Units 1–4 done with depth; 5–9 pending. IT 250 (eighth) is the new build, all units
   to full depth. All new content must have §7A tables.
4. **Vary the teaching technique** (Feynman, analogy, compare/contrast, worked example,
   misconception-first, scenario) — don't default every concept to "definition + 3 bullets".
5. **Keep the shared visual system** (palette, fonts, slide types) so all decks look like one course.

Run the pre-ship checklist in the standard before declaring a deck done.

## Build
- Diagrams: `cd <sem> && python3 build_unitN_images.py` → PNGs in `<sem>/images/`.
- Deck: `python3 build_unitN_pptx.py` → `IT###_UnitN.pptx` (in the same folder).
- Content source of truth is `UnitN_material.md`; slides are built from it (and carry the same §7A tables).
- IT 246 (sixth) scripts share `sixth/deckkit.py` (`from deckkit import *`; `save("…")` writes relative to
  the script — no hardcoded paths). Copy `deckkit.py` into each new course folder (e.g. `eighth/`).
- Legacy IT 220 (fourth) scripts predate deckkit and carry their own copied helpers — leave them unless touched.
