# Unit 4 — Database Normalization · Content Outline

**4 LHs → 4 sessions (S18–S21) · 50 min each**
This is the *content map* — what will fill each slot before we generate full material.
Local examples use Nepal / South Asia. Review and tell me what to swap.

> Template per session (from the guide):
> Opening hook (5m) → Content sections (35m) → Check for understanding (5m) →
> Real-life application (3m) → Summary & takeaways (2m), with speaker notes + visual cues.

> **Running example used across S18–S21** (one table students follow the whole unit):
> `ENROLL(StudentRoll, StudentName, StudentPhone[multi], CourseCode, CourseTitle, InstructorID, InstructorName, InstructorDept, Grade)`
> A single "everything in one table" college enrollment sheet — deliberately full of redundancy.
> We anomaly-hunt it in S18, then decompose it step-by-step 1NF → 2NF → 3NF → BCNF → 4NF across S19–S21.

---

## Unit 4 learning outcomes (what students can do after S18–S21)
1. Explain the informal design guidelines for good relational schemas and identify insertion, deletion, and update anomalies in a bad design.
2. Define and detect functional dependencies (FDs) and the keys they imply.
3. Apply 1NF, 2NF, and 3NF to decompose a table, step by step, with justification.
4. Define BCNF and distinguish it from 3NF; recognise multivalued dependencies and apply 4NF.
5. State and check the two correctness properties of a decomposition: lossless join and dependency preservation.

---

## S18 — Informal Design Guidelines & Functional Dependencies

**Hook:** "Here's one giant spreadsheet a college uses to track enrollments. A student changes their phone number — and we have to edit it in 11 rows. Miss one, and the database now 'believes' two different phone numbers. What went wrong?" → bad design breeds anomalies.

**Concepts & how each will be filled:**

1. **What makes a schema 'good' (informal guidelines)**
   - Definition: design goals — clear semantics per relation, minimal redundancy, few nulls, no spurious tuples on join.
   - Theory bullets: each relation should represent one "thing"; don't mix entities; avoid storing the same fact twice.
   - Global example: keeping `Customer` and `Order` info crammed into one table vs. split.
   - Local example: the all-in-one `ENROLL` sheet above from a Kathmandu college — student, course, and instructor facts jammed together.
   - Misconception: *"Fewer tables = simpler = better."* Correction: fewer tables often means more redundancy and more anomalies.

2. **Redundancy and the three anomalies**
   - Definition: anomaly = an update problem caused by redundant storage.
   - Insertion anomaly: can't add a new course (CourseCode, CourseTitle) until a student enrolls in it — course detail has nowhere to live.
   - Deletion anomaly: the last student dropping a course erases the course/instructor facts entirely.
   - Update anomaly: instructor changes department → must update every row; partial update = inconsistent data.
   - Local example: in `ENROLL`, "Instructor Sharma moves from CSIT to BIM dept" must be fixed in dozens of rows.
   - Mini case: eSewa stores a merchant's commission rate copied into every transaction row; the rate changes → which rows are now wrong?
   - Fun analogy: writing your home address on every page of a 200-page notebook — move house and you re-write 200 pages.

3. **Functional Dependency (FD)**
   - Definition: X → Y means "if you know X, you know exactly one Y." X *determines* Y.
   - Theory bullets: read as "determines"; FDs come from real-world rules, not from current data; trivial vs non-trivial FD.
   - Global example: `ISBN → BookTitle`.
   - Local example (from `ENROLL`): `StudentRoll → StudentName`; `CourseCode → CourseTitle`; `InstructorID → InstructorName, InstructorDept`; `{StudentRoll, CourseCode} → Grade`.
   - Misconception: *"X → Y means Y → X too."* Correction: FDs are one-directional (Roll determines Name; Name does not determine Roll — two students named "Anish").
   - Fun analogy: national ID number → person; the number pins down exactly one citizen, but a name doesn't.

4. **Keys via FDs (link back to keys)**
   - Definition: a key is an attribute set that functionally determines *every* attribute; candidate key = minimal such set.
   - Local example: in `ENROLL`, the key is `{StudentRoll, CourseCode}` — together they determine Grade and (transitively) everything else.
   - Bridge note: these FDs are the raw material for every normal form coming next.

**Check for understanding:**
- MCQ1: Being unable to add a new course because no student has enrolled yet is which anomaly? (a) update (b) insertion ✅ (c) deletion (d) join
- MCQ2: `CourseCode → CourseTitle` means: (a) titles determine codes (b) each code maps to exactly one title ✅ (c) codes are unique rows (d) nothing
- Discussion: "Find one FD that holds in your own college's marksheet, and one pair of columns where neither determines the other."

**Real-life application:** every time a Nepali fintech (Khalti, eSewa) or e-commerce (Daraz) team designs a new feature table, spotting FDs and anomalies *first* is what prevents data corruption later.

**Summary:** (1) good schemas minimise redundancy; (2) redundancy causes insertion/deletion/update anomalies; (3) FDs (X → Y) formalise the rules and reveal keys. **Next:** turning these FDs into formal normal forms, starting with 1NF.

**Visual cues:** the messy `ENROLL` table on screen with redundant cells highlighted; three callout boxes (insert/delete/update anomaly) pointing at specific rows; an arrow diagram of the FDs. Mark slides [THEORY]/[EXAMPLE].

---

## S19 — Normal Forms Based on Primary Keys · First Normal Form (1NF)

**Hook:** "One cell in our enrollment sheet says StudentPhone = '9801, 9842, 9818'. Is that one value or three? Can you query 'who has number 9842'? This single fat cell is why 1NF exists."

**Concepts & how each will be filled:**

1. **Normalization & normal forms — the idea**
   - Definition: normalization = a stepwise process of refining tables to reduce redundancy/anomalies, judged against FDs and keys.
   - Theory bullets: normal forms are a ladder (1NF ⊂ 2NF ⊂ 3NF ⊂ BCNF); each fixes a specific class of anomaly; based on the primary key.
   - Misconception: *"Normalization is one big action."* Correction: it's incremental — you climb one rung at a time.
   - Fun analogy: decluttering a room one drawer at a time, not all at once.

2. **First Normal Form (1NF)**
   - Definition: every attribute holds a single, atomic value; no repeating groups, no multivalued cells, no nested tables.
   - Theory bullets: each cell = one value; each row identified by the key; no "list inside a cell."
   - Global example: an `Orders` table with a comma-separated `Items` column → violates 1NF.
   - Local example (running): `StudentPhone = '9801,9842,9818'` and repeating `Course1, Course2, Course3` columns both break 1NF.
   - Mini case: Nagarik App storing a citizen's multiple documents in one text field — can't validate or search them individually.
   - Misconception: *"1NF just means no duplicate rows."* Correction: 1NF is about atomic values + no repeating groups, not row uniqueness.

3. **Fixing to 1NF (first decomposition step)**
   - How: split multivalued/repeating data into separate rows or a separate table.
   - Local example: pull phones into `STUDENT_PHONE(StudentRoll, Phone)`; flatten course columns into one row per (Roll, CourseCode).
   - Result table now in 1NF: `ENROLL_1NF(StudentRoll, StudentName, CourseCode, CourseTitle, InstructorID, InstructorName, InstructorDept, Grade)` with key `{StudentRoll, CourseCode}`.
   - Note to flag: 1NF removed fat cells but redundancy still remains — sets up S20.

**Check for understanding:**
- MCQ1: A column storing "9801, 9842, 9818" violates which normal form? → 1NF ✅
- MCQ2: 1NF primarily requires: (a) no redundancy (b) atomic single-valued attributes ✅ (c) one table only (d) a foreign key
- Discussion: "Look at any online form you've filled (eSewa registration, college admission). Find a field that would be a 1NF violation if dumped into one column."

**Real-life application:** REST APIs and CSV exports break the moment a field secretly holds a list — 1NF discipline is what keeps Daraz product attributes queryable and filterable.

**Summary:** (1) normalization is a step-by-step ladder; (2) 1NF demands atomic values and no repeating groups; (3) we split the running table into 1NF but redundancy remains. **Next:** 2NF and 3NF — attacking the redundancy that 1NF left behind.

**Visual cues:** before/after of the multivalued phone cell; "1NF checklist" badge; show the running table transitioning to `ENROLL_1NF`. Mark [THEORY]/[EXAMPLE].

---

## S20 — Second (2NF) and Third (3NF) Normal Forms

**Hook:** "Our 1NF table has key `{StudentRoll, CourseCode}`. But `StudentName` depends only on `StudentRoll` — half the key. And `InstructorDept` depends on `InstructorID`, not the key at all. These two 'wrong dependencies' are exactly what 2NF and 3NF kill."

**Concepts & how each will be filled:**

1. **Partial dependency & Second Normal Form (2NF)**
   - Definition: 2NF = is in 1NF AND no non-key attribute depends on only *part* of a composite key (no partial dependency).
   - Theory bullets: only matters when the key is composite; remove partial FDs into their own table.
   - Local example (running): in `ENROLL_1NF`, `StudentRoll → StudentName` and `CourseCode → CourseTitle` are partial dependencies on key `{StudentRoll, CourseCode}`.
   - Decomposition: split into `STUDENT(StudentRoll, StudentName)`, `COURSE(CourseCode, CourseTitle, InstructorID, InstructorName, InstructorDept)`, `ENROLL(StudentRoll, CourseCode, Grade)`.
   - Misconception: *"Every table must reach 2NF separately."* Correction: a table with a single-attribute key is automatically in 2NF.
   - Fun analogy: a shared grocery bill where some items belong to only one roommate — split them out so nobody pays for what isn't theirs.

2. **Transitive dependency & Third Normal Form (3NF)**
   - Definition: 3NF = is in 2NF AND no non-key attribute depends on another non-key attribute (no transitive dependency through a non-key).
   - Theory bullets: kills "key → non-key → non-key" chains.
   - Local example (running): in the `COURSE` table, `CourseCode → InstructorID → InstructorName, InstructorDept` is transitive; instructor facts repeat for every course they teach.
   - Decomposition: split into `COURSE(CourseCode, CourseTitle, InstructorID)` and `INSTRUCTOR(InstructorID, InstructorName, InstructorDept)`.
   - Mini case: a Khalti `Transaction` table storing `MerchantID → MerchantCity → CityRegion`; region repeats everywhere until you break the chain.
   - Misconception: *"3NF means absolutely no redundancy ever."* Correction: 3NF removes the common transitive redundancy, but a few odd cases survive — that's why BCNF exists (preview).

3. **The fully decomposed design (running example payoff)**
   - Final 3NF set: `STUDENT(StudentRoll, StudentName)`, `STUDENT_PHONE(StudentRoll, Phone)`, `COURSE(CourseCode, CourseTitle, InstructorID)`, `INSTRUCTOR(InstructorID, InstructorName, InstructorDept)`, `ENROLL(StudentRoll, CourseCode, Grade)`.
   - Re-check the S18 anomalies: each one is now gone (add a course with no students ✓, drop last student without losing course ✓, change instructor dept in one place ✓).

**Check for understanding:**
- MCQ1: A non-key attribute depending on only part of a composite key is a: (a) transitive dependency (b) partial dependency ✅ (c) multivalued dependency (d) trivial FD
- MCQ2: `CourseCode → InstructorID → InstructorDept` is an example of a ____ dependency, fixed by 3NF. → transitive ✅
- Discussion: "Take the final 5-table design and re-run the 'instructor changes department' update. How many rows change now, and why is that better?"

**Real-life application:** this exact 1NF→2NF→3NF split is the everyday schema review on any Nepali product team — it's what keeps a user's profile, their orders, and merchant data from corrupting each other.

**Summary:** (1) 2NF removes partial dependencies on a composite key; (2) 3NF removes transitive dependencies through non-key attributes; (3) the running table is now anomaly-free across five clean tables. **Next:** the stricter BCNF, plus multivalued dependencies/4NF and how to know a decomposition was *safe*.

**Visual cues:** color-code each FD (partial = red, transitive = orange) on the table; an animated split tree showing 1NF → 2NF → 3NF; the "anomalies eliminated" checklist re-shown with all three ticked. Mark [THEORY]/[EXAMPLE].

---

## S21 — BCNF · Multivalued Dependency & 4NF · Properties of Decomposition (closes Unit 4)

**Hook:** "Our 3NF design looks clean — but here's a course where every section is taught in a fixed room, and we still get a weird repeating glitch. 3NF says it's fine; reality says it isn't. Welcome to BCNF — and to knowing when a split is actually *safe*."

**Concepts & how each will be filled:**

1. **Boyce-Codd Normal Form (BCNF)**
   - Definition: for every non-trivial FD X → Y in the table, X must be a superkey. (Stricter than 3NF.)
   - Theory bullets: BCNF is 3NF with no exceptions for prime attributes; 3NF allowed a determinant that wasn't a superkey, BCNF doesn't.
   - Local example: `SECTION(CourseCode, Instructor, Room)` where each instructor uses one fixed room (`Instructor → Room`) but `Instructor` isn't a superkey → 3NF-OK but BCNF-violating; decompose into `(Instructor, Room)` and `(CourseCode, Instructor)`.
   - Misconception: *"3NF and BCNF are the same."* Correction: they're equal *most* of the time, but differ when there are overlapping candidate keys / a non-superkey determinant.
   - Fun analogy: 3NF is the building code that's "good enough"; BCNF is the strict inspector who flags the one corner everyone else ignored.

2. **Multivalued Dependency (MVD) & Fourth Normal Form (4NF)**
   - Definition: MVD X ↠ Y = for each X, a *set* of independent Y values exists, independent of the other attributes; 4NF = in BCNF with no non-trivial MVD (unless X is a superkey).
   - Theory bullets: MVDs cause a multiplying "cartesian product" redundancy even when there's no FD problem.
   - Local example: `STUDENT_ACTIVITY(StudentRoll, Course, Hobby)` — a student's courses and hobbies are independent, so every course pairs with every hobby → rows explode. Split into `(StudentRoll, Course)` and `(StudentRoll, Hobby)`.
   - Local twist: link back to `STUDENT_PHONE` — multiple phones AND multiple emails in one table would be the classic 4NF violation.
   - Misconception: *"4NF is the same as 1NF since both are about multiple values."* Correction: 1NF bans lists *in a cell*; 4NF bans independent multivalued facts *combined in one table*.

3. **Properties of relational decomposition**
   - Lossless (non-additive) join: re-joining the decomposed tables gives back exactly the original — no fewer, no spurious extra rows.
   - Theory bullets: a binary decomposition is lossless if the shared attribute is a key of at least one resulting table.
   - Local example: `STUDENT ⋈ ENROLL` on `StudentRoll` reconstructs the original cleanly (lossless); a careless split that loses the link produces *spurious tuples*.
   - Dependency preservation: every original FD can still be enforced without re-joining tables.
   - Mini case: a decomposition that is lossless but *not* dependency-preserving — the trade-off when forcing BCNF; sometimes 3NF is kept on purpose to preserve a dependency.
   - Misconception: *"Any split into smaller tables is safe."* Correction: a bad split is lossy (spurious tuples on join) — losslessness must be verified, not assumed.
   - Fun analogy: tearing a photo in two and taping it back — lossless means you get the exact photo back, not a blurry overlap.

4. **Unit 4 synthesis**
   - One slide: anomalies → FDs → 1NF → 2NF → 3NF → BCNF → 4NF, with the running `ENROLL` example shown at each rung, plus "is this decomposition lossless & dependency-preserving?" as the final gate.

**Check for understanding:**
- MCQ1: A table is in 3NF but a non-superkey determines another attribute. It violates: (a) 1NF (b) 2NF (c) BCNF ✅ (d) nothing
- MCQ2: Re-joining decomposed tables produces extra, incorrect rows. The decomposition is: (a) lossless (b) lossy / has spurious tuples ✅ (c) dependency-preserving (d) in 4NF
- Discussion: "Give a real example where independent multivalued facts (e.g. a person's multiple phones and multiple skills) would blow up into redundant rows, and how you'd 4NF-split it."

**Real-life application:** when a Nepali bank or telecom (Ntc/Ncell) audits its database before a migration, the litmus test is exactly this — are tables in (at least) 3NF/BCNF, and is every historical split lossless so no records were silently duplicated or lost?

**Summary:** (1) BCNF tightens 3NF so every determinant is a superkey; (2) 4NF removes independent multivalued redundancy beyond BCNF; (3) a good decomposition must be lossless and ideally dependency-preserving. **Next unit:** putting designed schemas to work with SQL (Unit 5).

**Visual cues:** the BCNF counterexample side-by-side with its fix; an MVD "row explosion" grid (courses × hobbies); a lossless vs lossy join animation showing spurious tuples appearing; the full normal-form ladder as the closing diagram. Mark [THEORY]/[EXAMPLE].

---

## END-OF-UNIT QUIZ — Unit 4: Database Normalization

> Consolidated assessment covering S18–S21. Suggested: 10 MCQs + 3 short-answer + 1 applied decomposition task. Correct MCQ answers marked ✅.

### Part A — Multiple Choice (10)
1. Being unable to record a new course until a student enrolls is a/an: (a) update anomaly (b) insertion anomaly ✅ (c) deletion anomaly (d) join anomaly
2. `InstructorID → InstructorName` is best described as a: (a) multivalued dependency (b) functional dependency ✅ (c) transitive key (d) foreign key
3. A candidate key is a minimal attribute set that: (a) has no nulls (b) functionally determines all attributes ✅ (c) is the first column (d) is indexed
4. A column storing "9801,9842,9818" violates: (a) 1NF ✅ (b) 2NF (c) 3NF (d) BCNF
5. 2NF is only at risk when the table has a: (a) single-column key (b) composite/multi-attribute key ✅ (c) foreign key (d) null value
6. `CourseCode → InstructorID → InstructorDept` is a: (a) partial dependency (b) transitive dependency ✅ (c) trivial FD (d) MVD
7. BCNF requires that for every non-trivial FD X → Y, X is a: (a) prime attribute (b) superkey ✅ (c) foreign key (d) single column
8. Independent multivalued facts (courses and hobbies) crammed in one table violate: (a) 1NF (b) 2NF (c) 3NF (d) 4NF ✅
9. A decomposition that produces spurious tuples when re-joined is: (a) lossless (b) lossy ✅ (c) dependency-preserving (d) in BCNF
10. The property that lets every original FD be checked without re-joining is: (a) lossless join (b) dependency preservation ✅ (c) atomicity (d) minimality

### Part B — Short Answer (3)
1. List the three anomalies and give a one-line example of each from a single "all-in-one" enrollment table.
2. Explain the difference between a partial dependency and a transitive dependency, naming the normal form that removes each.
3. Why can a decomposition be lossless but *not* dependency-preserving? State the practical trade-off (BCNF vs 3NF).

### Part C — Applied Task (1)
Given the un-normalized table
`ENROLL(StudentRoll, StudentName, StudentPhone[multi], CourseCode, CourseTitle, InstructorID, InstructorName, InstructorDept, Grade)`:
1. Write the functional (and any multivalued) dependencies.
2. Identify the primary key.
3. Decompose it step by step to BCNF/4NF, showing the table set at each stage (1NF → 2NF → 3NF → BCNF/4NF).
4. Confirm your final decomposition is lossless and state whether it is dependency-preserving.

### Answer-key note (for instructor)
Full worked solution to Part C = the running `ENROLL` example threaded through S18–S21; final design:
`STUDENT(StudentRoll, StudentName)`, `STUDENT_PHONE(StudentRoll, Phone)`, `COURSE(CourseCode, CourseTitle, InstructorID)`, `INSTRUCTOR(InstructorID, InstructorName, InstructorDept)`, `ENROLL(StudentRoll, CourseCode, Grade)`.

---

## Open questions before I generate Unit 4 material
1. Keep the single running `ENROLL` example threaded through all four sessions, or use a fresh table per session?
2. Is the **BCNF counterexample** (`Instructor → Room`) the right level of difficulty, or should I pick a simpler/Nepal-specific one?
3. End-of-unit quiz size — is **10 MCQ + 3 short + 1 applied** right, or do you want it shorter/longer?
4. Keep speaker notes + visual/diagram cues inline (for PPT), or trim to lean markdown?
