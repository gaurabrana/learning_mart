# Unit 5 — SQL · Content Outline

**15 LHs → 15 sessions (S22–S36) · 50 min each**
This is the *content map* — what will fill each slot before we generate full material.
Local examples use Nepal / South Asia. Review and tell me what to swap.
This is the largest, most **practical/hands-on** unit — most sessions end at a live SQL editor.

> **Target DBMS: MySQL / MariaDB.** All SQL syntax (e.g. `AUTO_INCREMENT`, `LIMIT`, string
> functions, stored-procedure/trigger syntax) will follow MySQL. Where ANSI-standard SQL
> differs from MySQL, the speaker notes will flag it.

> Template per session (from the guide):
> Opening hook (5m) → Content sections (35m) → Check for understanding (5m) →
> Real-life application (3m) → Summary & takeaways (2m), with speaker notes + visual cues.

---

## Running sample schema (used across ALL sessions S22–S36)
A tiny **college database** — students refer to it constantly so cognitive load stays on SQL, not the domain.

```sql
Student(roll PK, name, program, semester, dob, email)
Course(course_id PK, title, credits, dept)
Instructor(inst_id PK, name, dept, salary)
Enrollment(roll FK→Student, course_id FK→Course, sem, grade, marks)   -- PK(roll, course_id, sem)
Teaches(inst_id FK→Instructor, course_id FK→Course, sem)
```
> Speaker note: print this schema on a take-home card / pin it on every slide footer. Sample seed data: ~8 students (Sita, Hari, Bishal, Anjali…), 5 courses (IT220 DBMS, MGT201, ECO101…), 4 instructors. Reuse the *same* rows in every session so query results are predictable.

---

## Unit 5 learning outcomes (what students can do after S22–S36)
1. Define a schema in SQL with correct data types and all constraint kinds (PK/FK/CHECK/NOT NULL/UNIQUE), and alter/drop it.
2. Write SELECT queries with WHERE/FROM, renaming, tuple variables, and string/pattern operations.
3. Sort, de-duplicate, and combine result sets (ORDER BY, DISTINCT, UNION/INTERSECT/EXCEPT).
4. Summarize data with aggregate functions, GROUP BY and HAVING, and reason correctly about NULLs and three-valued logic.
5. Write nested subqueries using IN, SOME/ALL, EXISTS/NOT EXISTS, and UNIQUE.
6. Create and use views and derived relations, and explain which views are updatable.
7. Modify data with INSERT/UPDATE/DELETE and join tables with all join types (INNER/OUTER/NATURAL/USING/ON).
8. Explain the basic role of stored procedures, DML triggers, and indexes, and when each helps.

---

## S22 — DDL & Data Types · Constraints · Domain Types · Schema Definition  *(hands-on)*

**Hook:** "Before you can ask the database anything, you have to *tell it what a student even is*. Today we build the boxes; from tomorrow we fill and query them."

**Concepts & how each will be filled:**

1. **DDL & CREATE TABLE**
   - Definition: DDL = the sub-language that *defines* structure (CREATE/ALTER/DROP).
   - Snippet: `CREATE TABLE Student(roll INT PRIMARY KEY, name VARCHAR(50), program VARCHAR(20));`
   - Local example: building the `Student` table for Pokhara University's BIM intake.
   - Misconception: *"CREATE TABLE also adds the data."* Correction: it makes an empty structure only.

2. **Data / domain types in SQL**
   - INT, DECIMAL(p,s), VARCHAR(n)/CHAR(n), DATE, BOOLEAN; CHAR vs VARCHAR.
   - Local example: store NPR amounts as `DECIMAL(10,2)`, not FLOAT (rounding errors in fee tables).
   - Mini case: phone number stored as VARCHAR not INT (leading 0 in 98XXXXXXXX, '+977').
   - Fun analogy: data types = sizes of tiffin boxes — wrong size wastes space or won't fit.

3. **Specifying constraints**
   - PRIMARY KEY, FOREIGN KEY (+ON DELETE), NOT NULL, UNIQUE, CHECK, DEFAULT.
   - Snippet: `CHECK (marks BETWEEN 0 AND 100)`, `email VARCHAR(60) UNIQUE`, `FOREIGN KEY (roll) REFERENCES Student(roll)`.
   - Local example: a student can't enroll in a course that doesn't exist → FK on `Enrollment.course_id`.
   - Misconception: *"PK and UNIQUE are the same."* Correction: PK = UNIQUE + NOT NULL + one per table.

4. **Schema definition: ALTER & DROP**
   - Snippet: `ALTER TABLE Student ADD email VARCHAR(60);` / `DROP TABLE Enrollment;`
   - Mini case: college adds a `email` column mid-semester without losing existing rows → ALTER, not re-create.

**Check for understanding:**
- MCQ1: Which constraint forbids empty values but allows duplicates? (a) PRIMARY KEY (b) UNIQUE (c) NOT NULL ✅ (d) CHECK
- MCQ2: `DROP TABLE` belongs to which language? → DDL ✅
- Discussion: "List 3 columns for an eSewa `Wallet` table and pick the data type + one constraint for each."

**Real-life application:** every backend feature in eSewa/Khalti starts with a migration — `CREATE`/`ALTER TABLE`. This is a literal day-1 job task.

**Summary:** (1) DDL defines structure; (2) right data type per column; (3) constraints enforce rules at the DB level. **Next:** now that tables exist, we *ask questions* — SELECT/FROM/WHERE.

**Visual cues:** annotated `CREATE TABLE` slide with each constraint colour-coded; data-type cheat-sheet table. Mark slides [THEORY]/[SNIPPET]/[HANDS-ON].

---

## S23 — DML Basics: the SELECT, FROM, and WHERE clauses  *(hands-on)*

**Hook:** "There are millions of rows in a telecom's customer table. How do you pull *just the Ncell users in Pokhara*? One sentence of SQL."

**Concepts & how each will be filled:**

1. **The basic query: SELECT … FROM …**
   - Definition: FROM = which table(s); SELECT = which columns.
   - Snippet: `SELECT name, program FROM Student;` and `SELECT * FROM Course;`
   - Misconception: *"SELECT chooses rows."* Correction: SELECT chooses **columns** (projection); WHERE chooses rows.

2. **The WHERE clause (filtering rows)**
   - Comparison (`=, <>, <, >=`), logical (`AND, OR, NOT`), `BETWEEN`, `IN`.
   - Snippet: `SELECT name FROM Student WHERE program='BIM' AND semester=4;`
   - Local example: `SELECT * FROM Instructor WHERE dept='IT' AND salary > 60000;`
   - Mini case: Daraz "show items between Rs 500 and Rs 1500" → `WHERE price BETWEEN 500 AND 1500`.

3. **The FROM clause with multiple tables (preview of joins)**
   - Cartesian product warning: `FROM Student, Enrollment` without a condition = every-row-times-every-row.
   - Snippet: `SELECT name, grade FROM Student, Enrollment WHERE Student.roll = Enrollment.roll;`
   - Misconception: *"Listing two tables just merges them sensibly."* Correction: you must add the matching condition or you get a cross product.

4. **Column expressions & aliases teaser**
   - Snippet: `SELECT name, marks*1.0 AS percentage FROM Enrollment;` (alias detail expanded in S24).

**Check for understanding:**
- MCQ1: Which clause filters *rows*? (a) SELECT (b) FROM (c) WHERE ✅ (d) ORDER BY
- MCQ2: `SELECT * FROM Student;` returns? → all columns, all rows ✅
- Discussion: "Write in plain English a WHERE condition for 'Khalti users who joined in 2025 and live in Kathmandu.'"

**Real-life application:** every search box, filter, and report in any app is a SELECT … WHERE underneath.

**Summary:** (1) SELECT = columns, FROM = tables, WHERE = row filter; (2) AND/OR/BETWEEN/IN build conditions; (3) listing tables without a condition = dangerous cross product. **Next:** renaming things and searching *inside text* (LIKE & wildcards).

**Visual cues:** "SELECT(columns) ← FROM(tables) ← WHERE(rows)" flow arrow; before/after table showing rows filtered out.

---

## S24 — Rename Operation · Tuple Variables · String Operations  *(hands-on)*

**Hook:** "When you join the Student table *to itself* to find classmates, both copies are called 'Student'. How does SQL tell them apart?" → tuple variables.

**Concepts & how each will be filled:**

1. **The rename operation (AS)**
   - Rename columns and tables for readable output.
   - Snippet: `SELECT name AS student_name, marks AS score FROM Enrollment;`
   - Local example: report header reads "Student Name" not "name" for a college mark-sheet export.

2. **Tuple variables (table aliases)**
   - Definition: short alias bound to a table, essential for self-joins and multi-table queries.
   - Snippet: `SELECT s.name, e.grade FROM Student s, Enrollment e WHERE s.roll = e.roll;`
   - Mini case: self-join "students in the same program as Sita" using `Student s1, Student s2`.
   - Misconception: *"Aliases are just cosmetic."* Correction: for self-joins they're mandatory to disambiguate.

3. **String operations**
   - `LIKE` with wildcards `%` (any sequence) and `_` (single char); concatenation (`||` or `CONCAT`); UPPER/LOWER/TRIM.
   - Snippet: `SELECT name FROM Student WHERE name LIKE 'S%';` (names starting with S);
     `SELECT name FROM Student WHERE email LIKE '%@pu.edu.np';`
   - Local example: find all Ncell numbers → `WHERE phone LIKE '98%'`; find Gmail users `LIKE '%@gmail.com'`.
   - Misconception: *"`=` and `LIKE` are the same."* Correction: `=` is exact; `LIKE` does pattern matching.
   - Fun analogy: `%` = "blah blah anything", `_` = exactly one Scrabble tile.

**Check for understanding:**
- MCQ1: Which finds names ending in 'a'? (a) `LIKE 'a%'` (b) `LIKE '%a'` ✅ (c) `LIKE '_a'` (d) `= 'a'`
- MCQ2: `_` matches how many characters? → exactly one ✅
- Discussion: "Write a LIKE pattern for all college email IDs ending in `@pu.edu.np`."

**Real-life application:** the autocomplete/search-as-you-type on Daraz and Hamrobazar is `LIKE '%term%'` (or full-text) under the hood.

**Summary:** (1) AS renames columns/tables; (2) tuple variables disambiguate, enabling self-joins; (3) LIKE + `%`/`_` searches inside text. **Next:** controlling *order* and removing *duplicates*, plus set operations.

**Visual cues:** wildcard pattern → matching-rows table; self-join diagram with two labelled copies of Student.

---

## S25 — ORDER BY · DISTINCT · Set Operations (UNION/INTERSECT/EXCEPT)  *(hands-on)*

**Hook:** "A merit list isn't useful unless it's *sorted*, and a mailing list isn't useful if every name appears five times. SQL fixes both in one keyword each."

**Concepts & how each will be filled:**

1. **Ordering the display of tuples (ORDER BY)**
   - `ASC` (default) / `DESC`; multi-key sort.
   - Snippet: `SELECT name, marks FROM Enrollment ORDER BY marks DESC;`
   - Local example: rank-order the college merit list by `marks DESC, name ASC`.
   - Misconception: *"Rows come back sorted by default."* Correction: order is **not** guaranteed without ORDER BY.

2. **Duplicate tuples (DISTINCT / ALL)**
   - Snippet: `SELECT DISTINCT program FROM Student;` vs `SELECT program FROM Student;`
   - Mini case: list every *distinct* district from a Nagarik App users table.

3. **Set operations: UNION / INTERSECT / EXCEPT**
   - Definition: combine two result sets (must be union-compatible — same columns/types).
   - Snippet: `SELECT roll FROM Enrollment WHERE course_id='IT220' UNION SELECT roll FROM Enrollment WHERE course_id='MGT201';`
   - Local example: students enrolled in DBMS **INTERSECT** students enrolled in Economics; eSewa users **EXCEPT** Khalti users.
   - Misconception: *"UNION keeps duplicates."* Correction: `UNION` removes them; `UNION ALL` keeps them.
   - Fun analogy: Venn diagram — UNION = both circles, INTERSECT = overlap, EXCEPT = left circle minus overlap.

**Check for understanding:**
- MCQ1: Default sort direction of ORDER BY? → ascending (ASC) ✅
- MCQ2: Which set op removes duplicates? (a) UNION ALL (b) UNION ✅ (c) neither
- Discussion: "Give a real scenario where you'd use EXCEPT (e.g. 'who registered but never paid')."

**Real-life application:** leaderboards, top-sellers on Daraz, and "users in A but not B" marketing segments all use ORDER BY + set operations.

**Summary:** (1) ORDER BY sorts; (2) DISTINCT de-duplicates; (3) UNION/INTERSECT/EXCEPT combine union-compatible result sets. **Next:** counting and summarizing with aggregate functions.

**Visual cues:** Venn diagram for the three set ops; before/after sorted table.

---

## S26 — Aggregate Functions · GROUP BY · HAVING  *(hands-on)*

**Hook:** "What's the *average* salary in the IT department? How *many* students passed DBMS? You don't want 5,000 rows — you want one number."

**Concepts & how each will be filled:**

1. **The five aggregate functions**
   - COUNT, SUM, AVG, MIN, MAX.
   - Snippet: `SELECT COUNT(*), AVG(marks), MAX(marks) FROM Enrollment WHERE course_id='IT220';`
   - Local example: total daily transaction volume `SUM(amount)` on eSewa.
   - Misconception: *"COUNT(column) counts all rows."* Correction: `COUNT(col)` skips NULLs; `COUNT(*)` counts every row (link to S27).

2. **GROUP BY (per-group aggregates)**
   - Definition: collapse rows into groups, one aggregate row per group.
   - Snippet: `SELECT dept, AVG(salary) FROM Instructor GROUP BY dept;`
   - Local example: average marks **per program** (BIM vs BCA) `GROUP BY program`.
   - Misconception: *"You can SELECT any column with GROUP BY."* Correction: non-aggregated SELECT columns must appear in GROUP BY.

3. **HAVING (filter groups)**
   - HAVING filters *after* grouping; WHERE filters *before*.
   - Snippet: `SELECT course_id, COUNT(*) FROM Enrollment GROUP BY course_id HAVING COUNT(*) > 30;`
   - Mini case: "courses with more than 30 enrolled students" → HAVING.
   - Misconception: *"Use WHERE COUNT(*)>30."* Correction: aggregates can't go in WHERE; use HAVING.
   - Fun analogy: WHERE = bouncer at the door (per person); HAVING = inspector checking each *table* of guests after they sit.

**Check for understanding:**
- MCQ1: Which filters *groups* not rows? → HAVING ✅
- MCQ2: `COUNT(grade)` vs `COUNT(*)` differ when? → grade has NULLs ✅
- Discussion: "Write in words a query: 'departments whose average instructor salary exceeds Rs 70,000.'"

**Real-life application:** every dashboard KPI (daily revenue, active users, average order value on Daraz) is an aggregate + GROUP BY.

**Summary:** (1) COUNT/SUM/AVG/MIN/MAX summarize; (2) GROUP BY makes per-group rows; (3) WHERE filters rows, HAVING filters groups. **Next:** the tricky truth about NULL values.

**Visual cues:** rows-collapse-into-groups animation/diagram; WHERE-vs-HAVING placement on the query pipeline.

---

## S27 — Null Values · Three-Valued Logic  *(hands-on)*

**Hook:** "A student's `grade` is blank — they haven't been graded yet. Is `grade = grade` true? In SQL... not necessarily. Welcome to NULL."

**Concepts & how each will be filled:**

1. **What NULL means**
   - Definition: unknown / not-applicable / missing — *not* zero and *not* empty string.
   - Local example: `grade` is NULL for a student mid-semester; `salary` NULL for an unpaid intern instructor.
   - Misconception: *"NULL equals 0 or ''."* Correction: NULL is the absence of a value; `0` and `''` are values.

2. **Three-valued logic (TRUE / FALSE / UNKNOWN)**
   - Any comparison with NULL → UNKNOWN; `WHERE` keeps only TRUE rows.
   - Snippet: `WHERE grade = NULL` returns nothing — must use `WHERE grade IS NULL`.
   - Misconception: *"`= NULL` finds the blanks."* Correction: use `IS NULL` / `IS NOT NULL`.

3. **NULL in aggregates & arithmetic**
   - Aggregates (except `COUNT(*)`) ignore NULLs; arithmetic with NULL → NULL.
   - Snippet: `SELECT AVG(marks) FROM Enrollment;` ignores NULL marks (callback to S26).
   - Mini case: averaging marks where some students aren't graded — AVG silently drops them; is that what you want? (use COALESCE if not).
   - Fun analogy: NULL = a sealed box — you can't say it equals anything because you don't know what's inside.

**Check for understanding:**
- MCQ1: To find rows with missing email, use → `WHERE email IS NULL` ✅
- MCQ2: `SELECT 100 + NULL;` returns → NULL ✅
- Discussion: "Should a 'not yet graded' student count as 0 in the class average? How would NULL vs 0 change the result?"

**Real-life application:** payment systems must distinguish "balance = 0" (real, broke) from "balance = NULL" (account not yet created) — confusing them causes real bugs.

**Summary:** (1) NULL = unknown, not zero; (2) comparisons with NULL = UNKNOWN, use IS NULL; (3) aggregates skip NULLs. **Next:** queries inside queries — nested subqueries with IN and SOME/ALL.

**Visual cues:** three-valued truth table (AND/OR with UNKNOWN); "= NULL ✗ / IS NULL ✓" warning slide.

---

## S28 — Nested Subqueries: Set Membership (IN) · Set Comparison (SOME/ALL)  *(hands-on)*

**Hook:** "Find students enrolled in *any* IT course — but you don't know the course IDs yet. Let one query feed another."

**Concepts & how each will be filled:**

1. **Subqueries & set membership (IN / NOT IN)**
   - Definition: a query nested inside another; inner runs first, feeds the outer.
   - Snippet: `SELECT name FROM Student WHERE roll IN (SELECT roll FROM Enrollment WHERE course_id='IT220');`
   - Local example: "Khalti users who also have an eSewa account" → `WHERE user_id IN (SELECT user_id FROM esewa_users)`.
   - Misconception: *"NOT IN works fine with NULLs."* Correction: `NOT IN` with a NULL in the inner set can return no rows (callback to S27).

2. **Set comparison: SOME / ANY**
   - `> SOME` = greater than at least one.
   - Snippet: `SELECT name FROM Instructor WHERE salary > SOME (SELECT salary FROM Instructor WHERE dept='IT');`

3. **Set comparison: ALL**
   - `> ALL` = greater than every value.
   - Snippet: "the highest-paid instructor": `WHERE salary >= ALL (SELECT salary FROM Instructor);`
   - Mini case: Daraz "products priced higher than ALL items in Electronics".
   - Misconception: *"SOME and ALL mean the same."* Correction: SOME = at least one; ALL = every single one.
   - Fun analogy: `> SOME` = "taller than at least one classmate"; `> ALL` = "tallest in the class".

**Check for understanding:**
- MCQ1: `> ALL (subquery)` is true when value is greater than → every value in the set ✅
- MCQ2: Which can be rewritten with `IN`? → `= SOME` ✅
- Discussion: "Phrase one query for 'students who scored more than ALL of last year's batch.'"

**Real-life application:** "find users who did X but also Y" segmentation queries (marketing, fraud detection at fintechs) are subqueries with IN.

**Summary:** (1) subqueries feed outer queries; (2) IN tests membership; (3) SOME = at-least-one, ALL = every. **Next:** testing whether a relation is empty (EXISTS) or duplicate-free (UNIQUE).

**Visual cues:** nested-box diagram "inner result set → outer WHERE"; SOME-vs-ALL number-line illustration.

---

## S29 — Nested Subqueries: Test for Empty Relations (EXISTS) · Absence of Duplicates (UNIQUE)  *(hands-on)*

**Hook:** "Sometimes you don't care *what* the inner query returns — only *whether it returns anything at all*. That's EXISTS."

**Concepts & how each will be filled:**

1. **EXISTS / NOT EXISTS**
   - Definition: TRUE if the subquery returns ≥1 row; correlated subqueries reference the outer row.
   - Snippet (correlated): `SELECT name FROM Student s WHERE EXISTS (SELECT * FROM Enrollment e WHERE e.roll = s.roll);` → students with at least one enrollment.
   - Local example: "instructors who teach at least one course this semester" (EXISTS); "students enrolled in nothing" (NOT EXISTS).
   - Misconception: *"EXISTS cares about the selected columns."* Correction: it only checks row existence; `SELECT *` or `SELECT 1` is equivalent.

2. **NOT EXISTS for "for all" queries**
   - Mini case: "students enrolled in *every* IT course" expressed via double NOT EXISTS (preview-level; flagged as advanced).
   - Local example: customers with **no** failed transactions → `NOT EXISTS (... WHERE status='failed')`.

3. **Test for absence of duplicate tuples (UNIQUE)**
   - Definition: `UNIQUE(subquery)` is TRUE if the subquery has no duplicate rows.
   - Snippet: `SELECT course_id FROM Course c WHERE UNIQUE (SELECT roll FROM Enrollment e WHERE e.course_id=c.course_id AND e.sem='2026S');`
   - Misconception: *"UNIQUE the constraint and UNIQUE the predicate are the same thing."* Correction: one is a table constraint (S22), the other is a subquery test.
   - Fun analogy: EXISTS = "is anyone in the room?"; UNIQUE = "is everyone in the room a different person?".

**Check for understanding:**
- MCQ1: `EXISTS` returns true when the subquery → returns at least one row ✅
- MCQ2: To find students with no enrollment at all, use → `NOT EXISTS` ✅
- Discussion: "Compare `IN` vs `EXISTS` — when does each read more naturally?"

**Real-life application:** "send a reminder to customers who have NOT placed any order this month" is a textbook NOT EXISTS query in retention systems.

**Summary:** (1) EXISTS tests for any row; (2) NOT EXISTS expresses "none/for-all"; (3) UNIQUE tests duplicate-freeness. **Next:** building reusable virtual tables — derived relations and views.

**Visual cues:** correlated-subquery arrow looping back to outer row; "EXISTS ↔ NOT EXISTS" mirror slide.

---

## S30 — Derived Relations · Views (CREATE VIEW, why views)  *(hands-on)*

**Hook:** "You keep typing the same 6-line join for the merit list. What if you could save it under one name and just call it `MeritList`?"

**Concepts & how each will be filled:**

1. **Derived relations (subqueries in FROM)**
   - Definition: a subquery used as a table; must be aliased.
   - Snippet: `SELECT dept, avg_sal FROM (SELECT dept, AVG(salary) AS avg_sal FROM Instructor GROUP BY dept) AS d WHERE avg_sal > 60000;`
   - Misconception: *"You can't put a query in FROM."* Correction: you can — it's a derived relation (must give it an alias).

2. **Views: CREATE VIEW**
   - Definition: a named, stored *query* — a virtual table computed on demand.
   - Snippet: `CREATE VIEW MeritList AS SELECT roll, name, marks FROM Student NATURAL JOIN Enrollment ORDER BY marks DESC;` then `SELECT * FROM MeritList;`
   - Local example: a view `BIMStudents` exposing only BIM rows to the BIM coordinator.

3. **Why views (3 reasons)**
   - Simplicity (hide complex joins), security (show only allowed columns/rows), consistency (one definition reused).
   - Local example: bank teller view hides salary/account-balance columns they shouldn't see → security.
   - Mini case: Nagarik App showing a citizen only *their own* records via a per-user filtered view.
   - Misconception: *"A view stores its own copy of the data."* Correction: a (standard) view stores the *query*, not the data — it re-runs each time (contrast with materialized views, noted briefly).
   - Fun analogy: a view = a saved filter / a "window" into the table — you see through it, you don't duplicate the room.

**Check for understanding:**
- MCQ1: A standard view stores → the query definition, not the data ✅
- MCQ2: Which is NOT a reason to use views? (a) security (b) faster disk (c) simplicity ✅(as the wrong-benefit) — *(correct answer: faster disk is NOT a guaranteed benefit)* → faster disk ✅
- Discussion: "What columns would you hide in a view of the Instructor table shown to students?"

**Real-life application:** dashboards and role-based screens (admin vs teacher vs student portals) are almost always built on views for security + reuse.

**Summary:** (1) a subquery in FROM = derived relation; (2) a view = saved named query; (3) views give simplicity, security, consistency. **Next:** changing the data itself — INSERT, UPDATE, DELETE.

**Visual cues:** "view = window into base tables" diagram; before/after of a 6-line join collapsing into `SELECT * FROM MeritList`.

---

## S31 — Modification of the Database: Insertion · Deletion · Updates  *(hands-on)*

**Hook:** "Reading data is safe. *Changing* it is where careers are made or broken — one forgotten WHERE can wipe a whole table."

**Concepts & how each will be filled:**

1. **INSERT**
   - Snippet: `INSERT INTO Student(roll,name,program,semester) VALUES (101,'Sita','BIM',4);` and bulk insert with `INSERT ... SELECT`.
   - Local example: registering a new student; topping up a Khalti wallet row.
   - Misconception: *"Column order doesn't matter."* Correction: VALUES must match the column list order (or all columns if list omitted).

2. **UPDATE**
   - Snippet: `UPDATE Enrollment SET grade='A' WHERE roll=101 AND course_id='IT220';`
   - Local example: instructor salary revision `UPDATE Instructor SET salary = salary*1.10 WHERE dept='IT';`
   - Misconception / **danger**: *"`UPDATE Enrollment SET grade='A';`"* (no WHERE) updates **every** row. Correction: always test the WHERE with a SELECT first.

3. **DELETE**
   - Snippet: `DELETE FROM Enrollment WHERE sem='2024F';`
   - Mini case: dropping a course → FK behaviour (ON DELETE CASCADE vs RESTRICT, callback to S22).
   - Misconception: *"DELETE and DROP are the same."* Correction: DELETE removes rows (DML), DROP removes the whole table (DDL).
   - Fun analogy: DELETE = erasing lines in a notebook; DROP = throwing out the notebook.

**Check for understanding:**
- MCQ1: `DELETE FROM Student;` (no WHERE) does what? → removes all rows ✅
- MCQ2: To change existing values use → UPDATE ✅
- Discussion: "Why is running a SELECT with your WHERE clause *before* an UPDATE/DELETE a lifesaving habit?"

**Real-life application:** every "edit profile", "cancel order", "refund" action in eSewa/Daraz is an UPDATE or DELETE — with safeguards (transactions, soft-deletes).

**Summary:** (1) INSERT adds rows; (2) UPDATE changes them; (3) DELETE removes them — and a missing WHERE is catastrophic. **Next:** what happens when you try to modify *through a view*.

**Visual cues:** big red "WHERE?" warning slide; INSERT/UPDATE/DELETE acting on the same sample table side-by-side.

---

## S32 — Update of a View (updatable vs non-updatable views)

**Hook:** "You built the `BIMStudents` view yesterday. Can you `INSERT` a new student *through* it? Sometimes yes, sometimes the database says no — why?"

**Concepts & how each will be filled:**

1. **Modifying through a view**
   - Definition: changes to a simple view can pass through to the base table.
   - Snippet: `UPDATE BIMStudents SET semester=5 WHERE roll=101;` → updates the underlying Student table.

2. **Updatable views (the rules)**
   - Single base table, no aggregates/DISTINCT/GROUP BY, includes the needed NOT NULL columns, no derived columns.
   - Local example: `BIMStudents` (simple filter) is updatable.

3. **Non-updatable views**
   - Views with joins, aggregates, or computed columns generally can't be updated unambiguously.
   - Mini case: a view `DeptAvgSalary` (GROUP BY dept) — "raise the average to 80k" is meaningless to push back to rows → non-updatable.
   - Misconception: *"Any view can be edited like a table."* Correction: only views meeting the updatability rules; aggregated/joined views usually aren't.
   - Fun analogy: a view over an aggregate is like trying to "un-bake" a cake back into eggs and flour — you can't reverse the summary.

4. **WITH CHECK OPTION (brief)**
   - Prevents inserting/updating rows that would fall *outside* the view's filter.
   - Snippet idea: inserting a 'BCA' student through `BIMStudents WITH CHECK OPTION` is rejected.

**Check for understanding:**
- MCQ1: Which view is typically NOT updatable? (a) simple column subset (b) GROUP BY aggregate view ✅ (c) single-table filter
- MCQ2: `WITH CHECK OPTION` prevents → inserting rows that violate the view's condition ✅
- Discussion: "Why can't the database update a view that groups instructors by department average?"

**Real-life application:** admin panels expose editable views; understanding updatability prevents "why won't my save go through?" bugs.

**Summary:** (1) simple views can be modified through; (2) aggregated/joined views usually can't; (3) WITH CHECK OPTION guards the filter. **Next:** the heart of relational power — joins.

**Visual cues:** decision-tree "Is this view updatable?"; arrow showing UPDATE passing through a simple view but blocked by an aggregate view.

---

## S33 — Joined Relations: Join Types & Conditions (INNER/LEFT/RIGHT/FULL OUTER, NATURAL, USING/ON)  *(hands-on)*

**Hook:** "Student names live in one table, their grades in another. The query that *stitches them together* is the single most-used statement in real SQL: the JOIN."

**Concepts & how each will be filled:**

1. **INNER JOIN (matched rows only)**
   - Snippet: `SELECT s.name, e.grade FROM Student s INNER JOIN Enrollment e ON s.roll = e.roll;`
   - Local example: list each student with the courses they're enrolled in.
   - Misconception: *"JOIN keeps everything."* Correction: INNER JOIN drops rows with no match on both sides.

2. **OUTER joins: LEFT / RIGHT / FULL**
   - LEFT = all left rows + matches (NULLs where none); RIGHT = mirror; FULL = both sides.
   - Snippet: `SELECT s.name, e.course_id FROM Student s LEFT JOIN Enrollment e ON s.roll=e.roll;` → includes students with **no** enrollment (course_id NULL).
   - Mini case: "all students, even those who registered for nothing" → LEFT JOIN (callback to NOT EXISTS, S29).
   - Local example: all eSewa registered users LEFT JOIN their transactions → users who never transacted show NULLs.

3. **Join conditions: ON vs USING vs NATURAL**
   - `ON` = explicit condition; `USING(col)` = same-named column shortcut; `NATURAL JOIN` = auto-match all same-named columns.
   - Snippet: `... NATURAL JOIN Enrollment` vs `... JOIN Enrollment USING(roll)`.
   - Misconception: *"NATURAL JOIN is always safe."* Correction: it silently joins on *every* common column name — surprising results if tables share unexpected column names.
   - Fun analogy: INNER = only friends who *both* showed up; LEFT = the whole left guest list, marking who their plus-one was (or blank).

**Check for understanding:**
- MCQ1: Which join keeps unmatched rows from the left table? → LEFT (OUTER) JOIN ✅
- MCQ2: `NATURAL JOIN` matches on → all columns with the same name ✅
- Discussion: "Daraz wants 'all products, including those never ordered.' INNER or LEFT join? Why?"

**Real-life application:** essentially every multi-table report (orders+customers, transactions+users) is a JOIN; outer joins surface the "missing"/inactive cases that businesses care about.

**Summary:** (1) INNER = matches only; (2) LEFT/RIGHT/FULL keep unmatched rows with NULLs; (3) ON/USING/NATURAL specify the match. **Next:** packaging logic on the server — stored procedures.

**Visual cues:** the classic JOIN Venn diagrams (INNER/LEFT/RIGHT/FULL); two sample tables → joined result with NULLs highlighted.

---

## S34 — Basic Concepts of Stored Procedures

**Hook:** "What if a 20-line enrollment routine — check seats, insert, update count — could be stored *in the database* and run with one call: `CALL enroll(101,'IT220');`?"

**Concepts & how each will be filled:**

1. **What a stored procedure is**
   - Definition: a named block of SQL (+ procedural logic) stored and executed on the server.
   - Snippet (shape only): `CREATE PROCEDURE enroll(IN r INT, IN c VARCHAR(10)) BEGIN INSERT INTO Enrollment(roll,course_id) VALUES(r,c); END;` → `CALL enroll(101,'IT220');`
   - Misconception: *"A procedure is just a saved SELECT (a view)."* Correction: views = virtual tables; procedures run multi-statement logic, accept parameters, and can modify data.

2. **Parameters (IN/OUT) & basic control flow**
   - IN/OUT/INOUT params; variables, IF, loops — mentioned at concept level (not deep coding).
   - Local example: a `transfer(from, to, amount)` procedure for an eSewa-style wallet move.

3. **Why use them**
   - Reuse, fewer round-trips (performance), centralized business logic, security (grant CALL not table access).
   - Mini case: bank fund-transfer as one procedure so the debit+credit always run together (links forward to transactions, Unit 6).
   - Fun analogy: a stored procedure = a saved recipe the kitchen runs on order, vs you dictating every step each time.

**Check for understanding:**
- MCQ1: A stored procedure is invoked using → `CALL` (or EXEC) ✅
- MCQ2: Main difference from a view? → procedure runs procedural logic / can modify data ✅
- Discussion: "Name one repeated operation in a college system worth turning into a stored procedure."

**Real-life application:** banks and fintechs push critical logic (transfers, interest calc) into stored procedures for consistency, security, and speed.

**Summary:** (1) procedure = stored, callable block of logic; (2) takes parameters, can modify data; (3) gives reuse, performance, security. **Next:** code that fires *automatically* — triggers — plus indexing for speed.

**Visual cues:** "app → CALL enroll() → server runs many statements" sequence diagram; procedure-vs-view comparison table.

---

## S35 — DML Triggers · Indexing  *(hands-on for indexing)*

**Hook:** "Every time a student is graded, the system should auto-log it — without the app remembering to. And when 'find roll 101' scans a million rows... why is it instant? Triggers and indexes."

**Concepts & how each will be filled:**

1. **DML triggers**
   - Definition: code that fires *automatically* on INSERT/UPDATE/DELETE (BEFORE/AFTER).
   - Snippet (shape): `CREATE TRIGGER log_grade AFTER UPDATE ON Enrollment FOR EACH ROW INSERT INTO GradeAudit(...) VALUES(OLD.grade, NEW.grade, NOW());`
   - Local example: auto-write to an audit table whenever a marks row changes (exam-integrity trail).
   - Misconception: *"You have to call a trigger."* Correction: triggers fire by themselves on the event — you never CALL them.

2. **OLD vs NEW & use cases**
   - Auditing, enforcing complex rules, auto-maintaining derived totals.
   - Mini case: a trigger that blocks marks > 100 (defence-in-depth alongside the CHECK from S22).

3. **Indexing (CREATE INDEX)**
   - Definition: an auxiliary structure (often B-tree) that speeds up lookups/sorts on a column.
   - Snippet: `CREATE INDEX idx_student_program ON Student(program);`
   - Fun analogy: an index = the index at the back of a textbook — find "DBMS" on page 212 instantly vs reading every page.

4. **When indexes help (and hurt)**
   - Help: frequent WHERE/JOIN/ORDER BY on that column. Hurt: slow down INSERT/UPDATE (index must be maintained), waste space if unused.
   - Local example: index `transactions(user_id)` so Khalti's history page loads fast.
   - Misconception: *"Index every column for speed."* Correction: over-indexing slows writes and bloats storage; index selectively.

**Check for understanding:**
- MCQ1: A trigger executes → automatically on a data-modification event ✅
- MCQ2: Indexes generally make ___ faster but ___ slower → reads faster, writes slower ✅
- Discussion: "Which column in the Enrollment table would you index, and why?"

**Real-life application:** audit triggers underpin compliance/fraud trails in fintech; correct indexing is the #1 reason a slow app page becomes fast.

**Summary:** (1) triggers auto-run on INSERT/UPDATE/DELETE; (2) indexes speed reads at the cost of write/space; (3) index selectively. **Next:** we pull all 15 sessions together in a recap + lab walkthrough.

**Visual cues:** trigger event-timeline (event → BEFORE → action → AFTER); "table scan vs index lookup" speed comparison diagram.

---

## S36 — SQL Recap + Lab Problem-Set Walkthrough  *(fully hands-on · closes Unit 5)*

**Hook:** "Fifteen sessions, one language. Today we take a blank database and a stack of real questions, and answer every one — live."

**Concepts & how each will be filled:**

1. **The SQL map (synthesis)**
   - One slide: DDL (define) → DML (query/modify) → views → joins → procedures/triggers/indexes; where each clause sits in the query pipeline (SELECT/FROM/WHERE/GROUP BY/HAVING/ORDER BY).
   - Callback grid linking each concept to its session (S22–S35).

2. **Guided lab problem set (graded difficulty, all on the college schema)**
   - Easy: "list all BIM students" (SELECT/WHERE, S23); "names starting with 'A'" (LIKE, S24).
   - Medium: "average marks per course" (GROUP BY, S26); "students with no enrollment" (LEFT JOIN / NOT EXISTS, S29/S33); "top 3 by marks" (ORDER BY + LIMIT, S25).
   - Hard: "students enrolled in every IT course" (NOT EXISTS, S29); "create a `MeritList` view and query it" (S30); "departments above average salary" (subquery, S28).
   - Each problem: state question → write SQL live → show result on seed data → note common mistakes.

3. **Common-mistakes review**
   - `= NULL` vs `IS NULL` (S27); missing WHERE on UPDATE/DELETE (S31); aggregate in WHERE vs HAVING (S26); NATURAL JOIN surprises (S33).

4. **Bridge to the lab project**
   - Tie to the syllabus lab project (individual/group ≤4): pick a domain (library, clinic, e-shop), design tables, write CRUD + reports.

**Check for understanding:**
- MCQ1: Correct clause order? → SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY ✅
- MCQ2: "Find rows where email is missing" uses → `IS NULL` ✅
- Discussion: "Pick a Nepali app and list 3 SQL queries its database must answer every day."

**Real-life application:** this problem-solving fluency *is* the marketable skill — SQL appears in nearly every data/backend job posting in Nepal and abroad.

**Summary:** (1) DDL builds, DML uses, views/joins/procedures/triggers/indexes extend; (2) clause order and NULL/WHERE habits prevent the classic bugs; (3) you can now read and write production-style SQL. **Next unit:** keeping data correct when many users hit it at once — transactions, concurrency & recovery (Unit 6).

**Visual cues:** the full "SQL pipeline" master diagram; live-coding screen; problem → query → result table for each lab item.

---

## END-OF-UNIT QUIZ — Unit 5: SQL (consolidated)
*Suggested: 20 MCQs + 5 short SQL-writing tasks. Mix recall + application. Answers marked ✅.*

### Part A — Concept MCQs
1. `CREATE TABLE` belongs to: (a) DML (b) DDL ✅ (c) DCL (d) TCL
2. Which is `PRIMARY KEY` equivalent to? → UNIQUE + NOT NULL ✅
3. To store NPR currency precisely, best type is: (a) FLOAT (b) DECIMAL ✅ (c) VARCHAR (d) INT
4. Which clause filters rows? → WHERE ✅
5. `SELECT` chooses: (a) rows (b) columns ✅
6. `LIKE '%a'` matches names that: → end with 'a' ✅
7. `_` in LIKE matches: → exactly one character ✅
8. Default ORDER BY direction: → ascending ✅
9. Which removes duplicates? (a) UNION ALL (b) UNION ✅
10. `INTERSECT` returns: → rows in both result sets ✅
11. Which can appear in WHERE? (a) `COUNT(*)>5` (b) `salary>5000` ✅
12. HAVING filters: → groups ✅
13. `WHERE grade = NULL` returns: → no rows ✅ (use IS NULL)
14. `COUNT(*)` vs `COUNT(col)` differ when: → col has NULLs ✅
15. `> ALL(subquery)` is true when value exceeds: → every value ✅
16. `EXISTS` is true when subquery: → returns ≥1 row ✅
17. A standard view stores: → the query, not the data ✅
18. A non-updatable view typically contains: → GROUP BY / aggregate / join ✅
19. `LEFT JOIN` keeps unmatched rows from: → the left table ✅
20. A DML trigger runs: → automatically on INSERT/UPDATE/DELETE ✅
21. Indexes typically make reads ___ and writes ___ : → faster / slower ✅
22. `CALL` is used to invoke a: → stored procedure ✅

### Part B — Write the SQL (on the college schema)
1. List name and program of all 4th-semester BIM students. *(SELECT/WHERE — S23)*
2. Show the average marks per course, only for courses with more than 30 students. *(GROUP BY + HAVING — S26)*
3. List students who have **no** enrollment. *(LEFT JOIN or NOT EXISTS — S29/S33)*
4. Find the name(s) of the highest-paid instructor. *(subquery `>= ALL` or MAX — S28)*
5. Create a view `MeritList(roll, name, marks)` sorted by marks descending, then select from it. *(CREATE VIEW — S30)*
6. Increase IT-department instructor salaries by 10%. *(UPDATE with WHERE — S31)*

### Part C — Short answer / discussion
- Explain the difference between `WHERE` and `HAVING` with one example each.
- Why is `IS NULL` required instead of `= NULL`? (three-valued logic)
- Give one real Nepali-app scenario each for INNER JOIN and LEFT JOIN.
- When would you add an index, and what is its cost?

---

## Open questions before I generate Unit 5 material
1. Keep the **college DB schema** (Student/Course/Enrollment/Instructor/Teaches) as the running example, or swap to a domain closer to the lab project (e.g. an e-shop / library)?
2. Target DBMS for snippets/labs — **MySQL** or **PostgreSQL**? (Affects string concat `||` vs `CONCAT`, `LIMIT` vs `TOP`, EXCEPT vs MINUS.)
3. S34/S35 (procedures, triggers, indexing) — keep at **concept depth** as outlined, or expand to full coding labs given they're exam-light but job-relevant?
4. End-of-unit quiz size — is **~22 MCQ + 6 SQL tasks + short answers** about right, or do you want it shorter/longer?
5. Should every "hands-on" session ship with a ready-to-run **seed-data SQL file** so students can follow along live?
