# IT 247 Lab Workbook — E-Commerce and Internet Marketing
### Sessions 1–6 · Hands-on Student Guide · PHP + MySQL

| | |
|---|---|
| **Student Name** | ________________________ |
| **Roll Number** | ________________________ |
| **Section / Group** | ________________________ |
| **Instructor** | ________________________ |
| **Academic Year** | 2082 / 2083 (BS) |

---

## How to Use This Workbook
This is your step-by-step guide for all 6 lab sessions. Read each step fully before doing it, note your
observations, and complete the checklist before asking your instructor to sign off.

- **Steps** — numbered instructions. Do them in order.
- **Expected Output** — how you know a step worked.
- **Notes** — write your own observations.
- **Checklist** — everything you must finish before submitting the session.

You will build **one PHP + MySQL store, incrementally, across all 6 sessions**. Pick a store theme in
Session 1 (electronics, books, clothing, handicrafts…) and keep it all semester.

### Lab Overview
| Session | Title | What You Build / Learn |
|---|---|---|
| 1 | Setup, Database & Dynamic Storefront | XAMPP + a product page that loads from MySQL |
| 2 | Cart, Checkout & Payment | Session cart + checkout that saves an order + sandbox payment |
| 3 | Security & Deployment | A secure store, live on a public HTTPS URL |
| 4 | Google Search Tools | Keyword research report |
| 5 | Google Ads & Analytics | Draft ad campaign + GA4 on your live store |
| 6 | Social Media Analysis | A social media audit report |

### The Demo Store: LearningMart
Your instructor has a working PHP + MySQL demo called **LearningMart** (product grid, cart, checkout,
backed by a real database). Use it as your visual + structural reference — you are **not** copying it, you
are building your own themed store (you may start from its skeleton and extend it). Any time you're unsure,
ask: *does mine look and work like LearningMart?*

> **Golden rule for this course:** your pages must run through **`http://localhost/...`** (Apache), not by
> double-clicking a file. PHP only runs on a server. And your **MySQL** service must be started in XAMPP,
> or every page will say "Connection failed".

---

# Phase 1 — Build

## Session 1 — Setup, Database & Dynamic Storefront
**Phase:** Build · **Duration:** ~2.5 hours · **Tools:** XAMPP, VS Code, phpMyAdmin, browser

By the end you'll have a product listing page that looks like a real shop — and the products come from a
**real database**, not hardcoded text. Open LearningMart on the projector as your target.

### What You Will Learn
- Install and run XAMPP (Apache + PHP + MySQL)
- Create an e-commerce database and tables in phpMyAdmin
- Connect PHP to MySQL with **PDO**
- Show products on a page using a PHP loop over database rows

### Steps
1. **Install XAMPP.** Download from apachefriends.org. Open the XAMPP Control Panel and **Start Apache
   and MySQL** (both should turn green). Visit `http://localhost` and `http://localhost/phpmyadmin` —
   both must load.
2. **Create your project.** Inside XAMPP's `htdocs/` folder, create a folder `mystore`. Open it in VS
   Code. Create `index.php`. Visit `http://localhost/mystore/index.php` to confirm it runs.
3. **Test PHP runs.** In `index.php`, output your store name and the time:
   `<h1>My Store</h1><p><?php echo date('h:i:s A'); ?></p>`. Refresh — the time changes. Right-click →
   View Source: you see the time, **not** the PHP. That's "server-side".
4. **Create the database.** Open phpMyAdmin → New → create a database called `demo`. Go to the **SQL**
   tab and run the table-creation script (`categories`, `products`, `users`, `orders`, `order_items` —
   use your instructor's `schema.sql`). Then insert at least **5 categories and 15 products** for your
   theme.
5. **Connect with PDO.** Create `base/connect.php`:
   `$pdo = new PDO("mysql:host=localhost;dbname=demo;charset=utf8mb4", "root", "");` and set
   `PDO::ATTR_ERRMODE` to exceptions. (Your XAMPP MySQL user is `root` with an empty password.)
6. **Show products from the DB.** In `index.php`, `include 'base/connect.php';`, then
   `$products = $pdo->query("SELECT * FROM products")->fetchAll();` and loop them into Bootstrap cards
   (image, name, price, category). Escape output with `htmlspecialchars()`.
7. **Compare with LearningMart.** Note one thing you'd improve.

> **EXPECTED OUTPUT — Session 1**
> ✓ Apache + MySQL run (green) in XAMPP
> ✓ `http://localhost/mystore/` loads your page
> ✓ The product grid shows **≥15 products loaded from MySQL**
> ✓ View Source shows HTML only — no PHP
> ✓ Each card shows name, price, and category

> **BEFORE YOU SUBMIT — tick each item**
> ☐ XAMPP Apache + MySQL started
> ☐ Database `demo` created with all 5 tables
> ☐ ≥5 categories and ≥15 products inserted
> ☐ `connect.php` connects with PDO (no errors)
> ☐ Products display from the database in a grid
> ☐ Page shown to instructor via `http://localhost/...`

**SESSION 1 NOTES — what I observed / want to improve:**
`________________________________________________________________`

**Glossary:** *PHP* (server-side language that runs before the page reaches the browser) · *MySQL*
(the database that stores your products/users/orders) · *phpMyAdmin* (a web tool to manage MySQL) ·
*PDO* (PHP's modern, secure way to talk to the database) · *XAMPP* (bundles Apache + PHP + MySQL on your
laptop) · *localhost* (your own computer acting as a web server).

---

## Session 2 — Cart, Checkout & Payment
**Phase:** Build · **Duration:** ~2.5 hours · **Tools:** PHP sessions, MySQL, eSewa/Khalti sandbox

You'll add a shopping cart, a checkout that saves a real order to the database, and a **sandbox** payment.
You will only ever use **test** credentials — no real money.

### What You Will Learn
- Store a cart in the PHP **session**
- Save an order into `orders` + `order_items` using a **transaction**
- Connect a payment sandbox and verify the result on the **server**

### Steps
1. **Understand the flow.** Draw: *Add to Cart → Cart page → Checkout form → Payment gateway → server
   verifies → Order saved*. Unlike a static site, here the **server** owns the cart and the order.
2. **Add to cart.** On the product page, an "Add to Cart" button stores `product_id → quantity` in
   `$_SESSION['cart']`. Show a cart count in the header.
3. **Cart page.** Build `cart.php` listing items (name, unit price, quantity, line total) with a grand
   total. Support update-quantity and remove. Don't allow more than the product's `stock`.
4. **Checkout.** Require login. Build a form (name, email, address). On submit, in a **PDO transaction**:
   insert into `orders`, insert each line into `order_items` (save `price_at_purchase`), reduce stock,
   clear the cart. Show a confirmation with the order number.
5. **Payment sandbox.** Use **eSewa ePay test** (test merchant code `EPAYTEST`) or **Khalti sandbox**
   (test keys from their docs). Send the order total to the gateway's test endpoint with success/failure
   return URLs.
6. **Verify server-side.** On success, verify the transaction with the gateway (PHP + your **secret**
   test key), then mark the order `paid` and store the transaction id. On failure, leave it unpaid.
7. **Keep keys secret.** Put keys in `config.php` (don't commit it).

> **EXPECTED OUTPUT — Session 2**
> ✓ Add-to-cart updates the header count; cart page totals are correct
> ✓ Checkout creates an `orders` + `order_items` record (check phpMyAdmin)
> ✓ Stock decreases; the cart clears after ordering
> ✓ A **sandbox** payment completes and the order is marked paid after server-side verification

> **BEFORE YOU SUBMIT — tick each item**
> ☐ Cart works (add / update / remove) and respects stock
> ☐ Checkout saves an order + items in a transaction
> ☐ Sandbox payment completes (test credentials only)
> ☐ Payment verified server-side before marking paid
> ☐ Order row visible in phpMyAdmin

**SESSION 2 NOTES — what happens when the payment returns to your site?**
`________________________________________________________________`

**Glossary:** *Session* (server memory tied to one user, via a cookie session id) · *Transaction* (a
group of DB writes that all succeed or all roll back) · *Sandbox / Test Mode* (fake payments, no real
money) · *Server-side verification* (asking the gateway "did this really get paid?" from PHP) · *Secret
key* (never put it in HTML/JS — it stays in server PHP).

---

## Session 3 — Security & Deployment
**Phase:** Build · **Duration:** ~2.5 hours · **Tools:** XAMPP, InfinityFree, phpMyAdmin, DevTools

You'll harden your store against common attacks and put it **live on the internet** with HTTPS, on a free
PHP host. Share your live URL with your instructor — you'll need it in Sessions 4 and 5.

### What You Will Learn
- Prevent **SQL injection** (prepared statements) and **XSS** (output escaping)
- Deploy a PHP + MySQL app to a free public host
- Understand why database credentials change between your laptop and the live host

### Steps
1. **SQL injection.** Confirm every query uses **prepared statements** (bound parameters), never string
   concatenation. Try `' OR '1'='1` in your login/search and confirm it fails. Write down why.
2. **XSS.** Wrap every user-provided value you print with `htmlspecialchars()` (the demo has a helper
   `e()`). Save `<script>alert('x')</script>` as a product name — it must display as text, not run.
3. **Passwords & sessions.** Confirm passwords are stored with `password_hash()` and checked with
   `password_verify()`. Regenerate the session id on login.
4. **Create the host.** Sign up at **infinityfree.com** → create a site (you get a free subdomain +
   free SSL). In the control panel, create a **MySQL database** and note its host, name, user, password.
5. **Upload your files.** Use the File Manager or FTP to copy your PHP files into the host's `htdocs`.
   Open the host's phpMyAdmin and **import** your `schema.sql` (+ your product data).
6. **Fix the database credentials.** ⚠️ On XAMPP it's `host=localhost, user=root, password=""`. On
   InfinityFree it's a **remote host** like `sqlXXX.infinityfree.com` with a generated user/password.
   Edit `connect.php` (or `config.php`) to the host's values — otherwise the live site says "Connection
   failed".
7. **Verify HTTPS & test live.** Open your InfinityFree URL, check the padlock, and run browse → cart →
   checkout → sandbox payment on the **live** site. Share the URL with your instructor.

> **EXPECTED OUTPUT — Session 3**
> ✓ Injection attempt (`' OR '1'='1`) fails; `<script>` shows as text
> ✓ Store is live at an InfinityFree HTTPS URL (padlock visible)
> ✓ Products, cart, and checkout work on the live URL
> ✓ Live site connects to the host's MySQL (creds changed from localhost)

> **BEFORE YOU SUBMIT — tick each item**
> ☐ All queries use prepared statements
> ☐ All output escaped with `htmlspecialchars()`
> ☐ Store deployed and live on an InfinityFree HTTPS URL
> ☐ Database imported on the host; creds updated for production
> ☐ Full flow works on the live site
> ☐ Live URL given to instructor

**SESSION 3 NOTES — your live URL + any deployment issues:**
`________________________________________________________________`

**Glossary:** *SQL Injection* (attacker sneaks SQL through an input; stopped by prepared statements) ·
*XSS* (attacker sneaks script through an input; stopped by output escaping) · *HTTPS/SSL* (encrypts data
between browser and server; the padlock) · *Deployment* (putting your site on a public server) ·
*InfinityFree* (a free host that runs PHP + MySQL, unlike static hosts).

---

# Phase 2 — Market

## Session 4 — Google Search Tools
**Phase:** Market · **Duration:** ~2 hours · **Tools:** Google Search Console, Keyword Planner

Now your store is live, help people find it. Register it with Google and research keywords.

### Steps
1. **Add property.** search.google.com/search-console → Add Property → URL prefix → paste your
   InfinityFree URL.
2. **Verify.** Copy the HTML **meta** verification tag. Paste it inside the `<head>` in your
   **`layout/header.php`** (so it's on every page), save, re-upload to the host, then click Verify.
3. **URL Inspection.** Paste your URL → Request Indexing. (It won't rank instantly — that's normal.)
4. **Keyword Planner.** ads.google.com → if no account, create one in **Expert mode → "Create an account
   without a campaign"** (skips billing) → Tools → Keyword Planner → Discover new keywords.
5. **Research.** Type 3 phrases about your store (e.g. for a tech store: "buy wireless earbuds Nepal",
   "smart watch Kathmandu"). Read volume & competition.
6. **Build the table.** Pick 10 relevant keywords; record keyword, monthly searches, competition
   (Low/Med/High), and a one-sentence reason for each.

> **EXPECTED OUTPUT — Session 4**
> ✓ Property verified (green tick)
> ✓ URL submitted for indexing
> ✓ 10 keywords with volume + competition + justification

> **BEFORE YOU SUBMIT** ☐ Property verified ☐ URL Inspection used ☐ 10 keywords with data ☐ justification for each

**Glossary:** *Keyword* (what a user types into Google) · *Search Volume* (avg monthly searches) ·
*Competition* (how many advertisers bid on it) · *Indexing* (Google storing your page) · *SEO* (getting
found without paying).

---

## Session 5 — Google Ads & Analytics
**Phase:** Market · **Duration:** ~2.5 hours · **Tools:** Google Ads, Google Analytics 4

Create a real ad campaign (saved as **draft** — no spending) and install GA4 on your live store.

### Steps
1. **New campaign.** ads.google.com → Expert mode → New Campaign. Goal: **Sales**. Type: **Search**. URL:
   your InfinityFree store.
2. **Targeting/budget.** Location: Nepal/Kathmandu. Language: English. Daily budget Rs. 100 — you'll save
   as **draft**, so nothing is charged.
3. **Ad group + keywords.** Name it after your main category. Add 5 keywords from Session 4.
4. **Ad copy.** 3 headlines (store name / main product / USP e.g. "Free delivery in Kathmandu") + 2
   descriptions. Preview it.
5. **Save as DRAFT.** Do **not** publish. Confirm it shows "Draft".
6. **GA4.** analytics.google.com → create a Web property → copy the Measurement ID `G-XXXXXXXXXX`.
7. **Install GA4.** Paste the gtag `<script>` into the `<head>` in **`layout/header.php`** (every page),
   **replace `G-XXXXXXXXXX` with your real ID**, save, re-upload. Open your store; GA4 **Realtime** should
   show 1 active user within ~30s. Screenshot it.

> **EXPECTED OUTPUT — Session 5**
> ✓ Ads campaign saved as **Draft** (1 ad group, 5 keywords, 3+2 ad copy)
> ✓ GA4 Measurement ID obtained and added to `header.php`
> ✓ GA4 Realtime shows an active user when you open the store

> **BEFORE YOU SUBMIT** ☐ Campaign is Draft (not published) ☐ 5 keywords added ☐ ad copy written ☐ GA4 in `header.php` with real ID ☐ Realtime screenshot saved

**Glossary:** *Google Ads* (paid search ads) · *Ad Group* (ads sharing keywords) · *CPC* (cost per click)
· *Quality Score* (ad/keyword/page relevance, 1–10) · *GA4* (web analytics) · *Measurement ID*
(`G-XXXXXXXXXX`, links GA4 to your site) · *Realtime* (who's on your site right now).

---

## Session 6 — Social Media Analysis
**Phase:** Market · **Duration:** ~2 hours · **Tools:** Facebook Business Suite, Instagram Insights, Buffer

Analyse a real Nepali business's social media and write a structured audit. This is part of your final
assessment.

### Steps
1. **List 3 Nepali e-commerce businesses** and the platforms they use. You'll pick one to audit.
2. **Facebook Business Suite** (business.facebook.com) — explore Insights (reach, page views, post
   performance). No page? Your instructor will demo.
3. **Instagram Insights** — on a Creator/Business account, view reach, impressions, follower activity.
4. **Buffer** (buffer.com free) — connect an account; explore Publish (scheduling) and Analyze. Screenshot.
5. **Choose a competitor** with an active page (e.g. Daraz Nepal, Sastodeal, a local shop).
6. **Analyse** — posting frequency, content types (photos/videos/reels/stories), avg likes/comments,
   replies, promotions.
7. **Engagement rate** — pick 5 recent posts: (likes + comments) ÷ followers × 100; average them.
8. **Audit report** — competitor + platforms, frequency, content, engagement estimate, 2 strengths,
   2 weaknesses, 3 recommendations for **your** store.

> **EXPECTED OUTPUT — Session 6**
> ✓ Explored Business Suite/Insights + Buffer (screenshot)
> ✓ One competitor analysed on all points
> ✓ Engagement rate from ≥5 posts
> ✓ 1-page audit with 3 recommendations

> **BEFORE YOU SUBMIT** ☐ Competitor + platforms ☐ frequency/content/engagement recorded ☐ engagement rate from 5+ posts ☐ Buffer screenshot ☐ 2 strengths + 2 weaknesses + 3 recommendations

**Glossary:** *Reach* (unique people who saw a post) · *Impressions* (total views, repeats included) ·
*Engagement* (likes + comments + shares) · *Engagement Rate* ((likes+comments)÷followers×100) · *Social
Media Audit* (structured review of a brand's social activity).

---

## Complete Glossary (all sessions)
**API** — how two systems talk (payment gateways use APIs). ·
**CPC** — cost per click in ads. ·
**CTR** — clicks ÷ impressions × 100. ·
**Engagement Rate** — social interactions ÷ followers × 100. ·
**GA4** — Google Analytics 4, web tracking. ·
**HTTPS/SSL** — encrypted browser↔server connection (the padlock). ·
**InfinityFree** — free PHP + MySQL host (used to deploy). ·
**Indexing** — Google adding your page to its database. ·
**Keyword** — a phrase users search. ·
**PDO** — PHP's secure database interface (prepared statements). ·
**password_hash()** — one-way password hashing in PHP. ·
**phpMyAdmin** — web UI to manage MySQL. ·
**Prepared Statement** — parameterised query; blocks SQL injection. ·
**Sandbox / Test Mode** — payment testing with no real money. ·
**Session** — per-user server memory (cart, login). ·
**SQL Injection** — attack via unsafe queries; stopped by prepared statements. ·
**Transaction** — all-or-nothing group of DB writes. ·
**XAMPP** — Apache + PHP + MySQL for local development. ·
**XSS** — script-injection attack; stopped by output escaping (`htmlspecialchars()`).
