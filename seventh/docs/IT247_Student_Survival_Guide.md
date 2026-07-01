# IT 247 Student Survival Guide — E-Commerce and Internet Marketing
### Everything you need to get through Sessions 1–6 without losing your mind · PHP + MySQL edition

| | |
|---|---|
| **What's inside** | Setup, concept explanations, troubleshooting, code snippets, mindset tips |
| **Who it's for** | Every IT 247 student — whether you've coded before or not |
| **When to use it** | Keep it open during every lab. Read it before if you can. |

---

## 1. Welcome — What This Course Is Really About
Before you panic about PHP, MySQL, payments, and Google Ads all at once — breathe. This guide makes it
manageable.

> **REMEMBER.** You do not need to be a programmer to pass. You need to be curious, willing to try, and
> okay with mistakes. Mistakes are how coding works — even senior developers break things constantly.

Over 6 sessions you build a complete **PHP + MySQL** online store, then market it with real tools:

| Session | What you do | End result |
|---|---|---|
| 1 | Set up XAMPP, create a database, show products with PHP | A storefront powered by a real database |
| 2 | Add a cart + checkout + sandbox payment | Customers can (pretend to) buy things |
| 3 | Secure and deploy your store | Real people can visit it online (HTTPS) |
| 4 | Research keywords, register with Google | Google knows your store exists |
| 5 | Build an ads campaign + install analytics | You can track visitors and run ads |
| 6 | Analyse a real business's social media | You understand digital marketing strategy |

### The four rules to remember all semester
1. **Errors are normal.** A red error message is the computer telling you *exactly* what's wrong. Read it,
   search it, fix it.
2. **It must run through `http://localhost/`.** PHP only works on a server. Double-clicking a `.php` file
   (file://) will **not** run it. And **MySQL must be started** in XAMPP, or every page errors.
3. **The 15-minute rule.** Stuck on the same thing for 15 minutes? Ask your instructor or a classmate.
   Don't suffer in silence.
4. **Compare with the demo.** The instructor's **LearningMart** demo works. Unsure if yours is right?
   Compare with it.

---

## 2. Before You Start — Setup Checklist
Do all of this before Session 1. If you skip it, you'll spend lab time installing instead of learning.

### Software to install
| Software | Where | Why |
|---|---|---|
| **XAMPP** | apachefriends.org | Bundles Apache + PHP + MySQL. This is your whole local server. |
| **VS Code** | code.visualstudio.com | Your code editor. Add the "PHP" + "PHP Intelephense" extensions. |
| **Chrome / Firefox** | you have it | For DevTools (F12) when debugging. |

### Accounts to create (all free)
| Account | Where | For |
|---|---|---|
| **Google account** | accounts.google.com | Search Console, Keyword Planner, GA4, Ads |
| **InfinityFree** | infinityfree.com | Deploying your PHP + MySQL store live (Session 3) |
| **eSewa / Khalti sandbox** | developer.esewa.com.np / docs.khalti.com | Payment test mode (Session 2) |
| **Buffer** | buffer.com | Social analytics (Session 6) |

> **WATCH OUT — where your files live.** Your project folder must sit inside XAMPP's **`htdocs/`**
> folder, and you open it at `http://localhost/yourfolder/`. Files outside `htdocs`, or opened by
> double-clicking, will not run PHP.

### Folder structure to set up now
```
htdocs/
  mystore/
    index.php          <- home / product listing
    product.php        <- single product
    cart.php           <- shopping cart (Session 2)
    checkout.php       <- checkout + payment (Session 2)
    base/connect.php   <- database connection (PDO)
    layout/header.php  <- shared top bar (SEO tag + GA4 go here later)
    layout/footer.php  <- shared footer
    assets/css/style.css
    assets/js/script.js
    config.php         <- DB creds + payment keys (do NOT share/commit)
```

> **Before Session 1, tick each:** ☐ XAMPP installed, Apache + MySQL start (green) ☐ `http://localhost`
> and `/phpmyadmin` load ☐ VS Code + PHP extensions ☐ Google, InfinityFree, eSewa/Khalti, Buffer accounts
> ☐ `htdocs/mystore/` created

---

## 3. Phase 1 — Building the Store (Sessions 1–3)

### How the pieces fit together
Think of your store like a shop building:

| Layer | Job | In this course |
|---|---|---|
| **HTML** | structure | the walls and shelves — what's on the page |
| **CSS** (Bootstrap 5) | looks | paint and layout — how it looks |
| **JavaScript** | small interactions | light switches — validation, buttons, dark mode |
| **PHP** | the brain (server) | decides what to show, talks to the database |
| **MySQL** | the storeroom | where products, users, and orders are actually kept |

The big difference from a plain website: **PHP runs on the server first**, builds the HTML (often using
data from MySQL), and only *then* sends finished HTML to the browser.

### The request flow (memorise this)
```
Browser asks for a page  →  Apache runs your PHP  →  PHP queries MySQL (with PDO)
   →  PHP builds HTML  →  Browser shows it (and runs your CSS/JS)
```

### A product card — from the database, in PHP
Instead of typing each product by hand, you loop over database rows:
```php
<?php
$products = $pdo->query("SELECT * FROM products")->fetchAll();
foreach ($products as $p): ?>
  <div class="card">
    <h3><?php echo htmlspecialchars($p['title']); ?></h3>
    <p class="price">Rs. <?php echo number_format($p['price']); ?></p>
    <a href="product.php?id=<?php echo (int)$p['id']; ?>" class="btn btn-dark">View</a>
  </div>
<?php endforeach; ?>
```
Change a product in phpMyAdmin → refresh → the page updates. That's the power of a database.

### Connecting to MySQL (PDO) — safely
```php
// base/connect.php  (on XAMPP)
$pdo = new PDO("mysql:host=localhost;dbname=demo;charset=utf8mb4", "root", "");
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
```
Always query user input with **prepared statements**, never by gluing strings:
```php
// SAFE — blocks SQL injection
$stmt = $pdo->prepare("SELECT * FROM products WHERE id = ?");
$stmt->execute([$_GET['id']]);
$product = $stmt->fetch();
```

### Responsive layout (works on mobile)
Bootstrap's grid handles most of it. For a custom product grid, one line of CSS does the job:
```css
.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 20px;
}
/* 4 columns on desktop → 2 on tablet → 1 on mobile, automatically */
```

### How a payment gateway fits in (Session 2)
When a customer clicks **Place Order**, your store doesn't handle the card — a **payment gateway**
(eSewa, Khalti, PayPal) does. In Nepal we use **eSewa/Khalti sandbox**:
1. Your PHP saves the order as *pending* and sends the amount to the gateway's **test** endpoint.
2. The customer pays on the gateway's page (test credentials).
3. The gateway redirects back to your **success** URL.
4. **Your PHP verifies** the payment with the gateway (using your **secret** test key) — *then* marks the
   order paid. Never trust the redirect alone; always verify on the server.

> **GOOD TO KNOW.** Everything in Sessions 1–3 uses **sandbox / test mode** — no real money moves. Get
> test credentials from the eSewa/Khalti developer docs. Your **secret key stays in PHP** (`config.php`),
> never in HTML or JavaScript.

### What HTTPS means, and hosting (Session 3)
`https://` means data between the browser and server is **encrypted** — essential for a store. When you
deploy to **InfinityFree**, you get free HTTPS automatically.

**Why not Netlify?** Netlify only serves *static* files — it can't run PHP or host a MySQL database. A
PHP + MySQL store needs a **PHP host** like InfinityFree (free PHP + MySQL + phpMyAdmin + SSL).

> **WATCH OUT — database credentials change when you deploy.** On your laptop (XAMPP) it's
> `host=localhost, user=root, password=""`. On InfinityFree it's a **remote** host like
> `sqlXXX.infinityfree.com` with a generated username and password. You **must** edit `connect.php` for
> the live site, or it will say "Connection failed" even though it worked on localhost.

---

## 4. Phase 2 — Marketing the Store (Sessions 4–6)

### Why your store doesn't appear on Google automatically
Google finds sites with a **crawler** that follows links. A brand-new store nobody links to might never be
found. **Google Search Console** lets you tell Google "I exist — please look." That's Session 4.

> **GOOD TO KNOW.** Your store may not appear in Google results during this course — totally normal for a
> new site. You're learning the *process*, not chasing a ranking.

> **PHP note:** in a PHP app your pages share one **`layout/header.php`**. So the Search Console
> verification meta tag and the GA4 script go **there once**, and every page gets them automatically —
> nicer than editing a separate `index.html`.

### Keywords — the foundation
| Type | Example (tech store) | Meaning |
|---|---|---|
| Too broad | `headphones` | Millions of results, mostly global. Hard to compete. |
| Too specific | `noise cancelling over-ear headphones under 3000 bhaktapur` | Almost nobody searches this. |
| Just right | `buy wireless earbuds Kathmandu` | Clear buyer intent, local, realistic. |

### Google Ads — you pay per click, not per view
Ads put your store at the top of results for your keywords. You pay only when someone **clicks** (CPC). In
Session 5 you build a full campaign but **save it as a draft** — no spending.

### GA4 — knowing who visits
GA4 is a small script in your `layout/header.php`. Once added, every visit records the page, time,
country, and device — so you learn what's popular and whether marketing works.
```html
<!-- inside <head> in layout/header.php — replace G-XXXXXXXXXX with your real ID -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

### Social media metrics — what they mean
| Metric | Simple definition | Example |
|---|---|---|
| Reach | unique people who saw a post | 500 people |
| Impressions | total views (repeats counted) | 800 |
| Engagement | likes + comments + shares | 45 |
| Engagement Rate | engagement ÷ followers × 100 | 45 / 2000 × 100 = 2.25% |
| CTR | clicks ÷ reach × 100 | 30 / 500 = 6% |

---

## 5. When You Get Stuck — Troubleshooting

### The 5-step checklist (try these first, every time)
1. **Did you save?** `Ctrl+S`. ~40% of "it's broken" is an unsaved file.
2. **Did you refresh?** `F5`. The browser may show the old page.
3. **Is Apache AND MySQL running?** Both must be green in XAMPP. MySQL off = "Connection failed".
4. **Read the PHP error.** PHP prints the file and line number. Read it — it's usually precise.
5. **Check the browser console** (`F12` → Console) for JavaScript errors in red.

### Common problems and exact fixes
**"Connection failed" / "SQLSTATE..."** — MySQL isn't started, the database name in `connect.php` doesn't
match the one in phpMyAdmin, or you didn't import the schema. Check all three.

**PHP code shows as plain text in the browser** — you opened the file by double-clicking (file://) or it's
not in `htdocs`. Open it via `http://localhost/mystore/...`.

**"Undefined array key" / blank page** — a `$_GET`/`$_POST`/row key doesn't exist. Check the name, and
that the query returned a row. Turn on error display while developing.

**Live site says "Connection failed" but localhost works** — you forgot to change the DB credentials from
`localhost/root` to your InfinityFree MySQL host/user/password. Edit `connect.php`/`config.php`.

**Sandbox payment "worked" but the order isn't marked paid** — you didn't verify server-side. After the
gateway redirects back, call its verification API from PHP before setting the order to `paid`.

**Search Console won't verify** — the meta tag must be on the **live** pages. Put it in
`layout/header.php`, re-upload to the host, wait ~30s, then Verify.

**GA4 Realtime shows 0** — you didn't replace `G-XXXXXXXXXX` with your real Measurement ID, or didn't
re-upload `header.php`. Fix and re-deploy.

**Keyword Planner asks for billing** — when creating the Ads account choose **Expert mode → "Create an
account without a campaign"**.

> **REMEMBER.** If nothing works, copy the **exact** error message and search it, starting with `PHP` or
> `MySQL`. Someone has hit the same error — usually with a clear fix.

---

## 6. How to Code Without Getting Frustrated
There will be moments when nothing works and it feels like everyone else gets it. That feeling is common
and temporary.

- **Save-refresh habit:** `Ctrl+S` then `F5` every couple of minutes. Don't make 20 changes then wonder
  what broke.
- **DevTools (F12):** *Console* = JS errors; *Network* = files/AJAX not loading; *Elements* = inspect HTML.
- **Search well:** not "my cart not working" → yes "php pdo fetch returns empty array" or paste the exact
  error like `SQLSTATE[42S02]: Base table or view not found`.

| Try yourself first when... | Ask the instructor when... |
|---|---|
| you haven't saved + refreshed | you've done all 5 debug steps |
| you haven't read the PHP error | stuck > 15 minutes |
| you haven't searched the error | the error makes no sense |
| stuck < 15 minutes | it worked, then suddenly stopped |

> **REMEMBER.** Coding is a test of patience, not intelligence. The students who do best aren't the ones
> who get it right first — they're the ones who keep going. Every bug you fix makes the next one easier.

---

## 7. Quick Reference Cards

**Session 1 — Setup, Database & Storefront**
```php
// base/connect.php  (XAMPP)
$pdo = new PDO("mysql:host=localhost;dbname=demo;charset=utf8mb4","root","");
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
// index.php
$products = $pdo->query("SELECT * FROM products")->fetchAll();
```
☐ XAMPP Apache+MySQL green ☐ DB `demo` + tables ☐ ≥15 products ☐ grid loads from DB

**Session 2 — Cart, Checkout & Payment**
```php
$_SESSION['cart'][$id] = ($_SESSION['cart'][$id] ?? 0) + 1;   // add to cart
$pdo->beginTransaction(); /* insert order + items, cut stock */ $pdo->commit();
// eSewa test merchant code: EPAYTEST   |   keys live in config.php (never in HTML)
```
☐ cart add/update/remove ☐ order saved in transaction ☐ sandbox pay verified server-side

**Session 3 — Security & Deployment**
```php
$stmt = $pdo->prepare("SELECT * FROM users WHERE email=?");  // prepared statement
echo htmlspecialchars($value);                               // output escaping
```
Deploy: InfinityFree → upload files → import schema in host phpMyAdmin → **change DB creds** → test HTTPS.
☐ live HTTPS URL ☐ injection/XSS fail ☐ creds updated ☐ URL to instructor

**Session 4 — Google Search Tools**
`search.google.com/search-console` → URL prefix → meta tag into `layout/header.php` → re-upload → Verify →
URL Inspection. ☐ verified ☐ 10 keywords + volume/competition/justification

**Session 5 — Ads & Analytics** — Ads: Expert mode → Search campaign → **Draft**. GA4: paste gtag into
`header.php`, replace `G-XXXXXXXXXX`, re-upload, watch Realtime. ☐ draft campaign ☐ GA4 realtime user

**Session 6 — Social Media Analysis** — `(likes + comments) ÷ followers × 100`, over 5 posts. Audit:
platform, frequency, content, engagement, 2 strengths, 2 weaknesses, 3 recommendations.

---

## 8. Final Assessment Preparation
At the end of Session 6 you present — a show-and-tell of what you built.

| Marks | Show | Notes |
|---|---|---|
| 20 | **Live deployed store** | Open your InfinityFree URL; products from DB, add-to-cart, checkout, mobile view |
| 10 | **Payment** | Sandbox payment on the live site; show the order row in phpMyAdmin |
| 10 | **Security** | HTTPS padlock; explain your prepared statements + output escaping |
| 15 | **Keyword report** | 10 keywords, volume, competition, justification |
| 15 | **Google Ads** | Draft campaign — headlines, keywords; explain CPC |
| 15 | **GA4 + Search Console** | Realtime active user + verified property |
| 10 | **Social audit** | Competitor analysis + 3 recommendations |
| 5 | **Explanation** | Explain your decisions clearly |

### What loses marks (avoid these)
- Demoing from **localhost** instead of the live InfinityFree URL
- Live site "Connection failed" because DB creds weren't changed from `localhost/root`
- Payment marked paid **without server-side verification**
- Ads campaign **published** instead of saved as draft
- GA4 still has `G-XXXXXXXXXX` instead of your real ID
- Keyword report with fewer than 10 keywords or no justifications
- Social audit with no engagement-rate calculation

> **The night before — tick each:** ☐ store live on an `https://...infinityfree...` URL ☐ can demo cart
> + checkout live ☐ sandbox order in phpMyAdmin ☐ Search Console verified ☐ 10-keyword report ☐ Ads draft
> with copy ☐ GA4 Realtime works ☐ social audit with engagement rate + 3 recommendations ☐ can explain
> SQL injection, XSS, HTTPS, CPC, engagement rate.

> **REMEMBER.** You built a real PHP + MySQL e-commerce store *and* used the same tools professional
> marketers use. That's genuinely impressive. Walk in confident — you have something real to show.
