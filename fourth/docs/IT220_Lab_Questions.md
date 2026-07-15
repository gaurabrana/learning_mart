# IT 220 — Lab Questions (answer from your own database)
### Database Management System · BIM 4th Semester · MySQL/MariaDB (XAMPP + phpMyAdmin)

These are the definitive lab questions for IT 220. You answer them by **documenting the Himalaya
College database you built across the 16 labs, in a printed lab report (A4)**. For every question,
write:

1. **The question** (as given here),
2. **The SQL or diagram** you produced (paste the exact statements in a code box),
3. **A screenshot** of the result on *your* screen — this is your proof it ran, and
4. **A 1–2 line explanation** in your own words.

Wherever a question says "show", "run", or "demonstrate", it means **include a screenshot** in your
report. You submit the printed report; the external examiner reads it and asks you to explain your own
work in the viva. Lay out your report using the **[Lab Report Format](IT220_Lab_Report_Format.md)**.

> Step-by-step help for every question is in **[IT220_Lab_Manual.md](IT220_Lab_Manual.md)** — the
> question numbers match the lab numbers.

---

## Part A — Setup & Design (Labs 1–7)

**Q1. Environment.** Show a screenshot of your **XAMPP Control Panel** with MySQL/MariaDB running
(green), and phpMyAdmin open at `http://localhost/phpmyadmin`. In one line, explain what phpMyAdmin
is versus what MySQL is.

**Q2. Inside the DBMS.** Show the query
`SELECT table_name FROM information_schema.tables WHERE table_schema='himalaya_college';` and its
result. Explain what "metadata" means and what the `information_schema` is.

**Q3. ER diagram.** Include your **ER diagram** of Himalaya College (Student, Teacher, Course,
Enrolment, FeePayment). Mark the primary keys and the relationships. Explain which relationship is
**many-to-many** and why.

**Q4. Relational schema.** Show your written schema (all 5 tables with PK/FK marked). Explain what a
**junction table** is and why `Enrolment` needs a **composite primary key**.

**Q5. Relational algebra.** Show your RelaX results for a **SELECT (σ)**, a **PROJECT (π)**, and a
**JOIN (⋈)**. Explain in one line what each of the three operations does.

**Q6. Functional dependencies.** Show the messy enrolment table and list the **functional
dependencies** you found in it. Explain what `X → Y` means.

**Q7. Normalization.** Show your **1NF → 2NF → 3NF** working for the messy table. Explain what problem
(anomaly) each step removed.

---

## Part B — Building & Querying (Labs 8–12)

**Q8. DDL & constraints.** Show your `CREATE TABLE` statements for `Student`, `Course`, and
`Enrolment`, and a phpMyAdmin screenshot of the 5 tables. Point to one **FOREIGN KEY** and explain
what it prevents.

**Q9. Querying.** Show one query using **WHERE**, one using an **aggregate + GROUP BY**, and one using
**HAVING**, each with its result. Explain why `WHERE grade = NULL` does not work and what you use
instead.

**Q10. Subqueries & views.** Show a **subquery** (students who have/haven't paid) and your
**`paid_students` view** being queried. Explain the difference between a table and a view.

**Q11. Modification & joins.** Show an **UPDATE** (with WHERE) and an **INNER JOIN** and a **LEFT
JOIN**, each with results. Explain the danger of an `UPDATE`/`DELETE` with no `WHERE`, and the
difference between INNER and LEFT JOIN.

**Q12. Procedures, triggers, indexing.** Show your **stored procedure** being `CALL`ed, your
**trigger** filling `payment_log` automatically after an INSERT, and an **`EXPLAIN`** using your
**index**. Explain what a trigger is in one line.

---

## Part C — Reliability & Project (Labs 13–16)

**Q13. Transactions.** Show a `START TRANSACTION` … `ROLLBACK` sequence with the balance **before and
after**. Explain what "atomic / all-or-nothing" means and name the four **ACID** properties.

**Q14. Concurrency.** Show two sessions where one **blocks** the other on the same row until `COMMIT`.
Explain what a **lock** is and what a **deadlock** is.

**Q15. Backup, recovery & security.** Show your **exported `.sql` backup**, a table **dropped then
restored via Import**, and `SHOW GRANTS` for a limited user. Explain "least privilege" and the roles
of `GRANT`/`REVOKE`.

**Q16. Project + NoSQL.** Present your complete project (diagram → schema → build → queries → security
→ backup) and your **relational-vs-NoSQL** comparison (include the sample JSON document). Explain one
situation where NoSQL fits better than a relational database.

---

### How this is used
- **Printed lab report (submitted):** answer all 16 questions — each with the SQL/diagram, a
  screenshot, and a short explanation. Follow the **Lab Report Format** guide, and get it signed off
  by your instructor before printing.
- **Viva (external + internal):** the examiner reads your report and asks you to **explain your own
  SQL** — e.g. "explain the join in Q11" or "why a transaction in Q13". If you built it yourself, you
  can explain it; a copied report falls apart here.

*(Instructor's version with model answers and marking: [IT220_Lab_Work_and_Viva.md](IT220_Lab_Work_and_Viva.md).)*
