# IT 220: Database Management System — Session Plan

**Program:** BIM, 4th Semester · **Credits:** 3 · **Lecture Hours:** 48
**Session length:** 50 min · **Cadence:** 3 lecture sessions/week **+ 1 practical session/week** → **16 teaching weeks**
*(The weekly practical is a separate 4th session; it does not consume the 48 lecture hours.)*
**Local-example context:** Nepal / South Asia

> Planning document only — no slide content yet. Once we approve this structure, we generate
> full session material one unit at a time (markdown first, then convert to PPT/PDF).

---

## Lecture-hour budget (sanity check)

| Unit | Title | LHs | Sessions |
|------|-------|-----|----------|
| 1 | Database Concepts and Architecture | 4 | 4 |
| 2 | Data Modelling: ER Model & Relational Model | 8 | 8 |
| 3 | Relational Algebra and Relational Calculus | 5 | 5 |
| 4 | Database Normalization | 4 | 4 |
| 5 | SQL | 15 | 15 |
| 6 | Transaction Processing, Concurrency Control & Recovery | 8 | 8 |
| 7 | Advanced Topics | 4 | 4 |
| — | **Total** | **48** | **48** |

48 sessions ÷ 3/week = **16 weeks** (last week has buffer/review built in).

---

## Week-by-week plan

### Week 1 — Unit 1: Database Concepts & Architecture (4 LHs)
- **S1** Database, DBMS, database users, DBA; advantages of databases over file systems
- **S2** Data models, schemas, instances; Three-Schema Architecture & data independence
- **S3** Database languages & interfaces; the database system environment

### Week 2 — Unit 1 → Unit 2
- **S4** Centralized vs Client/Server architectures; classification of DBMSs *(closes Unit 1)*
- **S5** *(Unit 2)* High-level conceptual data models; database design process
- **S6** Entity types, entity sets, attributes, keys

### Week 3 — Unit 2: ER & Relational Model
- **S7** Relationship types, sets, roles; structural constraints
- **S8** Weak entity types
- **S9** ER diagrams: naming conventions & design issues

### Week 4 — Unit 2 (cont.)
- **S10** Relationship types of degree higher than two
- **S11** Specialization & Generalization; their constraints & characteristics
- **S12** Converting ER diagrams to tables *(closes Unit 2)*

### Week 5 — Unit 3: Relational Algebra & Calculus (5 LHs)
- **S13** Intro to relational algebra; unary ops: SELECT and PROJECT
- **S14** Relational algebra operations from set theory (∪, ∩, −, ×)
- **S15** Binary ops: JOIN and DIVISION

### Week 6 — Unit 3 → Unit 4
- **S16** Additional relational operations; intro to Tuple Relational Calculus
- **S17** Domain Relational Calculus *(closes Unit 3)*
- **S18** *(Unit 4)* Informal design guidelines for relational schemas; functional dependencies

### Week 7 — Unit 4: Normalization (4 LHs)
- **S19** Normal forms based on primary keys; 1NF
- **S20** 2NF and 3NF
- **S21** BCNF; multivalued dependency & 4NF; properties of relational decomposition *(closes Unit 4)*

### Week 8 — Unit 5: SQL begins (15 LHs) — **midterm checkpoint**
- **S22** DDL & data types; specifying constraints; domain types; schema definition
- **S23** DML — `SELECT`, `WHERE`, `FROM` clauses
- **S24** Rename operation; tuple variables; string operations

### Week 9 — Unit 5 (cont.)
- **S25** Ordering display of tuples; duplicate tuples; set operations
- **S26** Aggregate functions
- **S27** `NULL` values and their behaviour

### Week 10 — Unit 5 (cont.)
- **S28** Nested subqueries: set membership, set comparison
- **S29** Nested subqueries: test for empty relations, absence of duplicates
- **S30** Derived relations; Views

### Week 11 — Unit 5 (cont.)
- **S31** Database modification: deletion, insertion, updates
- **S32** Update of a view
- **S33** Joined relations: join types & conditions

### Week 12 — Unit 5 close → Unit 6
- **S34** Stored procedures (basic concepts)
- **S35** DML triggers; indexing
- **S36** **SQL recap + lab problem set walkthrough** *(closes Unit 5)*

### Week 13 — Unit 6: Transactions, Concurrency & Recovery (8 LHs)
- **S37** Intro to transaction processing; transaction & system concepts
- **S38** Desirable properties of transactions (ACID)
- **S39** Serializable schedules

### Week 14 — Unit 6 (cont.)
- **S40** Two-Phase Locking concurrency control
- **S41** Timestamp ordering concurrency control
- **S42** Recovery concepts; NO-UNDO/REDO recovery based on deferred update

### Week 15 — Unit 6 close → Unit 7
- **S43** Recovery based on immediate update; shadow paging
- **S44** Database backup & recovery from catastrophic failures *(closes Unit 6)*
- **S45** *(Unit 7)* Database performance tuning; database security

### Week 16 — Unit 7 + wrap-up (4 LHs)
- **S46** Parallel & distributed databases (concepts)
- **S47** Data warehousing, data mining, Big Data, NoSQL *(closes Unit 7)*
- **S48** **Course review + project presentations / final Q&A**

---

## Laboratory & project track — weekly practical (16 sessions, one per week)

> **This is a separate 4th session each week**, on top of the three 50-min lecture sessions — it
> does **not** consume the 48 lecture hours. Per the syllabus, the lab requires writing SQL
> (create/insert/update/delete/select) plus a project (individual or groups of ≤4).
>
> **Design rule 1 — a practical runs every week from Week 1, even before the theory it needs is
> taught.** SQL labs therefore begin in **Week 4**, four weeks before Unit 5 starts in lectures.
> Beginners follow exact steps first; by the time Unit 5 is taught they already recognise every
> statement.
>
> **Design rule 2 — the lab is hands-on SQL only.** Relational algebra, relational calculus and
> pen-and-paper normalization are notation and reasoning, not runnable work: they stay in the
> **lectures** (Units 3–4) and the theory exam, and were removed from the lab track in 2026-08.
> Lab 3 (design) is the only non-SQL practical, and exists because the project needs a schema
> before it can be built.
>
> **One running database — "Model College"** (students, teachers, courses, enrolments, fee
> payments) — is built up across all 16 labs and doubles as the project. Nepal/South-Asia context
> throughout.

| Week | Theory so far | Practical (L#) | Tools |
|------|---------------|----------------|-------|
| 1 | U1 intro | **L1 — Setup & first query:** install XAMPP; start MySQL + Apache; open phpMyAdmin; create `demo_shop`; run `SELECT *`, a column list, and a `WHERE` | XAMPP + phpMyAdmin |
| 2 | U1 (architecture) | **L2 — Inside the DBMS:** server→database→table→row; query `information_schema` (catalog/metadata); create a limited user; `SHOW GRANTS` | phpMyAdmin |
| 3 | U2 (ER) | **L3 — Database design:** entities/attributes/keys/cardinality; resolve the M:N into an `Enrolment` junction table with a composite key; draw all 5 tables; export PNG; write the schema *(only non-SQL lab)* | dbdiagram.io |
| 4 | U2 (ER→tables) | **L4 — DDL & constraints:** `CREATE DATABASE`/`TABLE` × 5, data types, PK/FK/NOT NULL/CHECK/DEFAULT; `SHOW TABLES`/`DESCRIBE`; **break three constraints on purpose** | phpMyAdmin |
| 5 | U3 (rel. algebra) | **L5 — INSERT:** populate all 5 tables, parents before children; named-column INSERT using DEFAULT; trigger an FK error deliberately | phpMyAdmin |
| 6 | U3 → U4 | **L6 — SELECT, WHERE, ORDER BY:** column lists, `AS`, AND/OR, `IN`, `BETWEEN`, `LIKE`, `ORDER BY` (two keys), `DISTINCT`, `LIMIT` | phpMyAdmin |
| 7 | U4 (normalization) | **L7 — Aggregates & grouping:** COUNT/SUM/AVG/MIN/MAX, `GROUP BY`, `HAVING`, WHERE-vs-HAVING, `IS NULL` vs `= NULL` | phpMyAdmin |
| 8 | U5 (DDL) | **L8 — JOINs:** INNER (2- and 3-table), LEFT JOIN, the LEFT-JOIN+`IS NULL` trick to find non-payers, self-join, JOIN + GROUP BY | phpMyAdmin |
| 9 | U5 (SELECT) | **L9 — Subqueries:** scalar subqueries, `IN`/`NOT IN`, `EXISTS`/`NOT EXISTS`, derived table in `FROM` | phpMyAdmin |
| 10 | U5 (subqueries/views) | **L10 — Views:** `CREATE VIEW`; a 4-table `enrolment_sheet`; views are live not copies; update **through** a simple view; joined views are read-only | phpMyAdmin |
| 11 | U5 (modify/joins) | **L11 — UPDATE & DELETE:** the SELECT→UPDATE→SELECT habit; update using the existing value; DELETE blocked by an FK; the no-`WHERE` disaster rescued by `ROLLBACK` | phpMyAdmin |
| 12 | U5 close | **L12 — Procedures, triggers, indexing:** a stored procedure (`IN` and `OUT`), a DML audit trigger, `CREATE INDEX` + `EXPLAIN` before/after — **SQL practical test** | phpMyAdmin |
| 13 | U6 (transactions) | **L13 — Transactions:** `START TRANSACTION`/`COMMIT`/`ROLLBACK`; a transaction that fails halfway proving atomicity; `SAVEPOINT` | phpMyAdmin |
| 14 | U6 (concurrency) | **L14 — Concurrency:** two sessions → one blocks on a locked row until COMMIT; a different row does *not* block; isolation levels; `SHOW PROCESSLIST` | phpMyAdmin (2 tabs) |
| 15 | U6 close / U7 | **L15 — Backup, recovery & security:** Export `.sql` → DROP → Import restore; `CREATE USER`, `GRANT`/`REVOKE`, `SHOW GRANTS` before/after; grant on a **view** only | phpMyAdmin |
| 16 | U7 + wrap-up | **L16 — Project demo:** present diagram → schema → build → data → queries → view/procedure/trigger/index → transaction → backup → limited user; run and modify queries live | project DBs |

**Project (Weeks 3–16):** carry the Model College database end-to-end — design (L3) → build (L4–L5)
→ query (L6–L10) → automate (L11–L12) → make it reliable (L13–L15) → demo (L16). Individual or
groups of ≤4; presented in S48.

---

## Assessment touchpoints (suggested)

- **Unit quizzes:** end of Units 1, 2, 4 (short MCQ/short-answer checks)
- **Midterm:** Week 8 — covers Units 1–4
- **SQL practical test:** Week 12 — hands-on querying
- **Final:** covers all units, SQL-heavy weighting
- **Project:** ER design + working database, demoed Week 16

---

## Learning outcomes by unit (for per-session prompts later)

- **U1** — Explain what a DBMS is and why it beats file-based storage; describe the three-schema architecture and DBMS classifications.
- **U2** — Model a real-world domain as an ER diagram and convert it to a normalized relational schema.
- **U3** — Express queries using relational algebra and relational calculus.
- **U4** — Identify functional dependencies and normalize schemas up to BCNF/4NF.
- **U5** — Write SQL for definition, manipulation, querying, views, procedures, triggers, and indexing.
- **U6** — Reason about ACID properties, concurrency control protocols, and recovery techniques.
- **U7** — Describe performance tuning, security, distributed/parallel DBs, warehousing, mining, Big Data, and NoSQL at a conceptual level.

---

## Suggested readings (from syllabus)

- Elmasri & Navathe — *Fundamentals of Database Systems*, 7th ed. (primary)
- Silberschatz, Korth & Sudarshan — *Database System Concepts*, 6th ed.
- Ramakrishnan & Gehrke — *Database Management Systems*, 3rd ed.
- Ullman & Widom — *A First Course in Database Systems*, 3rd ed.
- Özsu & Valduriez — *Principles of Distributed Database Systems*, 4th ed. (Unit 7)
- Fowler — *NoSQL for Dummies* (Unit 7)

---

## Next step

Approve this structure, then I'll generate full session material **one unit at a time** in
markdown (opening hook → content with Nepal/global examples + mini case studies →
check-for-understanding → real-life application → summary), using the guide's per-session
template. We convert approved units to PPT/PDF afterward.
