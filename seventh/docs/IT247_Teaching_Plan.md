# IT 247 — Teaching Plan (Instructor Playbook)
### E-Commerce and Internet Marketing · Lab · PHP + MySQL

This is the **step-by-step plan for running the lab**, anchored to the working **LearningMart** demo
(`seventh/demo/`). It's operational — what *you* do, in order. It complements the other docs:

| Doc | Who | Purpose |
|---|---|---|
| **This file** | You | How to run each session, setup, cheat-sheets, troubleshooting |
| [IT247_Lab_Questions.md](IT247_Lab_Questions.md) | Students | The 16 questions they answer in their report |
| [IT247_Lab_Report_Format.md](IT247_Lab_Report_Format.md) | Students | How to format the printed A4 report |
| [IT247_Student_Survival_Guide.md](IT247_Student_Survival_Guide.md) | Students | Setup + concepts + troubleshooting |
| [IT247_Student_Workbook.md](IT247_Student_Workbook.md) | Students | Per-session build steps |
| [IT247_Lab_Work_and_Viva.md](IT247_Lab_Work_and_Viva.md) | You | Model answers + viva + marking |

---

## Part 0 — One-time setup (do this before Session 1)

**Step 1 — Get the demo running on your machine (XAMPP or MAMP).**
1. Start Apache + MySQL.
2. Open phpMyAdmin (`http://localhost/phpmyadmin` on XAMPP, `http://localhost:8888/phpMyAdmin` on MAMP).
3. **Import** `seventh/demo/database/schema.sql` (creates the `demo` database, all tables, and 15 sample products with images).
4. Open the store: `http://localhost/demo/` (XAMPP) or `http://localhost:8888/demo/` (MAMP).
5. `base/connect.php` auto-detects XAMPP vs MAMP — if it can't connect, the error tells you what to check.

**Step 2 — Set up the payment sandboxes (see the cheat-sheet in Part 4).**
- **eSewa** works out of the box (public test credentials already in `config.php`).
- **Khalti** needs a test key: sign up at **test-admin.khalti.com**, copy your secret key into `config.php` → `$KHALTI['secret_key']`.

**Step 3 — (Before the marketing sessions) put a store on a public URL.**
- Deploy the demo (or a student's) to **InfinityFree** (see `DEPLOY.md`). Search Console and the live-visits GA4 demo need a **public HTTPS URL**.

**Step 4 — Set up the room.** Keep two things open on the projector all semester: the **LearningMart store** and **phpMyAdmin** (so "the database" is concrete).

**Step 5 — Hand out to students:** the **Lab Questions**, **Lab Report Format**, and **Survival Guide**. Tell them the deliverable is a **printed A4 lab report** answering the 16 questions, assessed by report + viva.

---

## Part 1 — The teaching arc

| Session | Focus | Students end with | Lab questions |
|---|---|---|---|
| 1 | Setup, database, storefront | Products showing from MySQL | Q1–Q4 |
| 2 | Cart, checkout, payment | Working cart + a sandbox payment | Q5–Q9 |
| 3 | Security & deployment | A live HTTPS store | Q10–Q11 |
| 4 | Search Console + Keyword research (Google Trends) | Keyword report | Q12–Q13 |
| 5 | Ad campaign plan + Analytics (GA4) | Campaign plan + GA4 tracking | Q14–Q15 |
| 6 | Social media analysis | A social media audit | Q16 |

**Golden teaching move every session:** *show it in LearningMart first → explain the concept → students build their own version → compare with LearningMart.*

---

## Part 2 — Session-by-session plan

### Session 1 — Setup, Database & Storefront (Q1–Q4)
1. **Demo:** open LearningMart + phpMyAdmin. Change a product's price in phpMyAdmin, refresh the store — show the page reflects the DB. That's the whole point of a dynamic site.
2. **Teach:** browser → Apache → PHP → MySQL → HTML (the request flow). Show `base/connect.php` (PDO) and `index.php` (loop over DB rows).
3. **Students build:** install XAMPP → create DB + tables (`schema.sql` as the model) → connect with PDO → show products in a grid.
4. **Then:** product detail (`product_detail.php`), category filter + search (`product.php`) — introduce **prepared statements** here (Q4).
5. **Watch for:** "Connection failed" (MySQL not started / wrong port), pages showing PHP as text (opened via `file://` instead of `http://localhost`).
6. **Covers:** Q1 (connection), Q2 (schema), Q3 (listing), Q4 (detail/search).

### Session 2 — Cart, Checkout & Payment (Q5–Q9)
1. **Demo:** register → log in → add to cart → checkout → pay with **eSewa test** → order shows as *paid* in phpMyAdmin. Show the `orders`, `order_items`, and `payments` tables filling in.
2. **Teach:**
   - **Auth** — `register.php`/`login.php`: `password_hash()` + `password_verify()`, sessions (Q5/Q6).
   - **Cart** — `cart.php` + the cart helpers in `base/functions.php`: session for guests, **persistent `cart` table** for logged-in users (Q7).
   - **Checkout** — `checkout.php`: saving `orders` + `order_items` in a **transaction** (Q8).
   - **Payment** — `base/payment.php` + `khalti.php`/`esewa.php`: initiate → gateway → **server-side verify** → mark paid (Q9). Stress: verify on the server, never trust the redirect.
3. **Students build:** auth → cart → checkout → integrate **one** gateway (eSewa is easiest — no key needed).
4. **Watch for:** the payment gotchas in Part 4 (Khalti key/host, eSewa login).
5. **Covers:** Q5–Q9.

### Session 3 — Security & Deployment (Q10–Q11)
1. **Demo:** in LearningMart, try `' OR '1'='1` at login (fails — prepared statements). Save `<script>alert(1)</script>` as a product name (renders as text — `htmlspecialchars`). Show the HTTPS padlock on the deployed URL.
2. **Teach:** SQL injection vs prepared statements; XSS vs output escaping; why DB credentials differ on the live host.
3. **Students build:** audit their queries; deploy to **InfinityFree** (`DEPLOY.md`); change `connect.php` creds for the host; confirm HTTPS.
4. **Watch for:** live site "Connection failed" (creds not changed from localhost/root); free-host quirks.
5. **Covers:** Q10 (security), Q11 (deployment).

### Session 4 — Search Console & Keyword research with Google Trends (Q12–Q13)
1. **Demo:** open Search Console with the deployed store; show the verified property + URL Inspection; open **Google Trends** (region Nepal) and research a seed term — Top vs Rising queries.
2. **Teach:** why a new site isn't on Google automatically (crawler/indexing); reading demand from the Trends bar; transactional vs commercial intent. *(Note: Keyword Planner now forces a credit card at signup, so we use Trends — free, no account.)*
3. **Students do:** verify their live store (HTML-file method), request indexing, build a **10-keyword report** (keyword, demand, intent, where used) and wire one keyword into a product title/description (model: `MARKETING_SAMPLES.md`).
4. **Covers:** Q12 (Search Console), Q13 (keyword report).

### Session 5 — Ad campaign plan & Analytics (Q14–Q15)
1. **Demo:** walk through a **written Search-campaign plan** (goal, ad group, keywords, ad copy, UTM landing URL) and GA4 **Realtime** — open the store and watch the visit appear; open a UTM URL and show it attributed to `google / cpc`.
2. **Teach:** CPC, ad groups, UTM attribution; GA4 basics. Show that in the demo you just set `$GA4_ID` in `config.php` and every page is tracked (the gtag snippet already lives in `header.php`).
3. **Students do:** write an **ad campaign plan** (model: `MARKETING_SAMPLES.md`) with a UTM landing URL — *no live account needed* (Google Ads requires a card; optional live route = Meta Ads Manager). Create a GA4 property, put the `G-XXXX` ID in **`config.php`**, confirm Realtime. (GA4 works on localhost too, so this needs no deploy.)
4. **Watch for:** GA4 ID left as placeholder; students trying to force a live Google Ads account past the card wall (use the plan instead); ad-blockers hiding Realtime (test in clean Chrome).
5. **Covers:** Q14 (campaign plan), Q15 (GA4).

### Session 6 — Social Media Analysis (Q16)
1. **Discuss:** which platforms Nepali e-commerce uses; why social matters (traffic, remarketing).
2. **Students do:** pick a real competitor, record posting frequency/content/engagement, compute engagement rate over 5 posts, write a 1-page audit (model: `MARKETING_SAMPLES.md`).
3. **Covers:** Q16.

---

## Part 3 — Demo file → lab-question map (what students study for each answer)

| Q | Topic | Demo file(s) to reference |
|---|-------|---------------------------|
| Q1 | DB connection | `base/connect.php` |
| Q2 | Schema / tables | `database/schema.sql` |
| Q3 | Product listing | `index.php`, `product.php` |
| Q4 | Detail & search | `product_detail.php`, `product.php` |
| Q5 | Register/login | `register.php`, `login.php` |
| Q6 | Sessions & logout | `base/functions.php`, `logout.php`, `layout/header.php` |
| Q7 | Cart | `cart.php`, cart helpers in `base/functions.php` |
| Q8 | Checkout & order | `checkout.php` |
| Q9 | Payment | `base/payment.php`, `base/khalti.php`, `base/esewa.php`, `payment_verify.php`, `esewa_verify.php` |
| Q10 | Security | prepared statements throughout + `htmlspecialchars` (see `product.php`, `login.php`) |
| Q11 | Deployment | `DEPLOY.md`, `base/connect.php` |
| Q12–Q16 | Marketing | `MARKETING_SAMPLES.md` + `layout/header.php` (GA4) |

---

## Part 4 — Payment sandbox cheat-sheet (the parts that trip people up)

**eSewa (works out of the box — public sandbox):**
- Already configured in `config.php` (`EPAYTEST` + public secret).
- **Login on the eSewa page:** eSewa ID `9711111111` (or …12/13/14) · password `Nepal@123` · token/OTP `123456` (fixed — not an SMS).

**Khalti (needs your test key):**
- Config must use the **sandbox host** `https://dev.khalti.com/api/v2/epayment/` (production `a.khalti.com` → "Invalid token").
- Get a test secret key from **test-admin.khalti.com** → put in `config.php` → `$KHALTI['secret_key']`.
- **Test payer:** Khalti ID `9800000000` (–`…005`) · MPIN `1111` · OTP `987654`.

**GA4:** set `$GA4_ID` (e.g. `G-XXXXXXXXXX`) in `config.php` → tracking is live on every page (works on localhost).

---

## Part 5 — Assessment (recap)
- **Deliverable:** a printed A4 lab report answering all 16 questions (`code + screenshot + explanation`) — see `IT247_Lab_Report_Format.md`.
- **Marks (adapt to your scheme):** report 50% · viva 40% · regularity 10%.
- **Viva is the anti-copying check** — point at an answer in *their* report and ask them to explain it (model answers in `IT247_Lab_Work_and_Viva.md`).

---

## Part 6 — Common problems & fixes (the ones we actually hit)

| Symptom | Cause | Fix |
|---|---|---|
| "Connection failed" | MySQL off / wrong port / DB not imported | Start MySQL; `connect.php` auto-tries 3306 (XAMPP) + 8889 (MAMP); import `schema.sql` |
| PHP shows as plain text | Opened via `file://` or outside webroot | Use `http://localhost[:8888]/demo/…` |
| Live site "Connection failed" | Still using `localhost/root` creds | Change `connect.php` to the host's MySQL host/user/pass |
| Khalti "Invalid token" | Production host or placeholder key | Use `dev.khalti.com` + a real test key from test-admin.khalti.com |
| eSewa login not working | Old test IDs | Use `9711111111` / `Nepal@123` / token `123456` |
| eSewa "Duplicate transaction UUID" | Reused UUID | Already fixed — the demo appends a unique suffix per attempt |
| GA4 shows no data | `$GA4_ID` empty / placeholder | Put your real `G-XXXX` in `config.php` |
| Cart lost after login | — | Not a bug: the guest cart **merges** into the saved cart on login; logged-in carts persist in the `cart` table |
