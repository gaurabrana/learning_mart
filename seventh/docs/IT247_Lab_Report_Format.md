# IT 247 — Lab Report Format (printed A4)
### How to prepare and print your lab report

Your lab report is the document you submit and are examined on. There is **no live demo** — so your
report must, on its own, prove that you built and ran the website. Follow this exact structure so every
report is consistent and easy for the examiner to mark.

Answer the 16 questions in **[IT247_Lab_Questions.md](IT247_Lab_Questions.md)**. Each answer =
**code + screenshot + explanation**.

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
- **IT 247: E-Commerce and Internet Marketing — Lab Report**
- Your store's name and theme (e.g. *"TechMart — an online electronics store"*)
- Student name, roll number, section/group
- Submitted to: (instructor name), Department of …
- Date

### 2. Certificate / sign-off page
A short certificate plus a sign-off table (the examiner looks for the instructor's signatures):

> *This is to certify that **[name]**, roll no. **[…]**, has completed the laboratory work of the course
> **IT 247: E-Commerce and Internet Marketing** during the academic year …, as recorded in this report.*
>
> Internal Examiner: ______________  External Examiner: ______________  Date: __________

| # | Lab work | Date completed | Instructor signature |
|---|----------|----------------|----------------------|
| 1 | Setup & DB connection | | |
| 2 | Database design | | |
| … | … | | |
| 11 | Social media analysis | | |

### 3. Index
A table: **Question no. · Title · Page no.** — so the examiner can jump to any answer.

### 4. Introduction (½ page)
- What you built (store name, what it sells)
- The tech stack: PHP, MySQL (PDO), Bootstrap 5, XAMPP (local), InfinityFree (live)
- The tools used in the marketing part (Search Console, Keyword Planner, Google Ads, GA4, Buffer)

### 5. Answers (main body)
Repeat this block for **each** question, Q1 → Q16:

> **Q[n]. [paste the question text]**
>
> **Code:**
> ```php
> // only the relevant file/lines for this question
> ```
>
> **Output:** *(a labelled screenshot — Fig n)*
>
> **Explanation:** 1–2 lines in your own words on what the code does / what the screenshot shows.

### 6. Conclusion (½ page)
What you learned building an e-commerce store and using the marketing tools; any challenges and how you
solved them.

---

## Formatting rules (keep it consistent)
- **Paper:** A4, portrait. Margins ~1 inch. Page numbers in the footer.
- **Body text:** a clean serif/sans font, size 11–12.
- **Code:** a **monospace** font (Consolas / Courier New), in a bordered box or shaded block, small enough
  to read but not tiny. Paste **only the relevant lines**, not the whole file.
- **Screenshots:** cropped to the relevant part, clear and legible, labelled *Fig 1, Fig 2, …*. A blurry or
  full-desktop screenshot loses marks.
- **Headers:** each Part (A: Website, B: Marketing) can start on a new page.
- **Your own work:** the code in the report must match the code you can explain in the viva.

## What makes a screenshot count as proof
- **phpMyAdmin** shots must show the actual table + rows (Q2 products, Q5 hashed password, Q8 order rows).
- **Browser** shots must show your page working (the product grid, the cart total, the logged-in name, the
  live HTTPS padlock in the address bar for Q11).
- For security (Q10), show the **result** — the injection being rejected, and the `<script>` printed as
  plain text.
- For marketing (Q12–Q16), show the tool's own screen (verified property, keyword table, draft campaign,
  GA4 Realtime, the audit).

## Before you print
1. Answer all 16 questions; check each has code **and** a screenshot **and** an explanation.
2. Get the sign-off table signed by your instructor.
3. Print, arrange in page order, and bind (spiral or staple) as your college requires.
