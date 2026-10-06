# IT 220 — Lab Questions (answer from your own database)
### Database Management System · BIM 4th Semester · MySQL/MariaDB (XAMPP + phpMyAdmin)

These are the definitive lab questions for IT 220. You answer them by **documenting the Model
College database you built across the 16 labs, in a printed lab report (A4)**. For every question,
write:

1. **The question** (as given here),
2. **The SQL** you ran (paste the exact statements in a code box),
3. **A screenshot** of the result on *your* screen — this is your proof it ran, and
4. **A 1–2 line explanation** in your own words.

Wherever a question says "show", "run", or "demonstrate", it means **include a screenshot** in your
report. You submit the printed report; the external examiner reads it and asks you to explain your own
work in the viva. Lay out your report using the **[Lab Report Format](IT220_Lab_Report_Format.md)**.

> Step-by-step help for every question is in **[IT220_Lab_Manual.md](IT220_Lab_Manual.md)** — the
> question numbers match the lab numbers.

> **Note:** relational algebra, relational calculus and pen-and-paper normalization are **lecture**
> topics (Units 3 and 4) and are examined in the theory paper, not in this lab report.

---

## Part A — Setup & design (Labs 1–3)

**Q1. Environment and your first query.** Show a screenshot of your **XAMPP Control Panel** with
MySQL/MariaDB running (green) and phpMyAdmin open at `http://localhost/phpmyadmin`. Then show
`SELECT * FROM product;` and `SELECT name FROM product WHERE price > 30;` with their results.
Explain in one line what phpMyAdmin is versus what MySQL is.

**Q2. Inside the DBMS.** Show the query
`SELECT table_name FROM information_schema.tables WHERE table_schema='demo_shop';` and its result,
and `SHOW GRANTS FOR 'college_clerk'@'localhost';` for the limited user you created. Explain what
"metadata" means, what `information_schema` is, and what a DBA does.

**Q3. Database design.** Include your **ER diagram** of Model College (Student, Teacher, Course,
Enrolment, FeePayment) exported as a PNG, plus the written schema with PK/FK marked. Explain which
relationship is **many-to-many**, why `Enrolment` exists, and why its primary key is **composite**.

---

## Part B — Building the database (Labs 4–5)

**Q4. DDL & constraints.** Show your `CREATE TABLE` statements for all five tables, the output of
`SHOW TABLES;` and `DESCRIBE Enrolment;`, and **one deliberate constraint violation with its error
message**. Point to one `FOREIGN KEY` and explain what it prevents.

**Q5. INSERT.** Show your `INSERT` statements for all five tables and `SELECT * FROM Student;` with
its result. Show the foreign-key error you get when inserting an `Enrolment` for a student who does
not exist. Explain why parent tables must be filled before child tables.

---

## Part C — Querying (Labs 6–10)

**Q6. SELECT, WHERE, ORDER BY.** Show one query using `WHERE` with `AND`/`OR`, one using `LIKE`, one
using `ORDER BY … DESC`, and one using `DISTINCT` — each with its result. Explain what `DISTINCT`
does and what the `%` in a `LIKE` pattern means.

**Q7. Aggregates, GROUP BY, HAVING, NULL.** Show `COUNT(*)`, a `GROUP BY` (students per semester or
per course), and a `HAVING` query, each with its result. Also show `WHERE grade = NULL` returning
nothing next to `WHERE grade IS NULL` returning rows. Explain the difference between `WHERE` and
`HAVING`, and why `= NULL` never works.

**Q8. JOINs.** Show an `INNER JOIN` across three tables (student name + course title + grade), a
`LEFT JOIN` that reveals students with no enrolment or no payment, and one **self-join**. Explain the
difference between `INNER` and `LEFT JOIN`, and what makes a JOIN possible.

**Q9. Subqueries.** Show a subquery using `IN`, one using `NOT IN` (students who have not paid), and
one using `EXISTS` or a derived table in `FROM`. Explain what a subquery is and give one case where a
JOIN would do the same job.

**Q10. Views.** Show `CREATE VIEW` for your `enrolment_sheet` (or `paid_students`) view, a query
against it, and an `UPDATE` made **through** a simple view changing the real table. Explain the
difference between a table and a view, and why a joined view is usually not updatable.

---

## Part D — Modifying and automating (Labs 11–12)

**Q11. UPDATE and DELETE.** Show a `SELECT` used to check the `WHERE` **before** an `UPDATE`, then the
`UPDATE` and a confirming `SELECT`. Show a `DELETE` that fails because of a foreign key. Explain the
danger of an `UPDATE`/`DELETE` with no `WHERE` and how a transaction can undo the mistake.

**Q12. Procedures, triggers, indexing.** Show your **stored procedure** being `CALL`ed, your
**trigger** filling `payment_log` automatically after an `INSERT`, and `EXPLAIN` before and after
`CREATE INDEX`. Explain in one line each what a stored procedure, a trigger, and an index are.

---

## Part E — Reliability & project (Labs 13–16)

**Q13. Transactions.** Show a `START TRANSACTION` … `ROLLBACK` sequence with the balance **before and
after**, and a transaction that fails halfway so that neither step is applied. Explain what
"atomic / all-or-nothing" means and name the four **ACID** properties.

**Q14. Concurrency.** Show two sessions where one **blocks** the other on the same row until `COMMIT`,
and show that a different row does **not** block. Explain what a lock is, that locks are per-row, and
what a deadlock is.

**Q15. Backup, recovery & security.** Show your **exported `.sql` backup**, a table **dropped then
restored via Import**, and `SHOW GRANTS` for a limited user **before and after** a `REVOKE`. Explain
"least privilege" and the roles of `GRANT`/`REVOKE`.

**Q16. Project.** Present your complete project — ER diagram → schema → build → data → queries →
view/procedure/trigger/index → transaction → backup → limited user. Be ready to run any query live
and modify it on request.

---

### How this is used
- **Printed lab report (submitted):** answer all 16 questions — each with the SQL, a screenshot, and
  a short explanation. Follow the **Lab Report Format** guide, and get it signed off by your
  instructor before printing.
- **Viva (external + internal):** the examiner reads your report and asks you to **explain your own
  SQL** — e.g. "explain the join in Q8" or "why a transaction in Q13" — and may ask you to change a
  query on the spot. If you built it yourself, you can explain it; a copied report falls apart here.

*(Instructor's version with model answers and marking: [IT220_Lab_Work_and_Viva.md](IT220_Lab_Work_and_Viva.md).)*
