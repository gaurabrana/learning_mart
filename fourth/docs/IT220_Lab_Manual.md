# IT 220 — Database Management System · Lab Manual (Student Workbook)
### BIM 4th Semester · 16 weekly practicals · **for complete beginners**

> **Read this first.** This manual assumes you have **never** installed a database, never written
> SQL, and have never seen a command line. Every step tells you exactly what to click, type, and
> expect to see. If a step doesn't work, read the **"If it goes wrong"** box under it before asking
> for help. Do the labs **in order** — each one builds on the last.
>
> **One running example.** Across all 16 labs we build **one** database — a small college called
> **Himalaya College** (students, teachers, courses, enrolments, fee payments). By Lab 16 you will
> have designed it, built it, queried it, secured it, and backed it up. This is also your **project**.

---

## The tools you will use (install once, in Lab 1)

| Tool | What it is | Why we use it |
|------|-----------|---------------|
| **XAMPP** | A free bundle that installs the **MySQL/MariaDB** database + a web server on your own computer | One installer gives you everything; works on Windows/Mac/Linux |
| **MySQL / MariaDB** | The actual **database server** (the "DBMS") | This is the software the whole course is about |
| **phpMyAdmin** | A **web page** (opens in your browser) that lets you click through databases and run SQL | Beginner-friendly — you see tables and results visually |
| **dbdiagram.io** | A free website for drawing **ER diagrams** | Used in Labs 3–4 for design |
| **RelaX** | A free website that runs **relational algebra** | Used in Labs 5–6 |

> **What is "SQL"?** SQL (say "sequel" or "S-Q-L") is the language you type to talk to a database —
> to create tables, put data in, and ask questions of the data. You will learn it from Lab 8 onward.
> Before that (Labs 1–7) you learn to *set up*, *design*, and *reason about* databases first.

---

## How to use this manual with your lab report

For **every** lab you must keep evidence for your final **lab report** (see
[IT220_Lab_Report_Format.md](IT220_Lab_Report_Format.md)). After each lab, save:
1. The **SQL / diagram** you produced (copy the text, or export).
2. A **screenshot** of the result on *your* screen.
3. A **one-line note** in your own words of what it did.

Take screenshots as you go — do **not** try to recreate them at the end of the semester.

---
---

# PART 1 — Setup & Foundations (Labs 1–7)
*You cannot write real SQL until Unit 5 (Week 8). These weeks get your tools working and teach you
to design a database on paper/tools first — which is the part beginners usually skip and regret.*

---

## Lab 1 (Week 1) — Install everything & see a database for the first time

**Goal:** Get XAMPP installed, start the database server, open phpMyAdmin, and run your first
*given* query to see live data. You are **not** expected to understand the SQL yet — just see it work.

### Before you start
- A laptop where you can install software (you may need the admin/login password).
- ~30 minutes and an internet connection for the download.

### Steps

**1. Download XAMPP.**
- Open your browser, go to **`https://www.apachefriends.org`**.
- Click the download for **your operating system** (Windows / macOS / Linux). The file is large
  (~150 MB); wait for it to finish.

**2. Install XAMPP.**
- Open the downloaded file and click **Next** through the installer, accepting the defaults.
- If Windows shows a security/firewall popup, click **Allow**.
- Finish and let it open the **XAMPP Control Panel** (Windows) or **manager-osx** (Mac).

**3. Start the database.**
- In the XAMPP Control Panel, find the row that says **MySQL** (on some versions it says
  **MariaDB** — same thing for us) and click its **Start** button.
- Also click **Start** next to **Apache** (this runs the web server that phpMyAdmin needs).
- Both rows should turn **green**.

**4. Open phpMyAdmin.**
- Open your browser and go to **`http://localhost/phpmyadmin`**.
- You should see a page with a list of databases on the left and tabs (Databases, SQL, Status…)
  across the top. **This is your window into the database server.**

**5. Load a sample database to look at.**
- Click the **SQL** tab at the top.
- A big empty text box appears. **Copy the block below exactly** and paste it in, then click **Go**
  (bottom right).

```sql
CREATE DATABASE demo_shop;
USE demo_shop;
CREATE TABLE product (
  id    INT PRIMARY KEY,
  name  VARCHAR(50),
  price INT
);
INSERT INTO product VALUES (1, 'Wai Wai Noodles', 20);
INSERT INTO product VALUES (2, 'Dairy Milk', 100);
INSERT INTO product VALUES (3, 'Frooti', 35);
```

- You should see a green **"success"** message. On the left, a new database **demo_shop** appears.

**6. Run your first query.**
- Still on the **SQL** tab, clear the box, type exactly this, and click **Go**:

```sql
SELECT * FROM product;
```

- A table appears showing your 3 products. **Congratulations — you just queried a database.**

### What you should see
A results grid with 3 rows (Wai Wai, Dairy Milk, Frooti). Take a **screenshot** of this.

### If it goes wrong
- **MySQL won't turn green / stops immediately (Windows):** usually another program uses its port.
  In the Control Panel click **Config → my.ini**, or simplest: close Skype and any other database,
  then Start again. If it still fails, restart the computer and try once more.
- **`http://localhost/phpmyadmin` shows "not found":** Apache isn't started — go back and Start
  Apache too.
- **"Access denied":** on a fresh XAMPP the username is **`root`** with an **empty password** — don't
  type a password.

### What you learned
A **database server** (MySQL) runs in the background; **phpMyAdmin** is just a friendly window onto
it; and **SQL** is the text you send to make it do things. `SELECT * FROM product` means "show me
every row from the product table."

---

## Lab 2 (Week 2) — Look inside the DBMS: databases, schemas, users

**Goal:** Understand the *structure* of a database server — the difference between a **database**, a
**table**, and a **row** — and create a **user** with limited permissions. This makes Unit 1's
"three-schema architecture" and "DBA" concrete.

### Steps

**1. See the three levels.** In phpMyAdmin, look at the left panel:
- The **server** holds many **databases** (you see `demo_shop` and some system ones).
- Click **demo_shop** → it holds **tables** (you see `product`).
- Click **product** → it holds **rows** (your 3 items) and **columns** (id, name, price).

Write this hierarchy in your report: **Server → Database → Table → Row/Column.**

**2. See the "catalog" (data about data).** Click the database **`information_schema`** on the left,
then its **TABLES** table, then **Browse**. This is the DBMS describing *itself* — every table on
the server is listed here. Run this on the **SQL** tab to prove it:

```sql
SELECT table_name FROM information_schema.tables WHERE table_schema = 'demo_shop';
```

You should get one row: `product`. **This is metadata — "data about the data".**

**3. Create a database user (the DBA's job).**
- Click the **User accounts** tab at the top.
- Click **Add user account**.
- User name: `college_clerk` · Host name: choose **Local** · Password: type `clerk123` (twice).
- **Do not** tick "Global privileges." Scroll down and click **Go**.

**4. Give that user limited rights.**
- Back on **User accounts**, click **Edit privileges** next to `college_clerk`.
- Click the **Database** tab, choose `demo_shop`, click **Go**.
- Tick only **SELECT** and **INSERT** (not DROP or DELETE), then **Go**.
- You have just made a user who can *read and add* data but cannot *delete tables*. That is what a
  **DBA (Database Administrator)** does — hand out only the rights each person needs.

### What you should see
The `information_schema` query returning `product`, and `college_clerk` listed with limited
privileges. Screenshot both.

### What you learned
The DBMS separates **physical storage**, the **logical tables** you see, and the **views/permissions**
each user gets — that layering is the **three-schema architecture**. A **DBA** manages users and
their privileges with `GRANT`/`REVOKE` (phpMyAdmin did the GRANT for you behind the scenes).

---

## Lab 3 (Week 3) — Design an ER diagram (on paper first, then a tool)

**Goal:** Before building any table, *design* the Himalaya College database as an **ER (Entity-
Relationship) diagram**. This is Unit 2 made practical.

> **Vocabulary (don't skip):**
> - **Entity** = a *thing* we store data about (a Student, a Course). Becomes a table.
> - **Attribute** = a *fact* about an entity (a student's name, roll no). Becomes a column.
> - **Primary key (PK)** = the attribute that *uniquely* identifies one row (roll_no for a student).
> - **Relationship** = how entities connect ("a student *enrols in* a course").
> - **Cardinality** = how many: one-to-one (1:1), one-to-many (1:N), many-to-many (M:N).

### Steps

**1. On paper**, list the entities of Himalaya College and their attributes:
- **Student** (roll_no [PK], name, address, phone, semester)
- **Teacher** (teacher_id [PK], name, department, phone)
- **Course** (course_code [PK], title, credit_hours)
- **Enrolment** — a student takes a course in a semester (this connects Student and Course)
- **FeePayment** (receipt_no [PK], amount, date) — belongs to a Student

**2. Decide the relationships and cardinality:**
- A **Student** *enrols in* many **Courses**, and a **Course** has many **Students** → **M:N**
  (many-to-many). *(This M:N is why we will need a junction table in Lab 4 — remember it.)*
- A **Teacher** *teaches* many **Courses**, a Course is taught by one Teacher → **1:N**.
- A **Student** *makes* many **FeePayments**, each payment belongs to one Student → **1:N**.

**3. Draw it in a tool.**
- Go to **`https://dbdiagram.io`** → click **Go to app** (no login needed to start).
- On the left code panel, delete the sample and type this (it draws the diagram on the right):

```
Table Student {
  roll_no int [pk]
  name varchar
  address varchar
  phone varchar
  semester int
}
Table Teacher {
  teacher_id int [pk]
  name varchar
  department varchar
}
Table Course {
  course_code varchar [pk]
  title varchar
  credit_hours int
  teacher_id int [ref: > Teacher.teacher_id]   // 1:N teacher→course
}
Table FeePayment {
  receipt_no int [pk]
  roll_no int [ref: > Student.roll_no]          // 1:N student→payment
  amount int
  paid_on date
}
```

- The diagram appears on the right with lines connecting the tables. **Export it: Export → PNG.**

### What you should see
A clean ER diagram showing Student, Teacher, Course, FeePayment and the lines between them.
(The M:N Student↔Course we will resolve in Lab 4.) Screenshot / export the diagram.

### If it goes wrong
- **Red error in dbdiagram:** you mistyped a keyword — check every `[pk]`, `ref:` and the curly
  braces `{ }`. Copy the block again carefully.

### What you learned
You **model the real world before touching SQL**. Entities become tables, attributes become columns,
and relationships become the foreign keys you'll create later. M:N relationships need special
handling — next lab.

---

## Lab 4 (Week 4) — Turn the ER diagram into tables (the relational schema)

**Goal:** Convert your Lab 3 design into a precise **table plan** with primary keys, foreign keys,
and — crucially — a **junction table** for the many-to-many relationship.

### Steps

**1. Resolve the M:N.** A student takes many courses and a course has many students. A single table
cannot store this. The rule: **every M:N becomes a new table in the middle** (a *junction* table)
that holds the two keys. We call it **Enrolment**:

```
Enrolment( roll_no  → Student.roll_no,
           course_code → Course.course_code,
           semester,
           grade )
```

Its **primary key** is the *pair* (roll_no, course_code) — a student can't enrol in the same course
twice. This is called a **composite primary key**.

**2. Add it to your dbdiagram** (append to the code from Lab 3):

```
Table Enrolment {
  roll_no int [ref: > Student.roll_no]
  course_code varchar [ref: > Course.course_code]
  semester int
  grade varchar
  indexes {
    (roll_no, course_code) [pk]   // composite primary key
  }
}
```

**3. Write out the full schema in text** (this goes in your report — it's your build plan for Lab 8):

```
Student(roll_no PK, name, address, phone, semester)
Teacher(teacher_id PK, name, department, phone)
Course(course_code PK, title, credit_hours, teacher_id FK→Teacher)
Enrolment(roll_no FK→Student, course_code FK→Course, semester, grade)   PK=(roll_no, course_code)
FeePayment(receipt_no PK, roll_no FK→Student, amount, paid_on)
```

### What you should see
The updated diagram now has **5 tables**, with Enrolment sitting between Student and Course.

### What you learned
- **Foreign key (FK):** a column that points to another table's primary key — it *enforces* that you
  can't enrol a student who doesn't exist.
- **Junction table:** how you store a many-to-many relationship.
- **Composite key:** a primary key made of two columns together.

---

## Lab 5 (Week 5) — Relational algebra by hand (RelaX)

**Goal:** Practise the operations from Unit 3 — **SELECT (σ), PROJECT (π), JOIN (⋈)** and set
operations — on sample data, using a tool that shows you the result of each.

### Steps

**1. Open the tool.** Go to **`https://dbis-uibk.github.io/relax`** → choose **"relalg" / RelaX
calculator**. It comes with a sample dataset (tables like `Student`, `Course`).

**2. Try each operation.** Type these one at a time in the query box and press **Enter/Execute**:

| You type | Meaning | Relational-algebra form |
|----------|---------|-------------------------|
| `Student` | show the whole table | (base relation) |
| `σ semester = 2 (Student)` | rows where semester is 2 | **SELECT** σ |
| `π Student.name (Student)` | only the name column | **PROJECT** π |
| `π name (σ semester = 2 (Student))` | names of 2nd-sem students | σ then π |
| `Student ⋈ Enrolment` | combine matching rows | **JOIN** ⋈ |

*(RelaX has buttons for the symbols σ π ⋈ ∪ ∩ − if you can't type them.)*

**3. Match each to plain English** in your report — e.g. "σ = filter rows, π = pick columns,
⋈ = combine two tables where a column matches."

### What you should see
Each query returns a small result table. Screenshot at least the SELECT, PROJECT, and JOIN results.

### What you learned
Relational algebra is the *math* behind SQL. When you write `SELECT name FROM Student WHERE
semester=2` in Lab 9, you are really doing **π** on top of **σ** — the same thing you did here.

---

## Lab 6 (Week 6) — Relational calculus & spotting functional dependencies

**Goal:** Express a couple of queries in **relational calculus** (Unit 3), then learn to **spot
functional dependencies (FDs)** in a messy table — the skill you need to normalize in Lab 7.

### Steps

**1. Calculus (short, on paper + RelaX).** Relational calculus describes *what* you want, not the
steps. Write, for the Student table:
- Tuple calculus: `{ t | t ∈ Student ∧ t.semester = 2 }` — "all tuples t in Student where semester = 2."
- Confirm it gives the same rows as `σ semester=2 (Student)` from Lab 5.

**2. Spot FDs in a bad table.** Look at this deliberately messy "enrolment sheet":

| roll_no | student_name | course_code | course_title | teacher_name |
|---------|-------------|-------------|--------------|--------------|
| 101 | Sita | CMP101 | Programming | Ram Sir |
| 101 | Sita | ENG101 | English | Gita Miss |
| 102 | Hari | CMP101 | Programming | Ram Sir |

Ask: *"if I know column X, is column Y always fixed?"* That arrow is a **functional dependency**:
- `roll_no → student_name` (a roll number always gives the same name) ✔
- `course_code → course_title` (a course code always gives the same title) ✔
- `course_code → teacher_name` (each course has one teacher here) ✔
- But `roll_no` alone does **not** give `course_code` (Sita has two) ✘

**3. Write the FD list** in your report. Notice the table repeats "Programming / Ram Sir" — that
**redundancy** is the problem normalization fixes next week.

### What you learned
A **functional dependency X → Y** means "X decides Y." Finding FDs tells you which facts belong in
which table — the foundation of normalization.

---

## Lab 7 (Week 7) — Normalization: fix a messy table step by step

**Goal:** Take the messy table from Lab 6 and normalize it to **1NF → 2NF → 3NF**, showing your work
(Unit 4). No SQL yet — this is pen-and-paper design.

### Steps — follow the ladder

**Start (unnormalized / has problems):**
`Enrolment(roll_no, student_name, course_code, course_title, teacher_name)`
Problems: the same course title and teacher are repeated on every row (**update anomaly** — change
the teacher and you must edit many rows).

**1. First Normal Form (1NF):** every cell holds **one value** (no lists), and there's a key.
Our table is already 1NF (no multi-valued cells). Key = (roll_no, course_code).

**2. Second Normal Form (2NF):** remove attributes that depend on **only part** of the composite key.
- `student_name` depends on `roll_no` alone → move it out to a **Student** table.
- `course_title` depends on `course_code` alone → move it to a **Course** table.

Result:
```
Student(roll_no PK, student_name)
Course(course_code PK, course_title, teacher_name)
Enrolment(roll_no, course_code)  PK=(roll_no, course_code)
```

**3. Third Normal Form (3NF):** remove attributes that depend on a **non-key** attribute.
- In Course, does `teacher_name` depend on the key `course_code`, or on something else? If a teacher
  can be identified separately, split teachers out:
```
Teacher(teacher_id PK, teacher_name)
Course(course_code PK, course_title, teacher_id FK→Teacher)
```

**Final (3NF):** Student, Teacher, Course, Enrolment — **the same design you drew in Lab 4.** That's
the point: good ER design already gives you normalized tables.

### What you should see
A written step-by-step showing 1NF → 2NF → 3NF with the reason for each split. This is a key exam
skill — keep it neat.

### What you learned
Normalization removes **redundancy** and **anomalies** by splitting one wide table into several
focused tables joined by keys. You now have a verified, normalized design ready to **build in SQL**.

---
---

# PART 2 — Building & Querying in SQL (Labs 8–12)
*Unit 5 has started. Now you write real SQL to build and use the Himalaya College database.*

> **Where you type SQL from now on:** phpMyAdmin → click your database → the **SQL** tab → type →
> **Go**. You can run one statement or several at once.

---

## Lab 8 (Week 8) — Create the database & tables (DDL) and add data

**Goal:** Build the normalized Himalaya College schema from Lab 4/7 using **DDL** (Data Definition
Language: `CREATE`), with proper keys and constraints, then `INSERT` sample data.

### Steps

**1. Create the database.** phpMyAdmin → **SQL** tab → run:

```sql
CREATE DATABASE himalaya_college;
USE himalaya_college;
```

**2. Create the tables** (run this whole block). Read the comments — they explain each **constraint**:

```sql
CREATE TABLE Teacher (
  teacher_id  INT PRIMARY KEY,                 -- unique id for each teacher
  name        VARCHAR(60) NOT NULL,            -- NOT NULL = must have a value
  department  VARCHAR(40),
  phone       VARCHAR(15)
);

CREATE TABLE Student (
  roll_no   INT PRIMARY KEY,
  name      VARCHAR(60) NOT NULL,
  address   VARCHAR(60),
  phone     VARCHAR(15),
  semester  INT CHECK (semester BETWEEN 1 AND 8)   -- CHECK = only allow 1..8
);

CREATE TABLE Course (
  course_code  VARCHAR(10) PRIMARY KEY,
  title        VARCHAR(60) NOT NULL,
  credit_hours INT DEFAULT 3,                   -- DEFAULT if none given
  teacher_id   INT,
  FOREIGN KEY (teacher_id) REFERENCES Teacher(teacher_id)  -- must be a real teacher
);

CREATE TABLE Enrolment (
  roll_no      INT,
  course_code  VARCHAR(10),
  semester     INT,
  grade        VARCHAR(2),
  PRIMARY KEY (roll_no, course_code),           -- composite key
  FOREIGN KEY (roll_no) REFERENCES Student(roll_no),
  FOREIGN KEY (course_code) REFERENCES Course(course_code)
);

CREATE TABLE FeePayment (
  receipt_no INT PRIMARY KEY,
  roll_no    INT,
  amount     INT NOT NULL,
  paid_on    DATE,
  FOREIGN KEY (roll_no) REFERENCES Student(roll_no)
);
```

- On the left you now see 5 tables under `himalaya_college`. **Screenshot the table list.**

**3. Insert data** (run this block):

```sql
INSERT INTO Teacher VALUES
 (1,'Ram Thapa','Computer','9841000001'),
 (2,'Gita Sharma','English','9841000002');

INSERT INTO Student VALUES
 (101,'Sita Rai','Bhaktapur','9801000101',2),
 (102,'Hari Karki','Lalitpur','9801000102',2),
 (103,'Mina Gurung','Kathmandu','9801000103',4);

INSERT INTO Course VALUES
 ('CMP101','Programming',3,1),
 ('ENG101','English',3,2),
 ('DBM220','Database Management',3,1);

INSERT INTO Enrolment VALUES
 (101,'CMP101',2,'A'),
 (101,'ENG101',2,'B'),
 (102,'CMP101',2,'A'),
 (103,'DBM220',4,NULL);

INSERT INTO FeePayment VALUES
 (5001,101,15000,'2026-01-10'),
 (5002,102,15000,'2026-01-12');
```

**4. Verify:** run `SELECT * FROM Student;` — you should see 3 students.

### If it goes wrong
- **"Cannot add or update a child row: a foreign key constraint fails":** you inserted a row that
  points to something that doesn't exist yet (e.g. an Enrolment before its Student). Insert **parents
  first** (Teacher, Student, Course) *then* children (Enrolment, FeePayment) — the order above already
  does this.
- **"Duplicate entry for key PRIMARY":** you ran the INSERT twice. Either skip it or delete the rows.

### What you learned
**DDL** builds structure. **Constraints** (`PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, `CHECK`,
`DEFAULT`) are the database *protecting itself* from bad data — the FK is why you can never enrol a
student who doesn't exist.

---

## Lab 9 (Week 9) — Ask questions: SELECT, WHERE, ORDER BY, aggregates

**Goal:** Query the data with the most-used SQL: filtering, sorting, and summarising (Unit 5). Run
each, read the result, and note what it does.

### Steps — run these one at a time

```sql
-- 1. Everything, specific columns
SELECT name, semester FROM Student;

-- 2. WHERE = filter rows
SELECT name FROM Student WHERE semester = 2;

-- 3. ORDER BY = sort; DESC = high to low
SELECT name, semester FROM Student ORDER BY name ASC;

-- 4. DISTINCT = remove duplicates
SELECT DISTINCT semester FROM Student;

-- 5. Aggregate functions summarise many rows into one number
SELECT COUNT(*) AS total_students FROM Student;
SELECT AVG(amount) AS average_fee FROM FeePayment;
SELECT MAX(amount) AS biggest_payment FROM FeePayment;

-- 6. GROUP BY = one summary row per group
SELECT semester, COUNT(*) AS how_many
FROM Student
GROUP BY semester;

-- 7. HAVING = filter AFTER grouping
SELECT course_code, COUNT(*) AS students_in_course
FROM Enrolment
GROUP BY course_code
HAVING COUNT(*) >= 2;

-- 8. NULL check — grade not yet given
SELECT roll_no, course_code FROM Enrolment WHERE grade IS NULL;
```

### What you should see
Each query returns a small, sensible result (e.g. query 6 shows semester 2 → 2 students, semester
4 → 1). Screenshot queries 2, 6, and 7.

### If it goes wrong
- **`WHERE grade = NULL` returns nothing:** you must use **`IS NULL`**, never `= NULL` — NULL means
  "unknown" and isn't equal to anything.

### What you learned
`SELECT … FROM … WHERE … GROUP BY … HAVING … ORDER BY` is the shape of almost every query.
**Aggregates** (COUNT/SUM/AVG/MIN/MAX) collapse many rows into a summary; **GROUP BY** does it per
category; **HAVING** filters those summaries.

---

## Lab 10 (Week 10) — Subqueries and Views

**Goal:** Write a query *inside* another query (subquery) and save a query as a reusable **view**.

### Steps

**1. Subquery — a query used as a value:**

```sql
-- Students who have made at least one fee payment
SELECT name FROM Student
WHERE roll_no IN (SELECT roll_no FROM FeePayment);

-- Students who have NOT paid (note NOT IN)
SELECT name FROM Student
WHERE roll_no NOT IN (SELECT roll_no FROM FeePayment);

-- EXISTS version (true if the inner query finds any row)
SELECT name FROM Student s
WHERE EXISTS (SELECT 1 FROM Enrolment e WHERE e.roll_no = s.roll_no);
```

**2. Create a View** — a saved query you can treat like a table:

```sql
CREATE VIEW paid_students AS
SELECT s.roll_no, s.name, f.amount, f.paid_on
FROM Student s
JOIN FeePayment f ON s.roll_no = f.roll_no;
```

Now use it like a table:

```sql
SELECT * FROM paid_students;
```

### What you should see
The subqueries return the right students (101 & 102 paid, 103 hasn't). `paid_students` behaves like
a table. Screenshot both.

### What you learned
A **subquery** lets one query depend on another's result. A **view** stores a query under a name so
you (or a limited user) can reuse it without rewriting the SQL — and without seeing the underlying
tables directly (a security/simplicity tool).

---

## Lab 11 (Week 11) — Changing data (UPDATE/DELETE) and JOINs

**Goal:** Modify existing data safely, and combine tables with every kind of **JOIN**.

### Steps

**1. Modify data:**

```sql
-- INSERT one new student
INSERT INTO Student VALUES (104,'Bikash Lama','Pokhara','9801000104',2);

-- UPDATE — ALWAYS include WHERE, or you change every row!
UPDATE Student SET phone = '9811111111' WHERE roll_no = 104;

-- DELETE — again, ALWAYS a WHERE
DELETE FROM Student WHERE roll_no = 104;
```

> ⚠️ **The most dangerous beginner mistake:** `UPDATE Student SET semester = 1;` with **no WHERE**
> changes *every* student. Always write the `WHERE` first.

**2. JOINs — combine tables:**

```sql
-- INNER JOIN: only rows that match in both tables
SELECT s.name, c.title, e.grade
FROM Enrolment e
JOIN Student s ON e.roll_no = s.roll_no
JOIN Course c ON e.course_code = c.course_code;

-- LEFT JOIN: keep ALL students, even those with no enrolment
SELECT s.name, e.course_code
FROM Student s
LEFT JOIN Enrolment e ON s.roll_no = e.roll_no;

-- Join to show each course with its teacher's name
SELECT c.title, t.name AS teacher
FROM Course c
JOIN Teacher t ON c.teacher_id = t.teacher_id;
```

### What you should see
The INNER JOIN lists student + course + grade together; the LEFT JOIN shows every student (a student
with no enrolment shows NULL for course). Screenshot both joins.

### What you learned
`UPDATE`/`DELETE` **must** have a `WHERE`. A **JOIN** stitches related tables back together using the
foreign keys you designed — **INNER** keeps only matches, **LEFT** keeps everything from the left
table.

---

## Lab 12 (Week 12) — Stored procedures, triggers, indexing · **SQL practical test week**

**Goal:** Automate logic inside the database with a **stored procedure** and a **trigger**, and speed
up queries with an **index**.

> **Note:** In phpMyAdmin, when you create a procedure or trigger that contains semicolons, set the
> **Delimiter** box (below the SQL area) to `$$` first, or use the code exactly as written below.

### Steps

**1. Stored procedure** — a saved block of SQL you can call by name:

```sql
DELIMITER $$
CREATE PROCEDURE students_in_semester(IN sem INT)
BEGIN
  SELECT roll_no, name FROM Student WHERE semester = sem;
END $$
DELIMITER ;
```

Run it:

```sql
CALL students_in_semester(2);
```

**2. Trigger** — SQL that runs *automatically* on an event. Make an audit log of new payments:

```sql
CREATE TABLE payment_log (
  log_id INT AUTO_INCREMENT PRIMARY KEY,
  receipt_no INT,
  logged_at DATETIME
);

DELIMITER $$
CREATE TRIGGER after_payment
AFTER INSERT ON FeePayment
FOR EACH ROW
BEGIN
  INSERT INTO payment_log (receipt_no, logged_at)
  VALUES (NEW.receipt_no, NOW());
END $$
DELIMITER ;
```

Test it — insert a payment, then check the log filled itself:

```sql
INSERT INTO FeePayment VALUES (5003, 103, 15000, '2026-01-15');
SELECT * FROM payment_log;
```

**3. Index** — speeds up searching a column:

```sql
CREATE INDEX idx_student_name ON Student(name);
-- See the plan: does the query use the index?
EXPLAIN SELECT * FROM Student WHERE name = 'Sita Rai';
```

### What you should see
`CALL` returns the 2nd-sem students; after the INSERT, `payment_log` has an auto-created row; EXPLAIN
shows the query can use `idx_student_name`. Screenshot all three.

### What you learned
- **Stored procedure:** reusable logic stored *in* the database, called by name.
- **Trigger:** logic that fires **automatically** on INSERT/UPDATE/DELETE — great for audit logs.
- **Index:** a lookup structure that makes searches faster (like a book's index).

---
---

# PART 3 — Reliability: Transactions, Recovery, Project (Labs 13–16)
*Unit 6 & 7. Now you make the database trustworthy under failure and finish your project.*

---

## Lab 13 (Week 13) — Transactions & ACID

**Goal:** See how a **transaction** groups steps so they **all succeed or all fail together** (Unit 6).
Example: paying fees should reduce a balance *and* record a receipt — never one without the other.

### Steps

**1. Set up a simple balance table:**

```sql
CREATE TABLE account (
  roll_no INT PRIMARY KEY,
  balance INT
);
INSERT INTO account VALUES (101, 20000), (102, 20000);
```

**2. A good transaction (COMMIT):**

```sql
START TRANSACTION;
UPDATE account SET balance = balance - 15000 WHERE roll_no = 101;
INSERT INTO FeePayment VALUES (5004, 101, 15000, '2026-01-20');
COMMIT;   -- both steps are now permanent, together
```

Check: `SELECT * FROM account WHERE roll_no = 101;` → balance is 5000.

**3. A rolled-back transaction (ROLLBACK):** imagine you notice a mistake before committing:

```sql
START TRANSACTION;
UPDATE account SET balance = balance - 99999 WHERE roll_no = 102;  -- oops, wrong amount
SELECT balance FROM account WHERE roll_no = 102;   -- see the temporary change
ROLLBACK;                                          -- undo everything
SELECT balance FROM account WHERE roll_no = 102;   -- back to 20000
```

### What you should see
After COMMIT the change stays; after ROLLBACK it disappears. Screenshot the balance before/after
ROLLBACK.

### What you learned
A transaction is **all-or-nothing** — the **A** in **ACID (Atomicity, Consistency, Isolation,
Durability)**. `COMMIT` makes changes permanent; `ROLLBACK` undoes them. This is why banks and
eSewa-style transfers use transactions.

---

## Lab 14 (Week 14) — Concurrency: two users at once

**Goal:** See what happens when **two sessions** touch the same data, and how the database uses
**locking** and **isolation levels** to keep things correct (Unit 6).

### Steps

**1. Open two SQL sessions.** Easiest way: open phpMyAdmin in **two browser tabs** (or one normal +
one incognito window). Call them **Tab A** and **Tab B**.

**2. See a lock.**
- In **Tab A** run (and do *not* commit yet):

```sql
START TRANSACTION;
UPDATE account SET balance = balance - 1000 WHERE roll_no = 101;
```

- In **Tab B** run:

```sql
UPDATE account SET balance = balance - 500 WHERE roll_no = 101;
```

- **Tab B waits** (spins) — it is *blocked* because Tab A holds a lock on that row.
- Go back to **Tab A** and run `COMMIT;` — now **Tab B** completes. The database made them take
  turns so neither overwrites the other blindly.

**3. Isolation levels (read the idea).** Run in a session:

```sql
SELECT @@transaction_isolation;   -- shows the current level (usually REPEATABLE-READ)
```

Note in your report: higher isolation (SERIALIZABLE) = safer but slower; lower = faster but risks
anomalies like **dirty reads** (reading another transaction's uncommitted change).

### What you should see
Tab B pausing until Tab A commits. Screenshot both tabs (the waiting one and then the completed one).

### What you learned
When many users share data, the DBMS uses **locks** so changes don't clash (**concurrency control**).
**Isolation levels** let you trade safety for speed. A **deadlock** is when two transactions each wait
for the other — the DBMS detects it and cancels one.

---

## Lab 15 (Week 15) — Backup, recovery & security

**Goal:** Make a **backup**, simulate a disaster, **restore** it, and set up basic **security** with
users and privileges (Unit 6 recovery + Unit 7 security).

### Steps

**1. Back up (export).** In phpMyAdmin, click the `himalaya_college` database → **Export** tab →
method **Quick** → format **SQL** → **Go**. A `.sql` file downloads. **This file is your backup** — it
contains the SQL to rebuild everything.

**2. Simulate a disaster.** Run (carefully!):

```sql
DROP TABLE payment_log;   -- pretend this was lost
```

Confirm it's gone (`SELECT * FROM payment_log;` errors).

**3. Restore.** Click the database → **Import** tab → **Choose file** → pick the `.sql` backup you
just downloaded → **Go**. The dropped table returns. *(If it complains that other tables already
exist, that's fine — the table you dropped is what matters; or restore into a fresh empty database to
see a clean recovery.)*

**4. Security — least privilege.** Recreate the limited user idea from Lab 2 with SQL:

```sql
CREATE USER 'clerk'@'localhost' IDENTIFIED BY 'clerk123';
GRANT SELECT, INSERT ON himalaya_college.* TO 'clerk'@'localhost';
-- NOT granting DROP/DELETE — the clerk cannot destroy data
REVOKE INSERT ON himalaya_college.* FROM 'clerk'@'localhost';  -- take a right back
SHOW GRANTS FOR 'clerk'@'localhost';
```

### What you should see
The export file on your disk; the table gone after DROP and back after Import; `SHOW GRANTS` listing
the clerk's limited rights. Screenshot the export dialog and the restored table.

### What you learned
**Backups** are your insurance — recovery means replaying them. **Security** follows *least
privilege*: give each user only the rights they need, using `GRANT` and `REVOKE`.

---

## Lab 16 (Week 16) — Project demo + a taste of NoSQL

**Goal:** Present your complete Himalaya College database as your **project**, and see how a **NoSQL**
database differs from the relational one you built (Unit 7).

### Steps

**1. Assemble your project** (individual or a group of up to 4). It must show the full journey:
- The **ER diagram** (Lab 3–4)
- The **normalized schema** (Lab 7)
- The **CREATE + INSERT** SQL (Lab 8)
- At least **5 useful queries** including a JOIN, an aggregate/GROUP BY, and a subquery (Labs 9–11)
- One **view**, one **stored procedure or trigger**, and one **index** (Labs 10, 12)
- A **transaction** example and a **backup** file (Labs 13, 15)

**2. Compare with NoSQL (understand, don't install).** In SQL, a student's data is spread across
rows in several tables. In a **document** (NoSQL, e.g. MongoDB) database, the *same* student could be
one document:

```json
{
  "roll_no": 101,
  "name": "Sita Rai",
  "enrolments": [
    { "course": "CMP101", "grade": "A" },
    { "course": "ENG101", "grade": "B" }
  ]
}
```

Write in your report: **relational** = fixed tables + relationships + strong consistency (great for
fees/records); **NoSQL document** = flexible, nested, scales easily (great for changing/huge data),
but weaker on cross-table guarantees.

**3. Present** your project to the class/instructor and answer questions on any part of it.

### What you should see
A complete, working database you can explain end to end, plus a written relational-vs-NoSQL
comparison.

### What you learned
You designed, built, queried, secured, and backed up a real relational database — and you can now
explain *when* a different model (NoSQL) fits better. **This is the whole course in one project.**

---
---

## Appendix A — Quick troubleshooting (all labs)

| Problem | Cause | Fix |
|---------|-------|-----|
| MySQL won't start (XAMPP) | Port 3306 in use / previous crash | Close other DB tools; restart PC; Start again |
| `http://localhost/phpmyadmin` not found | Apache not started | Start Apache in XAMPP |
| "Access denied for user root" | Typed a password | User `root`, password **empty** on fresh XAMPP |
| "Foreign key constraint fails" | Inserted child before parent | Insert Teacher/Student/Course **before** Enrolment/FeePayment |
| "Duplicate entry for PRIMARY" | Ran an INSERT twice | Don't re-run, or delete the duplicate row |
| `WHERE x = NULL` returns nothing | NULL isn't equal to anything | Use `IS NULL` / `IS NOT NULL` |
| Procedure/trigger gives a syntax error | Semicolons confuse phpMyAdmin | Set the **Delimiter** box to `$$` |
| An `UPDATE`/`DELETE` changed everything | You forgot `WHERE` | Restore from your backup (Lab 15) — and always write `WHERE` first |

## Appendix B — SQL keywords you learned, in one place

`CREATE DATABASE/TABLE`, `PRIMARY KEY`, `FOREIGN KEY … REFERENCES`, `NOT NULL`, `CHECK`, `DEFAULT`,
`INSERT INTO … VALUES`, `SELECT … FROM … WHERE`, `ORDER BY`, `DISTINCT`, `COUNT/SUM/AVG/MIN/MAX`,
`GROUP BY`, `HAVING`, `IS NULL`, subqueries `IN`/`NOT IN`/`EXISTS`, `CREATE VIEW`, `UPDATE`, `DELETE`,
`JOIN`/`LEFT JOIN … ON`, `CREATE PROCEDURE`/`CALL`, `CREATE TRIGGER`, `CREATE INDEX`, `EXPLAIN`,
`START TRANSACTION`/`COMMIT`/`ROLLBACK`, `CREATE USER`, `GRANT`/`REVOKE`, Export/Import (backup).

> **Next:** answer the questions in [IT220_Lab_Questions.md](IT220_Lab_Questions.md), lay them out
> using [IT220_Lab_Report_Format.md](IT220_Lab_Report_Format.md), and get each lab signed off.
