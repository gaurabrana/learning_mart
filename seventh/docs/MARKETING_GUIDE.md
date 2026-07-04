# LearningMart — Digital Marketing Guide
### Choose the tool → Use it → Integrate it into the project (properly)

This is the deep, step-by-step guide for the **marketing half** of the course (Units 6 / Sessions 4–6).
For each area you'll see **why this tool**, **how to use it**, and **how it's wired into the LearningMart
code**. Model outputs students imitate (keyword report, ad copy, social audit) are in
`MARKETING_SAMPLES.md`.

## The stack at a glance
| Goal | Tool (chosen) | Free alt. | Where it's integrated in the project |
|------|---------------|-----------|--------------------------------------|
| Be found (SEO) | On-page SEO + Google Search Console | Bing Webmaster | `<title>`/`<meta>`, `sitemap.php`, `robots.txt`, JSON-LD |
| Know what people search | Google Trends (no card) | Keyword Planner (needs billing) | keywords go into titles/descriptions + Ads |
| Paid traffic | Ad campaign plan (paper) | Meta Ads Manager (live) | landing = live product URLs + UTM tags |
| Measure | Google Analytics 4 | Matomo | `$GA4_ID` in `config.php`; `purchase` event |
| Reach / sharing | Facebook/Instagram + Buffer | Hootsuite | Open Graph tags for shareable links |

> **Prerequisite:** Search Console and Ads need the store on a **public HTTPS URL**. GA4, keyword
> research, and the social audit can be done **without** deploying. So do §0 (hosting) first.

---

## Start here — the order to do it in (once the website works)

You've finished building your store and it runs locally. Do marketing in **this order** — each step
unlocks the next. This assumes the standard project structure most of you have (`layout/header.php`,
`base/connect.php`, `config.php`); if your file layout differs, keep the **goal** and change the **where**
(see the note under the table).

| # | Do this | Where it lives in the project | Full section |
|---|---------|-------------------------------|--------------|
| 1 | **Deploy to a public HTTPS URL** | Upload `demo/` to InfinityFree `htdocs/`, import `schema.sql`, edit **only `config.php`** (`$APP_BASE`, `$DB`). Confirm the padlock. | §0 |
| 2 | **Point the site at its live URL** (base URL, and the `Sitemap:` line in `robots.txt`) | Set `$APP_BASE` in `config.php`; edit the `Sitemap:` line in `robots.txt`; check `/sitemap.php` returns XML. | §0, §1 |
| 3 | **Put the GA4 tag in your `<head>` on every page**, then confirm Realtime shows you | Set `$GA4_ID` in `config.php` — the gtag snippet then renders from `layout/header.php` site-wide. | §5 |
| 4 | **Verify in Search Console + submit your sitemap** + request indexing | Verify via HTML-file at root *or* the GA method; submit `sitemap.php`. | §2 |
| 5 | **Research keywords** (Google Trends, region = Nepal) → put transactional ones into your page **titles/descriptions** | Edit product `<title>`/`<meta>` in `product_detail.php` etc. | §3, §1 |
| 6 | **Write the ad campaign plan** (5 keywords + copy; landing = a real page **with UTM tags**) → see `google / cpc` in GA4 Realtime | Landing URL = a live `product.php?cat=…` with UTM params. | §4 |
| 7 | **Do the social audit** (competitor, engagement rate over 5 posts, 3 recs) + check links share nicely | Open Graph tags already on `product_detail.php`. | §6 |

**Why this order:** you can't verify Search Console or land ad clicks until the site is **live** (steps
1–2). GA4 (step 3) goes on before Search Console so you can use the easy "Google Analytics" verification
method and start collecting visits immediately. Keywords (step 5) must exist before the ad plan (step 6),
because the plan's keywords and the SEO edits both come from that research.

> **What's already built for you:** on-page SEO, `sitemap.php`, `robots.txt`, JSON-LD, Open Graph, the
> site-wide gtag snippet, and the `purchase` event are **already in the code**. Marketing is mostly
> *turning these on* (fill in `config.php`) plus the off-site work (Search Console, Trends, the plan, the
> audit) — not writing new code. Model outputs are in `MARKETING_SAMPLES.md`; worked viva answers grounded
> in our live store are in `IT247_Marketing_Viva_Answers.md`.
>
> **If your setup differs** (you didn't use `config.php`, or your files are laid out differently): the
> goals don't change — just do the same thing in your own structure. The base URL lives wherever your app
> keeps it; the **GA4 gtag snippet must sit in the `<head>` of every page** (put it in your shared
> header/layout so it loads site-wide); `robots.txt` and the sitemap go at your domain root; titles/meta
> go in your page `<head>`s. The **deliverables** (keyword report, ad plan, social audit) are the same no
> matter how your site is built.

---

## 0. Hosting the store — do this FIRST

**Why:** Search Console must reach a public URL to verify ownership; Google Ads sends clicks to a real
landing page; and to see live visitors in GA4 you need people able to open the site. Marketing can't
really start until the store is live.

**Choose a host:** **InfinityFree** — free PHP + MySQL + HTTPS. **Not** Netlify / GitHub Pages — those are
*static-only* and can't run PHP or a MySQL database. (Alternatives: 000webhost, AwardSpace, or any
cPanel / paid host.)

**Steps** (full walkthrough with screenshots-worth of detail in [`DEPLOY.md`](DEPLOY.md)):
1. Sign up at **infinityfree.com** → create a site (you get a free `…infinityfreeapp.com` subdomain).
2. Create a **MySQL database** in the control panel → note its **host, name, user, password**.
3. Import **`database/schema.sql`** via the host's phpMyAdmin — first delete the top two lines
   `CREATE DATABASE IF NOT EXISTS demo;` and `USE demo;` (you import into the DB the host gave you).
4. Upload all **`demo/`** files into **`htdocs/`** (File Manager or FTP).
5. **Edit `config.php` only** — this is the one file you change for production:
   - `$APP_BASE` → your live URL (no trailing slash)
   - `$DB` → the host's MySQL host / name / user / password
   - optionally `$KHALTI['secret_key']` and `$GA4_ID`
   *(You no longer touch `connect.php` — it reads `$DB` in production and auto-detects XAMPP/MAMP locally.)*
6. Update **`robots.txt`** `Sitemap:` line to the live URL, and place the Search Console verification file
   at the site root.
7. Open the URL → confirm the **HTTPS padlock** → test browse → register → cart → checkout.

> **Free-host caveat:** some free hosts block outbound requests (the cURL to Khalti/eSewa for payment
> verification). If a live payment errors for that reason, demo payments on XAMPP/MAMP and use the live
> site for the SEO + analytics parts — it's a hosting limit, not a code bug.

---

## 1. On-page SEO — the foundation (do this first, it's in the code)

**Why first:** no external tool helps if the site doesn't describe itself and can't be crawled. This is
"technical + on-page SEO" and it lives entirely in your project.

**What's already integrated in LearningMart (study these):**
- **Unique page titles + meta descriptions** — `index.php` (home) and `product_detail.php` (per product).
  A good title/description is what shows in Google results.
- **Canonical URL** on product pages (`<link rel="canonical">`) — avoids duplicate-URL confusion.
- **Dynamic `sitemap.php`** — lists home, product list, category, and every product URL as XML.
- **`robots.txt`** — allows crawling and points to the sitemap.
- **Structured data (`schema.org/Product` JSON-LD)** on product pages — lets Google show price/stock
  rich results.
- **Open Graph tags** on product pages (also used by social — see §6).

**How to extend it (teach students to):**
- Write a *unique, keyword-rich* title + description for each product (not the same text everywhere).
- Put the keywords from §3 into product **names/descriptions** and page titles.

**Check it:** open a product page → View Source → confirm `<title>`, `<meta name="description">`, the
`og:` tags, and the `application/ld+json` block. Visit `/sitemap.php` → you should see XML.

---

## 2. Google Search Console — get indexed (Session 4, Q12)

**Choose it:** the authoritative, free tool for how Google sees your site. (Alternative: Bing Webmaster
Tools — same idea for Bing.)

**Use it:**
1. search.google.com/search-console → **Add property → URL prefix** → paste your live URL.
2. **Verify** with the **HTML-file method**: download `google<...>.html`, upload it to your site root,
   click Verify. *(File method, not the meta tag, because a PHP site has per-page `<head>`s.)*
3. **Submit your sitemap:** Sitemaps → enter `sitemap.php` (or the full URL).
4. **URL Inspection** → paste a page → Request Indexing.

**Integrate:** the sitemap is already generated by `sitemap.php`; `robots.txt` already advertises it. On
deploy, put `robots.txt` and the verification file at the **domain root** and update the Sitemap URL.

---

## 3. Keyword research with Google Trends — research demand (Session 4, Q13)

**Choose it:** **Google Trends** (`trends.google.com`) — free, **no account, no credit card**, and it
shows real Nepal search interest + related "Top" and "Rising" queries. Use this as the default.

> **Why not Keyword Planner?** Keyword Planner also works and gives exact volume ranges, **but Google now
> forces you to enter payment info at signup** (even "Set up an account only" asks for a card in Nepal).
> For a no-cost lab that's a dead end, so we use Trends. Keyword Planner is **optional** — only if a
> student already has a billed Google Ads account. (Other free helpers: Google **autocomplete**, the
> **"People also search for"** box, and the **Keyword Surfer** Chrome extension.)

**Use it:**
1. Go to **trends.google.com** (no sign-in) → type a seed term (e.g. `wireless earbuds`).
2. Set **Region → Nepal**, **Past 12 months**.
3. Scroll to **Commonly searched queries** → read **Top queries** (steady demand — best for SEO) and
   **Rising queries** (fast-growing; **"Breakout"** = big recent spike — good for timely ads/posts).
4. Click **Clear** and repeat for 3–4 seeds that match your categories (`smart watch`, `bluetooth
   speaker`, `power bank`…). Each seed yields ~3–4 keywords → 10+ total.
5. Build a **10-keyword report** with columns **Keyword | Demand | Intent | Where to use it** (model:
   `MARKETING_SAMPLES.md`).

**Read the results properly (teach this):**
- **Demand** = length of the blue **Search interest** bar (long = High, half = Medium) — relative, not an
  exact count; that's fine here.
- **Intent** = *price / in nepal / 20000mah* → ready to **buy** (Transactional, most valuable); *best /
  for calls / review* → still **comparing** (Commercial).
- **Discard the noise.** Some related queries are off-topic — e.g. seed `power bank` surfaces
  `nepal rastra bank`, `bse sensex`, `sbi bank share price` (stock-market searches the word "bank"
  dragged in). Keep only terms a shopper for *your* product would type.

**Integrate (this is the point students miss):** the keywords aren't just a report — **feed them back into
the site**: use them in product **titles**, **meta descriptions**, and **descriptions** (§1), and as the
**keywords in your Ads campaign** (§4). Keyword research → on-page SEO + Ads is the loop.

---

## 4. Paid search — an ad campaign plan (Session 5, Q14)

**Choose it:** **Search** campaigns capture people already searching to buy — highest intent for a store.
(Display/Social ads are for awareness; start with Search.)

> **The point of this lab is to *understand how paid search works* — not to spend money.** You document
> the campaign as a written plan (a "paper campaign") and, above all, be able to explain the mechanism
> below. **Google Ads now requires a credit card even to set up an account**, so a plan is how we learn it
> at zero cost. *(Optional live route: **Meta / Facebook Ads Manager** lets you build a campaign without
> paying up front — screenshot the setup.)*

**How paid search actually works (be able to explain this):**
1. You pick **keywords**, a **max bid** (the most you'll pay for one click), and write an **ad**.
2. When someone searches a matching keyword, Google runs an **instant auction** among all advertisers
   bidding on it.
3. Your position is decided by **Ad Rank = your bid × Quality Score**, where **Quality Score** measures how
   relevant your ad *and* landing page are to the search. So a *more relevant* ad can outrank a *higher
   bidder* — money isn't the only lever.
4. You pay **per click (CPC)**, not per view — and usually only just enough to beat the advertiser below
   you, not your full max bid.
5. **Better relevance → higher Quality Score → better position at lower cost.** That's *why* your keywords,
   ad copy, and landing page all matter — they're the levers you control in the plan.

**Do it (write the plan):** Goal **Sales**, Type **Search**, location Nepal, planning budget Rs. 100 → one
ad group named after a category → **5 keywords from §3** (prefer transactional) → **3 headlines + 2
descriptions** → **landing URL = a real product/category page with UTM tags**. Template:
`MARKETING_SAMPLES.md`.

**Integrate into the project (this is the real, free, testable part):**
- **Landing page** = your live **product/category URL** (send "earbuds" ads to the earbuds page, not the
  homepage).
- **UTM tags** on the final URL so GA4 attributes the traffic, e.g.
  `…/product.php?cat=3&utm_source=google&utm_medium=cpc&utm_campaign=audio`.
- **Prove it works without spending:** open your own UTM landing URL, then check GA4 **Realtime → by
  source/medium** — you'll see `google / cpc`. That demonstrates the ad→analytics loop with zero cost.
- (Advanced) if you built a live draft, link Google Ads to GA4 so the `purchase` event (§5) counts as a
  **conversion**.

### Live option — Meta (Facebook/Instagram) Ads Manager (free to build)

Unlike Google Ads, Meta lets you build a **real** campaign **without paying or entering a card up front** —
you're only charged when it's published and delivering. So a student can go one step past the paper plan
and screenshot an actual draft at no cost. (It targets Facebook/Instagram audiences by interest/demographic
— good for **discovery**, whereas Search ads catch **intent**; mention that contrast in the viva.)

**Steps:**
1. Create a free **Facebook Page** for the store (Meta ads run *from* a Page, not a personal profile).
2. Open **Meta Business Suite → Ads Manager** → **Create** → objective **Traffic** (or **Sales**).
3. Set a small audience (e.g. Nepal, 18–45, interests: gadgets/electronics) and a **planning budget** —
   nothing is spent until you publish.
4. Write the ad (image + primary text + headline) and set the **destination URL to a live product/category
   page with UTM tags**, e.g.
   `https://study.gdev.infinityfreeapp.com/product.php?cat=3&utm_source=facebook&utm_medium=cpc&utm_campaign=audio`.
5. Stop at **Review/Draft** and **screenshot** it — that's the deliverable. (Publishing needs a payment
   method; the draft doesn't.)

**Integrate / prove it (free):** the shared link preview already works — Meta reads the **Open Graph tags**
on `product_detail.php`, so posts/ads show the product image, title and price. Open your own UTM link and
check GA4 **Realtime → by source/medium** to see `facebook / cpc`. *(Optional/advanced:* add the **Meta
Pixel** snippet to `layout/header.php` next to the gtag snippet to track a Meta-side `Purchase` conversion
— the Meta equivalent of the GA4 `purchase` event.)*

---

## 5. Google Analytics 4 — measurement (Session 5, Q15)

**Choose it:** the free standard; integrates with Ads/Search Console. (Alternative: Matomo, self-hosted.)

**Use it:** analytics.google.com → create a **Web** property → copy the Measurement ID `G-XXXXXXXXXX` →
**Reports → Realtime**.

**How it's integrated in LearningMart (this is "properly"):**
- **Site-wide pageviews:** set `$GA4_ID` in `config.php`. The gtag snippet is rendered from
  `layout/header.php` on **every** page automatically (open the site → Realtime shows you).
- **Conversion tracking:** `order_success.php` fires a GA4 **`purchase`** event (transaction id, value,
  items) whenever an order is paid — so you measure *revenue*, not just visits.
- **Extend it:** you can add `add_to_cart` (fire on the product page) and `begin_checkout` (fire on
  `checkout.php`) events the same way — a good student exercise.

**Check it:** set your real `G-` ID, open the store (works on localhost too), watch Realtime; complete a
paid order and see the `purchase` event under Realtime → Events.

---

## 6. Social media — reach + sharing (Session 6, Q16)

**Choose it:** for Nepal, **Facebook + Instagram** (and TikTok); **Buffer** (free) for scheduling +
analytics. (Alternative: Hootsuite.)

**Use it:** Facebook Business Suite / Instagram Insights for metrics (reach, engagement); analyse a real
competitor and compute engagement rate over 5 posts (template: `MARKETING_SAMPLES.md`).

**Integrate into the project:** the **Open Graph tags** on product pages (§1) mean that when someone shares
a product link on Facebook/Instagram/WhatsApp, it shows the **product image, title, and description**
instead of a bare link. Add **UTM tags** to links you post (e.g. `utm_source=facebook`) so GA4 shows how
much traffic social brings.

---

## The funnel (how it all connects)
```
SEO (be found)  ─┐
Ads (pay for it) ─┼──►  Visitors land on your store  ──►  GA4 measures behaviour  ──►  purchase event
Social (share)  ─┘                                                                     = conversion
```
Keyword research feeds SEO + Ads; UTM tags let GA4 tell you which channel actually sells; the `purchase`
event tells you revenue. Then you double down on what converts.

## What "success" looks like (what to check)
- **Search Console:** impressions & clicks climbing; pages indexed.
- **GA4:** users, and **conversions** (purchase events) by source/medium.
- **Ads:** CTR and CPC on the draft's estimates.
- **Social:** engagement rate and referral traffic (via UTM).

## Marketing checklist
- [ ] On-page SEO present (titles, descriptions, sitemap, robots, JSON-LD, OG) — mostly built-in
- [ ] Deployed to a public HTTPS URL
- [ ] Search Console verified + sitemap submitted + a page indexed
- [ ] 10-keyword report, keywords used in titles/descriptions
- [ ] Ad campaign plan (5 keywords, ad copy) with a product/category landing URL + UTM tags; GA4 Realtime shows the UTM source
- [ ] GA4 installed (`$GA4_ID`), Realtime confirmed, `purchase` event firing
- [ ] Social audit done; product links share nicely (OG tags)
