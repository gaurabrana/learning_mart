# IT 247 — Lab Questions (answer from your own website)
### E-Commerce and Internet Marketing · BIM / BITM 7th Semester

These are the definitive lab questions for IT 247. You answer them by **documenting the e-commerce website
you built in a printed lab report (A4)**. For every question, write:

1. **The question** (as given here),
2. **The relevant code** you wrote (paste the exact file/lines in a code box),
3. **A screenshot** of it working — taken from your screen; this is your proof it runs, and
4. **A 1–2 line explanation** in your own words.

Wherever a question says "show", "open", or "demonstrate", it means **include a screenshot** in your
report. You submit the printed report; the external examiner reads it and asks you to explain your own code
in the viva. Lay out your report using the **Lab Report Format** guide.

**Your store:** PHP + MySQL (PDO), built on XAMPP, deployed on InfinityFree.

---

## Part A — Your E-Commerce Website (16 questions total; 11 here)

**Q1. Database connection.** Show your `connect.php`. Did you use MySQLi or PDO, and why is PDO with
prepared statements the safer choice?

**Q2. Database design.** Show the `CREATE TABLE` statements for `products` and `categories` (mark the
primary key and foreign key), and include a phpMyAdmin screenshot of your `products` table with data.
Explain the relationship between the two tables.

**Q3. Product listing.** Show the code that lists all products from the database and the resulting product
grid. Explain how PHP loops over the rows to build the cards.

**Q4. Product detail & search.** Show your single-product page (fetched by `id`) and your product search.
Explain how the prepared statement stops SQL injection.

**Q5. Registration & login.** Show your registration and login code using `password_hash()` and
`password_verify()`, plus a phpMyAdmin screenshot proving the stored password is a **hash**, not plain
text.

**Q6. Sessions & logout.** Show how your site knows a user is logged in (the session) and your logout code.
Include a screenshot of the header while logged in.

**Q7. Shopping cart.** Show your add-to-cart code (session-based) and the cart page with 3 items and the
correct total. Is the total calculated on the **server** or in the **browser**, and why does that matter?

**Q8. Checkout & order.** Show the code that saves an order into `orders` + `order_items`, and a phpMyAdmin
screenshot of the created rows. Why did you use a **transaction**?

**Q9. Payment (sandbox).** Show your sandbox payment (eSewa/Khalti) and the code where it is **verified on
the server** before the order is marked paid. Include a screenshot of the test payment.

**Q10. Security.** Include screenshots showing (a) `' OR '1'='1` rejected at login, and (b)
`<script>alert(1)</script>` displayed as plain text. Name the technique/function that stops each.

**Q11. Deployment.** Include a screenshot of your live store's URL with the **HTTPS padlock**. Which host
did you use and why can this not run on Netlify? How do the database settings differ between XAMPP and the
live host?

---

## Part B — Digital Marketing (answer from your live store + tool screenshots)

**Q12. Search Console.** Include a screenshot of your **verified property** in Google Search Console. You
verify with the **HTML-file method** — upload the `google<...>.html` file Google gives you to your site
root. Where did you place that file, and why does verification need a live HTTPS URL?

**Q13. Keyword report.** Present your **10-keyword report** built with **Google Trends** (region = Nepal),
with columns **keyword, demand, intent, where you used it on the site**. Explain how you read "demand" from
the Search-interest bar, and the difference between **transactional** and **commercial** intent. Show one
product where you put a keyword into the `<title>`/`<meta description>`.

**Q14. Ad campaign plan.** Present a **Google Search ad campaign plan** for your store: the goal, one ad
group, **5 keywords** (from Q13), **3 headlines + 2 descriptions**, and the **landing URL with UTM tags**
pointing at a real product/category page. Google Ads now requires a credit card just to sign up, so you
**document the campaign as a written plan** instead of a live draft. Explain what **CPC** means and why you
send ads to a specific product page (not the homepage). *(Optional live route: if you can access **Meta /
Facebook Ads Manager** or an existing Google Ads account, build it there as a real draft and screenshot it.)*

**Q15. Analytics (GA4).** Include a screenshot of **GA4 Realtime** with an active user. Where is the GA4
tracking code placed on your site?

**Q16. Social media audit.** Present your **social media audit**. How did you calculate the **engagement
rate**, and what are your 3 recommendations for your own store?

---

### How this is used
- **Printed lab report (submitted):** answer all 16 questions — each with the code, a screenshot, and a
  short explanation. Follow the **Lab Report Format** guide for layout, and get it signed off by your
  instructor before printing.
- **Viva (external + internal):** the examiner reads your report and asks you to **explain your own code**
  — e.g. "explain the query in Q4" or "why a transaction in Q8". If you wrote it yourself, you can explain
  it; a copied report falls apart here.

*(Instructor's version with model answers and marking guidance: [IT247_Lab_Work_and_Viva.md](IT247_Lab_Work_and_Viva.md).)*
