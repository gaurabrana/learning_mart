# IT 220 — Unit 5: SQL
### Full Lecturer-Ready + Student-Revision Material

**Program:** BIM, 4th Semester · **Credits:** 3 · **Unit weight:** 15 lecture hours
**Sessions:** S22–S36 (50 min each) · **Local context:** Nepal / South Asia
**Format:** Markdown — source of truth; the built deck is `IT220_Unit5.pptx` (219 slides), regenerated via `build_unit5_pptx.py` (imports `deckkit.py`).

> Same two-reader format as Units 1–4. SQL is hands-on, so most sessions end at a **live SQL editor**
> and lean on **worked-query tables** and **solved-problem walkthroughs**. Dialect throughout:
> **MySQL / MariaDB** (note the `CONCAT` vs `||`, `LIMIT`, `AUTO_INCREMENT` specifics).
>
> **Running sample schema (one tiny college database, threaded through ALL sessions S22–S36):**
> ```sql
> Student(roll PK, name, program, semester, dob, email)
> Course(course_id PK, title, credits, dept)
> Instructor(inst_id PK, name, dept, salary)
> Enrollment(roll FK→Student, course_id FK→Course, sem, grade, marks)   -- PK(roll, course_id, sem)
> Teaches(inst_id FK→Instructor, course_id FK→Course, sem)
> ```
> **Seed data (identical every session so results are predictable):**
> Student — 101 Sita BIM s4 · 102 Hari BIM s4 · 103 Bishal BCA s4 · 104 Anjali BIM s6 · 105 Gita BCA s2.
> Course — IT220 DBMS 3 IT · MGT201 Mgmt 3 MGT · ECO101 Econ 3 ECO · IT250 DigiEcon 3 IT.
> Instructor — 11 Sharma IT 80000 · 12 Karki IT 60000 · 13 Thapa MGT 70000 · 14 Rai ECO NULL.
> Enrollment — e.g. 101 IT220 2026S A 88 · 102 IT220 2026S NULL NULL …

---

**📊 Depth table — The running sample schema (a tiny college database, used in every session)**

| Table | Columns (PK in bold, FK →) | One seed row (example data) |
|---|---|---|
| Student | roll · name · program · semester · dob · email | 101 · Sita · BIM · 4 · 2004-05-12 · sita@pu.edu.np |
| Course | course_id · title · credits · dept | IT220 · DBMS · 3 · IT |
| Instructor | inst_id · name · dept · salary | 11 · Sharma · IT · 80000 |
| Enrollment | roll → · course_id → · sem · grade · marks | 101 · IT220 · 2026S · A · 88 |
| Teaches | inst_id → · course_id → · sem | 11 · IT220 · 2026S |

*ℹ️ Pin this schema on every session. Seed data: ~5 students (Sita, Hari, Bishal, Anjali, Gita), 4 courses, 4 instructors. Same rows every session → predictable query results.*

---

## Unit 5 — Learning Outcomes
1. Define a schema with correct data types and all constraints (PK/FK/CHECK/NOT NULL/UNIQUE), and alter/drop it (S22).
2. Write SELECT queries with FROM/WHERE, renaming, tuple variables, and string/pattern operations (S23–S24).
3. Sort, de-duplicate, and combine result sets with ORDER BY, DISTINCT, UNION/INTERSECT/EXCEPT (S25).
4. Summarize data with aggregates, GROUP BY / HAVING, and reason correctly about NULLs & three-valued logic (S26–S27).
5. Write nested subqueries with IN, SOME/ALL, EXISTS/NOT EXISTS, UNIQUE (S28–S29).
6. Create and use views & derived relations and explain which views are updatable (S30, S32).
7. Modify data (INSERT/UPDATE/DELETE) and join tables with every join type (S31, S33).
8. Explain stored procedures, DML triggers, and indexes — and when each helps (S34–S35).

**Roadmap:** S22 DDL/constraints · S23 SELECT/FROM/WHERE · S24 rename/aliases/strings · S25 ORDER BY/DISTINCT/sets · S26 aggregates/GROUP BY/HAVING · S27 NULL & 3VL · S28 subqueries IN/SOME/ALL · S29 EXISTS/UNIQUE · S30 derived relations/views · S31 INSERT/UPDATE/DELETE · S32 view updatability · S33 joins · S34 stored procedures · S35 triggers/indexing · S36 recap + lab walkthrough. **Next:** Unit 6 — Transactions, concurrency & recovery.

---
---

# S22 — DDL · Data Types · Constraints · Schema Definition
**Lecture hour 1 (of 15) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`
[SLIDE] *"Before you can ask the database anything, you have to tell it what a student even IS. Today we build the boxes; from tomorrow we fill and query them."* → agenda: DDL & CREATE TABLE → data types → constraints → ALTER/DROP.

### 📚 CONTENT `[~35 min]`

#### Concept 1 — DDL & CREATE TABLE `[THEORY]` `[SNIPPET]` `[~9 min]`
**📖 In Depth.** **DDL (Data Definition Language)** is the SQL sub-language that **defines structure** — `CREATE`, `ALTER`, `DROP`. `CREATE TABLE` makes an **empty** table: you name it, list its columns, and give each column a data type. It creates the **structure only** — an empty shell with zero rows. Column order in the definition is the table's natural column order. DDL changes the **schema** (rare, big); DML (from S23 on) changes the **data** (constant).

Worked example:
```sql
CREATE TABLE Student(roll INT PRIMARY KEY, name VARCHAR(50), program VARCHAR(20));
```
A freshly created table returns nothing from `SELECT *` until you `INSERT` rows.

> **🌍 Real life.** Every backend feature at eSewa, Khalti, or a college portal begins with a **migration** — a `CREATE TABLE` (or `ALTER TABLE`) that defines where the new data will live. Building the Student table for a Pokhara University BIM intake is a literal day-1 job task.

> **🎯 Model exam answer.** *"What is DDL / CREATE TABLE?"* DDL defines database structure via CREATE, ALTER, and DROP. CREATE TABLE names a table and declares its columns with data types and constraints, producing an **empty** table. It changes the schema, not the data — inserting rows is a separate DML step.

> **🧠 Hook:** "CREATE TABLE builds an empty box — it does not put anything in it."

> **⚠️ Misconception.** *"CREATE TABLE also adds the data."* No — CREATE TABLE makes an empty structure with zero rows. Putting data in is a separate `INSERT` (S31).

> **🔑 Key terms:** DDL · CREATE / ALTER / DROP TABLE · schema vs data · empty structure.

**📊 Depth table — The three DDL commands — define, change, remove**

| DDL command | What it does | College example (MySQL) |
|---|---|---|
| CREATE TABLE | Make a new empty table | CREATE TABLE Course(course_id VARCHAR(6) PRIMARY KEY, title VARCHAR(40)); |
| ALTER TABLE | Change an existing table's structure | ALTER TABLE Student ADD email VARCHAR(60); |
| DROP TABLE | Delete a whole table + its data | DROP TABLE Teaches; |
| TRUNCATE TABLE | Empty a table but keep its structure | TRUNCATE TABLE Enrollment; |
| CREATE DATABASE | Make a new database to hold tables | CREATE DATABASE college; |
| SHOW / DESCRIBE | Inspect structure (MySQL helpers) | DESCRIBE Student; |

*ℹ️ DDL is about STRUCTURE. Note DROP removes the table itself; TRUNCATE only empties it. Both differ from DELETE (a DML row-remover, S31).*

---

#### Concept 2 — Data / Domain Types `[THEORY]` `[SNIPPET]` `[~9 min]`
**📖 In Depth.** A **data type** is the **domain** of a column — the set of values it may hold. Choosing the right type enforces correctness and saves space. Core MySQL types: **INT** (whole numbers — roll, credits), **DECIMAL(p,s)** (exact money — NPR fees), **VARCHAR(n)** (variable-length text up to n) / **CHAR(n)** (fixed length, padded), **DATE** (calendar dates — dob), **BOOLEAN** (true/false flags). **Never store money as FLOAT** — binary rounding corrupts fee/amount totals. Phone numbers are **VARCHAR**, not INT (leading 0 in 98XXXXXXXX, and '+977').

> **🌍 Real life.** eSewa/Khalti store wallet balances as DECIMAL (precise to the paisa), phone numbers as VARCHAR (to keep the leading 0 and '+977'), and timestamps as DATETIME. A fee table storing amounts as FLOAT would slowly drift by paisa across millions of rows — a real accounting bug.

> **🎯 Model exam answer.** *"What is a data type / domain?"* A data type declares a column's domain — the values it may hold — enforcing correctness and controlling storage. Common MySQL types: INT, DECIMAL(p,s) for exact money, VARCHAR(n)/CHAR(n) for text, DATE/DATETIME, BOOLEAN. Money uses DECIMAL (not FLOAT); phone numbers use VARCHAR (not INT) to preserve leading zeros.

> **🧠 Hook:** "Data type = the size of the tiffin box — wrong size wastes space or won't fit."

> **⚠️ Misconception.** *"FLOAT is fine for money."* FLOAT/DOUBLE are binary approximations: 0.1 + 0.2 is not exactly 0.3, so totals drift. Use DECIMAL(p,s) for any currency or exact amount; reserve FLOAT for scientific measurements where tiny error is acceptable.

> **🔑 Key terms:** data type / domain · INT · DECIMAL(p,s) · VARCHAR vs CHAR · DATE · money≠FLOAT · phone≠INT.

**📊 Depth table — Pick the right type — column → type → why (Nepal / IT)**

| Column | Right type (MySQL) | Wrong type | Why the wrong one breaks |
|---|---|---|---|
| roll (student ID) | INT | VARCHAR | numeric compare/sort as text mis-orders |
| fee amount (NPR) | DECIMAL(10,2) | FLOAT | binary rounding loses paisa in totals |
| phone (98XXXXXXXX) | VARCHAR(15) | INT | leading 0 and '+977' are lost |
| name | VARCHAR(50) | CHAR(50) | CHAR pads with spaces, wastes space |
| program code (e.g. 'BIM') | CHAR(3) | VARCHAR(3) | fixed-width code is ideal for CHAR |
| date of birth | DATE | VARCHAR | can't do date math or range filters |
| is_active flag | BOOLEAN | VARCHAR('yes') | free-text values drift ('Y','yes','TRUE') |

*ℹ️ The type is a first line of defence: it rejects wrong-shaped data before any constraint runs. Money = DECIMAL, identifiers with leading zeros = VARCHAR.*

---

#### Concept 3 — Specifying Constraints `[THEORY]` `[SNIPPET]` `[~9 min]`
**📖 In Depth.** A **constraint** is a rule the DBMS enforces on **every row**, rejecting data that breaks it. The six you must know: **PRIMARY KEY** (= UNIQUE + NOT NULL, one per table, identifies each row), **FOREIGN KEY** (links to another table's PK; optional `ON DELETE CASCADE/RESTRICT`), **NOT NULL** (forbids blanks), **UNIQUE** (forbids duplicates but allows one NULL), **CHECK** (validates a condition, e.g. marks 0–100), and **DEFAULT** (supplies a value if none given). Constraints move data-integrity rules into the database, so bad data is rejected regardless of which app inserts it.

> **🌍 Real life.** A college DB uses `FOREIGN KEY (roll) REFERENCES Student(roll)` so nobody can enroll a student who doesn't exist; `email VARCHAR(60) UNIQUE` so two accounts can't share an email; and `CHECK (marks BETWEEN 0 AND 100)` so a typo of 780 is rejected at the database, not just in the app.

> **🎯 Model exam answer.** *"List the constraints."* PRIMARY KEY (unique + not null, one per table), FOREIGN KEY (must match a parent row, with ON DELETE options), NOT NULL, UNIQUE, CHECK (a condition), and DEFAULT. They enforce integrity at the DB level.

> **🧠 Hook:** "A constraint is a bouncer at the door — bad data never gets in."

> **⚠️ Misconception.** *"PRIMARY KEY and UNIQUE are the same."* Not quite: PRIMARY KEY = UNIQUE + NOT NULL and there is only ONE per table; a table can have MANY UNIQUE columns, and UNIQUE still allows a single NULL. PK identifies the row; UNIQUE just prevents duplicate values.

> **🔑 Key terms:** PRIMARY KEY · FOREIGN KEY · NOT NULL · UNIQUE · CHECK · DEFAULT · PK = UNIQUE + NOT NULL.

**📊 Depth table — The six constraints — what each enforces (and PK vs UNIQUE)**

| Constraint | Rule it enforces | Duplicates? | NULLs? | College example |
|---|---|---|---|---|
| PRIMARY KEY | uniquely identifies a row | no | no | Student.roll |
| FOREIGN KEY | value must exist in parent table | depends | depends | Enrollment.course_id → Course |
| NOT NULL | value must be present | yes | no | Student.name NOT NULL |
| UNIQUE | no two rows share the value | no | one NULL ok | email VARCHAR(60) UNIQUE |
| CHECK | value satisfies a condition | yes | yes | CHECK (marks BETWEEN 0 AND 100) |
| DEFAULT | fills a value if none supplied | yes | - | semester INT DEFAULT 1 |

*ℹ️ The classic exam line: PRIMARY KEY = UNIQUE + NOT NULL, and only one per table. NOT NULL forbids blanks but ALLOWS duplicates; UNIQUE forbids duplicates but allows one blank.*

---

#### Concept 4 — Schema Definition: ALTER & DROP `[THEORY]` `[SNIPPET]` `[~8 min]`
**📖 In Depth.** **ALTER TABLE** changes an existing table's structure **without recreating it**; **DROP TABLE** deletes a table and all its data. These evolve a live schema safely as requirements change. `ALTER TABLE Student ADD email VARCHAR(60);` adds a column, keeping all rows; ALTER can also `MODIFY` a column's type or `DROP` a single column. `DROP TABLE Enrollment;` removes the whole table — structure and data — permanently. Adding a column mid-semester uses ALTER, never a re-create (which would lose data).

> **🌍 Real life.** Mid-semester, a college decides to email results, so it needs an email column. `ALTER TABLE Student ADD email VARCHAR(60);` adds it to all 5,000 existing rows instantly, no data lost. Re-creating the table instead would mean dropping every student first — a disaster.

> **🎯 Model exam answer.** *"Contrast ALTER and DROP."* ALTER TABLE modifies an existing table's structure in place — ADD/MODIFY/DROP a column — while preserving its rows. DROP TABLE permanently deletes the table and all its data. Schema evolution uses ALTER so existing data is retained; DROP is reserved for retiring a table entirely.

> **🧠 Hook:** "ALTER = renovate the room; DROP = demolish the building."

> **⚠️ Misconception.** *"To add a column I must drop and recreate the table."* That would destroy all existing rows. ALTER TABLE changes structure in place, keeping the data. Only use DROP when you genuinely want the table and its contents gone.

> **🔑 Key terms:** ALTER TABLE · ADD/MODIFY/DROP COLUMN · DROP TABLE · schema evolution · preserve data.

**📊 Depth table — ALTER vs DROP vs TRUNCATE — same table, very different effect**

| Statement (MySQL) | What survives | When you'd use it |
|---|---|---|
| ALTER TABLE Student ADD phone VARCHAR(15); | all rows + all old columns | add a field mid-semester |
| ALTER TABLE Student MODIFY name VARCHAR(80); | all rows, name column widened | names were getting truncated |
| ALTER TABLE Student DROP COLUMN dob; | all rows, minus that column | stop storing a field |
| TRUNCATE TABLE Enrollment; | the table structure, zero rows | wipe test data, keep the table |
| DROP TABLE Teaches; | nothing — table + data gone | retire a table permanently |

*ℹ️ ALTER preserves data while changing structure; TRUNCATE keeps structure but empties data; DROP destroys both. Always back up before DROP/TRUNCATE on live data.*

---

#### 🛠 SOLVED PROBLEM (deck) — Define the Enrollment table with every constraint kind
**Problem.** Write MySQL DDL for `Enrollment(roll, course_id, sem, grade, marks)`. Roll and course_id are foreign keys to Student and Course; the primary key is (roll, course_id, sem); marks must be 0–100; grade may be blank.

**Walkthrough.**
1. Start the table and list columns with types: `roll INT`, `course_id VARCHAR(6)`, `sem VARCHAR(5)`, `grade CHAR(2)`, `marks INT`.
2. Add the CHECK: `marks INT CHECK (marks BETWEEN 0 AND 100)` — rejects a typo like 780.
3. Declare the composite key: `PRIMARY KEY (roll, course_id, sem)` — a student takes a course once per semester.
4. Link the parents: `FOREIGN KEY (roll) REFERENCES Student(roll)`, `FOREIGN KEY (course_id) REFERENCES Course(course_id)`.
5. Leave grade nullable (mid-semester it is unknown) — do NOT add NOT NULL to it.

**Answer.**
```sql
CREATE TABLE Enrollment(roll INT, course_id VARCHAR(6), sem VARCHAR(5), grade CHAR(2),
  marks INT CHECK (marks BETWEEN 0 AND 100),
  PRIMARY KEY (roll,course_id,sem),
  FOREIGN KEY (roll) REFERENCES Student(roll),
  FOREIGN KEY (course_id) REFERENCES Course(course_id));
```
Note the composite PK and that grade stays nullable — it becomes the NULL example in S27.

#### 🛠 ACTIVITY `[~5 min]`
Design an eSewa Wallet table: list 3 columns, pick a data type AND one constraint for each, and justify both. Strong answers: `wallet_id INT PRIMARY KEY`; `balance DECIMAL(12,2) NOT NULL DEFAULT 0 CHECK (balance >= 0)`; `phone VARCHAR(15) UNIQUE NOT NULL`.

### 🧠 CHECK FOR UNDERSTANDING `[~5 min]`
- MCQ1: Which constraint forbids empty values but ALLOWS duplicates? → ✅ NOT NULL (NOT NULL only requires a value; it says nothing about duplicates).
- MCQ2: `DROP TABLE` belongs to which sub-language? → ✅ DDL (it defines/removes structure, like CREATE and ALTER).
- MCQ3: To store NPR fee amounts precisely, the best type is → ✅ DECIMAL(10,2) (exact; FLOAT drifts across many rows).
- Discussion: pick a Nepali app and name one table it needs, with a data type + constraint per column.

### 💡 REAL-LIFE APPLICATION `[~3 min]`
Every migration you ever write at a fintech or a college portal is DDL. Getting types and constraints right on day one prevents whole classes of bugs later — it is the difference between a database that protects your data and one that quietly corrupts it.

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
(1) DDL (CREATE/ALTER/DROP) defines structure; CREATE TABLE makes an EMPTY table. (2) Pick the right data type per column — DECIMAL for money, VARCHAR for phones/IDs with leading zeros. (3) Constraints (PK, FK, NOT NULL, UNIQUE, CHECK, DEFAULT) enforce integrity at the DB; PK = UNIQUE + NOT NULL. **Next:** now that the boxes exist, we ask questions of them — SELECT, FROM, WHERE.

---
---

# S23 — DML Basics: SELECT · FROM · WHERE
**Lecture hour 2 (of 15) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`
[SLIDE] *"There are millions of rows in a telecom's customer table. How do you pull JUST the Ncell users in Pokhara? One sentence of SQL."* → agenda: SELECT…FROM → WHERE → multi-table FROM (cross-product warning).

### 📚 CONTENT `[~35 min]`

#### Concept 1 — The Basic Query: SELECT … FROM … `[THEORY]` `[SNIPPET]` `[~8 min]`
**📖 In Depth.** The simplest query names **which columns** (`SELECT`) **from which table** (`FROM`). SELECT performs **projection** — it chooses **columns, not rows**. `SELECT name, program FROM Student;` returns two columns for every student; `SELECT * FROM Course;` returns ALL columns of every course. Column order in SELECT is the output order (independent of the table's order). It returns **every row** of the table unless a WHERE clause filters rows.

> **🌍 Real life.** Every list screen you see — a Daraz product grid, your eSewa transaction history, a college course catalogue — is a SELECT of specific columns FROM a table. The app rarely shows `SELECT *`; it picks exactly the columns the screen needs.

> **🎯 Model exam answer.** *"What is a basic query?"* `SELECT <columns> FROM <table>`. FROM names the source table(s); SELECT projects the chosen columns (`SELECT *` means all columns). It returns every row unless a WHERE clause filters rows — SELECT controls columns, not rows.

> **🧠 Hook:** "SELECT = which columns · FROM = which table. It projects, it doesn't filter rows."

> **⚠️ Misconception.** *"SELECT chooses which rows I get."* No — SELECT chooses COLUMNS (projection). Without a WHERE clause, you still get every row; you have just narrowed the columns. Row filtering is WHERE's job.

> **🔑 Key terms:** SELECT (projection) · FROM · SELECT * · columns not rows.

**📊 Depth table — Reading a SELECT — query → what comes back**

| Query (MySQL) | Columns returned | Rows returned |
|---|---|---|
| SELECT * FROM Student; | all 6 columns | all students |
| SELECT name FROM Student; | just name | all students (one column) |
| SELECT name, program FROM Student; | name + program | all students |
| SELECT title, credits FROM Course; | title + credits | all courses |
| SELECT DISTINCT program FROM Student; | program, de-duplicated | one per program (S25) |
| SELECT roll, marks FROM Enrollment; | roll + marks | every enrollment row |

*ℹ️ SELECT decides the COLUMNS (and their order). Without a WHERE clause you always get every row — projection alone never removes rows.*

---

#### Concept 2 — The WHERE Clause (Filtering Rows) `[THEORY]` `[SNIPPET]` `[~9 min]`
**📖 In Depth.** **WHERE** keeps only the rows whose condition is **TRUE**. It supports comparison operators (`=`, `<>`, `<`, `>=`), logical operators (`AND`, `OR`, `NOT`), and the shortcuts `BETWEEN` (inclusive range) and `IN` (list membership). `SELECT name FROM Student WHERE program='BIM' AND semester=4;` `<>` (or `!=`) means "not equal". Only rows evaluating to TRUE are kept (UNKNOWN/NULL rows are dropped — S27).

> **🌍 Real life.** Every search box, filter chip, and report is a WHERE underneath: Daraz 'price Rs 500–1500 AND category = phones', a telecom pulling 'Ncell users in Pokhara', a bank listing 'transactions above Rs 1,00,000 today'.

> **🎯 Model exam answer.** *"What does WHERE do?"* The WHERE clause filters rows, keeping only those whose condition evaluates to TRUE. It uses comparison operators, logical operators (AND/OR/NOT), and the shortcuts BETWEEN and IN. WHERE selects rows; SELECT selects columns.

> **🧠 Hook:** "WHERE is the row filter — it decides who stays and who is dropped."

> **⚠️ Misconception.** *"Adding more AND conditions returns more rows."* The opposite: each AND is more restrictive, so results shrink. OR broadens (more rows); AND narrows (fewer rows). Group mixed AND/OR with parentheses.

> **🔑 Key terms:** WHERE · comparison operators · AND/OR/NOT · BETWEEN · IN · keeps TRUE rows.

**📊 Depth table — WHERE conditions — operator → query → who is kept**

| Goal | WHERE condition (MySQL) | Rows kept |
|---|---|---|
| BIM 4th-sem students | program='BIM' AND semester=4 | Sita, Hari |
| IT instructors paid > 60k | dept='IT' AND salary > 60000 | Sharma |
| Daraz items Rs 500–1500 | price BETWEEN 500 AND 1500 | mid-range products |
| Courses in IT or ECO dept | dept IN ('IT','ECO') | IT220, IT250, ECO101 |
| Students NOT in BIM | program <> 'BIM' | Bishal, Gita |
| Marks below pass (40) | marks < 40 | failing enrollments |
| High marks OR is BIM | marks >= 80 OR program='BIM' | toppers + all BIM |

*ℹ️ Comparison (=,<>,<,>=), logical (AND/OR/NOT), and the shortcuts BETWEEN (inclusive range) and IN (list membership) build every filter. WHERE keeps only TRUE rows.*

---

#### Concept 3 — Multiple Tables in FROM (Cross-Product Warning) `[THEORY]` `[SNIPPET]` `[~8 min]`
**📖 In Depth.** Listing two tables in FROM **without a join condition** produces a **Cartesian (cross) product**: every row of one table paired with every row of the other. `FROM Student, Enrollment` with no condition = rows(Student) × rows(Enrollment). Add `WHERE Student.roll = Enrollment.roll` to keep only matching pairs — this equality is the **join condition** (explicit `JOIN` syntax comes in S33). 5 students × 8 enrollments = 40 meaningless rows without the condition.

> **🌍 Real life.** A mark-sheet needs a student's name (Student table) beside their grade (Enrollment table). `FROM Student, Enrollment WHERE Student.roll = Enrollment.roll` stitches them correctly; dropping that WHERE would pair every student with every enrollment — nonsense a marksheet must never show.

> **🎯 Model exam answer.** *"What is a cross product?"* Listing multiple tables in FROM without a condition yields a Cartesian product — every row of one paired with every row of the other. Adding a join condition (e.g. `WHERE Student.roll = Enrollment.roll`) keeps only the meaningful matched pairs. This implicit join foreshadows the explicit JOIN syntax of S33.

> **🧠 Hook:** "Two tables with no condition = every-row-times-every-row. Always add the match."

> **⚠️ Misconception.** *"Listing two tables just merges them sensibly."* It does NOT — you get a cross product (every combination) unless you add the join condition. Two 1,000-row tables become 1,000,000 rows.

> **🔑 Key terms:** cross / Cartesian product · join condition · multi-table FROM · matching rows.

**📊 Depth table — Cross product vs a proper join condition**

| Query | What it does | Result size (seed data) |
|---|---|---|
| FROM Student, Enrollment (no WHERE) | pairs EVERY student with EVERY enrollment | 5 × 8 = 40 rows (garbage) |
| ...WHERE Student.roll = Enrollment.roll | keeps only matching student+enrollment | 8 sensible rows |
| SELECT name, grade FROM Student, Enrollment WHERE Student.roll=Enrollment.roll | each student with their grade | 8 rows |
| FROM Course, Teaches (no condition) | every course × every teaching row | cross product |
| ...WHERE Course.course_id=Teaches.course_id | each course with its instructor link | matched rows only |

*ℹ️ Forgetting the join condition is the classic beginner disaster — a huge, meaningless result. The condition (roll = roll) is what makes a multi-table query correct.*

---

#### 🛠 ACTIVITY `[~5 min]`
Translate English to WHERE: write conditions for 'Khalti users who joined in 2025 AND live in Kathmandu' and 'products priced Rs 500–1500 OR on clearance'. Answers: `WHERE YEAR(joined)=2025 AND city='Kathmandu'`; `WHERE price BETWEEN 500 AND 1500 OR clearance=TRUE`.

### 🧠 CHECK FOR UNDERSTANDING `[~5 min]`
- MCQ1: Which clause filters ROWS? → ✅ WHERE (SELECT only picks columns).
- MCQ2: `SELECT * FROM Student;` returns → ✅ all columns, all rows (`*` = all columns, no WHERE = every row).
- MCQ3: `FROM Student, Enrollment` with no condition gives → ✅ a cross product (every combination).
- Discussion: name a screen in a Nepali app and write the SELECT…WHERE behind it.

### 💡 REAL-LIFE APPLICATION `[~3 min]`
Every filter, search, and report in every app you will ever build is a SELECT…WHERE. This is the single most-used shape in all of SQL — fluency here pays off in literally every data or backend job.

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
(1) SELECT picks COLUMNS (projection); FROM picks the table; WHERE picks ROWS. (2) WHERE uses =,<>,<,>=, AND/OR/NOT, BETWEEN, IN to keep only TRUE rows. (3) Listing tables in FROM without a join condition = a dangerous cross product. **Next:** renaming things and searching inside text — AS, tuple variables, and LIKE.

---
---

# S24 — Rename · Tuple Variables · String Operations
**Lecture hour 3 (of 15) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`
[SLIDE] *"When you join the Student table TO ITSELF to find classmates, both copies are called 'Student'. How does SQL tell them apart?"* → agenda: AS (rename) → tuple variables (aliases & self-joins) → string ops (LIKE, wildcards, CONCAT).

### 📚 CONTENT `[~35 min]`

#### Concept 1 — The Rename Operation (AS) `[THEORY]` `[SNIPPET]` `[~7 min]`
**📖 In Depth.** **AS** renames a column or table in the **output** (or for the query's duration) so results are readable and expressions get a name. The underlying table is **unchanged**. `SELECT name AS student_name, marks AS score FROM Enrollment;` AS on a computed column gives it a header: `marks*1.0/100 AS fraction`. The AS keyword is **optional** in MySQL (`name student_name` works) but clearer with it. It renames only the result — the stored column name never changes.

> **🌍 Real life.** A college marksheet export must show headers like 'Student Name' and 'Percentage', not the raw column names 'name' and a formula. `SELECT name AS 'Student Name', marks*1.0 AS 'Percentage'` produces a report humans can read, without touching the stored schema.

> **🎯 Model exam answer.** *"What is the rename operation?"* AS gives a column, expression, or table a new name for the query's output or duration. It makes reports readable, names computed and aggregate columns, and provides short table aliases — without altering the stored schema. In MySQL the AS keyword is optional but recommended.

> **🧠 Hook:** "AS = a nickname for output — the real column keeps its name."

> **⚠️ Misconception.** *"Renaming with AS changes the column in the table."* It does not — AS only labels the result set for this query. The stored column name is unchanged; the next query still sees the original name.

> **🔑 Key terms:** rename · AS · column alias · expression alias · table alias · output only.

**📊 Depth table — AS in action — expression → readable output header**

| Query fragment | Output header | Why rename |
|---|---|---|
| SELECT name AS "Student Name" | Student Name | human-readable report column |
| marks AS score | score | clearer than 'marks' in context |
| marks*1.0 AS percentage | percentage | computed column needs a name |
| COUNT(*) AS total_students | total_students | aggregates have no natural name (S26) |
| salary*12 AS annual_salary | annual_salary | label the derived value |
| Student AS s | (table alias s) | short name for multi-table queries |

*ℹ️ Rename columns for readable reports and to NAME computed/aggregate values (which otherwise get an ugly auto-name). Renaming a TABLE (Student AS s) leads straight into tuple variables.*

---

#### Concept 2 — Tuple Variables (Table Aliases) `[THEORY]` `[SNIPPET]` `[~9 min]`
**📖 In Depth.** A **tuple variable** is a short alias bound to a table (`Student s`). It shortens multi-table queries and is **MANDATORY for a self-join**, where a table is joined to itself and both copies need distinct names. `SELECT s.name, e.grade FROM Student s, Enrollment e WHERE s.roll = e.roll;` — prefix columns with the alias (`s.name`) to say which table you mean. Self-join: `FROM Student s1, Student s2` — two independent handles on one table. Without distinct aliases, a self-join is ambiguous and errors.

> **🌍 Real life.** To find everyone in Sita's program, you compare Student against itself: `FROM Student s1, Student s2 WHERE s2.name='Sita' AND s1.program=s2.program AND s1.roll<>s2.roll`. The two aliases s1 and s2 are the only way to hold two rows of the same table at once.

> **🎯 Model exam answer.** *"What is a tuple variable?"* A table alias — a short name bound to a table for a query, e.g. `Student s`. It shortens multi-table queries and disambiguates columns (`s.roll` vs `e.roll`). It is mandatory for a self-join, where the same table appears twice and each copy needs its own name (s1, s2).

> **🧠 Hook:** "Aliases are handles — a self-join needs two handles on the same table."

> **⚠️ Misconception.** *"Aliases are just cosmetic shortening."* For most queries, yes — but for a self-join they are MANDATORY: without two distinct names, SQL cannot tell the two copies of the table apart and the query is ambiguous.

> **🔑 Key terms:** tuple variable · table alias · self-join · disambiguation · s1/s2.

**📊 Depth table — Why tuple variables matter — with vs without aliases**

| Task | Query (MySQL) | Aliases needed? |
|---|---|---|
| student + their grade | FROM Student s, Enrollment e WHERE s.roll=e.roll | optional, but tidy |
| classmates (same program) | FROM Student s1, Student s2 WHERE s1.program=s2.program AND s1.roll<>s2.roll | MANDATORY (self-join) |
| instructor + course taught | FROM Instructor i, Teaches t WHERE i.inst_id=t.inst_id | optional, tidy |
| pairs of courses in same dept | FROM Course c1, Course c2 WHERE c1.dept=c2.dept AND c1.course_id<>c2.course_id | MANDATORY (self-join) |
| disambiguate same column name | s.roll vs e.roll | needed when names clash |

*ℹ️ For ordinary multi-table queries aliases are convenience; for a SELF-join they are mandatory — the two copies of the table must have different names to be referred to at all.*

---

#### Concept 3 — String Operations `[THEORY]` `[SNIPPET]` `[~9 min]`
**📖 In Depth.** SQL searches and transforms text: **LIKE** with wildcards `%` (any sequence) and `_` (exactly one character), **CONCAT()** for joining strings, and **UPPER/LOWER/TRIM** for case and whitespace. `SELECT name FROM Student WHERE name LIKE 'S%';` — names starting with S. `email LIKE '%@pu.edu.np'` — anything ending in that domain. `_` matches exactly one character; `%` matches any run (including none). `CONCAT(name,' (',program,')')` builds display strings — use CONCAT in MySQL (not `||`).

> **🌍 Real life.** The search-as-you-type on Daraz and Hamrobazar is `LIKE '%term%'` under the hood (or full-text search for scale); a college can list all official emails with `email LIKE '%@pu.edu.np'`; a telecom finds its number range with `phone LIKE '98%'`.

> **🎯 Model exam answer.** *"What are string operations?"* LIKE matches patterns using `%` (any sequence) and `_` (exactly one character); CONCAT() joins strings (MySQL uses CONCAT, not `||`); UPPER/LOWER/TRIM adjust case and whitespace. LIKE is pattern matching, distinct from `=` (exact match).

> **🧠 Hook:** "% = 'blah blah anything'; _ = exactly one Scrabble tile."

> **⚠️ Misconception.** *"= and LIKE are the same."* `=` is EXACT (`name = 'Sita'` matches only 'Sita'); LIKE does PATTERN matching with `%` and `_`. Also, `LIKE 'Sita'` with no wildcard behaves like `=` — the wildcards are what make LIKE powerful.

> **🔑 Key terms:** LIKE · % (any) · _ (one) · CONCAT · UPPER/LOWER/TRIM · pattern ≠ exact.

**📊 Depth table — LIKE patterns — pattern → meaning → sample match**

| Pattern (MySQL) | Meaning | Matches | Does NOT match |
|---|---|---|---|
| LIKE 'S%' | starts with S | Sita, Sharma | Hari |
| LIKE '%a' | ends with a | Sita, Anjali | Hari |
| LIKE '%it%' | contains 'it' | Sita, Smith | Hari |
| LIKE '_a%' | 2nd letter is a | Hari, Rai | Sita |
| LIKE '98%' | phone starts 98 (Ncell/Ntc) | 9841234567 | 01-4412345 |
| LIKE '%@pu.edu.np' | college email domain | sita@pu.edu.np | x@gmail.com |
| = 'Sita' | EXACT match only | Sita | sita, Sit |

*ℹ️ % = any sequence (incl. empty); _ = exactly one character. LIKE does PATTERN matching; = does EXACT matching — the two are not interchangeable.*

---

#### 🛠 ACTIVITY `[~5 min]`
Write the LIKE pattern: all college emails ending in '@pu.edu.np', and 'names with exactly 4 letters starting with A'. Answers: `email LIKE '%@pu.edu.np'`; `name LIKE 'A___'` (A + exactly three underscores).

### 🧠 CHECK FOR UNDERSTANDING `[~5 min]`
- MCQ1: Which finds names ENDING in 'a'? → ✅ `LIKE '%a'` (% before a matches any prefix, then a fixed final 'a').
- MCQ2: The `_` wildcard matches how many characters? → ✅ exactly one (`%` is the any-length one).
- MCQ3: A self-join REQUIRES → ✅ two distinct tuple-variable aliases on one table.
- Discussion: which Nepali app's search box is a `LIKE '%term%'` underneath?

### 💡 REAL-LIFE APPLICATION `[~3 min]`
The autocomplete and search on every app you use is string matching; readable report headers come from AS; and self-joins (find related rows in the same table) power 'people you may know' and 'related products' features everywhere.

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
(1) AS renames columns/tables in the OUTPUT for readable reports; the stored schema is unchanged. (2) Tuple variables (aliases) disambiguate columns and make self-joins possible (s1, s2). (3) LIKE + `%` (any) / `_` (one) searches inside text; `=` is exact; MySQL joins strings with CONCAT. **Next:** controlling ORDER, removing duplicates (DISTINCT), and combining result sets (UNION/INTERSECT/EXCEPT).

---
---

# S25 — ORDER BY · DISTINCT · Set Operations
**Lecture hour 4 (of 15) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`
[SLIDE] *"A merit list isn't useful unless it's SORTED, and a mailing list isn't useful if every name appears five times. SQL fixes both — one keyword each."* → agenda: ORDER BY (sorting) → DISTINCT (de-duplication) → UNION/INTERSECT/EXCEPT (combining result sets).

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Ordering the Display (ORDER BY) `[THEORY]` `[SNIPPET]` `[~8 min]`
**📖 In Depth.** **ORDER BY** sorts the result rows. **ASC** (ascending) is the default; **DESC** is descending. Multiple sort keys break ties left to right (`ORDER BY marks DESC, name ASC`). In MySQL, **LIMIT n** returns just the first n rows (useful for top-N): `... ORDER BY marks DESC LIMIT 3` gives the top 3. Rows have **NO reliable order** without ORDER BY — never assume one.

> **🌍 Real life.** A college merit list is `ORDER BY marks DESC, name ASC`; Daraz 'sort by price: low to high' is `ORDER BY price ASC`; 'top sellers' is `ORDER BY units_sold DESC LIMIT 10`. Any 'sorted by…' control in an app is an ORDER BY.

> **🎯 Model exam answer.** *"What does ORDER BY do?"* It sorts result rows by one or more keys; ASC (default) is ascending, DESC descending, and multiple keys break ties left to right. In MySQL, LIMIT n returns the first n rows for top-N queries. Without ORDER BY, row order is undefined.

> **🧠 Hook:** "No ORDER BY = no promised order. Want a merit list? You must sort it."

> **⚠️ Misconception.** *"Rows come back sorted by default."* They do NOT — without ORDER BY the DBMS may return rows in any order (and it can change between runs). If order matters, you must state it explicitly.

> **🔑 Key terms:** ORDER BY · ASC/DESC · multi-key sort · LIMIT (MySQL) · order not guaranteed.

**📊 Depth table — ORDER BY — goal → clause → what you get**

| Goal | Clause (MySQL) | Result |
|---|---|---|
| merit list, best first | ORDER BY marks DESC | 88, 76, 55, 40… |
| alphabetical roll | ORDER BY name ASC | Anjali, Bishal, Gita… |
| ties broken by name | ORDER BY marks DESC, name ASC | same marks → A before B |
| top 3 scorers | ORDER BY marks DESC LIMIT 3 | the three highest rows |
| cheapest 5 products | ORDER BY price ASC LIMIT 5 | 5 lowest prices |
| newest first | ORDER BY created_at DESC | latest transactions on top |

*ℹ️ ASC is the default; add DESC for descending. LIMIT (MySQL) after ORDER BY is the standard 'top-N' idiom. Without ORDER BY, row order is not guaranteed.*

---

#### Concept 2 — Duplicate Tuples (DISTINCT / ALL) `[THEORY]` `[SNIPPET]` `[~7 min]`
**📖 In Depth.** SELECT keeps duplicate rows by default (**ALL**). **DISTINCT** removes duplicate rows from the result, so each distinct combination of the selected columns appears once. `SELECT DISTINCT program FROM Student;` — one row per program. DISTINCT applies to the **WHOLE selected row**, not one column: `SELECT DISTINCT program, semester` keeps each distinct (program, semester) **pair**. ALL is the (rarely written) default that keeps duplicates.

> **🌍 Real life.** A 'choose your district' dropdown is `SELECT DISTINCT district FROM users` — you want each district once, not repeated per user. A tag cloud, a filter list, a 'departments we hire in' list — all are DISTINCT queries over a column with many repeats.

> **🎯 Model exam answer.** *"What is DISTINCT?"* By default SELECT returns all rows including duplicates (ALL). DISTINCT removes duplicate rows so each distinct combination of the selected columns appears once. It applies to the entire selected row, not a single column.

> **🧠 Hook:** "DISTINCT = 'one of each, please' — collapse repeats to a single row."

> **⚠️ Misconception.** *"DISTINCT de-duplicates just the first column."* No — DISTINCT considers the WHOLE selected row. `SELECT DISTINCT program, semester` returns each distinct (program, semester) PAIR, so a program can still appear several times with different semesters.

> **🔑 Key terms:** DISTINCT · ALL (default) · de-duplication · whole-row · distinct combinations.

**📊 Depth table — DISTINCT vs ALL — same query, different result**

| Query | Returns | Rows (seed data) |
|---|---|---|
| SELECT program FROM Student | every student's program (repeats) | BIM, BIM, BCA, BIM, BCA |
| SELECT DISTINCT program FROM Student | each program once | BIM, BCA |
| SELECT dept FROM Instructor | dept per instructor | IT, IT, MGT, ECO |
| SELECT DISTINCT dept FROM Instructor | each dept once | IT, MGT, ECO |
| SELECT DISTINCT program, semester FROM Student | distinct COMBINATIONS | (BIM,4),(BCA,4),(BIM,6),(BCA,2) |
| distinct districts (Nagarik App) | SELECT DISTINCT district FROM users | one row per district |

*ℹ️ DISTINCT de-duplicates the ENTIRE selected row. Selecting two columns with DISTINCT keeps each distinct pair — not each column de-duplicated separately.*

---

#### Concept 3 — Set Operations: UNION / INTERSECT / EXCEPT `[THEORY]` `[SNIPPET]` `[~10 min]`
**📖 In Depth.** Set operations combine two result sets that are **union-compatible** (same number of columns, compatible types). **UNION** = rows in either (duplicates removed); **UNION ALL** = rows in either (duplicates kept); **INTERSECT** = rows in both; **EXCEPT** (a.k.a. MINUS) = rows in the first but not the second. Both queries must return the same columns in the same order. **MySQL note:** UNION is native; older MySQL lacks INTERSECT/EXCEPT (emulate with `IN` / `NOT IN` or joins) — MariaDB 10.3+ and MySQL 8.0.31+ support them.

> **🌍 Real life.** Marketing segments are set operations: 'users in A but not B' (EXCEPT) targets 'registered but never paid'; 'in both A and B' (INTERSECT) finds cross-app users; 'in either' (UNION) merges two campaign lists into one de-duplicated mailing list.

> **🎯 Model exam answer.** *"Explain the set operations."* They combine two union-compatible result sets: UNION (rows in either, duplicates removed), UNION ALL (duplicates kept), INTERSECT (rows in both), and EXCEPT/MINUS (rows in the first but not the second). Both queries must return the same columns in the same order.

> **🧠 Hook:** "Venn: UNION = both circles, INTERSECT = overlap, EXCEPT = left minus overlap."

> **⚠️ Misconception.** *"UNION keeps duplicates."* No — UNION removes duplicates; UNION ALL keeps them. Also, the two queries must be union-compatible: same number of columns, in the same order, with compatible types — otherwise it errors.

> **🔑 Key terms:** UNION · UNION ALL · INTERSECT · EXCEPT · union-compatible · de-dup vs keep.

**📊 Depth table — The three set operations — what each keeps**

| Operation | Keeps rows that are… | Duplicates? | College / Nepal example |
|---|---|---|---|
| UNION | in query A OR query B | removed | students in IT220 OR MGT201 |
| UNION ALL | in A or B | KEPT | combine two logs, keep every entry |
| INTERSECT | in BOTH A and B | removed | students in DBMS AND Economics |
| EXCEPT | in A but NOT in B | removed | eSewa users EXCEPT Khalti users |
| (union-compatible) | same #cols + compatible types | - | required for all three |

*ℹ️ Union-compatibility (same columns, same order, compatible types) is mandatory. UNION removes duplicates; UNION ALL keeps them — and UNION ALL is faster when you know there are none.*

---

#### 🛠 SOLVED PROBLEM (deck) — Rank the merit list and find cross-enrolled students
**Problem.** (a) Produce the top-3 merit list of (name, marks); (b) list students enrolled in BOTH IT220 and MGT201.

**Walkthrough.**
1. (a) Join to get names with marks: `SELECT s.name, e.marks FROM Student s, Enrollment e WHERE s.roll=e.roll`.
2. (a) Sort best-first and cap it: `ORDER BY e.marks DESC LIMIT 3` → the top three scorers.
3. (b) Get IT220 rolls: `SELECT roll FROM Enrollment WHERE course_id='IT220'`.
4. (b) INTERSECT with MGT201 rolls to keep only students in BOTH courses.
5. (b) If your MySQL lacks INTERSECT, use `WHERE roll IN (…MGT201…)` on the IT220 set instead.

**Answer.**
```sql
-- (a)
SELECT s.name, e.marks FROM Student s, Enrollment e WHERE s.roll=e.roll ORDER BY e.marks DESC LIMIT 3;
-- (b)
SELECT roll FROM Enrollment WHERE course_id='IT220'
INTERSECT
SELECT roll FROM Enrollment WHERE course_id='MGT201';
```

#### 🛠 ACTIVITY `[~5 min]`
When would you use EXCEPT? Give a real Nepali-app scenario ('registered but never paid') and sketch the two union-compatible queries A and B whose difference answers it. Seeds: all users EXCEPT paying users = never-paid; enrolled EXCEPT graduated = still studying; registered EXCEPT attended = no-shows.

### 🧠 CHECK FOR UNDERSTANDING `[~5 min]`
- MCQ1: Default sort direction of ORDER BY is → ✅ ascending (ASC); you must write DESC for descending.
- MCQ2: Which set op removes duplicates? → ✅ UNION (UNION ALL deliberately keeps duplicates).
- MCQ3: INTERSECT returns rows that are → ✅ in BOTH sets (the overlap).
- Discussion: give a scenario where you'd use EXCEPT ('who registered but never paid').

### 💡 REAL-LIFE APPLICATION `[~3 min]`
Leaderboards, 'top sellers', de-duplicated dropdowns, and 'users in A but not B' marketing segments are all built from ORDER BY, DISTINCT, and set operations — everyday tools in analytics and product work.

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
(1) ORDER BY sorts (ASC default / DESC); LIMIT n (MySQL) gives top-N; no ORDER BY = no guaranteed order. (2) DISTINCT removes duplicate ROWS (whole selected row), collapsing repeats to one. (3) UNION/INTERSECT/EXCEPT combine union-compatible result sets; UNION de-dups, UNION ALL keeps duplicates. **Next:** summarizing data — the aggregate functions, GROUP BY, and HAVING.

---
---

# S26 — Aggregate Functions · GROUP BY · HAVING
**Lecture hour 5 (of 15) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`
[SLIDE] *"What's the AVERAGE salary in the IT department? How MANY students passed DBMS? You don't want 5,000 rows — you want one number."* → agenda: the five aggregates → GROUP BY (per-group) → HAVING (filter groups).

### 📚 CONTENT `[~35 min]`

#### Concept 1 — The Five Aggregate Functions `[THEORY]` `[SNIPPET]` `[~9 min]`
**📖 In Depth.** An **aggregate function** collapses many rows into a single summary value. The five: **COUNT, SUM, AVG, MIN, MAX**. Over a whole table they return one row. `SELECT COUNT(*), AVG(marks), MAX(marks) FROM Enrollment WHERE course_id='IT220';` **COUNT(*)** counts rows; **COUNT(col)** counts non-NULL values of col (S27). SUM/AVG work on numbers; MIN/MAX work on numbers, dates, and text. Aggregates **ignore NULLs** (except COUNT(*)) — a NULL mark is skipped by AVG.

> **🌍 Real life.** Every dashboard KPI is an aggregate: eSewa's 'total transactions today' is `COUNT(*)`, 'total volume' is `SUM(amount)`, 'average order value' on Daraz is `AVG(total)`. One number summarising millions of rows.

> **🎯 Model exam answer.** *"Name the aggregate functions."* COUNT (row/value count), SUM, AVG, MIN, MAX. Over a whole table they return a single row. All ignore NULLs except COUNT(*), which counts every row — so COUNT(*) and COUNT(col) differ when col contains NULLs.

> **🧠 Hook:** "An aggregate boils many rows down to ONE number."

> **⚠️ Misconception.** *"COUNT(column) counts all rows."* No — COUNT(col) counts only rows where col is NOT NULL. COUNT(*) counts every row regardless. They differ exactly when the column has NULLs (e.g. ungraded enrollments).

> **🔑 Key terms:** COUNT · SUM · AVG · MIN · MAX · COUNT(*) vs COUNT(col) · aggregates skip NULLs.

**📊 Depth table — The five aggregates — function → question → result**

| Function | Answers the question | College example | Result (seed) |
|---|---|---|---|
| COUNT(*) | how many rows? | students in IT220 | 4 |
| COUNT(grade) | how many non-NULL grades? | graded IT220 rows | 3 (one NULL) |
| SUM(marks) | total of a column? | total marks in IT220 | 259 |
| AVG(marks) | the average? | average IT220 marks | 86.3 (NULLs skipped) |
| MIN(salary) | the smallest? | lowest instructor salary | 60000 |
| MAX(marks) | the largest? | top mark in IT220 | 95 |

*ℹ️ COUNT(*) counts every row; COUNT(col) skips NULLs; AVG/SUM/MIN/MAX also skip NULLs. This NULL behaviour is the bridge to S27.*

---

#### Concept 2 — GROUP BY (Per-Group Aggregates) `[THEORY]` `[SNIPPET]` `[~9 min]`
**📖 In Depth.** **GROUP BY** splits rows into groups by a column's value and returns **one aggregate row per group**. `SELECT dept, AVG(salary) FROM Instructor GROUP BY dept;` — one row per dept; all IT instructors become a single IT row with the group's AVG. **Rule:** every non-aggregated column in SELECT must appear in GROUP BY (MySQL enforces this under `ONLY_FULL_GROUP_BY`). Grouping by two columns groups by their combination.

> **🌍 Real life.** A revenue-by-category chart is `SELECT category, SUM(amount) FROM sales GROUP BY category`; 'average marks per program' is `GROUP BY program`; 'orders per city' is `GROUP BY city`. Any 'per X' metric on a dashboard is a GROUP BY X.

> **🎯 Model exam answer.** *"What does GROUP BY do?"* It partitions rows into groups sharing a value and returns one aggregate row per group. Any column in SELECT not inside an aggregate must appear in GROUP BY (MySQL's ONLY_FULL_GROUP_BY). Grouping by multiple columns groups by their combination.

> **🧠 Hook:** "GROUP BY collapses rows into one summary row per group."

> **⚠️ Misconception.** *"With GROUP BY I can SELECT any column."* No — a non-aggregated column in SELECT MUST be in the GROUP BY list. `SELECT name, AVG(marks) … GROUP BY program` is illegal (which name? the group has many). Group by it or aggregate it.

> **🔑 Key terms:** GROUP BY · one row per group · non-aggregated columns must be grouped · per-group aggregate.

**📊 Depth table — GROUP BY — group by what → one row per group**

| Query | Groups formed | Output (one row per group) |
|---|---|---|
| GROUP BY dept (Instructor) | IT, MGT, ECO | dept + AVG(salary) each |
| GROUP BY program (Student) | BIM, BCA | program + COUNT(*) each |
| GROUP BY course_id (Enrollment) | per course | course_id + AVG(marks) each |
| GROUP BY program, semester | each (program, sem) pair | one row per combination |
| GROUP BY dept + COUNT(*) | per dept | dept + how many instructors |
| no GROUP BY, just AVG(salary) | whole table = one group | a single overall average |

*ℹ️ Golden rule: every column in SELECT that is NOT inside an aggregate must appear in GROUP BY (MySQL enforces this under ONLY_FULL_GROUP_BY). Grouping by two columns groups by their combination.*

---

#### Concept 3 — HAVING (Filter Groups) `[THEORY]` `[SNIPPET]` `[~9 min]`
**📖 In Depth.** **HAVING** filters **GROUPS after aggregation**, using aggregate conditions. **WHERE** filters rows **BEFORE** grouping; HAVING filters groups **AFTER**. Aggregates can appear in HAVING but **never in WHERE**. `SELECT course_id, COUNT(*) FROM Enrollment GROUP BY course_id HAVING COUNT(*) > 30;` The evaluation order is `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY`. Use WHERE to pre-filter rows, HAVING to filter the resulting groups.

> **🌍 Real life.** 'Courses with more than 30 students' is `GROUP BY course_id HAVING COUNT(*) > 30`; 'departments whose average salary exceeds Rs 70,000' is `GROUP BY dept HAVING AVG(salary) > 70000`. Any 'groups where the summary passes a threshold' report needs HAVING.

> **🎯 Model exam answer.** *"Contrast WHERE and HAVING."* HAVING filters groups after aggregation using aggregate conditions (e.g. `HAVING COUNT(*) > 30`); WHERE filters individual rows before grouping. Aggregates are allowed in HAVING but not in WHERE. Both can be used together: WHERE pre-filters rows, then HAVING filters the resulting groups.

> **🧠 Hook:** "WHERE = bouncer at the door (per person); HAVING = inspector of each seated table."

> **⚠️ Misconception.** *"Use WHERE COUNT(*) > 30."* Illegal — aggregates can't appear in WHERE (rows aren't grouped yet). The aggregate condition belongs in HAVING, which runs after GROUP BY.

> **🔑 Key terms:** HAVING · filters groups · WHERE filters rows · aggregate in HAVING not WHERE · evaluation order.

**📊 Depth table — WHERE vs HAVING — the classic confusion**

| Question | WHERE | HAVING |
|---|---|---|
| Filters what? | individual rows | groups (after GROUP BY) |
| Runs when? | before grouping | after grouping/aggregation |
| Aggregates allowed? | no (COUNT(*) is illegal here) | yes (COUNT(*)>30 is fine) |
| Example | WHERE marks >= 40 | HAVING AVG(marks) >= 40 |
| Analogy | bouncer per guest | inspector per table of guests |
| Can use both? | yes — WHERE then HAVING | WHERE marks IS NOT NULL … HAVING COUNT(*)>30 |

*ℹ️ Order of evaluation: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY. Put a plain-column condition in WHERE (faster, pre-filter); put an aggregate condition in HAVING.*

---

#### 🛠 SOLVED PROBLEM (deck) — Average marks per course, only busy courses
**Problem.** Show each course's average marks, but only for courses with more than 30 enrolled students, best average first.

**Walkthrough.**
1. Group the enrollments by course: `GROUP BY course_id`.
2. Compute the per-group summaries: `SELECT course_id, AVG(marks) AS avg_marks, COUNT(*) AS n`.
3. Keep only busy groups with an aggregate filter: `HAVING COUNT(*) > 30` (NOT a WHERE).
4. Optionally pre-filter ungraded rows first: `WHERE marks IS NOT NULL` (a per-row condition).
5. Sort the surviving groups: `ORDER BY avg_marks DESC`.

**Answer.**
```sql
SELECT course_id, AVG(marks) AS avg_marks, COUNT(*) AS n
FROM Enrollment
WHERE marks IS NOT NULL
GROUP BY course_id
HAVING COUNT(*) > 30
ORDER BY avg_marks DESC;
```
This one query touches WHERE, GROUP BY, HAVING, and ORDER BY together.

#### 🛠 ACTIVITY `[~5 min]`
Phrase the aggregate query 'departments whose average instructor salary exceeds Rs 70,000'. Decide which part is GROUP BY and which is HAVING. Answer: `SELECT dept, AVG(salary) FROM Instructor GROUP BY dept HAVING AVG(salary) > 70000` — the aggregate condition goes in HAVING, not WHERE.

### 🧠 CHECK FOR UNDERSTANDING `[~5 min]`
- MCQ1: Which clause filters GROUPS, not rows? → ✅ HAVING (runs after GROUP BY and can test aggregates).
- MCQ2: `COUNT(grade)` vs `COUNT(*)` differ when → ✅ grade has NULLs (COUNT(grade) skips NULLs).
- MCQ3: Which is ILLEGAL? → ✅ `WHERE COUNT(*)>30` (aggregates cannot appear in WHERE).
- Discussion: name one dashboard KPI in a Nepali app and write its aggregate + GROUP BY.

### 💡 REAL-LIFE APPLICATION `[~3 min]`
Every KPI tile, chart, and report — daily revenue, active users, average order value — is an aggregate with GROUP BY. This is the core of analytics and business-intelligence work.

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
(1) COUNT/SUM/AVG/MIN/MAX summarise many rows into one; all skip NULLs except COUNT(*). (2) GROUP BY makes one aggregate row per group; non-aggregated SELECT columns must be grouped. (3) WHERE filters rows (before), HAVING filters groups (after) — aggregates go in HAVING, never WHERE. **Next:** the tricky truth about missing data — NULL values and three-valued logic.

---
---

# S27 — NULL Values · Three-Valued Logic
**Lecture hour 6 (of 15) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`
[SLIDE] *"A student's grade is blank — they haven't been graded yet. Is grade = grade true? In SQL... not necessarily. Welcome to NULL."* → agenda: what NULL means → three-valued logic (IS NULL) → NULL in aggregates & arithmetic.

### 📚 CONTENT `[~35 min]`

#### Concept 1 — What NULL Means `[THEORY]` `[~7 min]`
**📖 In Depth.** **NULL** represents a **missing, unknown, or not-applicable** value. It is **NOT zero and NOT an empty string** — those are actual values; NULL is the absence of any value. `Enrollment.grade` is NULL for a student mid-semester (not yet graded); `Instructor.salary` is NULL for an unpaid intern (no salary applies). `0` means 'a value of zero'; `''` means 'an empty text'; NULL means 'we don't know'. A column allows NULL unless declared NOT NULL (S22).

> **🌍 Real life.** A payment system must distinguish `balance = 0` (a real account with no money) from `balance = NULL` (account not yet created). Showing a not-yet-created wallet as 'Rs 0' would tell a user they have an empty account that doesn't exist — a genuine bug that has shipped in real fintech products.

> **🎯 Model exam answer.** *"What does NULL mean?"* NULL represents missing, unknown, or not-applicable data — not zero and not an empty string, which are actual values. Distinguishing NULL from 0/'' is essential: a NULL balance (account not created) differs from a 0 balance (account with no money).

> **🧠 Hook:** "NULL = a sealed box: you can't say it equals anything, you don't know what's inside."

> **⚠️ Misconception.** *"NULL equals 0 or an empty string."* No — 0 and '' are real values; NULL is the absence of a value. `NULL + 5` is NULL (not 5); a NULL name is not the same as a blank name ''.

> **🔑 Key terms:** NULL · unknown/missing/not-applicable · not 0 · not empty string.

**📊 Depth table — NULL vs 0 vs '' — three different things**

| Value | Means | Wallet example | Wrong if you… |
|---|---|---|---|
| NULL | unknown / not applicable | account not created yet | treat it as 0 balance |
| 0 | a real zero | balance is genuinely empty | treat it as unknown |
| '' (empty string) | present but blank text | no nickname set | confuse with NULL name |
| grade = NULL | not yet graded | mid-semester enrollment | count it as a fail (0) |
| salary = NULL | no salary applies | unpaid intern instructor | include in AVG as 0 |
| marks = 0 | genuinely scored zero | student sat and failed | hide from the class average |

*ℹ️ Confusing NULL with 0 or '' is a real, expensive bug. A NULL balance ('account not created') must never be shown as Rs 0 ('you have no money').*

---

#### Concept 2 — Three-Valued Logic (TRUE / FALSE / UNKNOWN) `[THEORY]` `[~9 min]`
**📖 In Depth.** Because NULL is unknown, any comparison with NULL yields **UNKNOWN** (not TRUE or FALSE). SQL logic has **three values**; WHERE keeps only rows that are TRUE — UNKNOWN rows are dropped. `grade = NULL` evaluates to UNKNOWN, so it returns **NO rows** — never use it. Use `IS NULL` / `IS NOT NULL` to test for missing values. AND/OR follow three-valued truth tables (`TRUE AND UNKNOWN = UNKNOWN`); `NOT UNKNOWN` is still UNKNOWN.

> **🌍 Real life.** A report of 'students with no email on file' must use `WHERE email IS NULL`. A developer who writes `WHERE email = NULL` gets zero rows and wrongly concludes 'everyone has an email' — a silent, dangerous bug caused by three-valued logic.

> **🎯 Model exam answer.** *"Explain three-valued logic."* Any comparison involving NULL yields UNKNOWN, giving three-valued logic (TRUE/FALSE/UNKNOWN). WHERE keeps only TRUE rows, so `= NULL` (always UNKNOWN) returns nothing — you must use `IS NULL` / `IS NOT NULL`. Logical operators follow three-valued truth tables.

> **🧠 Hook:** "= NULL ✗ (always UNKNOWN) · IS NULL ✓ (the correct test)."

> **⚠️ Misconception.** *"= NULL finds the blanks."* It never does — `= NULL` is UNKNOWN for every row, so it returns nothing. Always use `IS NULL` / `IS NOT NULL`. Likewise `NOT IN` with a NULL in the list can return no rows (an S28 trap).

> **🔑 Key terms:** three-valued logic · TRUE/FALSE/UNKNOWN · IS NULL / IS NOT NULL · = NULL is always UNKNOWN.

**📊 Depth table — Testing for NULL — wrong vs right**

| Goal | Wrong (returns nothing / bug) | Right |
|---|---|---|
| find ungraded enrollments | WHERE grade = NULL | WHERE grade IS NULL |
| find graded enrollments | WHERE grade <> NULL | WHERE grade IS NOT NULL |
| students missing an email | WHERE email = NULL | WHERE email IS NULL |
| interns (no salary) | WHERE salary = NULL | WHERE salary IS NULL |
| treat NULL marks as 0 | AVG(marks) | AVG(COALESCE(marks,0)) |
| default a NULL grade text | grade | COALESCE(grade,'N/A') |

*ℹ️ = NULL and <> NULL always yield UNKNOWN, so they match no rows. Use IS NULL / IS NOT NULL. COALESCE(x, fallback) substitutes a value when x is NULL.*

---

#### Concept 3 — NULL in Aggregates & Arithmetic `[THEORY]` `[~8 min]`
**📖 In Depth.** Arithmetic with NULL gives NULL (`100 + NULL = NULL` — one NULL poisons an expression). Aggregates **ignore NULLs — except COUNT(*)**. `AVG(marks)` skips NULL marks entirely (they don't count in numerator or denominator); `COUNT(*)` counts NULL rows; `COUNT(col)` and SUM/AVG/MIN/MAX ignore them. This can silently change results, so decide deliberately whether a NULL should be dropped or treated as a value — use `COALESCE(marks,0)` if an ungraded student SHOULD count as 0.

> **🌍 Real life.** Averaging class marks where some students aren't yet graded: `AVG(marks)` silently drops the ungraded ones, giving the average of those graded. If policy says ungraded = 0, you must write `AVG(COALESCE(marks,0))` — otherwise the reported average is misleadingly high.

> **🎯 Model exam answer.** *"How does NULL behave in aggregates?"* Arithmetic with NULL yields NULL. Aggregates ignore NULLs — SUM/AVG/MIN/MAX and COUNT(col) skip them, while COUNT(*) counts every row. Use `COALESCE(x, fallback)` when a NULL should be treated as a concrete value (e.g. 0).

> **🧠 Hook:** "One NULL in a sum poisons it to NULL; aggregates quietly skip NULLs instead."

> **⚠️ Misconception.** *"Aggregates include NULL rows as zero."* No — SUM/AVG/MIN/MAX ignore NULLs entirely (they are not treated as 0). Only COUNT(*) counts NULL rows. If you want NULL to count as 0, wrap it in COALESCE.

> **🔑 Key terms:** arithmetic with NULL → NULL · aggregates skip NULLs · COUNT(*) counts all · COALESCE.

**📊 Depth table — How NULL behaves in maths and aggregates**

| Expression / aggregate | Result with a NULL present | Note |
|---|---|---|
| 100 + NULL | NULL | any arithmetic with NULL → NULL |
| marks * 1.0 (marks NULL) | NULL | the whole expression is NULL |
| AVG(marks) over {88, NULL, 90} | 89 (avg of 88 & 90) | NULL row dropped entirely |
| COUNT(*) over 3 rows (1 NULL) | 3 | counts the NULL row |
| COUNT(marks) over 3 rows (1 NULL) | 2 | skips the NULL |
| SUM(marks) with a NULL | sum of non-NULLs | NULL contributes nothing |
| AVG(COALESCE(marks,0)) | includes 0 for the NULL | makes NULL count as 0 |

*ℹ️ Aggregates silently drop NULLs, which can quietly change an average. Decide on purpose: exclude (default) or count-as-zero (COALESCE). COUNT(*) is the one aggregate that counts NULL rows.*

---

#### 🛠 ACTIVITY `[~5 min]`
Should a 'not yet graded' student count as 0 in the class average? Write both queries — `AVG(marks)` vs `AVG(COALESCE(marks,0))` — and discuss how NULL vs 0 changes the reported average. Both are defensible; the lesson is that NULL forces an explicit policy choice.

### 🧠 CHECK FOR UNDERSTANDING `[~5 min]`
- MCQ1: To find rows with a missing email, use → ✅ `WHERE email IS NULL` (`= NULL` is always UNKNOWN).
- MCQ2: `SELECT 100 + NULL;` returns → ✅ NULL (any arithmetic involving NULL yields NULL).
- MCQ3: Which aggregate counts NULL rows? → ✅ COUNT(*) (the others skip NULLs).
- Discussion: give a real bug caused by treating NULL as 0 (e.g. wallet balance).

### 💡 REAL-LIFE APPLICATION `[~3 min]`
Payment and identity systems live or die on the NULL-vs-0 distinction: 'balance = 0' (broke) vs 'balance = NULL' (no account) is a real production bug when confused. Correct NULL handling is a mark of a careful engineer.

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
(1) NULL = unknown/missing/not-applicable — not 0 and not an empty string. (2) Comparisons with NULL are UNKNOWN; use IS NULL / IS NOT NULL, never = NULL. (3) Arithmetic with NULL → NULL; aggregates skip NULLs (except COUNT(*)); COALESCE substitutes a value. **Next:** queries inside queries — nested subqueries with IN and SOME/ALL.

---
---

# S28 — Nested Subqueries: IN · SOME/ALL
**Lecture hour 7 (of 15) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`
[SLIDE] *"Find students enrolled in ANY IT course — but you don't know the course IDs yet. Let one query feed another."* → agenda: subqueries & IN/NOT IN → SOME/ANY → ALL.

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Subqueries & Set Membership (IN / NOT IN) `[THEORY]` `[SNIPPET]` `[~9 min]`
**📖 In Depth.** A **subquery** is a query nested inside another; the inner query runs and feeds its result to the outer. **IN** tests whether a value is in the inner result set; **NOT IN** tests the opposite. `SELECT name FROM Student WHERE roll IN (SELECT roll FROM Enrollment WHERE course_id='IT220');` — the inner query produces a set of rolls; the outer keeps students in that set. **NOT IN breaks if the inner set contains a NULL** (callback to S27) — it can return no rows.

> **🌍 Real life.** Segmentation queries at a fintech are IN subqueries: 'users who did X and also Y' = `WHERE user_id IN (SELECT user_id FROM did_Y)`. Fraud and marketing teams constantly ask 'who is in this other set too?' — exactly what IN answers.

> **🎯 Model exam answer.** *"What is a subquery / IN?"* A subquery is a query nested inside another; the inner runs first and feeds the outer. IN tests set membership (value is in the inner result), NOT IN tests absence. NOT IN is unsafe when the inner set contains NULL — it can return no rows — so filter NULLs or prefer NOT EXISTS.

> **🧠 Hook:** "Inner query runs first, its result feeds the outer WHERE."

> **⚠️ Misconception.** *"NOT IN works fine with NULLs."* It does NOT — if the inner subquery returns even one NULL, NOT IN can evaluate to UNKNOWN for every row and return nothing. Filter NULLs out of the inner set, or use NOT EXISTS (S29) instead.

> **🔑 Key terms:** subquery · IN (membership) · NOT IN · inner feeds outer · NOT IN + NULL trap.

**📊 Depth table — IN / NOT IN subqueries — question → query**

| Question | Query (MySQL) |
|---|---|
| students in IT220 | WHERE roll IN (SELECT roll FROM Enrollment WHERE course_id='IT220') |
| students in NO course | WHERE roll NOT IN (SELECT roll FROM Enrollment) |
| courses someone teaches | WHERE course_id IN (SELECT course_id FROM Teaches) |
| courses nobody teaches | WHERE course_id NOT IN (SELECT course_id FROM Teaches) |
| Khalti users also on eSewa | WHERE user_id IN (SELECT user_id FROM esewa_users) |
| students in an IT-dept course | WHERE roll IN (SELECT roll FROM Enrollment WHERE course_id IN (SELECT course_id FROM Course WHERE dept='IT')) |

*ℹ️ The inner query runs first and yields a set; IN keeps outer rows whose value is in it. Beware NOT IN when the inner set may contain NULL — pair it with WHERE col IS NOT NULL or use NOT EXISTS (S29).*

---

#### Concept 2 — Set Comparison: SOME / ANY `[THEORY]` `[SNIPPET]` `[~8 min]`
**📖 In Depth.** **SOME** (a synonym for **ANY**) compares a value to a set and is TRUE if the comparison holds for **AT LEAST ONE** element. `> SOME` means 'greater than at least one' = greater than the **MINIMUM** of the set. `SELECT name FROM Instructor WHERE salary > SOME (SELECT salary FROM Instructor WHERE dept='IT');` `= SOME` is equivalent to **IN** (matches at least one). SOME and ANY are interchangeable keywords in SQL/MySQL.

> **🌍 Real life.** 'Instructors who out-earn at least one IT instructor' is `salary > SOME (SELECT salary FROM Instructor WHERE dept='IT')`. It is a low bar — beating the lowest-paid person in the set is enough — which is exactly what 'at least one' means.

> **🎯 Model exam answer.** *"Define SOME/ANY."* SOME (a.k.a. ANY) compares a value against a set and is TRUE if the comparison holds for at least one element: `> SOME` means greater than the minimum, `= SOME` is equivalent to IN, `< SOME` means less than the maximum. It contrasts with ALL, which requires the comparison to hold for every element.

> **🧠 Hook:** "> SOME = 'taller than at least one classmate' — beat just one and you qualify."

> **⚠️ Misconception.** *"SOME and ALL mean the same."* They are opposites in strength: SOME needs the comparison to hold for AT LEAST ONE element; ALL needs it for EVERY element. `> SOME` is easy to satisfy; `> ALL` is hard.

> **🔑 Key terms:** SOME / ANY · at least one · > SOME = > MIN · = SOME = IN.

**📊 Depth table — SOME / ANY — operator → meaning → equivalent**

| Expression | TRUE when the value is… | Equivalent to |
|---|---|---|
| > SOME (set) | greater than at least one element | > MIN(set) |
| < SOME (set) | less than at least one element | < MAX(set) |
| = SOME (set) | equal to at least one element | IN (set) |
| <> SOME (set) | different from at least one element | (nearly always true) |
| >= SOME (set) | at least as big as one element | ≥ MIN(set) |
| salary > SOME (IT salaries) | paid more than some IT instructor | > lowest IT salary |

*ℹ️ SOME/ANY = 'at least one'. The handy identities: = SOME is IN, > SOME is > MIN(set), < SOME is < MAX(set).*

---

#### Concept 3 — Set Comparison: ALL `[THEORY]` `[SNIPPET]` `[~8 min]`
**📖 In Depth.** **ALL** is TRUE only if the comparison holds for **EVERY** element of the set. `> ALL` means 'greater than every value' — i.e. greater than the **MAXIMUM**. `SELECT name FROM Instructor WHERE salary >= ALL (SELECT salary FROM Instructor);` `>= ALL` over all salaries finds the highest-paid instructor. `<> ALL` is equivalent to **NOT IN** (different from every element).

> **🌍 Real life.** 'The highest-paid instructor' is `WHERE salary >= ALL (SELECT salary FROM Instructor)` — nobody earns more. Daraz's 'products priced higher than ALL items in Electronics' is `price > ALL (SELECT price FROM products WHERE category='Electronics')`.

> **🎯 Model exam answer.** *"Define ALL."* ALL is TRUE only if the comparison holds for every element of the set: `> ALL` means greater than the maximum, so `>= ALL` finds the top value; `<> ALL` is equivalent to NOT IN. It is the strong counterpart to SOME/ANY (at least one).

> **🧠 Hook:** "> ALL = 'tallest in the class' — you must beat EVERYONE."

> **⚠️ Misconception.** *"> ALL just means > SOME."* No — `> ALL` must beat the MAXIMUM (every element); `> SOME` only needs to beat the MINIMUM (one element). Confusing them turns 'the top scorer' into 'anyone above the bottom'.

> **🔑 Key terms:** ALL · every element · > ALL = > MAX · <> ALL = NOT IN · strongest form.

**📊 Depth table — SOME vs ALL — the crucial contrast**

| Expression | TRUE when value is… | Equivalent | Example |
|---|---|---|---|
| > SOME (set) | > at least one element | > MIN(set) | beats the weakest |
| > ALL (set) | > every element | > MAX(set) | beats everyone |
| = SOME (set) | = at least one | IN (set) | matches someone |
| <> ALL (set) | ≠ every element | NOT IN (set) | matches no one |
| >= ALL (salaries) | the maximum | the top value | highest-paid instructor |
| price > ALL (Electronics) | dearer than every item | > most expensive | premium product |

*ℹ️ SOME = at-least-one (easy); ALL = every-single-one (hard). > ALL is > MAX; > SOME is > MIN. <> ALL is NOT IN; = SOME is IN.*

---

#### 🛠 SOLVED PROBLEM (deck) — Find the highest-paid instructor two ways
**Problem.** List the name(s) of the highest-paid instructor. Show both the subquery-comparison approach and the MAX approach.

**Walkthrough.**
1. Understand 'highest-paid' = salary is >= every other salary (nobody earns more).
2. Approach A (`>= ALL`): keep instructors whose salary is `>= ALL` salaries in the table.
3. Approach B (MAX subquery): keep instructors whose salary equals `(SELECT MAX(salary) …)`.
4. Both handle ties correctly — if two share the top salary, both are returned.
5. Watch NULL salaries: an intern with NULL salary is neither the max nor compared meaningfully — add an `IS NOT NULL` guard for `>= ALL`.

**Answer.**
```sql
-- A)
SELECT name FROM Instructor WHERE salary >= ALL (SELECT salary FROM Instructor WHERE salary IS NOT NULL);
-- B)
SELECT name FROM Instructor WHERE salary = (SELECT MAX(salary) FROM Instructor);
```
Both return Sharma (80000).

#### 🛠 ACTIVITY `[~5 min]`
Phrase in SQL 'students who scored more than ALL of last year's batch'. Is this SOME or ALL? Answer shape: `WHERE marks > ALL (SELECT marks FROM last_year_batch)` — 'more than everyone' = `> ALL` (> MAX), not `> SOME`.

### 🧠 CHECK FOR UNDERSTANDING `[~5 min]`
- MCQ1: `> ALL (subquery)` is TRUE when the value is greater than → ✅ every value in the set (the maximum).
- MCQ2: Which can be rewritten with IN? → ✅ `= SOME` (equals at least one = set membership).
- MCQ3: NOT IN can return no rows when the inner set → ✅ contains a NULL.
- Discussion: phrase 'users who did X but also Y' as an IN subquery.

### 💡 REAL-LIFE APPLICATION `[~3 min]`
'Find users who did X but also Y' segmentation — the backbone of marketing, fraud detection, and analytics at every fintech — is written as IN and EXISTS subqueries. Subqueries let you answer questions when you don't yet know the exact values to filter on.

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
(1) A subquery nests inside another; the inner runs first and feeds the outer query. (2) IN tests set membership (= SOME); NOT IN tests absence (but breaks with a NULL in the set). (3) SOME/ANY = at least one (> SOME = > MIN); ALL = every one (> ALL = > MAX). **Next:** testing whether a relation is empty (EXISTS) or duplicate-free (UNIQUE).

---
---

# S29 — Nested Subqueries: EXISTS · UNIQUE
**Lecture hour 8 (of 15) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`
[SLIDE] *"Sometimes you don't care WHAT the inner query returns — only WHETHER it returns anything at all. That's EXISTS."* → agenda: EXISTS/NOT EXISTS → NOT EXISTS for 'for all' → UNIQUE predicate.

### 📚 CONTENT `[~35 min]`

#### Concept 1 — EXISTS / NOT EXISTS `[THEORY]` `[SNIPPET]` `[~9 min]`
**📖 In Depth.** **EXISTS** is TRUE if the subquery returns at least one row; **NOT EXISTS** is TRUE if it returns none. It is usually **CORRELATED** — the inner query references the current outer row. `SELECT name FROM Student s WHERE EXISTS (SELECT * FROM Enrollment e WHERE e.roll=s.roll);` The inner query re-runs for each outer row, using that row's values (`s.roll`). EXISTS only checks existence — `SELECT *`, `SELECT 1`, or `SELECT anything` are equivalent. NOT EXISTS finds outer rows for which the inner query is empty.

> **🌍 Real life.** Retention systems live on NOT EXISTS: 'send a reminder to customers who have NOT placed any order this month' is `WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.uid=c.uid AND o.month=…)`. It surfaces the inactive users a business most wants to win back.

> **🎯 Model exam answer.** *"Define EXISTS."* EXISTS is TRUE if its subquery returns at least one row, NOT EXISTS if none. It is typically correlated (the inner query references the outer row) and re-runs per outer row. Only row existence matters, so the subquery's SELECT list is irrelevant (`SELECT 1` is idiomatic).

> **🧠 Hook:** "EXISTS = 'is anyone in the room?' — it counts existence, not columns."

> **⚠️ Misconception.** *"EXISTS cares about the columns the subquery selects."* It does not — EXISTS only checks whether ANY row comes back; `SELECT *`, `SELECT 1`, `SELECT roll` are all equivalent. Only the WHERE inside the subquery matters.

> **🔑 Key terms:** EXISTS · NOT EXISTS · correlated subquery · existence not columns · SELECT 1.

**📊 Depth table — EXISTS / NOT EXISTS — question → correlated query**

| Question | Query (MySQL) |
|---|---|
| students with ≥1 enrollment | WHERE EXISTS (SELECT 1 FROM Enrollment e WHERE e.roll=s.roll) |
| students enrolled in nothing | WHERE NOT EXISTS (SELECT 1 FROM Enrollment e WHERE e.roll=s.roll) |
| instructors teaching this sem | WHERE EXISTS (SELECT 1 FROM Teaches t WHERE t.inst_id=i.inst_id) |
| courses nobody enrolled in | WHERE NOT EXISTS (SELECT 1 FROM Enrollment e WHERE e.course_id=c.course_id) |
| customers with a failed txn | WHERE EXISTS (SELECT 1 FROM txn WHERE txn.uid=u.uid AND status='failed') |
| customers with NO failed txn | WHERE NOT EXISTS (SELECT 1 FROM txn WHERE txn.uid=u.uid AND status='failed') |

*ℹ️ EXISTS short-circuits — it stops at the first matching row, so it is often faster than IN for correlated tests. The SELECT list inside EXISTS is irrelevant (use SELECT 1).*

---

#### Concept 2 — NOT EXISTS for 'For All' Queries `[THEORY]` `[~8 min]`
**📖 In Depth.** A 'for all' requirement ('students enrolled in EVERY IT course') has **no direct SQL keyword**. It is expressed as a **double NOT EXISTS**: 'there is NO IT course for which this student has NO enrollment'. Rewrite 'for all X, P' as 'there is no X where NOT P' (double negation). Outer: student s. Inner-1: for each IT course c. Inner-2: NOT EXISTS that enrollment. If no IT course is missing an enrollment, the student took them all. This is **relational division** — advanced; recognise the pattern.

> **🌍 Real life.** A bank flags 'customers with NO failed transactions' via a single NOT EXISTS (`… status='failed'`). The harder 'students enrolled in every IT course' uses double NOT EXISTS — the standard way SQL expresses 'for all', since it has no FORALL keyword.

> **🎯 Model exam answer.** *"How does SQL express 'for all'?"* SQL has no direct 'for all' operator, so universal requirements are expressed with NOT EXISTS of a counterexample. 'None' is a single NOT EXISTS; 'for all X' is a double NOT EXISTS ('there is no X for which the condition fails'). This is relational division.

> **🧠 Hook:** "'Took every IT course' = 'there is NO IT course they didn't take'."

> **⚠️ Misconception.** *"There must be a FORALL keyword."* There isn't — SQL expresses 'for all' indirectly through NOT EXISTS of the counterexample. 'Enrolled in every IT course' becomes 'no IT course exists in which they are not enrolled'.

> **🔑 Key terms:** NOT EXISTS · 'for all' via double negation · relational division · no FORALL keyword.

**📊 Depth table — 'For all' rewritten as double NOT EXISTS**

| Plain-English requirement | Double-negation rewrite | Difficulty |
|---|---|---|
| students in EVERY IT course | no IT course exists that they are NOT in | hard (division) |
| customers with NO failed txn | no txn exists with status='failed' | easy (single NOT EXISTS) |
| instructors teaching ALL IT courses | no IT course exists they do NOT teach | hard |
| students who passed ALL their courses | no enrollment of theirs has marks < 40 | medium |
| courses taken by ALL BIM students | no BIM student exists NOT enrolled in it | hard |
| users active EVERY day this week | no day this week exists with no activity | hard |

*ℹ️ The trick for every 'for all / every' query: flip it to 'there is NO counterexample' and write NOT EXISTS. Single NOT EXISTS handles 'none'; double NOT EXISTS handles 'for all'.*

---

#### Concept 3 — UNIQUE Predicate (Absence of Duplicates) `[THEORY]` `[~7 min]`
**📖 In Depth.** The **UNIQUE predicate** tests whether a subquery's result has **NO duplicate rows**: `UNIQUE(subquery)` is TRUE when every row it returns is distinct. It is **different from the UNIQUE table constraint** (S22). The constraint prevents duplicates in a table; the predicate tests a query result. **MySQL support is limited** — the idea is often expressed with `GROUP BY … HAVING COUNT(*)=1` instead.

> **🌍 Real life.** To check that no student double-registered for a course in a term, the UNIQUE predicate would test the enrolment subquery. In practice on MySQL you write `SELECT course_id FROM Enrollment GROUP BY course_id, sem HAVING COUNT(roll) <> COUNT(DISTINCT roll)` to find any course with duplicate registrations.

> **🎯 Model exam answer.** *"What is the UNIQUE predicate?"* `UNIQUE(subquery)` is TRUE when the subquery returns no duplicate rows — a query-time duplicate-freeness test. It differs from the UNIQUE table constraint (S22), which permanently prevents duplicate values from being stored. MySQL lacks the predicate; emulate it with `GROUP BY … HAVING COUNT(*)=1`.

> **🧠 Hook:** "UNIQUE (predicate) = 'is everyone in the room a different person?'"

> **⚠️ Misconception.** *"The UNIQUE constraint and the UNIQUE predicate are the same thing."* No — one is a stored table rule (S22) that prevents duplicates; the other is a query-time boolean test that checks whether a result set has duplicates. Same keyword, different roles.

> **🔑 Key terms:** UNIQUE predicate · duplicate-free test · vs UNIQUE constraint · MySQL: HAVING COUNT(*)=1.

**📊 Depth table — UNIQUE constraint vs UNIQUE predicate — same word, different jobs**

| Aspect | UNIQUE constraint (S22) | UNIQUE predicate (S29) |
|---|---|---|
| What it is | a table rule (DDL) | a boolean test in a query |
| Where it lives | CREATE TABLE … email UNIQUE | WHERE UNIQUE (subquery) |
| When it acts | on every INSERT/UPDATE | when the query runs |
| Purpose | prevent duplicate values ever stored | test if a result has duplicates |
| Returns | nothing (rejects bad data) | TRUE / FALSE |
| MySQL | fully supported | not supported — use HAVING COUNT(*)=1 |

*ℹ️ Don't conflate them: the constraint STOPS duplicates being stored; the predicate CHECKS whether a query result happens to be duplicate-free. In MySQL, emulate the predicate with GROUP BY … HAVING COUNT(*)=1.*

---

#### 🛠 ACTIVITY `[~5 min]`
IN vs EXISTS: which reads better? Compare both for 'students who are enrolled somewhere': `WHERE roll IN (SELECT roll FROM Enrollment)` vs `WHERE EXISTS (…correlated…)`. EXISTS shines for correlated 'does a related row exist?' and avoids the NOT IN + NULL trap; IN reads well for a flat value list.

### 🧠 CHECK FOR UNDERSTANDING `[~5 min]`
- MCQ1: EXISTS returns TRUE when the subquery → ✅ returns at least one row.
- MCQ2: To find students with NO enrollment at all, use → ✅ NOT EXISTS (TRUE exactly when the related set is empty).
- MCQ3: Inside EXISTS, `SELECT *` and `SELECT 1` are → ✅ equivalent (EXISTS only checks existence).
- Discussion: compare IN vs EXISTS — when does each read more naturally?

### 💡 REAL-LIFE APPLICATION `[~3 min]`
'Remind every customer who has NOT ordered this month' is a textbook NOT EXISTS query powering retention and re-engagement across e-commerce and fintech. Existence tests are how you find who is missing.

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
(1) EXISTS is TRUE if the (usually correlated) subquery returns any row; SELECT 1 is idiomatic. (2) NOT EXISTS expresses 'none' and, doubled, 'for all' (there is no counterexample). (3) The UNIQUE predicate tests a result for duplicates — distinct from the UNIQUE table constraint. **Next:** packaging queries for reuse — derived relations and views.

---
---

# S30 — Derived Relations · Views
**Lecture hour 9 (of 15) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`
[SLIDE] *"You keep typing the same 6-line join for the merit list. What if you could save it under one name and just call it MeritList?"* → agenda: derived relations (subquery in FROM) → CREATE VIEW → the 3 reasons for views.

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Derived Relations (Subquery in FROM) `[THEORY]` `[SNIPPET]` `[~8 min]`
**📖 In Depth.** A **derived relation** is a subquery used in the **FROM** clause as if it were a table. It **must be given an alias**. It lets you query the result of a query — for example, filter on an aggregate. `SELECT dept, avg_sal FROM (SELECT dept, AVG(salary) AS avg_sal FROM Instructor GROUP BY dept) AS d WHERE avg_sal > 60000;` The inner query builds a temporary result; the outer treats it as a table. It is the clean way to filter on an aggregate you just computed.

> **🌍 Real life.** A 'departments above the company-average salary' report first computes each department's average in a derived table, then filters it. Analytics queries constantly stack a filter/join on top of a GROUP BY result this way — the standard shape for multi-step aggregation.

> **🎯 Model exam answer.** *"What is a derived relation?"* A subquery placed in the FROM clause and used as a table; it must be given an alias. It lets the outer query filter, join, or aggregate over a computed intermediate result (e.g. filtering on a GROUP BY average that WHERE cannot reference directly).

> **🧠 Hook:** "A derived relation = a query pretending to be a table (needs a name tag)."

> **⚠️ Misconception.** *"You can't put a query in FROM."* You can — it's a derived relation (a.k.a. derived table / inline view). The one firm rule in MySQL: it must have an alias, e.g. `(SELECT …) AS d`, or the query errors.

> **🔑 Key terms:** derived relation · subquery in FROM · inline view · mandatory alias · filter on aggregate.

**📊 Depth table — Derived relations — why put a query in FROM**

| Task | Derived-relation query | Why not just WHERE? |
|---|---|---|
| depts averaging > 60k | FROM (SELECT dept, AVG(salary) avg_sal … GROUP BY dept) d WHERE avg_sal>60000 | can't filter AVG in WHERE |
| top-3 then join | FROM (SELECT … ORDER BY marks DESC LIMIT 3) t JOIN … | pre-limit before joining |
| per-course averages, filtered | FROM (SELECT course_id, AVG(marks) a … GROUP BY course_id) x WHERE a>=50 | reuse the computed avg |
| rank within a subset | FROM (SELECT … WHERE dept='IT') sub | narrow first, then process |
| aggregate of an aggregate | FROM (SELECT dept, COUNT(*) c … GROUP BY dept) g | count the groups |

*ℹ️ A derived relation names an intermediate result so the outer query can filter/join on computed columns (like an aggregate) that a single-level WHERE can't reach. Always alias it.*

---

#### Concept 2 — Views: CREATE VIEW `[THEORY]` `[SNIPPET]` `[~8 min]`
**📖 In Depth.** A **view** is a named, stored **QUERY** — a virtual table computed on demand. `CREATE VIEW` saves the query under a name; querying the view re-runs its definition against the current base data. `CREATE VIEW MeritList AS SELECT roll, name, marks FROM Student NATURAL JOIN Enrollment ORDER BY marks DESC;` then `SELECT * FROM MeritList;` behaves like a table but **stores no data**. The view always reflects the latest base-table data (it re-runs each time).

> **🌍 Real life.** Instead of pasting the 6-line merit-list join into every report, a college creates it once as `CREATE VIEW MeritList AS …` and everyone runs `SELECT * FROM MeritList`. The view always shows current marks because it re-runs its query against the live Student/Enrollment data each time.

> **🎯 Model exam answer.** *"What is a view?"* A named, stored query that behaves as a virtual table: `CREATE VIEW name AS <query>`. Querying it re-runs the definition against current base data, so it always reflects the latest rows and stores no data itself. This contrasts with a materialized view, which stores a physical (possibly stale) copy.

> **🧠 Hook:** "A view is a saved query with a name — a virtual table, not a copy."

> **⚠️ Misconception.** *"A view stores its own copy of the data."* A standard view stores only the QUERY definition, not the data — it recomputes on each access. A materialized view would store a copy (and can go stale); MySQL has no native materialized views.

> **🔑 Key terms:** view · CREATE VIEW · virtual table · stores query not data · vs materialized view.

**📊 Depth table — View vs base table vs derived relation**

| Aspect | Base table | View | Derived relation |
|---|---|---|---|
| Stores data? | yes | no (stores the query) | no (temporary) |
| Named & reusable? | yes | yes (persistent name) | no (query-local) |
| Reflects latest data? | is the data | yes, re-runs each time | yes |
| How created | CREATE TABLE | CREATE VIEW | (SELECT …) AS alias in FROM |
| Example | Student | MeritList, BIMStudents | (SELECT … GROUP BY …) d |
| Lifetime | permanent | until DROP VIEW | just this query |

*ℹ️ A view is a named, reusable derived relation stored in the schema. A standard view stores only the QUERY (recomputed each call); a MATERIALIZED view would store a data copy (MySQL has no native materialized views).*

---

#### Concept 3 — Why Views — Three Reasons `[THEORY]` `[~9 min]`
**📖 In Depth.** Views give three benefits: **SIMPLICITY** (hide a complex join behind one name), **SECURITY** (expose only allowed columns/rows), and **CONSISTENCY** (one definition reused everywhere). They do **NOT guarantee faster disk access** — a standard view re-runs its query. A hard 6-table join becomes `SELECT * FROM ReportView`; a teller view hides salary/balance columns; 'active student' defined once means every report agrees.

> **🌍 Real life.** Role-based portals are built on views: an admin, a teacher, and a student portal each read a different view of the same tables. A bank teller's view hides the salary and account-balance columns; the Nagarik App shows each citizen only their own records via a per-user filtered view — security and simplicity together.

> **🎯 Model exam answer.** *"Why use views?"* Simplicity (hide complex joins behind one name), security (expose only permitted columns/rows, e.g. hiding salary from a teller or filtering to a citizen's own records), and consistency (a single reused definition). They are not inherently faster on disk — a standard view recomputes on each access.

> **🧠 Hook:** "A view = a saved filter / window into the data — you see through it, you don't copy the room."

> **⚠️ Misconception.** *"Views make queries faster on disk."* Not for a standard view — it re-runs its query each time, so it isn't inherently faster (only a materialized view stores results). Views are for simplicity, security, and consistency, not raw speed.

> **🔑 Key terms:** views · simplicity · security · consistency · row/column hiding · not faster disk.

**📊 Depth table — The three reasons to use views (and the non-reason)**

| Reason | What it gives | Nepal / IT example |
|---|---|---|
| Simplicity | hide a complex join behind one name | MeritList instead of a 6-line join |
| Security | show only allowed columns/rows | teller sees no salary/balance columns |
| Consistency | one definition reused everywhere | 'active student' defined once, all reports agree |
| Row-level security | filter to a user's own data | Nagarik App: citizen sees only their records |
| Abstraction | apps depend on the view, not raw tables | refactor base tables without breaking apps |
| NOT a guaranteed benefit | faster disk access | a standard view re-runs; it isn't inherently faster |

*ℹ️ Simplicity, security, consistency (and abstraction) are the wins. Speed is NOT — a standard view recomputes each time. That 'faster disk' distractor is a classic exam trap.*

---

#### 🛠 SOLVED PROBLEM (deck) — Build and use a MeritList view
**Problem.** Create a view `MeritList(roll, name, marks)` for IT220 in 2026S sorted by marks descending, then query the top of it.

**Walkthrough.**
1. Write the underlying join: `SELECT s.roll, s.name, e.marks FROM Student s JOIN Enrollment e ON s.roll=e.roll WHERE e.course_id='IT220' AND e.sem='2026S'`.
2. Wrap it in `CREATE VIEW MeritList AS <that query> ORDER BY e.marks DESC`.
3. Now the complex join has a single reusable name: MeritList.
4. Query it like a table: `SELECT * FROM MeritList LIMIT 3;` for the top three.
5. Because it stores the QUERY, MeritList always reflects the latest marks.

**Answer.**
```sql
CREATE VIEW MeritList AS
SELECT s.roll, s.name, e.marks
FROM Student s JOIN Enrollment e ON s.roll=e.roll
WHERE e.course_id='IT220' AND e.sem='2026S'
ORDER BY e.marks DESC;

SELECT * FROM MeritList LIMIT 3;
```

#### 🛠 ACTIVITY `[~5 min]`
Design a view of the Instructor table to show to STUDENTS. Which columns do you expose (name, dept) and which do you hide (salary)? A student-facing view: `CREATE VIEW PublicInstructor AS SELECT inst_id, name, dept FROM Instructor` — hiding salary is column-level security.

### 🧠 CHECK FOR UNDERSTANDING `[~5 min]`
- MCQ1: A standard view stores → ✅ the query definition, not the data (it re-runs each access).
- MCQ2: Which is NOT a guaranteed benefit of a view? → ✅ faster disk access (a standard view recomputes).
- MCQ3: A subquery used in the FROM clause is a → ✅ derived relation (must be aliased).
- Discussion: which columns would you hide in a view of Instructor shown to students?

### 💡 REAL-LIFE APPLICATION `[~3 min]`
Admin/teacher/student portals and dashboards are almost always built on views for reuse and role-based security. Understanding views is essential to designing safe, maintainable data access.

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
(1) A subquery in FROM is a derived relation (must be aliased) — query the result of a query. (2) A view is a named, stored QUERY (virtual table); it stores no data and always reflects live rows. (3) Views give simplicity, security, and consistency — NOT guaranteed faster disk access. **Next:** changing the data itself — INSERT, UPDATE, DELETE (and the danger of a missing WHERE).

---
---

# S31 — Modifying Data: INSERT · UPDATE · DELETE
**Lecture hour 10 (of 15) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`
[SLIDE] *"Reading data is safe. CHANGING it is where careers are made or broken — one forgotten WHERE can wipe a whole table."* → agenda: INSERT → UPDATE (the WHERE danger) → DELETE (vs DROP).

### 📚 CONTENT `[~35 min]`

#### Concept 1 — INSERT `[THEORY]` `[SNIPPET]` `[~8 min]`
**📖 In Depth.** **INSERT** adds new rows. You list columns and matching VALUES, or insert the result of a SELECT for bulk loads. The VALUES order **must match the column list** (or all columns, in table order, if the list is omitted). `INSERT INTO Student(roll,name,program,semester) VALUES (101,'Sita','BIM',4);` Omitting the column list means you must supply all columns in table order. Bulk: `INSERT INTO Archive SELECT * FROM Enrollment WHERE sem='2024F';` Columns not listed take their DEFAULT (S22) or NULL.

> **🌍 Real life.** Registering a new student, adding a Khalti wallet row, recording a new order — each is an INSERT. Bulk archival ('move last year's enrollments to an archive table') uses `INSERT … SELECT` to copy many rows in one statement.

> **🎯 Model exam answer.** *"What does INSERT do?"* It adds rows: `INSERT INTO t(cols) VALUES(...)`, where VALUES align with the named columns by position (omitted columns take DEFAULT or NULL). Omitting the column list requires all columns in table order. `INSERT … SELECT` bulk-loads rows from a query. Listing columns explicitly is the safer habit.

> **🧠 Hook:** "INSERT = add a new row; VALUES must line up with the named columns."

> **⚠️ Misconception.** *"Column order doesn't matter in INSERT."* It does — VALUES are matched to columns by position. If you omit the column list you must supply every column in exact table order; a mismatch either errors or silently stores data in the wrong column.

> **🔑 Key terms:** INSERT · column list · VALUES order · INSERT … SELECT (bulk) · DEFAULT/NULL for omitted.

**📊 Depth table — INSERT forms — column list, order, bulk**

| Form | Example (MySQL) | Note |
|---|---|---|
| explicit columns | INSERT INTO Student(roll,name) VALUES (106,'Rita') | others get DEFAULT/NULL |
| all columns, in order | INSERT INTO Course VALUES ('IT250','Digital Economy',3,'IT') | must match table order |
| multiple rows at once | INSERT INTO Student(roll,name) VALUES (107,'A'),(108,'B') | one statement, many rows |
| from a query (bulk) | INSERT INTO Archive SELECT * FROM Enrollment WHERE sem='2024F' | copy rows across tables |
| wrong: values mis-ordered | INSERT INTO Student(roll,name) VALUES ('Sita',101) | type/order mismatch → error or bad data |

*ℹ️ VALUES must align with the column list by position. Omitting the column list forces all columns in exact table order — brittle if the schema changes, so listing columns is safer.*

---

#### Concept 2 — UPDATE `[THEORY]` `[SNIPPET]` `[~9 min]`
**📖 In Depth.** **UPDATE** changes values in existing rows. **SET** assigns new values; **WHERE decides WHICH rows change**. Omitting WHERE updates **EVERY row** — the single most dangerous mistake in SQL. `UPDATE Enrollment SET grade='A' WHERE roll=101 AND course_id='IT220';` You can compute new values: `SET salary = salary*1.10` (a 10% raise). UPDATE can set several columns at once (`SET a=…, b=…`). Test the WHERE with a SELECT first.

> **🌍 Real life.** 'Edit profile', 'change delivery address', 'apply a 10% salary revision' are UPDATEs. A bank raising IT-department salaries runs `UPDATE Instructor SET salary=salary*1.10 WHERE dept='IT'`; the WHERE is what stops every employee in the company getting the raise.

> **🎯 Model exam answer.** *"What does UPDATE do?"* It modifies existing rows: SET assigns new (possibly computed) values, and WHERE selects which rows change. Omitting WHERE updates every row — a common catastrophe — so always preview the affected rows with a matching SELECT first, and use transactions in production.

> **🧠 Hook:** "UPDATE without WHERE rewrites the WHOLE table. Always SELECT first."

> **⚠️ Misconception.** *"`UPDATE Enrollment SET grade='A';`"* with no WHERE gives EVERY student an A. The fix: always test your WHERE with a SELECT first, and in production wrap changes in a transaction so you can ROLLBACK (Unit 6).

> **🔑 Key terms:** UPDATE · SET · WHERE scopes it · missing WHERE = all rows · SELECT-first habit.

**📊 Depth table — UPDATE — safe vs catastrophic**

| Statement | Effect | Verdict |
|---|---|---|
| UPDATE Enrollment SET grade='A' WHERE roll=101 AND course_id='IT220' | one specific enrollment | safe (targeted) |
| UPDATE Instructor SET salary=salary*1.10 WHERE dept='IT' | IT instructors get a 10% raise | safe (scoped) |
| UPDATE Enrollment SET grade='A' | EVERY row gets grade A | catastrophe (no WHERE) |
| UPDATE Student SET semester=semester+1 WHERE program='BIM' | promote all BIM students | safe (scoped) |
| SELECT * FROM Enrollment WHERE roll=101 (first!) | preview which rows WOULD change | the lifesaving habit |

*ℹ️ Always run a SELECT with your intended WHERE first to see exactly which rows will change. An UPDATE with no WHERE rewrites every row — there is no undo without a transaction (Unit 6) or backup.*

---

#### Concept 3 — DELETE `[THEORY]` `[SNIPPET]` `[~8 min]`
**📖 In Depth.** **DELETE** removes rows (a DML operation on data). WHERE decides which rows; no WHERE deletes them all (but keeps the table). `DELETE FROM Enrollment WHERE sem='2024F';` removes only that semester's rows. DELETE differs from **DROP** (DDL), which removes the whole table structure, and **TRUNCATE**, which fast-empties it. Dropping a course may trigger FK behaviour: `ON DELETE CASCADE` vs `RESTRICT` (S22).

> **🌍 Real life.** 'Cancel order', 'remove item from cart', 'clear old logs' are DELETEs — usually soft-deletes (a status flag) in production so nothing is truly lost. Purging last year's enrollments is `DELETE FROM Enrollment WHERE sem='2024F'`; the WHERE keeps this year's data intact.

> **🎯 Model exam answer.** *"What does DELETE do vs DROP?"* DELETE removes rows from a table (DML); WHERE scopes which rows, and no WHERE deletes all rows while keeping the table. It differs from DROP (DDL), which removes the whole table, and TRUNCATE, which fast-empties it. FK `ON DELETE CASCADE/RESTRICT` rules govern child rows.

> **🧠 Hook:** "DELETE = erase lines in a notebook; DROP = throw out the whole notebook."

> **⚠️ Misconception.** *"DELETE and DROP are the same."* No — DELETE (DML) removes ROWS and keeps the table (and can be rolled back in a transaction); DROP (DDL) removes the entire TABLE and its structure. Confusing them can destroy a schema, not just data.

> **🔑 Key terms:** DELETE (rows, DML) · DROP (table, DDL) · TRUNCATE · ON DELETE CASCADE/RESTRICT · soft-delete.

**📊 Depth table — DELETE vs DROP vs TRUNCATE — what disappears**

| Command | Removes | Keeps | Language |
|---|---|---|---|
| DELETE FROM t WHERE … | matching rows | table + other rows | DML |
| DELETE FROM t | all rows | the empty table | DML |
| TRUNCATE TABLE t | all rows (fast, no per-row log) | the empty table | DDL |
| DROP TABLE t | the whole table + all data | nothing | DDL |
| ON DELETE CASCADE | child rows too, automatically | referential integrity | constraint (S22) |
| ON DELETE RESTRICT | blocks delete if children exist | the parent row | constraint (S22) |

*ℹ️ DELETE (DML) removes rows and can be rolled back in a transaction; DROP (DDL) removes the table. FK ON DELETE rules decide what happens to child rows when a parent is deleted.*

---

#### 🛠 SOLVED PROBLEM (deck) — A safe UPDATE workflow (preview before you change)
**Problem.** Give IT-department instructors a 10% raise — safely, so you never accidentally raise everyone.

**Walkthrough.**
1. FIRST preview the target rows: `SELECT inst_id, name, salary FROM Instructor WHERE dept='IT';` — confirm it's the right people.
2. Check the WHERE returns ONLY the intended rows (Sharma, Karki) and nobody else.
3. Run the scoped update: `UPDATE Instructor SET salary = salary*1.10 WHERE dept='IT';`
4. Verify: re-run the SELECT and confirm the new salaries (80000→88000, 60000→66000).
5. In production, wrap steps 3–4 in a transaction so a mistake can ROLLBACK (Unit 6).

**Answer.**
```sql
SELECT inst_id,name,salary FROM Instructor WHERE dept='IT';   -- preview
UPDATE Instructor SET salary = salary*1.10 WHERE dept='IT';    -- apply (WHERE = the safety catch)
```

#### 🛠 ACTIVITY `[~5 min]`
Why SELECT before you change? Explain why running a SELECT with your WHERE before an UPDATE/DELETE is lifesaving, then write the SELECT you'd run before 'delete all 2024F enrollments'. The SELECT previews the exact rows the change will hit — no surprises. Mention soft-deletes and transactions as extra safety nets.

### 🧠 CHECK FOR UNDERSTANDING `[~5 min]`
- MCQ1: `DELETE FROM Student;` (no WHERE) does what? → ✅ removes ALL rows (keeps the table).
- MCQ2: To change existing values, use → ✅ UPDATE (`UPDATE … SET`).
- MCQ3: DELETE differs from DROP because DELETE → ✅ removes rows but keeps the table (DELETE is DML; DROP is DDL).
- Discussion: why is a SELECT-with-your-WHERE before UPDATE/DELETE a lifesaving habit?

### 💡 REAL-LIFE APPLICATION `[~3 min]`
Every 'edit', 'cancel', 'refund', and 'top-up' in eSewa/Daraz is an INSERT/UPDATE/DELETE — guarded by transactions and soft-deletes. The missing-WHERE mistake has taken down real production databases; the SELECT-first habit prevents it.

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
(1) INSERT adds rows (VALUES must match columns; INSERT … SELECT bulk-loads). (2) UPDATE changes rows via SET; WHERE scopes it — a missing WHERE rewrites the whole table. (3) DELETE removes rows (DML, keeps the table); DROP removes the table (DDL). Always SELECT-first. **Next:** what happens when you modify data THROUGH a view — updatable vs non-updatable views.

---
---

# S32 — Update of a View (Updatable vs Non-Updatable)
**Lecture hour 11 (of 15) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`
[SLIDE] *"You built the BIMStudents view yesterday. Can you INSERT a new student THROUGH it? Sometimes yes, sometimes the database says no — why?"* → agenda: modifying through a view → updatability rules → non-updatable views → WITH CHECK OPTION.

### 📚 CONTENT `[~35 min]`

#### Concept 1 — Modifying Through a View `[THEORY]` `[~7 min]`
**📖 In Depth.** Changes to a **SIMPLE** view can pass through to its base table: an UPDATE/INSERT/DELETE on the view modifies the underlying rows. This works only when the mapping from view rows to base rows is **unambiguous**. `UPDATE BIMStudents SET semester=5 WHERE roll=101;` updates the Student table. The view must map each of its rows to **exactly one base-table row**. Simple column/row subsets of ONE table are the updatable case; the DBMS rewrites the view modification into a base-table modification.

> **🌍 Real life.** An admin panel often exposes an editable view rather than the raw table. Editing a student's semester in the BIMStudents view writes straight through to the Student table — the coordinator never touches the base table directly, but their save still lands there.

> **🎯 Model exam answer.** *"What is modifying through a view?"* Running INSERT/UPDATE/DELETE against a view; for an updatable view the DBMS rewrites this into a modification of the underlying base table, since the view stores no data. This works only when each view row maps unambiguously to exactly one base-table row.

> **🧠 Hook:** "A simple view is a clear window — changes pass straight through the glass to the table."

> **⚠️ Misconception.** *"Editing a view only changes the view, not the real data."* For an updatable view, the change passes THROUGH to the base table — the view has no data of its own. If it were non-updatable, the save would be rejected instead.

> **🔑 Key terms:** modify through view · pass-through to base table · unambiguous row mapping · views store no data.

**📊 Depth table — Does the modification pass through the view?**

| View | Modification | Passes through? |
|---|---|---|
| BIMStudents (filter of Student) | UPDATE … SET semester=5 | yes — one base row per view row |
| BIMStudents | INSERT a new BIM student | yes (needs the NOT NULL cols) |
| PublicInstructor (name, dept only) | UPDATE dept | yes — single table subset |
| MeritList (Student JOIN Enrollment) | UPDATE marks | ambiguous / blocked (join) |
| DeptAvgSalary (GROUP BY dept) | UPDATE avg_salary | no — aggregate can't map back |
| a view with a computed column | UPDATE that column | no — derived value |

*ℹ️ A modification passes through only when the DBMS can map each view row to exactly one base-table row. Single-table filters/subsets qualify; joins, aggregates, and computed columns generally do not.*

---

#### Concept 2 — Updatable Views — the Rules `[THEORY]` `[~9 min]`
**📖 In Depth.** A view is **updatable** when it maps cleanly to **one base table**: built on a SINGLE table (no joins), no aggregates / DISTINCT / GROUP BY, no derived (computed) columns, and it includes the base table's required NOT NULL columns (so an INSERT can supply them). Only then can the DBMS translate a view modification into an unambiguous base-table modification.

> **🌍 Real life.** `BIMStudents = SELECT roll,name,program,semester FROM Student WHERE program='BIM'` is updatable: one table, no aggregates, no computed columns, and it carries the NOT NULL columns, so you can UPDATE or even INSERT a BIM student through it.

> **🎯 Model exam answer.** *"When is a view updatable?"* When it maps cleanly to a single base table: no joins, no aggregates/GROUP BY/DISTINCT, no derived columns, and it includes the base table's NOT NULL columns so inserts can supply them. Only then can a view modification become an unambiguous base-table modification.

> **🧠 Hook:** "Updatable = simple, single-table, no summarising, no computed columns."

> **⚠️ Misconception.** *"Any view can be edited like a table."* Only views meeting the updatability rules — single table, no aggregates/DISTINCT/GROUP BY, no derived columns, and the required NOT NULL columns present. Break any rule and the DBMS rejects the modification.

> **🔑 Key terms:** updatable view · single table · no aggregate/GROUP BY/DISTINCT · no derived columns · NOT NULL present.

**📊 Depth table — The updatability checklist — pass all to be updatable**

| Rule | Updatable view | Non-updatable if… |
|---|---|---|
| Single base table | one table only | it joins two+ tables |
| No aggregates | plain columns | it uses SUM/AVG/COUNT… |
| No GROUP BY / DISTINCT | row-for-row | it groups or de-duplicates |
| No computed columns | stored columns only | it has marks*1.0 etc. |
| Includes NOT NULL cols | can insert a valid row | required columns are missing |
| Example | BIMStudents | DeptAvgSalary, MeritList |

*ℹ️ All boxes must be ticked. A view fails updatability the moment it joins, aggregates, groups, de-duplicates, or computes — because the DBMS can no longer map a view row to one base row.*

---

#### Concept 3 — Non-Updatable Views & WITH CHECK OPTION `[THEORY]` `[~9 min]`
**📖 In Depth.** Views with **joins, aggregates, GROUP BY, or computed columns** are generally **NON-updatable** — the change can't be mapped back to base rows unambiguously (you can't push an average back to individual salaries). **WITH CHECK OPTION** guards an updatable view so you can't insert/update a row that falls **OUTSIDE the view's filter**. Inserting a 'BCA' student through `BIMStudents WITH CHECK OPTION` is rejected — it stops rows 'disappearing' from a view the moment they're inserted.

> **🌍 Real life.** A DeptAvgSalary view (GROUP BY dept) can't be updated — 'raise this department's average to 80k' has no single-row meaning. And `BIMStudents WITH CHECK OPTION` rejects inserting a BCA student, so a row can't vanish from the very view you inserted it through.

> **🎯 Model exam answer.** *"Which views are non-updatable, and what is WITH CHECK OPTION?"* Views built on joins, aggregates, GROUP BY, DISTINCT, or computed columns are generally non-updatable, because a change cannot be mapped back to base rows unambiguously. WITH CHECK OPTION protects an updatable view by rejecting inserts/updates that would place a row outside the view's defining condition.

> **🧠 Hook:** "You can't un-bake a cake: an aggregate view can't be pushed back into individual rows."

> **⚠️ Misconception.** *"If a view won't save my change, it's a bug."* Often it's correct behaviour: aggregated/joined views are non-updatable by design, and WITH CHECK OPTION deliberately blocks rows that would fall outside the view's filter.

> **🔑 Key terms:** non-updatable · joins/aggregates/DISTINCT/computed · WITH CHECK OPTION · guard the filter.

**📊 Depth table — Non-updatable views and the CHECK OPTION guard**

| View / clause | Why non-updatable / what it guards | Attempted change |
|---|---|---|
| DeptAvgSalary (GROUP BY dept) | aggregate can't map to rows | 'set avg=80k' — meaningless |
| MeritList (Student JOIN Enrollment) | which base table gets the change? | UPDATE marks — ambiguous |
| Pct (marks*1.0 AS pct) | derived column has no base storage | UPDATE pct — impossible |
| a DISTINCT view | de-dup loses row identity | UPDATE a merged row — ambiguous |
| BIMStudents WITH CHECK OPTION | guards the filter (program='BIM') | INSERT a 'BCA' row — REJECTED |
| BIMStudents WITH CHECK OPTION | guards the filter | UPDATE program to 'BCA' — REJECTED |

*ℹ️ Joins/aggregates/DISTINCT/computed columns break the row mapping → non-updatable. WITH CHECK OPTION keeps an updatable view honest: it forbids changes that would put a row outside the view's own condition.*

---

#### 🛠 ACTIVITY `[~5 min]`
Why can't you update an aggregate view? Explain why the DBMS can't update DeptAvgSalary (instructors grouped by dept average), and sketch what 'set the IT average to 80,000' would mean for the individual salaries. There's no single way back — the mapping from one aggregate value to many rows is ambiguous, so the DBMS refuses ('can't un-bake the cake').

### 🧠 CHECK FOR UNDERSTANDING `[~5 min]`
- MCQ1: Which view is typically NOT updatable? → ✅ GROUP BY aggregate view (an aggregate can't map back to base rows).
- MCQ2: WITH CHECK OPTION prevents → ✅ inserting/updating rows that violate the view's condition.
- MCQ3: A view is updatable only if it is built on → ✅ a single base table with no aggregates/derived cols.
- Discussion: why can't the database update a view that groups instructors by department average?

### 💡 REAL-LIFE APPLICATION `[~3 min]`
Admin panels expose editable views; knowing which are updatable prevents the frustrating 'why won't my save go through?' bug and guides safe, role-based data editing.

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
(1) Simple single-table views can be modified THROUGH (the change passes to the base table). (2) Views with joins, aggregates, GROUP BY, DISTINCT, or computed columns are generally non-updatable. (3) WITH CHECK OPTION blocks inserts/updates that would put a row outside the view's filter. **Next:** the heart of relational power — joining tables (INNER/OUTER/NATURAL/ON/USING).

---
---

# S33 — Joined Relations: Join Types & Conditions
**Lecture hour 12 (of 15) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`
[SLIDE] *"Student names live in one table, their grades in another. The query that stitches them together is the single most-used statement in real SQL: the JOIN."* → agenda: INNER JOIN → OUTER joins (LEFT/RIGHT/FULL) → conditions (ON/USING/NATURAL).

### 📚 CONTENT `[~35 min]`

#### Concept 1 — INNER JOIN (Matched Rows Only) `[THEORY]` `[SNIPPET]` `[~9 min]`
**📖 In Depth.** An **INNER JOIN** combines rows from two tables where the join condition matches. Rows with **no match on EITHER side are dropped**. It is the default JOIN. `SELECT s.name, e.grade FROM Student s INNER JOIN Enrollment e ON s.roll=e.roll;` Only students who HAVE an enrollment appear; unenrolled students are dropped. The explicit-JOIN form replaces the S23 comma-and-WHERE style. `JOIN` with no `INNER` keyword still means INNER JOIN.

> **🌍 Real life.** A marksheet report is `Student INNER JOIN Enrollment ON s.roll=e.roll` — each student beside their grades. Any student who registered for nothing simply won't appear, which is fine for a marksheet but wrong if you need a full class roll.

> **🎯 Model exam answer.** *"What is an INNER JOIN?"* It returns only rows where the join condition matches in both tables (`… FROM A INNER JOIN B ON A.k=B.k`), dropping unmatched rows on either side. JOIN without a qualifier means INNER JOIN. It replaces the older comma-plus-WHERE syntax with a clearer, explicit form.

> **🧠 Hook:** "INNER JOIN keeps only rows that match on BOTH sides."

> **⚠️ Misconception.** *"JOIN keeps everything from both tables."* No — INNER JOIN drops any row without a match on both sides. To keep unmatched rows (e.g. students with no enrollment), you need an OUTER join.

> **🔑 Key terms:** INNER JOIN · ON condition · matches on both sides · unmatched dropped · default JOIN.

**📊 Depth table — INNER JOIN — matched pairs only**

| Join | What it returns | Who is dropped |
|---|---|---|
| Student INNER JOIN Enrollment ON roll | students WITH their enrollments | students with no enrollment |
| Course INNER JOIN Teaches ON course_id | courses that ARE taught | courses nobody teaches |
| Instructor JOIN Teaches ON inst_id | instructors WITH a course | instructors teaching nothing |
| Enrollment JOIN Course ON course_id | enrollments + course titles | (none — every FK matches) |
| orders JOIN customers ON cust_id | orders with customer details | orphan orders (bad data) |

*ℹ️ INNER JOIN = intersection: a row appears only if it has a match on both sides. It silently hides unmatched rows — which is exactly what LEFT/RIGHT/FULL joins fix.*

---

#### Concept 2 — OUTER Joins: LEFT / RIGHT / FULL `[THEORY]` `[SNIPPET]` `[~9 min]`
**📖 In Depth.** **OUTER joins** keep unmatched rows and fill the missing side with **NULLs**. **LEFT** keeps all left-table rows; **RIGHT** keeps all right-table rows; **FULL** keeps both. They surface the 'missing' cases. `SELECT s.name, e.course_id FROM Student s LEFT JOIN Enrollment e ON s.roll=e.roll;` keeps every student; those with no enrollment show `course_id = NULL`. **MySQL has no FULL OUTER JOIN** — emulate it with `LEFT JOIN UNION RIGHT JOIN`.

> **🌍 Real life.** 'All eSewa registered users and their transactions — including users who never transacted' is `users LEFT JOIN transactions`; the never-active users appear with NULL transaction columns. That NULL is exactly the inactive-user list a growth team wants (callback to NOT EXISTS, S29).

> **🎯 Model exam answer.** *"What are OUTER joins?"* They keep unmatched rows and NULL-fill the missing side: LEFT keeps all left-table rows, RIGHT all right-table rows, FULL keeps unmatched rows from both. They reveal 'missing' cases. MySQL lacks FULL OUTER JOIN, emulated by `LEFT JOIN UNION RIGHT JOIN`.

> **🧠 Hook:** "OUTER keeps the lonely rows too — the missing side is filled with NULL."

> **⚠️ Misconception.** *"An outer join is just a slower inner join."* No — it returns DIFFERENT rows: it keeps unmatched rows (with NULLs) that an INNER JOIN drops. Choosing INNER when you needed LEFT silently hides the very rows (inactive users, unsold products) you were looking for.

> **🔑 Key terms:** LEFT / RIGHT / FULL OUTER JOIN · keep unmatched · NULL fill · MySQL: no FULL (UNION trick).

**📊 Depth table — INNER vs LEFT vs RIGHT vs FULL — which unmatched rows survive**

| Join type | Keeps unmatched from… | NULLs appear for… | Use it to… |
|---|---|---|---|
| INNER | neither | (none) | list only matched pairs |
| LEFT (OUTER) | the LEFT table | missing right side | keep all students, even unenrolled |
| RIGHT (OUTER) | the RIGHT table | missing left side | keep all enrollments, even orphaned |
| FULL (OUTER) | both tables | either missing side | reconcile two lists completely |
| MySQL FULL | (not supported) | - | LEFT JOIN UNION RIGHT JOIN |

*ℹ️ Outer joins are how a business sees the MISSING cases — students who enrolled in nothing, users who never transacted, products never ordered. The unmatched side is filled with NULL (link back to S27).*

---

#### Concept 3 — Join Conditions: ON · USING · NATURAL `[THEORY]` `[SNIPPET]` `[~9 min]`
**📖 In Depth.** Three ways to state the match: **ON** gives an explicit condition (`… JOIN Enrollment e ON s.roll = e.roll` — most explicit, always safe, and the only form supporting non-equi joins); **USING(col)** is a shortcut when both tables share the column name (`… JOIN Enrollment USING(roll)`); **NATURAL JOIN** auto-matches **ALL columns with the same name** (`… NATURAL JOIN Enrollment`). NATURAL is **risky** — it silently uses ALL shared names, including unexpected ones.

> **🌍 Real life.** Daraz's 'all products, including those never ordered' is `products LEFT JOIN order_items ON products.id=order_items.product_id` — an explicit ON, chosen over NATURAL so a shared column like created_at can't silently corrupt the match. Production code overwhelmingly uses ON for predictability.

> **🎯 Model exam answer.** *"Contrast ON, USING, NATURAL."* ON gives an explicit (and possibly non-equi) condition; USING(col) is a shortcut for an equi-join on a shared column name (keeping one copy); NATURAL JOIN auto-joins on all columns with the same name. NATURAL is risky because unexpected shared names silently change the join — ON is the safe default.

> **🧠 Hook:** "ON = you name the match; NATURAL = the DB guesses it (and can guess wrong)."

> **⚠️ Misconception.** *"NATURAL JOIN is always safe and convenient."* It silently joins on EVERY common column name. If Student and Enrollment both have a 'sem' column, NATURAL JOIN matches on roll AND sem — usually not what you meant. Prefer ON (or USING).

> **🔑 Key terms:** ON (explicit) · USING(col) · NATURAL JOIN · NATURAL risk · prefer ON.

**📊 Depth table — ON vs USING vs NATURAL — control vs convenience**

| Clause | How it matches | Pros | Risk |
|---|---|---|---|
| ON A.k=B.k | explicit condition you write | full control, any condition | more typing |
| USING(k) | same-named column, once | concise, one k column in output | both must share the name |
| NATURAL JOIN | ALL common column names | shortest to write | silent wrong match on extra shared names |
| ON (unequal) | e.g. ON a.x > b.y | non-equi joins possible | only ON supports this |
| NATURAL surprise | Student & Enrollment share 'sem'? | - | joins on roll AND sem unexpectedly |

*ℹ️ Prefer ON in real code — it is explicit and predictable. NATURAL JOIN is convenient but dangerous: add a column with a shared name later and every NATURAL join silently changes meaning.*

---

#### 🛠 SOLVED PROBLEM (deck) — List every student and their grade — including the unenrolled
**Problem.** Produce a full class roll showing each student's name and course grade, keeping students who registered for nothing.

**Walkthrough.**
1. Recognise 'keep the unenrolled too' means an OUTER join, not INNER.
2. Put Student on the left and keep all its rows: `Student s LEFT JOIN Enrollment e`.
3. State the match explicitly with `ON s.roll = e.roll` (avoid NATURAL's surprises).
4. Select the columns: `s.name, e.course_id, e.grade`.
5. Students with no enrollment appear with course_id and grade = NULL (the S27 NULL again).

**Answer.**
```sql
SELECT s.name, e.course_id, e.grade
FROM Student s LEFT JOIN Enrollment e ON s.roll = e.roll
ORDER BY s.name;   -- unenrolled students show NULL grade
```
Swap LEFT→INNER to watch the unenrolled students vanish — the visible difference between the join types.

#### 🛠 ACTIVITY `[~5 min]`
INNER or LEFT for Daraz? Daraz wants 'all products, INCLUDING those never ordered'. Answer: `products LEFT JOIN order_items ON products.id=order_items.product_id` — never-ordered products appear with NULL order columns, exactly the 'dead stock' report. 'Include the ones with no match' is the signal for an OUTER (LEFT) join.

### 🧠 CHECK FOR UNDERSTANDING `[~5 min]`
- MCQ1: Which join keeps unmatched rows from the LEFT table? → ✅ LEFT (OUTER) JOIN (NULL-filling the missing right side).
- MCQ2: NATURAL JOIN matches on → ✅ all columns with the same name (hence its risk).
- MCQ3: INNER JOIN returns rows that → ✅ match in BOTH tables (dropping unmatched rows).
- Discussion: Daraz wants 'all products, including never-ordered' — INNER or LEFT? Why?

### 💡 REAL-LIFE APPLICATION `[~3 min]`
Essentially every multi-table report — orders+customers, transactions+users, students+grades — is a JOIN, and OUTER joins surface the inactive/missing cases businesses care about most. JOIN fluency is the core of real SQL work.

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
(1) INNER JOIN keeps only rows matching on both sides; unmatched rows are dropped. (2) LEFT/RIGHT/FULL OUTER joins keep unmatched rows, NULL-filling the missing side (MySQL lacks FULL). (3) ON (explicit) is the safe default; USING is a shared-name shortcut; NATURAL auto-matches all common names (risky). **Next:** packaging logic on the server — stored procedures.

---
---

# S34 — Basic Concepts of Stored Procedures
**Lecture hour 13 (of 15) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`
[SLIDE] *"What if a 20-line enrollment routine — check seats, insert, update the count — could be stored IN the database and run with one call: CALL enroll(101,'IT220')?"* → agenda: what a stored procedure is → parameters & control flow → why use them.

### 📚 CONTENT `[~35 min]`

#### Concept 1 — What a Stored Procedure Is `[THEORY]` `[SNIPPET]` `[~9 min]`
**📖 In Depth.** A **stored procedure** is a named block of SQL plus procedural logic, stored in the database and executed on the server with **CALL**. Unlike a view, it can run many statements, take parameters, and modify data. `CREATE PROCEDURE enroll(IN r INT, IN c VARCHAR(10)) BEGIN INSERT INTO Enrollment(roll,course_id) VALUES(r,c); END;` — invoke with `CALL enroll(101,'IT220');`. It lives on the server, so the logic is central and reused by every app. A view is a virtual TABLE; a procedure is executable LOGIC.

> **🌍 Real life.** An enrollment routine — check seats remain, insert the enrollment, decrement the seat count — is stored once as a procedure and run with `CALL enroll(101,'IT220')`. Every app (web, mobile, admin) calls the same server-side logic, so the rules can't drift between clients.

> **🎯 Model exam answer.** *"What is a stored procedure?"* A named block of SQL and procedural logic stored in the database and executed on the server via CALL. Unlike a view (a virtual table from one query), it can contain many statements, accept parameters, use control flow, and modify data — packaging reusable multi-step logic centrally.

> **🧠 Hook:** "A stored procedure = a saved recipe the kitchen runs on order."

> **⚠️ Misconception.** *"A procedure is just a saved SELECT (a view)."* No — a view is a virtual table (one query, no parameters, read-oriented). A procedure runs multi-statement procedural logic, accepts parameters, and can modify data. Different tools for different jobs.

> **🔑 Key terms:** stored procedure · CREATE PROCEDURE · CALL · server-side logic · vs view (data).

**📊 Depth table — Stored procedure vs view — logic vs virtual table**

| Aspect | View | Stored procedure |
|---|---|---|
| What it is | a named query (virtual table) | a named block of logic |
| Statements | one SELECT | many (INSERT/UPDATE/IF/loops) |
| Parameters | no | yes (IN/OUT/INOUT) |
| Can modify data? | only if updatable (S32) | yes, directly |
| Invoked with | SELECT * FROM view | CALL proc(args) |
| Best for | reuse a query / security | reuse multi-step business logic |

*ℹ️ A view packages a QUERY; a procedure packages LOGIC (multiple statements, parameters, control flow). Reaching for a procedure signals a multi-step operation, not just a saved SELECT.*

---

#### Concept 2 — Parameters & Basic Control Flow `[THEORY]` `[SNIPPET]` `[~8 min]`
**📖 In Depth.** Procedures take parameters — **IN** (input), **OUT** (return a value), **INOUT** (both) — and can use variables, IF, and loops. This makes them small programs that run inside the database. `CREATE PROCEDURE transfer(IN frm INT, IN to INT, IN amt DECIMAL(10,2))`. Control flow: `DECLARE` variables, `IF … THEN`, `WHILE` loops. Kept at concept level here — the point is 'procedures can hold logic', not deep coding.

> **🌍 Real life.** An eSewa-style `transfer(from, to, amount)` procedure checks the sender's balance (IF), debits one wallet and credits the other, and can return the new balance via an OUT parameter. Parameters let the one procedure serve every transfer, whatever the accounts and amount.

> **🎯 Model exam answer.** *"What parameters and control flow do procedures use?"* IN (input), OUT (output back to the caller), INOUT (both), plus variables, IF conditions, and loops. This lets a procedure act as a small program beside the data: e.g. a `transfer(from,to,amount)` that validates the balance and performs the debit and credit.

> **🧠 Hook:** "IN = ingredients you hand in; OUT = the dish handed back."

> **⚠️ Misconception.** *"Parameters are just for input."* Not only — IN feeds values in, but OUT returns results to the caller and INOUT does both. A transfer procedure can return the new balance through an OUT parameter rather than requiring a second query.

> **🔑 Key terms:** IN / OUT / INOUT parameters · variables · IF · loops · reusable server-side logic.

**📊 Depth table — Procedure parameters & logic — what each part does**

| Element | Role | Wallet-transfer example |
|---|---|---|
| IN param | value passed into the procedure | frm, to, amt |
| OUT param | value returned to the caller | OUT new_balance DECIMAL(10,2) |
| INOUT param | passed in and updated | INOUT retries INT |
| variable (DECLARE) | local working value | DECLARE bal DECIMAL(10,2) |
| IF … THEN | conditional logic | IF bal < amt THEN reject |
| the two writes | debit + credit together | UPDATE sender; UPDATE receiver |

*ℹ️ Parameters make a procedure reusable with different inputs; IN/OUT/INOUT control data direction. Control flow (IF, loops) lets the procedure make decisions server-side — a small program next to the data.*

---

#### Concept 3 — Why Use Stored Procedures `[THEORY]` `[~9 min]`
**📖 In Depth.** Procedures give **reuse** (write once, call from web, mobile, and admin), **performance** (one CALL runs many statements server-side — one round-trip, not ten), **centralized business logic** (one place, not copied in every app), and **security** (grant CALL without granting table access). Keeping a debit+credit together in one procedure bridges to transactions (Unit 6).

> **🌍 Real life.** Banks and fintechs put fund transfers and interest calculations in stored procedures so the logic is identical across every channel, runs fast in one round-trip, and can be granted (CALL) to staff without exposing the underlying tables. One definition, consistently applied.

> **🎯 Model exam answer.** *"Why use stored procedures?"* Reuse (write once, call from every app), performance (one server round-trip runs many statements), centralized business logic (rules can't drift between clients), and security (GRANT CALL without table access). Ideal for critical shared operations like fund transfers — which also motivates transactions (Unit 6).

> **🧠 Hook:** "A procedure = the recipe the kitchen keeps, so every order comes out the same."

> **⚠️ Misconception.** *"Procedures are outdated — put all logic in the app."* For critical, shared, data-close logic (transfers, audits) procedures give consistency, security, and fewer round-trips that app-only logic can't match. Many systems use both: app logic for UI, procedures for critical data operations.

> **🔑 Key terms:** reuse · performance (round-trips) · centralized logic · security (GRANT CALL) · consistency.

**📊 Depth table — Why procedures — benefit → concrete payoff (Nepal / IT)**

| Benefit | What it gives | Example |
|---|---|---|
| Reuse | write logic once, call everywhere | enroll() called by web + app + admin |
| Performance | fewer client-server round-trips | one CALL vs 10 separate queries |
| Centralized logic | rules live in one place | fee calculation can't drift between apps |
| Security | GRANT CALL, not table access | staff can enroll without raw table rights |
| Consistency | related steps run together | debit + credit in one transfer() |
| Maintainability | fix the rule in one spot | change the seat-limit check once |

*ℹ️ Banks and fintechs push critical logic (transfers, interest calc) into procedures for consistency, security, and speed. The debit+credit-together point leads straight into transactions (Unit 6).*

---

#### 🛠 ACTIVITY `[~5 min]`
What deserves to be a procedure? Name one repeated multi-step operation in a college system worth making a procedure, and list the steps it would bundle (e.g. enroll = check seats → insert → update count). Seeds: enroll a student, publish results (compute grades + lock + notify), promote a semester. Multi-step + repeated + critical = a good candidate.

### 🧠 CHECK FOR UNDERSTANDING `[~5 min]`
- MCQ1: A stored procedure is invoked using → ✅ CALL (or EXEC).
- MCQ2: The main difference from a view is that a procedure → ✅ runs procedural logic / can modify data.
- MCQ3: Which parameter mode returns a value to the caller? → ✅ OUT (and INOUT); IN only passes in.
- Discussion: name one college-system operation worth turning into a stored procedure.

### 💡 REAL-LIFE APPLICATION `[~3 min]`
Banks and fintechs push transfers and interest calculations into stored procedures for consistency, speed, and security — grasping them prepares you for real backend and database work.

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
(1) A stored procedure is a named, callable block of server-side logic (`CALL proc(args)`). (2) It takes IN/OUT/INOUT parameters and can run many statements and modify data (unlike a view). (3) Benefits: reuse, performance (fewer round-trips), centralized logic, and security (GRANT CALL). **Next:** code that fires automatically (triggers) and structures that make reads fast (indexes).

---
---

# S35 — DML Triggers · Indexing
**Lecture hour 14 (of 15) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`
[SLIDE] *"Every time a student is graded, the system should auto-log it — without the app remembering to. And when 'find roll 101' scans a million rows... why is it instant? Triggers and indexes."* → agenda: DML triggers → OLD/NEW & use cases → indexing → when indexes help/hurt.

### 📚 CONTENT `[~35 min]`

#### Concept 1 — DML Triggers `[THEORY]` `[SNIPPET]` `[~9 min]`
**📖 In Depth.** A **trigger** is code that fires **AUTOMATICALLY** on an INSERT, UPDATE, or DELETE — **BEFORE** or **AFTER** the event. You never call a trigger; the data-modification event fires it. `CREATE TRIGGER log_grade AFTER UPDATE ON Enrollment FOR EACH ROW INSERT INTO GradeAudit(...) VALUES(OLD.grade,NEW.grade,NOW());` BEFORE triggers can validate/adjust a row; AFTER triggers react (e.g. audit). `FOR EACH ROW` runs the trigger once per affected row. Triggers enforce rules and side-effects the app can't forget to run.

> **🌍 Real life.** Exam-integrity systems use an AFTER UPDATE trigger on the marks column to write every change (old value, new value, timestamp, user) to a GradeAudit table — so any tampering leaves a trail, automatically, whether the change came from the app, an admin script, or raw SQL.

> **🎯 Model exam answer.** *"What is a DML trigger?"* Code that fires automatically on an INSERT, UPDATE, or DELETE, either BEFORE (validate/adjust) or AFTER (react), running FOR EACH ROW affected. It is never called explicitly — the event fires it — making it ideal for audit trails, enforcing rules, and maintaining derived data regardless of which client made the change.

> **🧠 Hook:** "A trigger fires by itself on the event — you never CALL it."

> **⚠️ Misconception.** *"You have to call a trigger like a procedure."* No — a trigger fires by ITSELF on its INSERT/UPDATE/DELETE event; there is no CALL. That's its power (nothing can bypass it) and its danger (hidden side-effects if overused).

> **🔑 Key terms:** trigger · BEFORE/AFTER · INSERT/UPDATE/DELETE · fires automatically · FOR EACH ROW · audit.

**📊 Depth table — Trigger uses — event → automatic action**

| Trigger fires on | Timing | Automatic action |
|---|---|---|
| UPDATE of Enrollment.marks | AFTER | write old+new to GradeAudit (audit trail) |
| INSERT into Enrollment | BEFORE | reject if marks > 100 (defence-in-depth) |
| DELETE from Student | AFTER | archive the deleted row |
| UPDATE of wallet balance | AFTER | log the change for fraud analysis |
| INSERT into orders | AFTER | decrement stock automatically |
| UPDATE of salary | BEFORE | block a raise above a policy cap |

*ℹ️ Triggers run side-effects the application must never forget — audits, derived-total maintenance, extra validation. BEFORE can veto/adjust the change; AFTER reacts once it has happened.*

---

#### Concept 2 — OLD vs NEW & Trigger Use Cases `[THEORY]` `[~8 min]`
**📖 In Depth.** Inside a row-level trigger, **OLD** refers to the row's values before the change and **NEW** to the values after. Comparing them powers auditing, complex rule enforcement, and auto-maintaining derived totals. On UPDATE both exist; on INSERT only NEW exists; on DELETE only OLD exists. Audit: log `OLD.grade → NEW.grade` with `NOW()` on every marks change. A BEFORE trigger blocking `marks > 100` backs up the CHECK from S22 (defence-in-depth).

> **🌍 Real life.** A marks-audit trigger stores OLD.marks, NEW.marks, and NOW() every time a grade changes, giving investigators a complete before/after history. A BEFORE UPDATE trigger that rejects `NEW.marks > 100` adds a second line of defence behind the S22 CHECK constraint.

> **🎯 Model exam answer.** *"Explain OLD and NEW."* In a row-level trigger, OLD holds the pre-change values and NEW the post-change values; INSERT exposes only NEW, DELETE only OLD, UPDATE both. Comparing them enables auditing (log OLD→NEW), enforcing cross-value rules (block NEW.marks>100), and auto-maintaining derived totals.

> **🧠 Hook:** "OLD = the row before · NEW = the row after — compare them to react."

> **⚠️ Misconception.** *"Triggers can do everything, so put all logic in them."* Over-using triggers creates hidden, hard-to-debug side-effects ('why did this row change?'). Use them for audits, integrity, and derived-data upkeep — not as a dumping ground for business logic better kept visible in procedures/app code.

> **🔑 Key terms:** OLD (before) · NEW (after) · availability per event · audit & rule enforcement · defence-in-depth.

**📊 Depth table — OLD vs NEW by event, and what you'd do**

| Event | OLD available? | NEW available? | Typical use |
|---|---|---|---|
| INSERT | no | yes | validate/adjust NEW before storing |
| UPDATE | yes | yes | audit OLD→NEW; block bad changes |
| DELETE | yes | no | archive OLD before it's gone |
| BEFORE UPDATE marks>100 | yes | yes | reject NEW.marks>100 (with S22 CHECK) |
| AFTER UPDATE grade | yes | yes | INSERT (OLD.grade,NEW.grade,NOW()) to audit |
| AFTER INSERT order | no | yes | decrement stock by NEW.qty |

*ℹ️ OLD/NEW availability follows the event: INSERT has only NEW, DELETE only OLD, UPDATE has both. Comparing OLD and NEW is how a trigger audits changes and enforces cross-value rules.*

---

#### Concept 3 — Indexing (CREATE INDEX) `[THEORY]` `[SNIPPET]` `[HANDS-ON]` `[~9 min]`
**📖 In Depth.** An **index** is an auxiliary structure (usually a **B-tree**) that lets the DBMS find rows by a column's value quickly, instead of scanning the whole table. It speeds up **lookups, joins, and sorts** on that column. `CREATE INDEX idx_student_program ON Student(program);` A B-tree index lets a lookup jump to the row in a few hops, not a full scan. Indexes help WHERE, JOIN, and ORDER BY on the indexed column. The primary key is automatically indexed; you add indexes for other hot columns.

> **🌍 Real life.** Khalti's transaction-history page filters by user_id over millions of rows; an index on `transactions(user_id)` turns a full-table scan into an instant lookup, so the page loads in milliseconds. Correct indexing is the single most common fix that turns a slow screen fast.

> **🎯 Model exam answer.** *"What is an index?"* An auxiliary (usually B-tree) structure that lets the DBMS locate rows by a column's value in a few hops instead of scanning the whole table, accelerating WHERE, JOIN, and ORDER BY on that column. `CREATE INDEX name ON table(col)`. The primary key is indexed automatically; other frequently queried columns are indexed deliberately.

> **🧠 Hook:** "An index = the index at the back of a textbook — jump to the page, don't read every one."

> **⚠️ Misconception.** *"An index stores a separate copy of the data."* It stores an ordered structure of key values plus pointers to rows — not a full duplicate. Also, an index doesn't change query RESULTS, only their SPEED; a query returns the same rows with or without it.

> **🔑 Key terms:** index · B-tree · CREATE INDEX · table scan vs lookup · speeds WHERE/JOIN/ORDER BY.

**📊 Depth table — Table scan vs index lookup — the speed difference**

| Query | Without index | With index on the column |
|---|---|---|
| WHERE roll = 101 | scan every row | jump straight to it (B-tree) |
| WHERE program='BIM' | scan whole table | seek matching rows fast |
| JOIN … ON s.roll=e.roll | slow row-by-row match | fast indexed lookup per row |
| ORDER BY marks | sort all rows each time | read in index order (pre-sorted) |
| transactions WHERE user_id=… | scan millions of rows | index makes history load instant |
| Khalti history page | slow, times out | idx on (user_id) → fast |

*ℹ️ An index turns a full table scan (read every row) into a targeted lookup (a few B-tree hops). This is the #1 reason a slow app page becomes fast — index the columns you filter, join, and sort on.*

---

#### Concept 4 — When Indexes Help — and Hurt `[THEORY]` `[~8 min]`
**📖 In Depth.** Indexes **speed reads but slow writes** (every INSERT/UPDATE/DELETE must also maintain the index) and use extra storage. Index **selectively**: the columns you frequently filter, join, or sort on — not every column. Help: frequent WHERE/JOIN/ORDER BY on a high-selectivity column. Hurt: many indexes slow inserts/updates; unused indexes are pure overhead. Don't index everything 'just in case'.

> **🌍 Real life.** On the Enrollment table, indexing roll (used in almost every join to Student) and course_id (used to filter by course) pays off hugely; indexing rarely-queried columns just slows every grade entry. A write-heavy audit log, by contrast, is often left lightly indexed so inserts stay fast.

> **🎯 Model exam answer.** *"When do indexes help and hurt?"* They speed reads (WHERE/JOIN/ORDER BY) but slow writes, since every INSERT/UPDATE/DELETE must update each index, and they consume storage. Index selectively — the frequently filtered/joined/sorted, high-selectivity columns — rather than every column. Over-indexing degrades a write-heavy system.

> **🧠 Hook:** "Every index you add is another book you must re-sort on every write."

> **⚠️ Misconception.** *"Index every column for maximum speed."* Over-indexing slows every INSERT/UPDATE/DELETE (each index must be maintained) and wastes storage. Index the columns you actually filter, join, or sort on — selectivity and read-frequency decide, not 'just in case'.

> **🔑 Key terms:** index trade-off · reads faster / writes slower · storage cost · selectivity · index selectively.

**📊 Depth table — Index this? — decision guide**

| Column / situation | Index it? | Why |
|---|---|---|
| Enrollment.roll (joined often) | yes | speeds the student-grade join |
| Student.program (filtered often) | yes | fast WHERE program='BIM' |
| transactions.user_id (history page) | yes | turns a scan into a lookup |
| a rarely queried notes column | no | overhead with no read benefit |
| a column with 2 values (gender) | usually no | low selectivity — scan is as fast |
| a write-heavy log's every column | no | each index slows every INSERT |

*ℹ️ Index the columns you READ by (filter/join/sort), especially high-selectivity ones. Over-indexing slows writes and wastes storage — the classic 'index everything' mistake makes a write-heavy system slower, not faster.*

---

#### 🛠 SOLVED PROBLEM (deck) — Choose and create the right index for a slow query
**Problem.** A grades page runs `SELECT * FROM Enrollment WHERE roll = ?` for a student's transcript, and it's slow. Diagnose and fix it.

**Walkthrough.**
1. Confirm the filter column: the query filters (and joins) on roll — the hot column.
2. Check the current plan: `EXPLAIN SELECT * FROM Enrollment WHERE roll=101;` — a full scan means no useful index.
3. Create a targeted index: `CREATE INDEX idx_enrollment_roll ON Enrollment(roll);`
4. Re-run EXPLAIN — it should now show an index lookup instead of a scan.
5. Don't over-do it: add indexes only for the columns actually filtered/joined (roll, course_id), not every column.

**Answer.**
```sql
EXPLAIN SELECT * FROM Enrollment WHERE roll=101;    -- shows a full scan
CREATE INDEX idx_enrollment_roll ON Enrollment(roll);  -- now a fast B-tree lookup
```

#### 🛠 ACTIVITY `[~5 min]`
Which Enrollment column to index, and why? Consider how the table is queried (by roll? course_id? grade?) and weigh the read benefit against the write cost. roll and course_id are the natural indexes (constant joins/filters); grade is rarely a filter and low-selectivity, so skip it.

### 🧠 CHECK FOR UNDERSTANDING `[~5 min]`
- MCQ1: A trigger executes → ✅ automatically on a data-modification event (you never CALL it).
- MCQ2: Indexes generally make ___ faster but ___ slower → ✅ reads faster / writes slower.
- MCQ3: In an UPDATE trigger, the value BEFORE the change is → ✅ OLD (NEW holds post-change values).
- Discussion: which column in the Enrollment table would you index, and why?

### 💡 REAL-LIFE APPLICATION `[~3 min]`
Audit triggers underpin fraud and compliance trails in fintech; correct indexing is the #1 reason a slow app page becomes fast. Both are everyday tools for real database performance and integrity work.

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
(1) Triggers fire automatically on INSERT/UPDATE/DELETE (BEFORE/AFTER); OLD/NEW compare pre/post values. (2) Indexes (B-trees) turn full table scans into fast lookups for WHERE/JOIN/ORDER BY. (3) Indexes speed reads but slow writes and use storage — index selectively, not every column. **Next:** pulling all 15 sessions together — recap + a live lab problem-set walkthrough.

---
---

# S36 — SQL Recap + Lab Problem-Set Walkthrough (closes Unit 5)
**Lecture hour 15 (of 15) · 50 minutes**

### 🎯 OPENING — Hook `[~5 min]`
[SLIDE] *"Fifteen sessions, one language. Today we take a blank database and a stack of real questions, and answer every one — live."* → agenda: the SQL map → graded lab problems (easy→hard) → common-mistakes review → bridge to the lab project. Fully hands-on.

### 📚 CONTENT `[~35 min]`

#### Concept 1 — The SQL Map (Synthesis) `[THEORY]` `[~8 min]`
**📖 In Depth.** All of SQL fits one map: **DDL** defines structure; **DML** queries and modifies data; **views, joins, procedures, triggers, and indexes** extend it. Within a query, clauses run in a fixed logical order: `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY`. You WRITE SELECT first but the engine RUNS FROM first and SELECT almost last. Every concept in S22–S35 slots onto this single pipeline.

> **🌍 Real life.** A real backend query touches the whole map at once: a Daraz sales dashboard JOINs orders to customers (S33), filters with WHERE (S23), summarises with GROUP BY/HAVING (S26), handles NULLs (S27), reads from a VIEW (S30), and runs fast because of INDEXES (S35). One report, fifteen sessions.

> **🎯 Model exam answer.** *"Give the SQL map and clause order."* DDL builds structures, DML queries/modifies data, and views, joins, procedures, triggers, and indexes extend it. The logical execution order is `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY` — different from the written order — which explains alias scope and why aggregate conditions belong in HAVING.

> **🧠 Hook:** "Write order ≠ run order: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY."

> **⚠️ Misconception.** *"SQL clauses run in the order I type them."* No — the engine runs `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY`. That's why you can't use a SELECT alias in WHERE, and why aggregate filters go in HAVING, not WHERE.

> **🔑 Key terms:** SQL map · DDL/DML/views/joins/procedures/triggers/indexes · clause execution order · write vs run order.

**📊 Depth table — The Unit-5 callback grid — concept → session → one-line recall**

| Concept | Session | One-line recall |
|---|---|---|
| DDL & constraints | S22 | CREATE/ALTER/DROP; PK=UNIQUE+NOT NULL; DECIMAL for money |
| SELECT/FROM/WHERE | S23 | SELECT=columns, WHERE=rows; no condition = cross product |
| rename / aliases / strings | S24 | AS; self-join needs s1,s2; LIKE % (any) _ (one) |
| ORDER BY / DISTINCT / sets | S25 | sort; de-dup; UNION removes dups, UNION ALL keeps |
| aggregates / GROUP BY / HAVING | S26 | summaries; WHERE before, HAVING after grouping |
| NULL & 3-valued logic | S27 | IS NULL not = NULL; aggregates skip NULLs |
| subqueries IN/SOME/ALL | S28 | IN=member; >SOME=>MIN; >ALL=>MAX |
| EXISTS / UNIQUE | S29 | EXISTS=any row; NOT EXISTS='none'/'for all' |
| derived relations / views | S30 | subquery in FROM; view=saved query, no data |
| INSERT/UPDATE/DELETE | S31 | missing WHERE = whole table; SELECT-first |
| view updatability | S32 | single table, no aggregate/join; WITH CHECK OPTION |
| joins | S33 | INNER=both; LEFT keeps unmatched; prefer ON |
| stored procedures | S34 | CALL; logic + params; not a view |
| triggers / indexes | S35 | triggers auto-fire; index reads faster, writes slower |

*ℹ️ One-page map of the whole unit — each concept, its session, and the single line to remember. Use it to navigate revision and to see how the pieces connect on the query pipeline.*

---

#### 🛠 SOLVED PROBLEM (deck) · Lab EASY — Basic SELECT/WHERE and pattern matching
**Problem.** (1) List name and program of all 4th-semester BIM students. (2) List students whose name starts with 'A'.

**Walkthrough.** Filter on two columns with AND (`program='BIM' AND semester=4`) and project the two requested columns; use `LIKE 'A%'` for 'starts with A' (a leading 'A' fixes the first letter, `%` matches the rest). Test against the seed data (Anjali matches; Sita/Hari do not).

**Answer.**
```sql
-- 1)
SELECT name, program FROM Student WHERE program='BIM' AND semester=4;
-- 2)
SELECT name FROM Student WHERE name LIKE 'A%';
```

#### 🛠 SOLVED PROBLEM (deck) · Lab MEDIUM — Aggregation, top-N, and the 'missing' rows
**Problem.** (3) Average marks per course, only courses with >30 students. (4) Students with NO enrollment. (5) Top 3 students by marks.

**Walkthrough.** (3) `GROUP BY course_id`, then filter groups with `HAVING COUNT(*)>30` (not WHERE). (4) 'No enrollment' = LEFT JOIN keeping the NULL right side (or NOT EXISTS). (5) `ORDER BY marks DESC` then `LIMIT 3`.

**Answer.**
```sql
-- 3)
SELECT course_id, AVG(marks) FROM Enrollment GROUP BY course_id HAVING COUNT(*)>30;
-- 4)
SELECT s.name FROM Student s LEFT JOIN Enrollment e ON s.roll=e.roll WHERE e.roll IS NULL;
-- 5)
SELECT s.name, e.marks FROM Student s JOIN Enrollment e ON s.roll=e.roll ORDER BY e.marks DESC LIMIT 3;
```

#### 🛠 SOLVED PROBLEM (deck) · Lab HARD — Subqueries, views, and 'for all'
**Problem.** (6) Highest-paid instructor. (7) Create and query a MeritList view. (8) Students enrolled in EVERY IT course.

**Walkthrough.** (6) Highest-paid = salary equals the MAX salary (handles ties). (7) Save the join as a view, then select from it sorted. (8) 'Every IT course' = there is NO IT course the student is NOT enrolled in — the S29 double NOT EXISTS (relational division).

**Answer.**
```sql
-- 6)
SELECT name FROM Instructor WHERE salary=(SELECT MAX(salary) FROM Instructor);
-- 7)
CREATE VIEW MeritList AS SELECT roll,name,marks FROM Student JOIN Enrollment USING(roll);
SELECT * FROM MeritList ORDER BY marks DESC;
-- 8)
SELECT s.name FROM Student s
WHERE NOT EXISTS (SELECT 1 FROM Course c WHERE c.dept='IT'
  AND NOT EXISTS (SELECT 1 FROM Enrollment e WHERE e.roll=s.roll AND e.course_id=c.course_id));
```

**📊 Depth table — Common-mistakes review — the classic Unit-5 bugs**

| Mistake | Why it's wrong | The fix | Session |
|---|---|---|---|
| WHERE grade = NULL | = NULL is always UNKNOWN → no rows | WHERE grade IS NULL | S27 |
| UPDATE/DELETE with no WHERE | changes/wipes EVERY row | add WHERE; SELECT-first | S31 |
| WHERE COUNT(*) > 30 | aggregates illegal in WHERE | use HAVING COUNT(*)>30 | S26 |
| NATURAL JOIN everywhere | silently joins on all shared names | use ON / USING explicitly | S33 |
| NOT IN with a NULL in the set | returns no rows unexpectedly | filter NULLs / use NOT EXISTS | S28 |
| INNER when you needed LEFT | hides the unmatched rows you wanted | use LEFT OUTER JOIN | S33 |
| money as FLOAT | binary rounding drifts totals | use DECIMAL(p,s) | S22 |

*ℹ️ These seven bugs account for most real-world SQL errors. Recognising them on sight — and the one-line fix for each — is what separates a fluent SQL writer from a beginner.*

---

#### Concept 2 — Bridge to the Lab Project `[THEORY]`
**📖 In Depth.** The syllabus lab project (individual or group ≤4) asks you to pick a domain — library, clinic, or e-shop — design the tables (Units 1–4), then write CRUD and reports (this unit): CREATE TABLE with constraints, INSERT seed data, SELECT/JOIN reports, a couple of views, and sensible indexes. This end-to-end fluency — design plus SQL — is the marketable outcome of the whole course.

> **🌍 Real life.** The Unit-5 skills combine directly into the lab project: model a chosen domain as tables with constraints, seed it with INSERTs, answer questions with SELECT/JOIN/GROUP BY reports, expose role-based VIEWs, and add INDEXes for speed.

> **⚠️ Misconception.** *"SQL is just for exams."* It is one of the most-requested skills on nearly every data/backend job posting in Nepal and abroad. The lab project is a portfolio piece — a small but complete database you can demo in an interview.

> **🔑 Key terms:** lab project · design → CRUD → reports · views + indexes · portfolio piece · job-relevant SQL.

#### 🛠 ACTIVITY `[~5 min]`
Three queries a Nepali app runs daily: pick an app (eSewa, Daraz, a college portal) and list 3 SQL queries its database must answer every day (a filter, an aggregate, a join). Seeds: daily transaction total (SUM+GROUP BY date), a user's history (WHERE user_id + ORDER BY date), orders-with-customer (JOIN).

### 🧠 CHECK FOR UNDERSTANDING `[~5 min]`
- MCQ1: The correct clause EXECUTION order is → ✅ `FROM→WHERE→GROUP BY→HAVING→SELECT→ORDER BY` (the engine runs FROM first, SELECT near last).
- MCQ2: 'Find rows where email is missing' uses → ✅ IS NULL.
- MCQ3: 'Students enrolled in EVERY IT course' is expressed with → ✅ double NOT EXISTS ('for all' = 'no counterexample').
- Discussion: pick a Nepali app and list 3 SQL queries its database must answer every day.

### 💡 REAL-LIFE APPLICATION `[~3 min]`
This problem-solving fluency IS the marketable skill: SQL appears on nearly every data and backend job posting in Nepal and abroad. The lab project turns it into a portfolio piece you can demo.

### 📝 SUMMARY & TAKEAWAYS `[~2 min]`
(1) DDL builds, DML uses, and views/joins/procedures/triggers/indexes extend — all on one query pipeline. (2) Clause order (`FROM→WHERE→GROUP BY→HAVING→SELECT→ORDER BY`) and NULL/WHERE habits prevent the classic bugs. (3) You can now read and write production-style SQL — and build a complete lab-project database. **Next unit:** keeping data correct when many users hit it at once — transactions, concurrency & recovery (Unit 6).

---
---

## 📎 Unit 5 · Cheat Sheet — one-page SQL revision reference (MySQL / MariaDB)
- **DDL & constraints (S22)** — CREATE/ALTER/DROP TABLE. Types: INT, DECIMAL(p,s) for money, VARCHAR/CHAR, DATE, BOOLEAN. Constraints: PRIMARY KEY (=UNIQUE+NOT NULL), FOREIGN KEY, NOT NULL, UNIQUE, CHECK, DEFAULT.
- **Query basics (S23–S25)** — `SELECT cols FROM t WHERE rows`; AND/OR/NOT, BETWEEN, IN. AS renames; s1/s2 self-join; LIKE % (any) _ (one). ORDER BY … DESC, LIMIT n; DISTINCT; UNION/INTERSECT/EXCEPT (UNION ALL keeps dups).
- **Aggregates & NULL (S26–S27)** — COUNT/SUM/AVG/MIN/MAX; GROUP BY (per group), HAVING (filter groups, aggregates ok). WHERE before, HAVING after. NULL: use IS NULL; aggregates skip NULLs; COALESCE(x,0).
- **Subqueries (S28–S29)** — IN=member (=SOME); >SOME=>MIN; >ALL=>MAX; <>ALL=NOT IN. EXISTS=any row; NOT EXISTS='none'/'for all' (double). Beware NOT IN + NULL.
- **Views & modify (S30–S32)** — Derived relation = subquery in FROM (alias!). VIEW = saved query, no data (not faster). Updatable = single table, no aggregate/join/DISTINCT/derived col; WITH CHECK OPTION. INSERT/UPDATE/DELETE — WHERE or whole table.
- **Joins, procs, triggers, index (S33–S35)** — INNER=both; LEFT/RIGHT/FULL keep unmatched (NULLs); prefer ON. Procedure=CALL, logic+params. Trigger fires auto (BEFORE/AFTER, OLD/NEW). Index=B-tree; reads faster, writes slower; index selectively.

---

## END-OF-UNIT QUIZ — Unit 5: SQL (consolidated) · answers ✅

### Part A — Concept MCQs
1. `CREATE TABLE` belongs to → ✅ DDL. 2. PRIMARY KEY is equivalent to → ✅ UNIQUE + NOT NULL. 3. To store NPR currency precisely, use → ✅ DECIMAL. 4. Which clause filters rows? → ✅ WHERE. 5. SELECT chooses → ✅ columns (projection). 6. `LIKE '%a'` matches names that → ✅ end with 'a'. 7. `_` in LIKE matches → ✅ exactly one character. 8. Default ORDER BY direction is → ✅ ascending (ASC). 9. Which removes duplicates? → ✅ UNION (UNION ALL keeps them). 10. INTERSECT returns → ✅ rows in BOTH result sets. 11. Which can appear in WHERE? → ✅ `salary>5000` (not `COUNT(*)>5`). 12. HAVING filters → ✅ groups. 13. `WHERE grade = NULL` returns → ✅ no rows (use IS NULL). 14. `COUNT(*)` vs `COUNT(col)` differ when → ✅ col has NULLs. 15. `> ALL(subquery)` is true when the value exceeds → ✅ every value. 16. EXISTS is true when the subquery → ✅ returns ≥1 row. 17. A standard view stores → ✅ the query, not the data. 18. A non-updatable view typically contains → ✅ GROUP BY / aggregate / join. 19. LEFT JOIN keeps unmatched rows from → ✅ the left table. 20. A DML trigger runs → ✅ automatically on INSERT/UPDATE/DELETE. 21. Indexes typically make reads ___ and writes ___ → ✅ faster / slower. 22. CALL invokes a → ✅ stored procedure.

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

## ✅ Unit 5 complete
S22–S36 delivered to standard: DDL & constraints · SELECT/FROM/WHERE · rename/tuple-variables/strings · ORDER BY/DISTINCT/set-operations · aggregates & GROUP BY/HAVING · NULL & three-valued logic · subqueries (IN/SOME/ALL, EXISTS/UNIQUE) · derived relations & views · INSERT/UPDATE/DELETE · view updatability · joins (INNER/OUTER/NATURAL) · stored procedures · DML triggers & indexing · full recap + lab walkthrough. Built to `COURSE_MATERIAL_STANDARD.md` including the §7A depth rule — 47 worked-SQL / comparison / scaffolding tables on the slide face, self-contained and PDF-safe, MySQL / MariaDB throughout, on one running college schema.

This markdown is the source of truth; the built deck is **`IT220_Unit5.pptx` (219 slides)**, regenerated via `build_unit5_pptx.py` (imports `deckkit.py`). **Next unit:** Unit 6 — Transactions, Concurrency & Recovery.
