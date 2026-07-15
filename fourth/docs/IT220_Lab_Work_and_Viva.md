# IT 220 — Laboratory Work Record & Viva Question Set (Instructor Copy)
### Database Management System · BIM 4th Semester · MySQL/MariaDB (XAMPP + phpMyAdmin)

This is the **instructor/examiner** companion to the student docs. It lists every lab work, its tasks
and expected output, what the student must record, and the **viva questions with model answers**. It
maps 1:1 to the 16 weekly practicals in [IT220_session_plan.md](../IT220_session_plan.md) and to the
step-by-step [IT220_Lab_Manual.md](IT220_Lab_Manual.md).

- **Running project:** the **Himalaya College** database (students, teachers, courses, enrolments, fee
  payments) — one database built up across all 16 labs, and also the student's project.
- **Environment:** MySQL/MariaDB via **XAMPP**, driven through **phpMyAdmin**. Chosen because it is
  the gentlest on-ramp for absolute beginners (visual + SQL in one place, one installer).
- **Audience:** treat every student as a **complete beginner** — the manual assumes zero prior
  knowledge; assess understanding, not speed.

---

## How the lab record is kept and assessed

**Each lab-work entry in the student's report must contain:**
1. **Lab number & title**, date, student name/roll.
2. **Objective** (1–2 lines, student's own words).
3. **The SQL / diagram** they produced for that lab (just what's new).
4. **A screenshot of the working output** on their machine.
5. **Answers to that lab's viva questions.**

**Assessment (printed lab report + viva — adjust to your college's scheme):**
| Part | Weight | What it checks |
|---|---|---|
| Printed lab report (all 16 questions: SQL + screenshot + explanation) | 50% | Every lab documented with correct SQL and working screenshots |
| Viva voce (external + internal) on the report | 40% | Student can **explain their own SQL** — the anti-copying check |
| Regularity / attendance / sign-offs | 10% | Work done across the semester, not the night before |

> **The viva is the real test.** A document can be copied; a student who actually built the database
> can explain any query, and a copied report cannot. Point at a query in their report and ask them to
> read it aloud in plain English.

> **Zero-tolerance rule (state it up front):** an `UPDATE` or `DELETE` written without a `WHERE`
> clause in a graded query fails that lab work — it shows the student doesn't understand the danger.

---

## List of Lab Works (16) → weekly sessions

| Lab | Title | Week | Syllabus unit |
|-----|-------|------|----------------|
| 1 | Install XAMPP; first look at a database | 1 | U1 |
| 2 | Inside the DBMS: databases, catalog, users | 2 | U1 |
| 3 | ER diagram (dbdiagram.io) | 3 | U2 |
| 4 | ER → relational schema (keys, junction table) | 4 | U2 |
| 5 | Relational algebra (RelaX) | 5 | U3 |
| 6 | Relational calculus & spotting FDs | 6 | U3→U4 |
| 7 | Normalization 1NF→2NF→3NF | 7 | U4 |
| 8 | DDL: create tables + constraints + INSERT | 8 | U5 |
| 9 | SELECT, WHERE, aggregates, GROUP BY, HAVING | 9 | U5 |
| 10 | Subqueries & views | 10 | U5 |
| 11 | UPDATE/DELETE & JOINs | 11 | U5 |
| 12 | Stored procedures, triggers, indexing (**practical test**) | 12 | U5 |
| 13 | Transactions & ACID | 13 | U6 |
| 14 | Concurrency & locking | 14 | U6 |
| 15 | Backup, recovery & security (GRANT/REVOKE) | 15 | U6/U7 |
| 16 | Project demo + NoSQL comparison | 16 | U7 |

---

# Part 1 — Setup & Foundations

## Lab Work 1 — Install XAMPP & first look
**Objective:** Get a working database server and run one query.
**Tasks:** Install XAMPP; start MySQL + Apache; open phpMyAdmin; create the sample `demo_shop`; run
`SELECT * FROM product`.
**Expected output:** phpMyAdmin shows 3 product rows.
**Record:** screenshot of the running Control Panel + the query result.
**Viva (model answers):**
- *What is the difference between MySQL and phpMyAdmin?* → MySQL is the **database server** (does the
  real work); phpMyAdmin is just a **web interface** to click through it and run SQL.
- *What does `SELECT * FROM product` mean?* → "Return every column (`*`) of every row from the
  `product` table."
- *Why open phpMyAdmin at `http://localhost` and not a file?* → It's served by the local Apache web
  server; the database only answers through the server.

## Lab Work 2 — Inside the DBMS
**Objective:** Understand server→database→table→row, metadata, and users.
**Tasks:** Navigate the hierarchy; query `information_schema`; create user `college_clerk` with only
SELECT+INSERT on one database.
**Expected output:** metadata query returns `product`; limited user exists.
**Record:** screenshots of the `information_schema` result and the user's privileges.
**Viva:**
- *What is metadata / the data dictionary?* → "Data about the data" — the DBMS's own catalog of every
  database, table, and column (`information_schema`).
- *What does a DBA do here?* → Manages users and grants each only the privileges they need.
- *Relate this to the three-schema architecture.* → Physical storage (internal), the logical tables
  (conceptual), and per-user views/permissions (external) are separated.

## Lab Work 3 — ER diagram
**Objective:** Model the domain before building.
**Tasks:** Identify entities/attributes/keys; draw the diagram in dbdiagram.io; export PNG.
**Expected output:** a diagram with 4–5 entities and their relationships.
**Record:** the exported diagram.
**Viva:**
- *Entity vs attribute?* → Entity = a thing we store (Student); attribute = a fact about it (name).
- *Which relationship is many-to-many and how do you know?* → Student↔Course: one student takes many
  courses **and** one course has many students.
- *What is cardinality?* → How many of one entity relate to the other (1:1, 1:N, M:N).

## Lab Work 4 — ER → relational schema
**Objective:** Convert the diagram to tables with keys.
**Tasks:** Resolve the M:N into an `Enrolment` junction table with a composite key; write the full
schema with PK/FK.
**Expected output:** 5-table schema; diagram updated.
**Record:** the written schema + updated diagram.
**Viva:**
- *What is a foreign key?* → A column referencing another table's primary key; it enforces a valid
  relationship (e.g. `Enrolment.roll_no` must be a real `Student`).
- *Why a junction table?* → A many-to-many relationship can't fit in either table; the junction stores
  the pairs.
- *What is a composite primary key?* → A key made of two columns together (roll_no + course_code),
  unique as a pair.

## Lab Work 5 — Relational algebra
**Objective:** Perform σ, π, ⋈ and set operations.
**Tasks:** Run SELECT, PROJECT, JOIN in RelaX; map each to English.
**Expected output:** correct result relations.
**Record:** screenshots of σ, π, ⋈ results.
**Viva:**
- *What does SELECT (σ) do vs PROJECT (π)?* → σ picks **rows**; π picks **columns**.
- *What does JOIN (⋈) do?* → Combines two relations on matching attribute values.
- *How does this relate to SQL?* → `SELECT cols FROM t WHERE cond` is π over σ; SQL `JOIN` is ⋈.

## Lab Work 6 — Relational calculus & FDs
**Objective:** Express a query declaratively; identify functional dependencies.
**Tasks:** Write a tuple-calculus expression; list FDs in the messy table.
**Expected output:** correct FD list (roll_no→name, course_code→title, etc.).
**Record:** the calculus expression + FD list.
**Viva:**
- *Algebra vs calculus?* → Algebra says **how** (step-by-step operations); calculus says **what** (a
  description of the result).
- *What is a functional dependency?* → `X → Y`: knowing X always determines Y.
- *Why do repeated values (Programming/Ram Sir) signal a problem?* → Redundancy → update anomalies;
  normalization fixes it.

## Lab Work 7 — Normalization
**Objective:** Normalize to 3NF with reasoning.
**Tasks:** Take the messy table 1NF→2NF→3NF; justify each split.
**Expected output:** Student/Teacher/Course/Enrolment (matches Lab 4).
**Record:** the step-by-step normalization.
**Viva:**
- *What does 2NF remove?* → Partial dependencies (attributes depending on only part of a composite
  key).
- *What does 3NF remove?* → Transitive dependencies (a non-key attribute depending on another non-key
  attribute).
- *Why normalize at all?* → To remove redundancy and insert/update/delete anomalies.

---

# Part 2 — Building & Querying

## Lab Work 8 — DDL & constraints
**Objective:** Build the schema in SQL with constraints, then INSERT.
**Tasks:** `CREATE DATABASE` + 5 tables with PK/FK/NOT NULL/CHECK/DEFAULT; insert sample rows in the
right order.
**Expected output:** 5 populated tables.
**Record:** the CREATE script + a screenshot of the table list + a SELECT.
**Viva:**
- *What is DDL vs DML?* → DDL defines structure (`CREATE`/`ALTER`/`DROP`); DML changes data
  (`INSERT`/`UPDATE`/`DELETE`/`SELECT`).
- *Why did the FK insert order matter?* → A child row (Enrolment) needs its parent (Student/Course) to
  already exist.
- *What does a CHECK constraint do?* → Rejects values outside a rule (semester 1–8).

## Lab Work 9 — Querying
**Objective:** Filter, sort, summarise.
**Tasks:** WHERE; ORDER BY; DISTINCT; COUNT/AVG/MAX; GROUP BY; HAVING; IS NULL.
**Expected output:** correct summaries (e.g. count per semester).
**Record:** screenshots of a WHERE, a GROUP BY, and a HAVING query.
**Viva:**
- *WHERE vs HAVING?* → WHERE filters **rows before** grouping; HAVING filters **groups after**.
- *What does an aggregate function do?* → Collapses many rows into one value (COUNT, SUM, AVG…).
- *Why `IS NULL` not `= NULL`?* → NULL means "unknown" and is never equal to anything, including NULL.

## Lab Work 10 — Subqueries & views
**Objective:** Nest a query; save a query as a view.
**Tasks:** `IN`/`NOT IN`/`EXISTS` subqueries; `CREATE VIEW paid_students`.
**Expected output:** correct students; view queryable.
**Record:** subquery results + the view result.
**Viva:**
- *What is a subquery?* → A query whose result feeds an outer query.
- *Table vs view?* → A table stores data; a view is a **saved query** that computes its rows on demand.
- *Give a use for a view.* → Simplify complex joins, or expose limited columns to a restricted user.

## Lab Work 11 — Modification & joins
**Objective:** Change data safely; join tables.
**Tasks:** INSERT/UPDATE/DELETE with WHERE; INNER JOIN; LEFT JOIN.
**Expected output:** correct joined results.
**Record:** the UPDATE + both joins.
**Viva:**
- *Why is `UPDATE` without `WHERE` dangerous?* → It changes **every** row.
- *INNER vs LEFT JOIN?* → INNER keeps only matching rows; LEFT keeps all left-table rows (NULLs where
  no match).
- *What makes a JOIN possible?* → A shared key (the foreign key) linking the tables.

## Lab Work 12 — Procedures, triggers, indexing (**practical test week**)
**Objective:** Automate logic; speed up search.
**Tasks:** a stored procedure (`CALL`); an AFTER INSERT trigger writing to `payment_log`; a
`CREATE INDEX` + `EXPLAIN`.
**Expected output:** procedure returns rows; trigger auto-logs; EXPLAIN uses the index.
**Record:** all three, with screenshots.
**Viva:**
- *What is a stored procedure?* → Named, reusable SQL logic stored in the database.
- *What is a trigger?* → SQL that runs **automatically** on an INSERT/UPDATE/DELETE event.
- *What does an index do (and cost)?* → Speeds up reads on a column; costs extra storage and slightly
  slower writes.

---

# Part 3 — Reliability & Project

## Lab Work 13 — Transactions & ACID
**Objective:** Group steps atomically.
**Tasks:** COMMIT example; ROLLBACK example on a balance.
**Expected output:** committed change stays; rolled-back change vanishes.
**Record:** balance before/after ROLLBACK.
**Viva:**
- *What are the four ACID properties?* → Atomicity, Consistency, Isolation, Durability.
- *What does ROLLBACK do?* → Undoes all changes since `START TRANSACTION`.
- *Give a real case needing a transaction.* → A fee payment: deduct balance **and** record receipt —
  both or neither.

## Lab Work 14 — Concurrency & locking
**Objective:** See two sessions contend for a row.
**Tasks:** two tabs; one holds a lock, the other waits until COMMIT; inspect isolation level.
**Expected output:** the second session blocks then completes.
**Record:** screenshots of the waiting and completed sessions.
**Viva:**
- *What is a lock?* → A hold the DBMS places on data so others can't change it mid-transaction.
- *What is a deadlock?* → Two transactions each waiting on the other; the DBMS aborts one.
- *Isolation level trade-off?* → Higher = safer but slower; lower = faster but risks dirty/non-repeatable
  reads.

## Lab Work 15 — Backup, recovery & security
**Objective:** Export, restore, and restrict access.
**Tasks:** Export `.sql`; DROP a table; Import to restore; `CREATE USER` + `GRANT`/`REVOKE`;
`SHOW GRANTS`.
**Expected output:** table lost then recovered; limited user's grants listed.
**Record:** export dialog, restored table, SHOW GRANTS.
**Viva:**
- *What is a backup and how do you recover?* → A saved copy (the `.sql` script); recovery re-runs it to
  rebuild data.
- *What is "least privilege"?* → Give each user only the rights they need — nothing more.
- *GRANT vs REVOKE?* → GRANT gives a privilege; REVOKE takes it back.

## Lab Work 16 — Project + NoSQL
**Objective:** Present the full build; contrast relational vs NoSQL.
**Tasks:** assemble diagram→schema→build→queries→security→backup; write the relational-vs-document
comparison with the sample JSON.
**Expected output:** a complete, explainable project.
**Record:** the project pack + comparison.
**Viva:**
- *Relational vs NoSQL document model?* → Relational = fixed tables + relationships + strong
  consistency; document = flexible nested data that scales, weaker cross-table guarantees.
- *When would you choose NoSQL?* → Rapidly changing/unstructured or very large-scale data where rigid
  schemas hurt.
- *Walk me through one query in your project.* → (Student explains their own SQL — the key check.)

---

## External Viva & Practical Exam — guidance

**How the external viva typically runs (adapt to your college):**
1. **Report check** — the examiner reads the printed A4 lab report and confirms all 16 questions have
   SQL + screenshot + explanation, signed off by the internal instructor.
2. **Viva Q&A** — the examiner points at queries and asks the student to **explain their own SQL** and
   answer the per-lab questions above, plus the cross-cutting ones below.

**Evidence checklist the report should contain:**
- ☐ ER diagram + normalized (3NF) schema of Himalaya College
- ☐ `CREATE TABLE` script with PK/FK/constraints; 5 populated tables
- ☐ Queries: WHERE, aggregate+GROUP BY, HAVING, subquery, INNER & LEFT JOIN
- ☐ A view, a stored procedure, a trigger, an index (+EXPLAIN)
- ☐ A transaction (COMMIT + ROLLBACK) and a concurrency/locking demo
- ☐ An exported backup + a restore; a limited user (GRANT/REVOKE)
- ☐ A relational-vs-NoSQL comparison

**Cross-cutting viva questions (whole course):**
- *Trace how your ER diagram became the actual tables.*
- *Which of your tables is a junction table, and why does it exist?*
- *Name three constraints in your schema and what each protects against.*
- *Explain one JOIN in your project in plain English.*
- *Why are transactions necessary in a fee-payment system?* (U6 link)
- *Give one advantage and one limitation of NoSQL vs your relational design.* (U7 link)

**Suggested viva marking (out of the viva weight):** explanation of their **own** SQL (40%),
design/normalization understanding (25%), reliability (transactions/backup) understanding (20%),
advanced/NoSQL concepts (15%).

---

> **Companion documents:** the student-facing [Lab Questions](IT220_Lab_Questions.md), the beginner
> step-by-step [Lab Manual](IT220_Lab_Manual.md), and the [Lab Report Format](IT220_Lab_Report_Format.md).
> Lab numbers here map to the 16 weekly practicals in the session plan.
