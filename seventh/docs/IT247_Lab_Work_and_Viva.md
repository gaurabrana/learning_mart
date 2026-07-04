# IT 247 — Laboratory Work Record & Viva Question Set
### E-Commerce and Internet Marketing · BIM / BITM 7th Semester · PHP + MySQL

This is the official list of **lab works** for IT 247. Each student completes every lab work, records it
in a **lab report/record**, and gets it signed off by the internal instructor. At the end of the semester,
an **external examiner** reviews the lab record, watches a **live demo of the deployed store**, and
conducts a **viva** — the viva questions for each lab are included here (with short model answers for the
examiner/instructor).

- **Reference project:** the **LearningMart** demo (`seventh/demo/`). Students build **their own themed
  store**, using LearningMart as a working reference.
- **Stack:** PHP + MySQL (PDO), Bootstrap 5 — developed on **XAMPP**, deployed on **InfinityFree**.
- **These lab works map onto the 6 teaching sessions** in the Lab Guide / Workbook (mapping below).

---

## How the lab record is kept and assessed

**Each lab-work entry in the student's report must contain:**
1. **Lab number & title**, date, student name/roll.
2. **Objective** (1–2 lines, student's own words).
3. **The key code** they wrote for that lab (not the whole project — just what's new).
4. **A screenshot of the working output** on their machine (and, from Lab 8, the live URL).
5. **Answers to that lab's viva questions.**

**Assessment (printed lab report + viva — adjust to your college's scheme):**
| Part | Weight | What it checks |
|---|---|---|
| Printed lab report (all 16 questions: code + screenshot + explanation) | 50% | Every lab documented with correct code and working screenshots |
| Viva voce (external + internal) on the report | 40% | Student can **explain their own code** — the anti-copying check |
| Regularity / attendance / sign-offs | 10% | Work done across the semester, not the night before |

> **No live demo:** students submit a **printed A4 lab report** documenting their build; the examiner
> assesses the report and questions the student on it. Because a document can be copied, the viva is the
> real test — a student who built it can explain any part; a copied report cannot. See the
> **Lab Report Format** guide for the required document structure.

> **Zero-tolerance rule (state it up front):** any database query that concatenates user input into SQL
> (instead of a **prepared statement**) fails that lab work — regardless of whether it "works."

---

## List of Lab Works (11) → teaching sessions

| Lab | Title | Teaching session | Syllabus unit |
|-----|-------|------------------|----------------|
| 1 | Environment setup & connecting PHP to MySQL | Session 1 | Unit 3 (infrastructure) |
| 2 | Database design & creating the tables | Session 1 | Unit 4 (systematic approach) |
| 3 | Product catalog, detail, category & search (from DB) | Session 1 | Unit 4 (site tools) |
| 4 | User registration, login & sessions | Session 2 | Unit 5 (security) |
| 5 | Shopping cart (session-based) | Session 2 | Unit 1/4 (features) |
| 6 | Checkout, orders & sandbox payment | Session 2 | Unit 2 / Unit 5 (payment) |
| 7 | Security hardening | Session 3 | Unit 5 (threats & solutions) |
| 8 | Deployment to a live public host | Session 3 | Unit 4 |
| 9 | SEO: Search Console & Keyword research (Google Trends) | Session 4 | Unit 6 (SEO) |
| 10 | Ad campaign plan & Analytics (GA4) | Session 5 | Unit 6 (PPC, analytics) |
| 11 | Social media analysis | Session 6 | Unit 6 (social media marketing) |

---

# Phase 1 — Build (PHP + MySQL)

## Lab Work 1 — Environment Setup & Connecting PHP to MySQL
**Objective:** Set up XAMPP and prove PHP can run and talk to MySQL.

**Tasks (implement these):**
1. Install XAMPP; start Apache + MySQL; confirm `http://localhost` and `/phpmyadmin` load.
2. Create a project folder inside `htdocs/` and an `index.php` that prints your store name and the
   current server time (proves PHP runs server-side).
3. Create `base/connect.php` with a **PDO** connection to a MySQL database.
4. Print a one-line "Connected to database ✅" message when the connection succeeds.

**Expected output:** Your page loads via `http://localhost/...`, shows the live time, and confirms a
successful database connection.

**Record in report:** `index.php` + `connect.php` code, and a screenshot of the running page.

**Viva questions (model answers):**
- *What does "server-side" mean?* → PHP runs on the server and only sends finished HTML; the browser
  never sees the PHP.
- *Trace what happens when you open a PHP page.* → Browser → Apache runs PHP → (PHP queries MySQL) →
  PHP outputs HTML → browser renders it.
- *Why open pages via `http://localhost` and not by double-clicking the file?* → PHP only executes
  through the web server; `file://` shows raw code and can't run PHP.

---

## Lab Work 2 — Database Design & Creating the Tables
**Objective:** Design and create the relational database the whole store runs on.

**Tasks:**
1. Draw an **ER diagram** with `categories`, `products`, `users`, `orders`, `order_items` (show keys and
   relationships).
2. In phpMyAdmin, create the database and all tables with correct types, primary keys, and foreign keys.
3. Insert **at least 5 categories and 15 products** for your theme, each with a realistic price and stock.
4. Write one `SELECT` that joins `products` to their category name.

**Expected output:** All tables populated in phpMyAdmin; the join query returns products with category
names.

**Record in report:** ER diagram, the `CREATE TABLE` script, and a screenshot of the products table + the
join query result.

**Viva questions:**
- *What is a foreign key?* → A column that references a primary key in another table, enforcing a valid
  relationship (e.g. `products.category_id` → `categories.id`).
- *Why store `price_at_purchase` in `order_items` instead of always reading `products.price`?* → Prices
  change; an order must remember what the customer actually paid.
- *Why is `order_items` a separate table?* → An order has many products and a product appears in many
  orders — a many-to-many relationship needs a junction table.

---

## Lab Work 3 — Product Catalog, Detail, Category & Search (from the DB)
**Objective:** Show real products from the database and let users browse, view, and search.

**Tasks:**
1. Render a **product grid** on the home/products page by querying the DB and looping the rows.
2. Build a **single-product** page (`product_detail.php?id=`) using a **prepared statement**.
3. Add **category browsing** (`product.php?cat=`) and a **search box** (`?q=`) — both using prepared
   statements (no string concatenation).
4. Handle the "no results / bad id" case gracefully.

**Expected output:** Products load live from MySQL; category filter and search return matching products; a
detail page opens for any product.

**Record in report:** the listing + detail + search code, and screenshots of a category view, a search
result, and a product detail page.

**Viva questions:**
- *What is a prepared statement and which attack does it stop?* → A parameterised query where input is
  bound separately from SQL; it stops **SQL injection**.
- *Show the line that passes the search term safely.* → e.g. `$stmt->execute(['%'.$q.'%'])` with `LIKE ?`.
- *What happens if someone visits `product_detail.php?id=abc`?* → It's cast to int / not found, so you show
  a friendly "product not found", not an error.

---

## Lab Work 4 — User Registration, Login & Sessions
**Objective:** Let customers register and log in securely.

**Tasks:**
1. Build a **registration** form; validate inputs server-side; reject duplicate emails.
2. Store the password with **`password_hash()`** (never plain text).
3. Build **login** using `password_verify()`; on success store the user in `$_SESSION`.
4. Build **logout** (destroy session). Show the user's name + Logout in the header when logged in.

**Expected output:** Register → log in → see your name in the header → log out. In phpMyAdmin the stored
password is a **hash**, not plain text.

**Record in report:** register/login/logout code + screenshots of the flow + a phpMyAdmin screenshot
proving the password is hashed.

**Viva questions:**
- *Why hash passwords instead of storing them?* → So a database leak doesn't expose real passwords;
  `password_hash()` also adds a random salt automatically.
- *What is a session and how does the server remember you?* → Server-side per-user storage keyed by a
  session id kept in a cookie.
- *What is `password_verify()` doing?* → Re-hashing the entered password with the stored salt and
  comparing — without ever un-hashing.

---

## Lab Work 5 — Shopping Cart (Session-Based)
**Objective:** Add-to-cart, update quantity, remove, and show totals — using the session.

**Tasks:**
1. Store the cart in `$_SESSION['cart']` as `product_id → quantity`.
2. Wire "Add to Cart" on the product pages; show a cart count in the header.
3. Build `cart.php`: list items with unit price, quantity, line total, and a grand total.
4. Support **update quantity** and **remove**; don't allow more than available stock.

**Expected output:** Adding, updating, and removing items recalculates totals and updates the header
badge; the cart survives page navigation.

**Record in report:** cart code + a screenshot of a cart with several items and a correct total.

**Viva questions:**
- *Why keep the cart in the session and not the database here?* → Simpler for a guest; downside is it's
  lost on logout/expiry and doesn't move between devices.
- *Is the total calculated in the browser or on the server? Why does it matter?* → On the server — the
  browser can be tampered with, so prices must never be trusted from the client.
- *How do you stop a user ordering more than you have?* → Cap the quantity at the product's `stock`.

---

## Lab Work 6 — Checkout, Orders & Sandbox Payment
**Objective:** Turn a cart into a saved order and take a **test** payment.

**Tasks:**
1. Require login to check out.
2. On submit, inside a **transaction**: create the `orders` row, insert each `order_items` line (store
   `price_at_purchase`), reduce stock, clear the cart.
3. Integrate a **payment sandbox** — **eSewa ePay test** (`EPAYTEST`) or **Khalti sandbox**.
4. On the gateway's callback, **verify the payment server-side** (PHP + secret test key) before marking
   the order `paid`.

**Expected output:** A completed checkout creates an order in phpMyAdmin with correct items/total; stock
drops; a sandbox payment completes and the order is marked paid after verification.

**Record in report:** checkout + payment code, a screenshot of the sandbox payment, and the `orders` /
`order_items` rows in phpMyAdmin.

**Viva questions:**
- *Why wrap order creation + stock update in a transaction?* → So a mid-way failure rolls everything back
  — you never save an order without reducing stock (or vice-versa).
- *Why verify the payment on the server instead of trusting the redirect?* → The browser redirect can be
  faked; only the gateway's verification API confirms real payment.
- *Why does the secret key stay in PHP, never in HTML/JS?* → Anyone can read client-side code; a leaked
  secret key lets others charge/refund on your account.

---

## Lab Work 7 — Security Hardening
**Objective:** Defend the store against the common attacks from Unit 5.

**Tasks:**
1. **SQL injection:** confirm every query uses prepared statements; try `' OR '1'='1` on login/search and
   show it fails.
2. **XSS:** escape all user output with `htmlspecialchars()`; save `<script>alert(1)</script>` as a
   product name and show it renders as text.
3. Confirm passwords are hashed and the session id is regenerated on login.
4. Write a short **security checklist** mapping each fix to the threat it addresses.

**Expected output:** Documented proof that injection and XSS attempts fail.

**Record in report:** before/after evidence of an attempted attack + the security checklist.

**Viva questions:**
- *Explain SQL injection and your defence.* → Attacker injects SQL via input; prepared statements bind
  input as data, so it can't change the query.
- *Explain XSS and your defence.* → Attacker injects script via input; escaping output with
  `htmlspecialchars()` makes it display as text, not run.
- *What's the difference between hashing and encryption?* → Hashing is one-way (can't be reversed);
  encryption is two-way. Passwords are hashed.

---

## Lab Work 8 — Deployment to a Live Public Host
**Objective:** Put the PHP + MySQL store online with HTTPS.

**Tasks:**
1. Create an **InfinityFree** account and site (free subdomain + free SSL).
2. Upload the PHP files; create a MySQL database on the host; **import your schema** via the host's
   phpMyAdmin.
3. **Change the DB credentials** in `connect.php` from `localhost/root` to the host's MySQL host/user/pass.
4. Verify the padlock (HTTPS) and run the full flow (browse → cart → checkout → sandbox pay) live.

**Expected output:** The store runs at a public `https://…` URL with the database working.

**Record in report:** the live URL, a screenshot of the padlock, and a note on what DB credentials changed.

**Viva questions:**
- *Why can't this run on Netlify?* → Netlify only serves static files; it can't run PHP or host MySQL.
- *Why do the database credentials differ on the live host?* → The host's MySQL is a separate server with
  its own hostname/user/password — not `localhost/root`.
- *What does HTTPS protect, and what does it not?* → It encrypts data in transit (so it can't be read on
  the network); it does not secure bad server code or a weak database.

---

# Phase 2 — Market (Digital Marketing Tools)

## Lab Work 9 — SEO: Search Console & Keyword research (Google Trends)
**Objective:** Register the live store with Google and research keywords.

**Tasks:**
1. Add the store as a property in **Google Search Console**; verify with the **HTML-file method** — upload
   the `google<...>.html` file to the **site root** (`htdocs/`). *(File method, not the meta tag — a live
   HTTPS URL is required for Google to fetch it.)*
2. Submit `sitemap.php`, then use **URL Inspection** to request indexing of a product page.
3. Research keywords with **Google Trends** (`trends.google.com`, region = Nepal) — 3–4 seed terms, read
   the **Top** and **Rising** queries. *(Why Trends, not Keyword Planner: Google now forces a credit card
   at Ads signup, so Trends is the no-cost default. See `MARKETING_GUIDE.md §3`.)*
4. Produce a **10-keyword report** — columns **keyword, demand, intent, where used on the site** — and
   put at least one keyword into a product's `<title>`/`<meta description>`. Model: `MARKETING_SAMPLES.md`.

**Expected output:** A verified Search Console property and a 10-keyword report wired into the site.

**Record in report:** screenshot of the verified property + the keyword table + the edited product's
View-Source showing the keyword in the title/description.

**Viva questions:**
- *Why doesn't a new store appear on Google automatically?* → Google's crawler finds sites via links; a
  brand-new unlinked site may never be found until you tell Search Console.
- *How did you read "demand" in Google Trends?* → The length of the Search-interest bar (relative interest,
  not an exact count) — longer bar = more searches.
- *Transactional vs commercial intent?* → *price / in nepal / 20000mah* = ready to buy (transactional,
  target these first); *best / review* = still comparing (commercial).
- *Why verify with a file at the site root?* → Google fetches it over your live HTTPS URL to prove you
  control the domain; a local/insecure site can't be verified.

---

## Lab Work 10 — Ad campaign plan & Analytics (GA4)
**Objective:** Design a paid-search campaign and track live visitors.

> **Why a plan, not a live draft:** Google Ads now requires a **credit card at signup** (even "set up an
> account only"), so students document the campaign as a **written plan** instead. Same learning outcome,
> no cost. *(Optional live route: build a real draft in **Meta / Facebook Ads Manager**, or in Google Ads
> if the student already has a billed account, and screenshot it.)*

**Tasks:**
1. Write a **Search campaign plan**: goal **Sales**, one ad group, **5 keywords** (from Lab 9, prefer
   transactional), **3 headlines + 2 descriptions**.
2. Give the **landing URL** = a real **product/category page** on the live store, with **UTM tags**, e.g.
   `…/product.php?cat=3&utm_source=google&utm_medium=cpc&utm_campaign=audio`.
3. Create a **GA4** property; set the real Measurement ID in **`config.php`** (`$GA4_ID`) — the snippet is
   already rendered site-wide from `layout/header.php`. Confirm a visit appears in **Realtime**.
4. **Test the loop (free & real):** open your own UTM landing URL, then show GA4 **Realtime → by source /
   medium** attributing you to `google / cpc`. This proves the ad→analytics integration without spending.

**Expected output:** A written campaign plan (keywords + ad copy + UTM landing URL) and GA4 Realtime
showing an active user (bonus: attributed to your UTM source).

**Record in report:** the campaign-plan table, the UTM landing URL, and the GA4 Realtime screenshot.

**Viva questions:**
- *What is CPC?* → Cost Per Click — you pay only when someone clicks your ad, not for views.
- *How does the ad auction decide placement and cost?* → When someone searches your keyword, Google runs an
  instant auction; position = **Ad Rank = bid × Quality Score** (relevance of ad + landing page). A more
  relevant ad can outrank a higher bidder, and you pay only enough to beat the advertiser below you — which
  is why keywords, ad copy, and landing page all matter.
- *Why send ads to a product page, not the homepage?* → The visitor searched for a specific product;
  landing them on it (not a generic page) means fewer clicks lost → higher conversion (and higher Quality
  Score).
- *What do UTM tags do?* → They tag the URL so GA4 can attribute the visit to the campaign/source/medium —
  that's how you know which channel actually sells.
- *What does GA4 track once installed?* → Page views, device, country, source/medium, and events like the
  `purchase` conversion for every visitor.

---

## Lab Work 11 — Social Media Analysis
**Objective:** Analyse a real business's social presence and produce an audit.

**Tasks:**
1. Choose a real Nepali e-commerce business with an active page.
2. Record posting frequency, content types, avg likes/comments, replies, promotions.
3. Calculate an **engagement rate** over 5 posts: `(likes + comments) ÷ followers × 100`.
4. Explore **Buffer** (free) for scheduling/analytics.
5. Write a **1-page audit**: competitor, platforms, engagement estimate, 2 strengths, 2 weaknesses, 3
   recommendations for your own store.

**Expected output:** A 1-page structured social media audit with an engagement-rate calculation.

**Record in report:** the audit + a Buffer dashboard screenshot.

**Viva questions:**
- *Difference between reach and impressions?* → Reach = unique people; impressions = total views
  (repeats counted).
- *How is engagement rate calculated?* → (likes + comments) ÷ followers × 100.
- *Why does social media matter for e-commerce?* → Direct traffic, brand awareness, and remarketing to
  people who already engaged.

---

## External Viva & Practical Exam — guidance

**How the external viva typically runs (adapt to your college):**
1. **Report check** — the examiner reads the printed A4 lab report and confirms all questions are answered
   with code + screenshots + explanation, signed off by the internal instructor.
2. **Viva Q&A** — the examiner points to answers in the report and asks the student to **explain their own
   code** (from the per-lab questions above, plus the cross-cutting ones below). This is where a copied
   report is exposed.

**What the report should contain as evidence (checklist):**
- ☐ A themed store with ≥15 products in ≥5 categories, loaded from MySQL
- ☐ Working register/login (hashed passwords) and a session cart
- ☐ Checkout that saves an order in a transaction + a verified sandbox payment
- ☐ Prepared statements everywhere; output escaped
- ☐ Store live on a public HTTPS URL
- ☐ 10-keyword SEO report (Google Trends), GA4 Realtime, an ad campaign plan (with UTM landing URL), and a social media audit

**Cross-cutting viva questions (whole course):**
- *Explain the request flow of your store from browser to database and back.*
- *Which part of your project is the View, and which is the Model/database logic?*
- *Name three security measures in your code and the threat each one stops.*
- *Why did you choose your product category, and which keywords did you target for it?*
- *What is the difference between e-commerce and e-business?* (Unit 1 link)
- *Explain B2C vs B2B with an example.* (Unit 2 link)

**Suggested viva marking (out of the viva weight):** clarity of explanation of their **own** code (40%),
security understanding (20%), marketing tools understanding (20%), e-commerce concepts (20%).

---

> **Note on the other documents:** this is the **assessment companion** to the
> [Teaching Plan](IT247_Teaching_Plan.md) (instructor playbook), the
> [Student Workbook](IT247_Student_Workbook.md) (build steps), and the
> [Survival Guide](IT247_Student_Survival_Guide.md) (setup/troubleshooting). The lab-work numbers here map
> to the 6 teaching sessions in the table above.
