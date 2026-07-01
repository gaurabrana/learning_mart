# Unit 3 — The Relational Algebra & Relational Calculus · Content Outline

**5 LHs → 5 sessions (S13–S17) · 50 min each**
This is the *content map* — what will fill each slot before we generate full material.
Local examples use Nepal / South Asia. Review and tell me what to swap.

> Template per session (from the guide):
> Opening hook (5m) → Content sections (35m) → Check for understanding (5m) →
> Real-life application (3m) → Summary & takeaways (2m), with speaker notes + visual cues.

---

## Unit 3 learning outcomes (what students can do after S13–S17)
1. Explain what relational algebra is and why it is the *procedural* foundation of query languages like SQL.
2. Apply the unary operations SELECT (σ) and PROJECT (π) to filter rows and pick columns.
3. Apply the set-theory operations UNION, INTERSECTION, DIFFERENCE, and CARTESIAN PRODUCT (with union-compatibility rules).
4. Apply the binary operations JOIN (theta / equi / natural) and DIVISION, and combine operations into query expressions.
5. Use additional operations (aggregate / grouping, outer joins) and read & write queries in both Tuple Relational Calculus and Domain Relational Calculus (the *declarative* counterpart).

> **Running sample relations used throughout Unit 3** (kept tiny on purpose):
> `Student(sid, name, program, city)` · `Enrollment(sid, course, grade)` · `Course(course, credit)` · `Instructor(iid, name, dept)`
> Reused across S13–S17 so students track *the same data* through every operation.

---

## S13 — Introduction to Relational Algebra · Unary Operations: SELECT (σ) & PROJECT (π)

**Hook:** "When you search 'students from Pokhara with grade A' on the college portal, the system is silently doing two tiny operations — pick the right *rows*, then keep only the *columns* you asked for. Today we name them." → σ and π.

**Concepts & how each will be filled:**

1. **What relational algebra is**
   - Definition: a formal, *procedural* language — a set of operations that take relation(s) as input and produce a relation as output.
   - Theory bullets: closure property (output is always a relation, so operations chain); it is the theoretical basis of SQL; "procedural" = you specify *how* (step by step) vs calculus's *what*.
   - Global example: any SQL `SELECT` query is internally translated into a relational-algebra expression by the optimizer.
   - Local example: the eSewa transaction-history screen = a chain of relational-algebra steps over a Transactions relation.
   - Misconception: *"Relational algebra is just SQL."* Correction: SQL is a real query language; relational algebra is the underlying math — closed-form, no duplicates by definition, no display formatting.
   - Fun analogy: operations are LEGO bricks — each takes a table and snaps onto the next.

2. **SELECT (σ) — choosing rows**
   - Definition: σ_<condition>(R) returns the tuples of R that satisfy the condition (horizontal filter).
   - Theory bullets: condition uses =, ≠, <, >, ≤, ≥ and AND/OR/NOT; result has the *same schema* as R; degree unchanged, cardinality ≤ original.
   - Global example: σ_{grade='A'}(Enrollment).
   - Local example (on sample data): σ_{city='Pokhara'}(Student) → only the Pokhara students.
   - Mini case: a college wants "all students in BIM program who are from Kathmandu" → σ_{program='BIM' AND city='Kathmandu'}(Student).
   - Misconception: *"SELECT picks columns."* Correction: in relational algebra σ picks ROWS — confusingly, SQL's keyword `SELECT` does the column job (π). Flag this naming trap explicitly.

3. **PROJECT (π) — choosing columns**
   - Definition: π_<attribute list>(R) keeps only the listed columns (vertical filter) and removes the rest.
   - Theory bullets: result schema = only listed attributes; **duplicate rows are automatically removed** (relations are sets); degree decreases.
   - Global example: π_{name, program}(Student).
   - Local example: π_{name}(σ_{city='Pokhara'}(Student)) → just the names of Pokhara students (composition of σ then π).
   - Mini case: Daraz wants a mailing list — only customer names + districts, no order details → projection onto two columns; duplicates collapse so a repeat customer appears once.
   - Misconception: *"π keeps duplicate rows like SQL does."* Correction: pure relational algebra removes duplicates automatically; SQL needs `DISTINCT`.

4. **Composing σ and π (sequences & renaming preview)**
   - Order matters for readability/efficiency: filter rows first (σ) then trim columns (π) is the common pattern.
   - Tease the rename operator (ρ) — needed later for self-joins; full treatment in S15.

**Check for understanding:**
- MCQ1: Which operation reduces the number of *columns*? (a) σ (b) π ✅ (c) UNION (d) JOIN
- MCQ2: σ_{credit>3}(Course) changes which of these? (a) the schema (b) the number of rows ✅ (c) the column names (d) nothing
- Discussion: "Open any app on your phone with a filter (Daraz price filter, eSewa date filter). Which part is σ and which is π?"

**Real-life application:** every "search + show selected fields" feature (college result lookup, Khalti transaction filter) is σ then π — the two most-used operations in all of querying.

**Summary:** (1) relational algebra = procedural, closed operations over relations; (2) σ filters rows by condition; (3) π keeps chosen columns and drops duplicates. **Next:** treating whole relations as *sets* — UNION, INTERSECTION, DIFFERENCE, CARTESIAN PRODUCT.

**Visual cues:** show the `Student` table, then animate σ shading rows and π shading columns; side-by-side "σ = horizontal cut / π = vertical cut" diagram; a callout box on the SQL-`SELECT`-vs-σ naming trap. Mark slides [THEORY]/[EXAMPLE].

---

## S14 — Relational Algebra Operations from Set Theory (UNION, INTERSECTION, DIFFERENCE, CARTESIAN PRODUCT)

**Hook:** "A college merges its morning and day-shift student lists for a single notice. How do you combine two tables without listing anyone twice — and what if their columns don't match?" → set operations + union compatibility.

**Concepts & how each will be filled:**

1. **Union compatibility (the gatekeeper rule)**
   - Definition: two relations are union-compatible if they have the same number of attributes and matching domains (column-by-column).
   - Theory bullets: required for UNION, INTERSECTION, DIFFERENCE (NOT for Cartesian product); column *names* can differ, domains must align.
   - Local example: `MorningStudents(sid, name)` and `DayStudents(sid, name)` are compatible; `Student(sid,name,program,city)` and `Course(course,credit)` are not.
   - Misconception: *"Any two tables can be UNIONed."* Correction: they must be union-compatible first.

2. **UNION (∪)**
   - Definition: R ∪ S = all tuples in R or S (duplicates removed).
   - Global example: customers who used a coupon ∪ customers who used cashback.
   - Local example: MorningStudents ∪ DayStudents → one deduplicated student list.
   - Mini case: Ntc prepaid users ∪ Ntc postpaid users = all Ntc subscribers, each counted once.

3. **INTERSECTION (∩)**
   - Definition: R ∩ S = tuples present in *both*.
   - Local example: students enrolled in 'DBMS' ∩ students enrolled in 'Java' → those taking both.
   - Mini case: people who have *both* an eSewa and a Khalti account (overlap analysis).

4. **SET DIFFERENCE (−)**
   - Definition: R − S = tuples in R but not in S; **not commutative** (R−S ≠ S−R).
   - Local example: AllStudents − GraduatedStudents → currently active students.
   - Misconception: *"Difference works both ways like subtraction-as-distance."* Correction: order matters — emphasize with a concrete flip.

5. **CARTESIAN PRODUCT (×)**
   - Definition: R × S pairs *every* tuple of R with *every* tuple of S; result degree = sum, cardinality = product.
   - Theory bullets: usually meaningless alone, produces huge results; becomes useful only when followed by σ — which is exactly a JOIN (bridge to S15).
   - Local example: Student × Course on the tiny tables → show the row-count explosion (e.g. 4 students × 3 courses = 12 rows), most pairings nonsensical.
   - Misconception: *"Cartesian product combines related rows."* Correction: it blindly pairs everything; relating them needs a following condition.
   - Fun analogy: × is like inviting every student to dance with every course — the matchmaking (meaningful pairing) only happens when you add a condition.

**Check for understanding:**
- MCQ1: Which operation does NOT require union compatibility? (a) UNION (b) INTERSECTION (c) CARTESIAN PRODUCT ✅ (d) DIFFERENCE
- MCQ2: If R has 5 rows and S has 4 rows, R × S has how many rows? → 20 ✅
- Discussion: "Give a real Nepali example where you'd want INTERSECTION (overlap) vs DIFFERENCE (what's missing)."

**Real-life application:** merging mailing lists (UNION), finding common customers across eSewa/Khalti (INTERSECTION), and finding lapsed users = all-users − active-users (DIFFERENCE) are everyday analytics tasks.

**Summary:** (1) UNION/INTERSECTION/DIFFERENCE need union-compatible relations; (2) DIFFERENCE is order-sensitive; (3) CARTESIAN PRODUCT pairs everything and is the raw material for JOIN. **Next:** adding a condition to × to get meaningful matches — the JOIN, plus DIVISION.

**Visual cues:** Venn diagrams for ∪/∩/− over two student lists; an animated × showing the grid of all pairings ballooning; a compatibility-check checklist box.

---

## S15 — Binary Operations: JOIN (theta / equi / natural) & DIVISION

**Hook:** "Your marksheet shows the course *name* and your *grade* together — but those two facts live in two different tables. What stitches them into one row?" → JOIN.

**Concepts & how each will be filled:**

1. **From Cartesian product to JOIN**
   - Definition: a JOIN = CARTESIAN PRODUCT followed by a SELECT on a matching condition (R ⋈_condition S).
   - Theory bullets: avoids the meaningless pairings of ×; keeps only rows that satisfy the join condition.
   - Recap bridge from S14's Student × Course to motivate it.

2. **Theta join (⋈_θ)**
   - Definition: join on any comparison condition θ (=, <, >, ≤, ≥, ≠).
   - Global example: ⋈ where Salary > MinWage on two relations.
   - Local example: pair students with scholarship slabs where marks ≥ slab_threshold.

3. **Equijoin**
   - Definition: a theta join whose condition uses only equality (=).
   - Local example: Student ⋈_{Student.sid = Enrollment.sid} Enrollment → each student matched to their enrollments; the join column appears twice.
   - Misconception: *"Equijoin removes the duplicate matching column."* Correction: equijoin keeps BOTH columns; only the natural join removes the duplicate.

4. **Natural join (⋈)**
   - Definition: equijoin on all attributes with the *same name*, then automatically removes the duplicate column.
   - Local example: Student ⋈ Enrollment (joining automatically on `sid`) → clean combined table with one `sid`. Then π_{name, course, grade} to produce a marksheet row.
   - Misconception: *"Natural join matches by column position."* Correction: it matches by identical attribute *names* — a renamed/mismatched column silently breaks the join or turns it into a Cartesian product.
   - Fun analogy: natural join = a zipper — teeth (matching `sid`) line up and merge into one.

5. **DIVISION (÷)**
   - Definition: R ÷ S returns tuples in R associated with *all* tuples in S — the "for all" operation.
   - Theory bullets: used for "find X related to every Y" queries; hardest operation conceptually, so anchor it in one strong example.
   - Local example: "Which students are enrolled in *all* core BIM courses?" → Enrollment(sid, course) ÷ CoreCourses(course).
   - Mini case: "Which delivery riders have covered *every* district in the valley?" (Daraz/Pathao-style) → Coverage(rider, district) ÷ ValleyDistricts(district).
   - Misconception: *"Division finds students in ANY of the courses."* Correction: it's *ALL* (universal), not *any* (existential) — contrast with a simple σ/JOIN.

**Check for understanding:**
- MCQ1: Which join automatically drops the duplicate join column? (a) theta (b) equijoin (c) natural join ✅ (d) Cartesian product
- MCQ2: "Students enrolled in every core course" is best expressed with → DIVISION ✅
- Discussion: "Describe a real 'must match ALL of them' situation (e.g. a rider covering all districts, a student passing all subjects) — that's division."

**Real-life application:** joins build every report that combines tables — a bank statement (account ⋈ transactions), a Daraz invoice (order ⋈ product ⋈ customer); division powers "qualified for all requirements" checks (eligible for graduation, completed all KYC steps).

**Summary:** (1) JOIN = × + condition; (2) theta → equi → natural is a narrowing family, natural join removes the duplicate column; (3) DIVISION answers "related to ALL of a set." **Next:** operations beyond pure algebra — aggregates, grouping, outer joins — and the *declarative* world of Tuple Relational Calculus.

**Visual cues:** animation morphing Student × Course → JOIN (rows dropping away); "zipper" graphic for natural join; a worked DIVISION grid showing which sid survives because it matched every required course.

---

## S16 — Additional Relational Operations (Aggregate, Outer Join, etc.) · Intro to Tuple Relational Calculus

**Hook:** "Relational algebra so far can't answer 'what's the *average* grade?' or keep a student who enrolled in *nothing*. We need a few extra tools — and a totally different way of asking questions." → aggregates, outer joins, then calculus.

**Concepts & how each will be filled:**

1. **Aggregate functions & grouping (ℱ)**
   - Definition: ℱ (script F) applies COUNT, SUM, AVG, MAX, MIN, optionally grouped by attributes: <grouping attrs> ℱ <function list>(R).
   - Theory bullets: not expressible in the basic 6 operations — added as an extension; grouping partitions then aggregates per group.
   - Global example: AVG(grade) over Enrollment.
   - Local example: program ℱ COUNT(sid)(Student) → number of students per program; course ℱ AVG(grade)(Enrollment) → average grade per course.
   - Mini case: eSewa: merchant ℱ SUM(amount)(Transactions) → total collected per merchant.
   - Misconception: *"Aggregate is one of the basic relational operations."* Correction: it's an *additional/extended* operation; basic algebra has no built-in counting.

2. **Outer joins (⟕ ⟖ ⟗)**
   - Definition: keep unmatched tuples too, padding the missing side with NULLs. LEFT (⟕) keeps all left rows, RIGHT (⟖) all right rows, FULL (⟗) both.
   - Theory bullets: contrast with inner (natural/theta) join which DROPS unmatched rows.
   - Local example: Student ⟕ Enrollment → keeps a newly-admitted student who hasn't enrolled in any course yet (grade columns = NULL).
   - Mini case: a bank report listing *every* account including those with zero transactions this month → LEFT outer join account ⟕ transactions.
   - Misconception: *"Inner join shows everyone."* Correction: inner join silently hides rows with no match — outer join is needed to keep them.

3. **Other additional operations (brief)**
   - Outer union (combining partially-compatible relations); generalized projection (computed columns). One line each — mention, don't drill.

4. **Tuple Relational Calculus (TRC) — declarative thinking**
   - Definition: a *non-procedural* / declarative language — you describe *what* tuples you want, not *how* to get them. Form: { t | COND(t) }.
   - Theory bullets: t is a tuple variable ranging over a relation; uses predicates and quantifiers ∃ (there exists) and ∀ (for all); same expressive power as relational algebra (relational completeness).
   - Global example: { t | t ∈ Student AND t.city = 'Pokhara' } → equivalent to S13's σ.
   - Local example: { t.name | t ∈ Student AND t.program = 'BIM' } → names of BIM students (declarative version of π∘σ).
   - Mini case: "students who are enrolled in at least one course" using ∃: { t | t ∈ Student AND ∃ e (e ∈ Enrollment AND e.sid = t.sid) }.
   - Misconception: *"Calculus and algebra give different answers."* Correction: they're equivalent in power — algebra says HOW, calculus says WHAT; same result set.
   - Fun analogy: algebra = giving turn-by-turn driving directions; calculus = telling the taxi the destination address and letting it figure out the route.

**Check for understanding:**
- MCQ1: Which keeps students who enrolled in NO course? (a) natural join (b) equijoin (c) LEFT outer join ✅ (d) division
- MCQ2: Tuple relational calculus is best described as → declarative / non-procedural ✅
- Discussion: "Phrase one query about your college in plain English, then say whether you described HOW (algebra) or WHAT (calculus)."

**Real-life application:** dashboards live on aggregates (total sales per merchant on Khalti, students per program); outer joins build "include everyone, even the inactive" reports; declarative thinking is exactly how you reason in SQL day-to-day.

**Summary:** (1) aggregates/grouping add counting & summarizing; (2) outer joins keep unmatched rows with NULLs; (3) TRC describes *what* you want using tuple variables and quantifiers, equal in power to algebra. **Next:** the second calculus — Domain Relational Calculus — which closes the unit.

**Visual cues:** group-and-aggregate table (raw Enrollment → grouped averages); inner-vs-outer join diagram with NULL padding highlighted; a split "HOW vs WHAT" slide pairing one algebra expression with its TRC twin.

---

## S17 — The Domain Relational Calculus (closes Unit 3)

**Hook:** "Yesterday we asked for whole *tuples*. Today we go one level finer — we name a variable for each *column value* and describe the answer field by field. Same power, different feel." → DRC.

**Concepts & how each will be filled:**

1. **Domain Relational Calculus (DRC) — the idea**
   - Definition: a declarative calculus where variables range over *domains* (individual attribute values) rather than whole tuples. Form: { <x1, x2, ..., xn> | COND(x1, ..., xn) }.
   - Theory bullets: each xi is a domain variable bound to a column; uses ∃ and ∀; basis of the QBE (Query-By-Example) interface; relationally complete (= algebra = TRC).
   - Global example: { <n> | ∃ s, c, p ( <s, n, p, c> ∈ Student AND c = 'Pokhara') } → names of Pokhara students.
   - Local example (on sample data): { <n, p> | ∃ s, c ( <s, n, p, c> ∈ Student ) } → name + program of every student (DRC version of π).
   - Mini case: "names of students enrolled in 'DBMS'": { <n> | ∃ s, p, c ( <s,n,p,c> ∈ Student AND ∃ g ( <s,'DBMS',g> ∈ Enrollment ) ) }.

2. **TRC vs DRC — the key contrast**
   - Tuple variable ranges over rows (`t.name`); domain variable ranges over column values (a separate variable per attribute).
   - Theory bullets: DRC names every attribute explicitly in the angle-bracket list → more verbose but maps directly onto QBE-style "fill in the blanks" tools.
   - Misconception: *"DRC and TRC are the same thing with different symbols."* Correction: the variable's *scope* differs — whole tuple vs single value; show the same query both ways side by side.
   - Fun analogy: TRC hands you a whole form (the tuple); DRC hands you the individual blanks (the fields) to fill.

3. **Safety of expressions (both calculi)**
   - Definition: a calculus expression is *safe* if it produces a finite result drawn from the database values (no infinite/unbounded answers).
   - Local example: { <x> | NOT(<x> ∈ Student) } is *unsafe* — infinitely many values aren't students; contrast with a properly bounded query.
   - Misconception: *"Any condition you can write is a valid query."* Correction: unsafe expressions are disallowed because they'd return infinite results.

4. **Unit 3 synthesis**
   - One slide tying it together: algebra (procedural: σ, π, set ops, JOIN, DIVISION, aggregates, outer joins) ⇄ calculus (declarative: TRC over tuples, DRC over domains) → all relationally equivalent → all underlie SQL (Unit 5).
   - Tease forward: in Unit 5, SQL gives a practical, friendly syntax for everything formalized here.

**Check for understanding:**
- MCQ1: In domain relational calculus, variables range over → individual attribute values / domains ✅
- MCQ2: An expression that would return an infinite set of values is called → unsafe ✅
- Discussion: "Why might a non-programmer find DRC-style 'fill in the blank' (QBE) easier than writing algebra? Where have you seen fill-in-the-blank query forms?"

**Real-life application:** Query-By-Example interfaces (the visual 'fill the columns' query builders in tools like MS Access / report designers used in many Nepali offices and banks) are DRC made visual; understanding it demystifies those drag-and-fill report tools.

**Summary:** (1) DRC uses one variable per column and describes the answer field-by-field; (2) TRC vs DRC differ in variable scope, not power; (3) safe expressions only — and algebra, TRC, DRC are all equivalent and all feed SQL. **Next unit:** putting good *structure* under all this — Database Normalization (Unit 4).

**Visual cues:** the same query shown three ways (algebra / TRC / DRC) stacked for comparison; a QBE-style grid screenshot mapped onto DRC variables; a closing "Unit 3 map" graphic linking procedural ⇄ declarative ⇄ SQL.

---

## END-OF-UNIT QUIZ — Unit 3 (consolidated)

> Use after S17 as a review/assessment. Mix of recall + application. Correct answers marked ✅.
> Suggested: 12 MCQs + 4 short-answer/expression-writing + 2 discussion. Spread across all five sessions.

### Part A — Multiple Choice (12)
1. Relational algebra is best described as a ______ query language. (a) declarative (b) procedural ✅ (c) graphical (d) natural
2. Which operation selects ROWS based on a condition? (a) π (b) σ ✅ (c) ∪ (d) ÷
3. The PROJECT (π) operation automatically removes ______ from its result. (a) NULLs (b) columns (c) duplicate rows ✅ (d) conditions
4. Which set operation does NOT require union compatibility? (a) ∪ (b) ∩ (c) − (d) × ✅
5. R has 6 rows, S has 5 rows. R × S has ______ rows. → 30 ✅
6. SET DIFFERENCE (R − S) is: (a) commutative (b) not commutative ✅ (c) the same as ∩ (d) always empty
7. A JOIN is equivalent to a Cartesian product followed by a ______. (a) PROJECT (b) UNION (c) SELECT ✅ (d) DIVISION
8. Which join removes the duplicate matching column automatically? (a) theta (b) equijoin (c) natural join ✅ (d) outer
9. The query "students enrolled in ALL core courses" is expressed with → DIVISION (÷) ✅
10. To keep students who enrolled in NO course, use a → LEFT OUTER JOIN ✅
11. In TUPLE relational calculus, a variable ranges over → whole tuples (rows) ✅
12. In DOMAIN relational calculus, a variable ranges over → single attribute values (domains) ✅

### Part B — Short answer / write the expression (4)
Use the sample relations `Student(sid,name,program,city)`, `Enrollment(sid,course,grade)`, `Course(course,credit)`.
13. Write a relational-algebra expression for "names of students from Kathmandu." → π_{name}(σ_{city='Kathmandu'}(Student)) ✅
14. Write an expression producing each student's name with their course and grade. → π_{name,course,grade}(Student ⋈ Enrollment) ✅
15. Express "average grade per course." → course ℱ AVG(grade)(Enrollment) ✅
16. Write the TRC for "names of students in the 'BIM' program." → { t.name | t ∈ Student AND t.program = 'BIM' } ✅

### Part C — Discussion / applied (2)
17. Take one Nepali app (eSewa, Khalti, Daraz, a college portal). Pick one screen and decompose it into relational-algebra operations (which σ, π, JOIN, aggregate is happening?).
18. Explain in your own words why relational algebra (HOW) and relational calculus (WHAT) always give the same answer, and why SQL needed both ideas behind it.

---

## Open questions before I generate Unit 3 material
1. Keep the single running schema (`Student / Enrollment / Course / Instructor`) across all 5 sessions, or use a fresh themed dataset per session?
2. How heavy should the **DIVISION** and **calculus quantifier (∃/∀)** treatment be for a no-prior-DB audience — full worked grids, or lighter intuition-first?
3. Are the **Nepali examples** here the right set (eSewa/Khalti/Daraz/Ntc/Ncell/bank/college/QBE-in-MS-Access), or swap any?
4. Quiz scope — is the **per-session 2 MCQ + 1 discussion PLUS the consolidated end-of-unit quiz** the right amount, or trim one?
5. Should I keep inline **speaker notes + visual cues** (PPT-ready) or produce a leaner version?
