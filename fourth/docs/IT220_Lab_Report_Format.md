# IT 220 — Lab Report Format (printed A4)
### Database Management System · How to prepare and print your lab report

Your lab report is the document you submit and are examined on. It must, on its own, prove that you
designed, built, queried, and secured the **Himalaya College** database. Follow this exact structure
so every report is consistent and easy for the examiner to mark.

Answer the 16 questions in **[IT220_Lab_Questions.md](IT220_Lab_Questions.md)**. Each answer =
**SQL/diagram + screenshot + explanation**.

---

## Order of pages

1. **Cover page**
2. **Certificate / sign-off page**
3. **Index (table of contents)**
4. **Introduction** (½ page)
5. **Answers to Q1–Q16** (the main body)
6. **Conclusion** (½ page)

---

### 1. Cover page
Centered, one page:
- College / campus name and logo
- **IT 220: Database Management System — Lab Report**
- The database you built: *"Himalaya College — a student/course/fees database"*
- Student name, roll number, section/group
- Submitted to: (instructor name), Department of …
- Date

### 2. Certificate / sign-off page
A short certificate plus a sign-off table (the examiner looks for the instructor's signatures):

> *This is to certify that **[name]**, roll no. **[…]**, has completed the laboratory work of the
> course **IT 220: Database Management System** during the academic year …, as recorded in this
> report.*
>
> Internal Examiner: ______________  External Examiner: ______________  Date: __________

| # | Lab work | Date completed | Instructor signature |
|---|----------|----------------|----------------------|
| 1 | Install XAMPP; first look | | |
| 2 | Inside the DBMS | | |
| 3 | ER diagram | | |
| 4 | ER → relational schema | | |
| 5 | Relational algebra | | |
| 6 | Calculus & functional dependencies | | |
| 7 | Normalization | | |
| 8 | DDL & constraints | | |
| 9 | Querying (SELECT/aggregates) | | |
| 10 | Subqueries & views | | |
| 11 | Modification & joins | | |
| 12 | Procedures, triggers, indexing | | |
| 13 | Transactions & ACID | | |
| 14 | Concurrency & locking | | |
| 15 | Backup, recovery & security | | |
| 16 | Project + NoSQL | | |

### 3. Index
A table: **Question no. · Title · Page no.** — so the examiner can jump to any answer.

### 4. Introduction (½ page)
- What you built (the Himalaya College database — what it stores and why).
- The tools: MySQL/MariaDB via XAMPP, phpMyAdmin, dbdiagram.io (design), RelaX (relational algebra).
- One line on how the labs progressed: design → build → query → secure → back up.

### 5. Answers (main body)
Repeat this block for **each** question, Q1 → Q16:

> **Q[n]. [paste the question text]**
>
> **SQL / Diagram:**
> ```sql
> -- only the relevant statements for this question
> ```
>
> **Output:** *(a labelled screenshot — Fig n)*
>
> **Explanation:** 1–2 lines in your own words on what the SQL does / what the screenshot shows.

### 6. Conclusion (½ page)
What you learned building a database from ER design to backup; any errors you hit (e.g. a foreign-key
failure) and how you fixed them.

---

## Formatting rules (keep it consistent)
- **Paper:** A4, portrait. Margins ~1 inch. Page numbers in the footer.
- **Body text:** a clean serif/sans font, size 11–12.
- **SQL / code:** a **monospace** font (Consolas / Courier New), in a bordered or shaded box. Paste
  **only the relevant statements**, not the whole database.
- **Screenshots:** cropped to the relevant part, clear and legible, labelled *Fig 1, Fig 2, …*. A
  blurry or full-desktop screenshot loses marks.
- **Diagrams:** the ER diagram (Q3) should be exported cleanly (PNG), not photographed off a screen.
- **Your own work:** the SQL in the report must match what you can explain in the viva.

## What makes a screenshot count as proof
- **phpMyAdmin** shots must show the actual table + rows (Q8 the 5 tables; Q12 the auto-filled
  `payment_log`; Q15 the restored table).
- **Result grids** must show your query's real output (Q9 the GROUP BY counts; Q11 the joined rows).
- For transactions (Q13), show the balance **before and after** ROLLBACK.
- For concurrency (Q14), show the **second session waiting**, then completing after COMMIT.
- For design (Q3, Q7), show the ER diagram and the normalization steps.

## Before you print
1. Answer all 16 questions; check each has SQL/diagram **and** a screenshot **and** an explanation.
2. Get the sign-off table signed by your instructor.
3. Print, arrange in page order, and bind (spiral or staple) as your college requires.

---

> **Companion documents:** [IT220_Lab_Questions.md](IT220_Lab_Questions.md) (what to answer),
> [IT220_Lab_Manual.md](IT220_Lab_Manual.md) (step-by-step how), and
> [IT220_Lab_Work_and_Viva.md](IT220_Lab_Work_and_Viva.md) (instructor/viva copy).
