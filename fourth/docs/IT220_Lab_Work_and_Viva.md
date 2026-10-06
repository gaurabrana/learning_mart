# IT 220 — Laboratory Work Record & Viva Question Set (Instructor Copy)
### Database Management System · BIM 4th Semester · MySQL/MariaDB (XAMPP + phpMyAdmin)

This is the **instructor/examiner** companion to the student docs. It lists every lab work, its tasks
and expected output, what the student must record, and the **viva questions with model answers**. It
maps 1:1 to the 16 weekly practicals in [IT220_session_plan.md](../IT220_session_plan.md) and to the
step-by-step [IT220_Lab_Manual.md](IT220_Lab_Manual.md).

- **Running project:** the **Model College** database (students, teachers, courses, enrolments, fee
  payments) — one database built up across all 16 labs, and also the student's project.
- **Environment:** MySQL/MariaDB via **XAMPP**, driven through **phpMyAdmin**. Chosen because it is
  the gentlest on-ramp for absolute beginners (visual + SQL in one place, one installer).
- **Audience:** treat every student as a **complete beginner** — the manual assumes zero prior
  knowledge; assess understanding, not speed.

> **Scope decision (2026-08).** This lab is **hands-on SQL only**. Relational algebra, relational
> calculus and pen-and-paper normalization were removed from the lab track — they are notation and
> reasoning, not runnable work, and are taught and examined in the **lectures** (Units 3 and 4).
> The syllabus lab clause asks only for SQL (create/insert/delete/update/select) plus a project;
> every lab from 4 onward is the student typing SQL and reading a result. Lab 3 (design) is the sole
> non-SQL lab and exists because the project needs a schema before it can be built.

---

## How the lab record is kept and assessed

**Each lab-work entry in the student's report must contain:**
1. **Lab number & title**, date, student name/roll.
2. **Objective** (1–2 lines, student's own words).
3. **The SQL** they ran for that lab (just what's new).
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
> read it aloud in plain English — then ask them to **change** it ("now only semester 4").

> **Zero-tolerance rule (state it up front):** an `UPDATE` or `DELETE` written without a `WHERE`
> clause in a graded query fails that lab work — it shows the student doesn't understand the danger.
> **One exception:** Lab 11 step 5 deliberately runs a no-`WHERE` `UPDATE` *inside* a transaction and
> undoes it with `ROLLBACK`. That is the taught demonstration of the danger, and Q11 asks for it —
> do not penalise it. The rule targets a no-`WHERE` statement offered as a *working* query.

---

## List of Lab Works (16) → weekly sessions

| Lab | Title | Week | Syllabus unit |
|-----|-------|------|----------------|
| 1 | Install XAMPP; first query | 1 | U1 |
| 2 | Inside the DBMS: catalog & users | 2 | U1 |
| 3 | Database design (ER diagram + schema) | 3 | U2 |
| 4 | DDL: create tables & constraints | 4 | U5 |
| 5 | INSERT: populating the database | 5 | U5 |
| 6 | SELECT, WHERE, ORDER BY, DISTINCT | 6 | U5 |
| 7 | Aggregates, GROUP BY, HAVING, NULL | 7 | U5 |
| 8 | JOINs (inner, left, self) | 8 | U5 |
| 9 | Subqueries | 9 | U5 |
| 10 | Views | 10 | U5 |
| 11 | UPDATE & DELETE | 11 | U5 |
| 12 | Procedures, triggers, indexing (**practical test**) | 12 | U5 |
| 13 | Transactions & ACID | 13 | U6 |
| 14 | Concurrency & locking | 14 | U6 |
| 15 | Backup, recovery & security | 15 | U6/U7 |
| 16 | Project demo | 16 | U7 |

> **Note on sequencing.** SQL labs start in **Week 4**, four weeks before Unit 5 begins in lectures
> (Week 8). This is deliberate: beginners need repetition, and following exact steps before the
> theory arrives means that when Unit 5 is taught they already recognise every statement. Labs 4–7
> are "type this and see what happens"; by Week 8 the lecture explains what they have been doing.

---

# Part 1 — Getting set up

## Lab Work 1 — Install XAMPP & first query
**Objective:** Get a working database server and run queries against it.
**Tasks:** Install XAMPP; start MySQL + Apache; open phpMyAdmin; create the practice `demo_shop`;
run `SELECT *`, a column list, and a `WHERE`.
**Expected output:** phpMyAdmin shows 3 product rows; the `WHERE price > 30` query returns 2.
**Record:** screenshot of the running Control Panel + two query results.
**Viva (model answers):**
- *What is the difference between MySQL and phpMyAdmin?* → MySQL is the **database server** (does the
  real work); phpMyAdmin is just a **web interface** to click through it and run SQL.
- *What does `SELECT * FROM product` mean?* → "Return every column (`*`) of every row from the
  `product` table."
- *What did adding `WHERE price > 30` change?* → It filtered the **rows** — only products over Rs 30.
- *Why open phpMyAdmin at `http://localhost` and not a file?* → It's served by the local Apache web
  server; the database only answers through the server.

**Practical note for the instructor:** the XAMPP download is ~150 MB. Have the Windows and macOS
installers on a USB stick or LAN share — a class of 40 downloading simultaneously will not finish in
50 minutes. Verify the macOS path on one machine beforehand (current XAMPP for Mac ships as a VM and
reaches phpMyAdmin differently from Windows).

## Lab Work 2 — Inside the DBMS
**Objective:** Understand server→database→table→row, the catalog, and users.
**Tasks:** Navigate the hierarchy; query `information_schema` (tables, columns, count of schemas);
create user `college_clerk` with only SELECT+INSERT on `demo_shop`; confirm with `SHOW GRANTS`.
**Expected output:** metadata query returns `product`; the column query lists id/name/price with
types; `SHOW GRANTS` shows only SELECT, INSERT.
**Record:** screenshots of the `information_schema` result and `SHOW GRANTS`.
**Viva:**
- *What is metadata / the data dictionary?* → "Data about the data" — the DBMS's own catalog of every
  database, table, and column (`information_schema`).
- *What does a DBA do here?* → Manages users and grants each only the privileges they need.
- *Relate this to the three-schema architecture.* → Physical storage (internal), the logical tables
  (conceptual), and per-user views/permissions (external) are separated.
- *Why can't `college_clerk` drop a table?* → That privilege was never granted — least privilege.

## Lab Work 3 — Database design
**Objective:** Model the domain before building it. **The only non-SQL lab.**
**Tasks:** Identify entities/attributes/keys; resolve the M:N into an `Enrolment` junction table with
a composite key; draw all 5 tables in dbdiagram.io; export PNG; write the schema in text.
**Expected output:** a 5-table diagram with Enrolment between Student and Course, plus the written
schema with PK/FK marked.
**Record:** the exported diagram + the written schema.
**Viva:**
- *Entity vs attribute?* → Entity = a thing we store (Student); attribute = a fact about it (name).
- *Which relationship is many-to-many and how do you know?* → Student↔Course: one student takes many
  courses **and** one course has many students.
- *What is cardinality?* → How many of one entity relate to the other (1:1, 1:N, M:N).
- *Why does `Enrolment` exist?* → A many-to-many relationship can't fit in either table; the junction
  table stores the pairs.
- *What is a composite primary key and why here?* → A key made of two columns together
  (roll_no + course_code); a student can't enrol in the same course twice.
- *What is a foreign key?* → A column referencing another table's primary key; it enforces a valid
  relationship.

---

# Part 2 — Building and querying in SQL

## Lab Work 4 — DDL & constraints
**Objective:** Build the Lab 3 schema for real, with constraints that defend the data.
**Tasks:** `CREATE DATABASE`; `CREATE TABLE` × 5 with PK/FK/NOT NULL/CHECK/DEFAULT; `SHOW TABLES`;
`DESCRIBE`; then **deliberately violate three constraints** and capture the errors.
**Expected output:** 5 tables; DESCRIBE showing PRI on keys; three red error messages.
**Record:** the CREATE script, `SHOW TABLES`, `DESCRIBE Enrolment`, and one constraint error.
**Viva:**
- *What is DDL vs DML?* → DDL defines structure (`CREATE`/`ALTER`/`DROP`); DML changes data
  (`INSERT`/`UPDATE`/`DELETE`/`SELECT`).
- *Name three constraints in your schema and what each prevents.* → PK stops duplicates; FK stops
  pointing at a non-existent row; NOT NULL stops a missing value; CHECK stops an out-of-range value.
- *What does a CHECK constraint do?* → Rejects values outside a rule (semester 1–8).
- *Why is `Enrolment`'s PRIMARY KEY written on its own line?* → It spans two columns — a composite key.
- *What happened when you inserted teacher_id 999?* → The FK rejected it; teacher 999 does not exist.

## Lab Work 5 — INSERT
**Objective:** Populate all five tables in the correct order.
**Tasks:** INSERT parents (Teacher/Student/Course) then children (Enrolment/FeePayment); a
named-column INSERT that relies on DEFAULT; read everything back; trigger an FK error on purpose.
**Expected output:** 5 students, 8 enrolments, 4 payments; `STA201` with credit_hours = 3 unset by
hand; an FK error for student 999.
**Record:** the INSERT script, `SELECT * FROM Student;`, and the FK error.
**Viva:**
- *Why did the insert order matter?* → A child row (Enrolment) needs its parent (Student/Course) to
  already exist.
- *You never typed credit_hours for STA201 — why is it 3?* → The column has `DEFAULT 3`.
- *What is the difference between the two INSERT forms?* → Positional (all columns in order) vs named
  (`INSERT INTO t (a,b) VALUES …`), where unlisted columns take DEFAULT or NULL.
- *What does the FK error protect against?* → Orphan rows — an enrolment for a student who doesn't
  exist.

## Lab Work 6 — SELECT, WHERE, ORDER BY, DISTINCT
**Objective:** Retrieve and filter data — the most-used statement in SQL.
**Tasks:** column lists, `AS`, `WHERE` with AND/OR, `IN`, `BETWEEN`, `LIKE`, `ORDER BY` (incl. two
keys), `DISTINCT`, `LIMIT`.
**Expected output:** correct row subsets; `DISTINCT semester` returns just 2 and 4.
**Record:** screenshots of a `WHERE`, a `LIKE`, and an `ORDER BY`.
**Viva:**
- *What does `WHERE` filter — rows or columns?* → **Rows.** The column list after SELECT picks columns.
- *What does `%` mean in `LIKE 'S%'`?* → Any sequence of characters — so "starts with S".
- *What does `DISTINCT` do?* → Removes duplicate values from the result.
- *How do you sort high-to-low?* → `ORDER BY column DESC`.
- *`ORDER BY semester DESC, name ASC` — what does the second key do?* → Breaks ties within a semester,
  sorting those students by name.

## Lab Work 7 — Aggregates, GROUP BY, HAVING, NULL
**Objective:** Summarise many rows into useful numbers, and handle unknown values.
**Tasks:** COUNT/SUM/AVG/MIN/MAX; GROUP BY (per semester, per course, per student);
HAVING; the WHERE-vs-HAVING comparison; `IS NULL` vs `= NULL`; `COUNT(*)` vs `COUNT(column)`.
**Expected output:** semester 2 → 3 students, semester 4 → 2; CMP101 → 3 students; roll 101 total
20000; `= NULL` returns **zero rows**.
**Record:** screenshots of the GROUP BY, the HAVING, and the `= NULL` vs `IS NULL` pair.
**Viva:**
- *WHERE vs HAVING?* → WHERE filters **rows before** grouping; HAVING filters **groups after**.
- *What does an aggregate function do?* → Collapses many rows into one value (COUNT, SUM, AVG…).
- *Why `IS NULL` not `= NULL`?* → NULL means "unknown" and is never equal to anything, including NULL.
- *Why does `COUNT(*)` differ from `COUNT(grade)`?* → `COUNT(*)` counts rows; `COUNT(grade)` skips
  NULLs.
- *Why must every non-aggregated column appear in GROUP BY?* → Otherwise the DBMS can't decide which
  row's value to show for the group.

## Lab Work 8 — JOINs
**Objective:** Reassemble data split across tables.
**Tasks:** INNER JOIN (2- and 3-table); LEFT JOIN; the LEFT-JOIN-plus-`IS NULL` trick to find
non-payers; a self-join on Student; JOIN combined with GROUP BY.
**Expected output:** name+title+grade rows; every student listed by the LEFT JOIN; non-payers = 104
and 105.
**Record:** the INNER JOIN, the LEFT JOIN, and the non-payer query.
**Viva:**
- *INNER vs LEFT JOIN?* → INNER keeps only matching rows; LEFT keeps all left-table rows (NULLs where
  no match).
- *What makes a JOIN possible?* → A shared key — the foreign key linking the tables.
- *How did you find students who paid nothing?* → LEFT JOIN to FeePayment, then keep rows where the
  payment side `IS NULL`.
- *Why `s.name` and not just `name`?* → Both joined tables have a `name` column — it must be qualified.
- *What is a self-join?* → Joining a table to itself (aliased twice) to compare rows within it — here,
  classmates in the same semester.
- *What happens if you omit `ON`?* → A cartesian product: every row paired with every row.

## Lab Work 9 — Subqueries
**Objective:** Feed one query's result into another.
**Tasks:** scalar subquery (`= (SELECT MAX…)`, `> (SELECT AVG…)`); `IN` / `NOT IN`; `EXISTS` /
`NOT EXISTS`; a derived table in `FROM`.
**Expected output:** paid students = 101/102/103; unpaid = 104/105 (matching Lab 8's answer).
**Record:** the `IN`, the `NOT IN`, and the derived table.
**Viva:**
- *What is a subquery?* → A query whose result feeds an outer query.
- *You got the same unpaid students in Lab 8 with a JOIN — which is better?* → Both are correct; JOINs
  often perform better on large data, subqueries can read more clearly. (Accept either with reasoning.)
- *When must you use `IN` instead of `=`?* → When the subquery returns more than one row.
- *What does `EXISTS` return?* → True/false — whether the inner query found any row at all.
- *Why does a subquery in `FROM` need an alias?* → SQL requires every derived table to be named.

## Lab Work 10 — Views
**Objective:** Save a query under a name and reuse it.
**Tasks:** `CREATE VIEW paid_students` and `enrolment_sheet` (4-table join); query them; show a view
reflecting an underlying UPDATE; UPDATE **through** a simple view; fail to update a joined view;
`SHOW FULL TABLES WHERE table_type='VIEW'`.
**Expected output:** views queryable like tables; the simple view's UPDATE changes the real Student
row; the joined view's UPDATE errors.
**Record:** `enrolment_sheet` output + the update-through-view result.
**Viva:**
- *Table vs view?* → A table stores data; a view is a **saved query** that computes its rows on demand.
- *You updated a row after creating the view — why did the view change too?* → It isn't a copy; it
  re-runs its SELECT every time.
- *Give a use for a view.* → Simplify complex joins, or expose limited columns to a restricted user.
- *Why couldn't you UPDATE `enrolment_sheet`?* → It joins four tables — the DBMS can't tell which
  underlying row to change.
- *How does a view relate to the three-schema architecture?* → It is an **external** schema — one
  user's tailored window onto the conceptual tables.

## Lab Work 11 — UPDATE & DELETE
**Objective:** Change data safely.
**Tasks:** the SELECT→UPDATE→SELECT habit; multi-column UPDATE; UPDATE using the existing value;
DELETE with WHERE; a DELETE blocked by a foreign key; and the no-WHERE disaster rescued by ROLLBACK.
**Expected output:** "N rows affected" matching the SELECT's prediction; FK error on deleting roll
101; every semester set to 1 then restored by ROLLBACK.
**Record:** the SELECT-then-UPDATE pair, the FK error, and the rollback recovery.
**Viva:**
- *Why is `UPDATE` without `WHERE` dangerous?* → It changes **every** row.
- *What is the safe habit?* → Run the `WHERE` as a `SELECT` first to see exactly which rows will change.
- *Why did `DELETE FROM Student WHERE roll_no = 101` fail?* → Child rows in Enrolment/FeePayment
  reference it; the FK prevents orphans.
- *How would you delete that student properly?* → Delete the children first, then the parent.
- *You wiped every semester in step 5 — how did you recover?* → It was inside a transaction, so
  `ROLLBACK` undid it. Outside a transaction, restore from the backup.

## Lab Work 12 — Procedures, triggers, indexing (**practical test week**)
**Objective:** Put logic inside the database; speed up search.
**Tasks:** a stored procedure with `IN`; a second with `OUT`; an AFTER INSERT trigger writing to
`payment_log`; `EXPLAIN` before and after `CREATE INDEX`; `SHOW INDEX`.
**Expected output:** `CALL` returns rows; `@t` = 20000; `payment_log` fills itself; EXPLAIN's `key`
column changes from NULL to the index name.
**Record:** all four, with screenshots.
**Viva:**
- *What is a stored procedure?* → Named, reusable SQL logic stored in the database.
- *What is a trigger?* → SQL that runs **automatically** on an INSERT/UPDATE/DELETE event.
- *You never inserted into `payment_log` — how did the row get there?* → The AFTER INSERT trigger on
  FeePayment wrote it.
- *What is `NEW.receipt_no`?* → The value from the row being inserted, available inside the trigger.
- *What does an index do (and cost)?* → Speeds up reads on a column; costs extra storage and slightly
  slower writes.
- *What changed in your two EXPLAIN outputs?* → The `key` column went from NULL to
  `idx_student_name`, and the estimated `rows` dropped. (Accept "no change, dataset too small" **if**
  the student explains why.)

---

# Part 3 — Reliability and the project

## Lab Work 13 — Transactions & ACID
**Objective:** Group statements so they succeed or fail together.
**Tasks:** COMMIT example; ROLLBACK example on a balance; a transaction that fails halfway (duplicate
receipt) proving atomicity; SAVEPOINT + `ROLLBACK TO`.
**Expected output:** committed change stays; rolled-back change vanishes; the failed transaction
leaves the balance untouched.
**Record:** balance before/after ROLLBACK, and the failed-halfway result.
**Viva:**
- *What are the four ACID properties?* → Atomicity, Consistency, Isolation, Durability.
- *What does ROLLBACK do?* → Undoes all changes since `START TRANSACTION`.
- *In step 4 the INSERT failed — why did the balance not drop?* → Atomicity: the whole group was
  rolled back, so the deduction was undone too. **This is the key question of the lab.**
- *Give a real case needing a transaction.* → A fee payment: deduct balance **and** record receipt —
  both or neither.
- *What is a SAVEPOINT for?* → Undoing part of a transaction while keeping the earlier part.

## Lab Work 14 — Concurrency & locking
**Objective:** See two sessions contend for a row.
**Tasks:** two tabs; one holds a lock, the other waits until COMMIT; show a **different** row not
blocking; inspect the isolation level; optionally `SHOW PROCESSLIST`.
**Expected output:** the second session blocks then completes; the different-row update runs instantly.
**Record:** screenshots of the waiting session and the completed one.
**Viva:**
- *What is a lock?* → A hold the DBMS places on data so others can't change it mid-transaction.
- *Why did Tab B wait?* → Tab A's uncommitted transaction held a lock on that row.
- *Why did updating roll 102 not wait?* → InnoDB locks **rows**, not whole tables.
- *What is a deadlock?* → Two transactions each waiting on the other; the DBMS aborts one.
- *Isolation level trade-off?* → Higher = safer but slower; lower = faster but risks dirty/non-repeatable
  reads.

## Lab Work 15 — Backup, recovery & security
**Objective:** Export, restore, and restrict access.
**Tasks:** Export `.sql`; DROP a table; Import to restore; `CREATE USER` + `GRANT`/`REVOKE` +
`SHOW GRANTS` before and after; a second user granted `SELECT` on a **view only**.
**Expected output:** table lost then recovered; grants visibly change after the REVOKE; `reader` can
see the view but not the base table.
**Record:** export dialog, restored table, both `SHOW GRANTS` outputs.
**Viva:**
- *What is a backup and how do you recover?* → A saved copy (the `.sql` script); recovery re-runs it to
  rebuild data.
- *What is actually inside the `.sql` file?* → `CREATE TABLE` and `INSERT` statements — the SQL to
  rebuild everything.
- *What is "least privilege"?* → Give each user only the rights they need — nothing more.
- *GRANT vs REVOKE?* → GRANT gives a privilege; REVOKE takes it back.
- *Why grant on a view instead of the table?* → The user sees only the slice the view exposes — the
  external schema, enforced.

## Lab Work 16 — Project demo
**Objective:** Present the full build and defend it live.
**Tasks:** assemble diagram → schema → build → data → queries → view/procedure/trigger/index →
transaction → backup → limited user; run queries live on request.
**Expected output:** a complete, explainable, working database.
**Record:** the project pack.
**Viva:**
- *Walk me through one query in your project.* → (Student explains their own SQL — the key check.)
- *Now change it to show only semester 4.* → (Live modification — the strongest anti-copying test.)
- *Which of your tables is a junction table, and why does it exist?*
- *Trace how your ER diagram became the actual tables.*

---

## External Viva & Practical Exam — guidance

**How the external viva typically runs (adapt to your college):**
1. **Report check** — the examiner reads the printed A4 lab report and confirms all 16 questions have
   SQL + screenshot + explanation, signed off by the internal instructor.
2. **Viva Q&A** — the examiner points at queries and asks the student to **explain their own SQL** and
   answer the per-lab questions above, plus the cross-cutting ones below.

**Evidence checklist the report should contain:**
- ☐ ER diagram + written schema of Model College (Q3)
- ☐ `CREATE TABLE` script with PK/FK/constraints + a captured constraint error (Q4)
- ☐ `INSERT` script for all 5 tables + a foreign-key error (Q5)
- ☐ Queries: WHERE/LIKE/ORDER BY, aggregate+GROUP BY, HAVING, `IS NULL` vs `= NULL` (Q6–Q7)
- ☐ INNER JOIN, LEFT JOIN, self-join, subquery (Q8–Q9)
- ☐ A view, an update through a view (Q10)
- ☐ SELECT-checked UPDATE, a DELETE blocked by an FK (Q11)
- ☐ A stored procedure, a trigger, an index + EXPLAIN (Q12)
- ☐ A transaction (COMMIT + ROLLBACK) and a concurrency/locking demo (Q13–Q14)
- ☐ An exported backup + a restore; a limited user with GRANT/REVOKE (Q15)

**Cross-cutting viva questions (whole course):**
- *Trace how your ER diagram became the actual tables.*
- *Which of your tables is a junction table, and why does it exist?*
- *Name three constraints in your schema and what each protects against.*
- *Explain one JOIN in your project in plain English.*
- *Show me a query, then change it live.* (The single best anti-copying check.)
- *Why are transactions necessary in a fee-payment system?* (U6 link)
- *If this database served 10,000 students, what would you index and why?* (U7 link)

**Suggested viva marking (out of the viva weight):** explanation of their **own** SQL (45%),
design/schema understanding (20%), querying — joins/aggregates/subqueries (20%), reliability
(transactions/backup/security) understanding (15%).

---

> **Companion documents:** the student-facing [Lab Questions](IT220_Lab_Questions.md), the beginner
> step-by-step [Lab Manual](IT220_Lab_Manual.md), and the [Lab Report Format](IT220_Lab_Report_Format.md).
> Lab numbers here map to the 16 weekly practicals in the session plan.
