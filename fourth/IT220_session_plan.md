# IT 220: Database Management System — Session Plan

**Program:** BIM, 4th Semester · **Credits:** 3 · **Lecture Hours:** 48
**Session length:** 50 min · **Cadence:** 3 sessions/week → **16 teaching weeks**
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

## Laboratory & project track (runs in parallel)

| Phase | Aligns with | Lab focus |
|-------|-------------|-----------|
| Lab 1 | Weeks 8–9 | `CREATE DATABASE`/`TABLE`, data types, constraints, `INSERT` |
| Lab 2 | Week 10 | `SELECT` queries: filtering, ordering, aggregates, `NULL` handling |
| Lab 3 | Week 11 | Subqueries, views, `UPDATE`/`DELETE` |
| Lab 4 | Week 12 | Joins, stored procedures, triggers, indexing |
| **Project** | Weeks 5–16 | Design (ER → relational → normalized schema) then implement in SQL. Individual or groups of ≤4. Present in S48. |

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
