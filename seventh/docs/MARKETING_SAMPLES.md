# IT 247 — Marketing Reference Samples

> Model outputs students imitate for the marketing lab works. Numbers are illustrative — replace with real data.

---

# Keyword Research Report — LearningMart (SAMPLE / reference)

Store: LearningMart — an online **tech products** store (phones, laptops, audio, wearables, accessories),
Nepal. Prepared with **Google Trends** (`trends.google.com`, region = Nepal) — no account or credit card
needed. (Google Keyword Planner works too, but it now forces payment info at signup, so Trends is the
default for this lab.)

**How this report was built:** entered 4 seed terms one at a time in Google Trends (region **Nepal**,
past 12 months) — `wireless earbuds`, `smart watch`, `bluetooth speaker`, `power bank` — and read the
**Top queries** and **Rising queries** panels. Kept the on-topic buying terms, **discarded the noise**
(e.g. searching "power bank" surfaces `nepal rastra bank`, `bse sensex`, `sbi bank share price` — those
are stock-market searches the word "bank" dragged in, not our product, so they're dropped).

> **Note:** "Demand" here is read from the **length of the blue "Search interest" bar** in Trends
> (long = High, half = Medium), not an exact monthly number — Trends shows relative interest, which is
> fine for this lab. When you do it, use the terms **your** seeds surface for your region.

| # | Keyword | Demand (Trends bar) | Intent | Where to use it on the site |
|---|---------|--------------------|--------|-----------------------------|
| 1 | wireless earbuds price in nepal | Med | 💰 Transactional | Earbuds product **title** + meta description |
| 2 | best wireless earbuds for calls | Med (Breakout) | Commercial | Earbuds **description** bullet |
| 3 | smart watch price in nepal | High | 💰 Transactional | Smartwatch product **title** |
| 4 | best smart watch | Med (+20%) | Commercial | Smartwatch **meta description** |
| 5 | samsung smart watch | Med | Commercial (brand) | Product **name** — only if you stock Samsung |
| 6 | bluetooth speaker price in nepal | High | 💰 Transactional | Speaker product **title** |
| 7 | jbl bluetooth speaker | Med | Commercial (brand) | Speaker product **name** (if JBL) |
| 8 | best bluetooth speaker | Med (+10%) | Commercial | Speaker **description** |
| 9 | power bank price in nepal | High | 💰 Transactional | Power bank product **title** |
| 10 | power bank 20000mah | Med | 💰 Transactional (spec) | Power bank **description** (specs) |

**Reading the report:**
- **Demand** = length of the blue **Search interest** bar in the Top/Rising panels (relative, not an exact
  count). Longer bar = more people search it.
- **Intent** = what the searcher wants. Words like **price / in nepal / 20000mah** = ready to **buy**
  (Transactional — most valuable). Words like **best / for calls** = still **comparing** (Commercial).
  Prioritise transactional keywords for product titles and Ads.
- **"Breakout"** in Rising queries = a term whose searches spiked recently — good for timely posts/ads.

**Closing the loop (this is the graded part):** take a transactional keyword and put it into a real
product on your live site — e.g. earbuds → title `Wireless Earbuds — Price in Nepal | Buy Online`, meta
description `Buy wireless earbuds in Nepal at the best price. Great for calls, fast delivery.` Reload the
page → **View Source** → confirm the keyword is now in `<title>` and `<meta name="description">`. That is
research → on-page SEO.

---

# Ad Campaign Plan — LearningMart (SAMPLE / reference)

Use this as the model for the **Q14 campaign plan**. Google Ads now requires a credit card at signup, so
you document this as a **written plan (paper campaign)** — no account needed, no spend. *(Optional: build
it live in **Meta / Facebook Ads Manager**, or in Google Ads if you already have a billed account.)*
Everything below is exactly what your plan table should contain.

## Campaign settings
- **Goal:** Sales
- **Campaign type:** Search
- **Landing (Final) URL:** a specific **product/category page** on your live store, **with UTM tags** —
  `https://study.gdev.infinityfreeapp.com/product.php?cat=1&utm_source=google&utm_medium=cpc&utm_campaign=audio`
  *(send "earbuds" ads to the earbuds page, not the homepage)*
- **Locations:** Nepal (or Kathmandu Valley)
- **Language:** English
- **Daily budget:** Rs. 100 *(a planning figure — used to estimate reach; nothing is spent)*
- **Bidding:** Maximize clicks (simple, good for learning)

## Ad group: "Audio — Earbuds & Speakers"
**Keywords (5):**
1. `wireless earbuds price in nepal`
2. `"wireless earbuds"` (phrase match)
3. `best wireless earbuds for calls`
4. `bluetooth speaker price in nepal`
5. `portable speaker nepal`

**Responsive search ad copy:**
- **Headline 1:** LearningMart Nepal
- **Headline 2:** Wireless Earbuds & Speakers
- **Headline 3:** Free Delivery in Kathmandu
- **Description 1:** Shop genuine earbuds, speakers and headphones at honest prices.
- **Description 2:** Fast delivery across Nepal. Pay easily with Khalti. Order today.

## What to explain in your report
- **CPC (cost per click):** you pay only when someone clicks the ad — not for views.
- **Why a specific product page (not the homepage):** the searcher wants that product; landing them on it
  loses fewer clicks → higher conversion.
- **What the UTM tags do:** they let **GA4 attribute the visit** to `source=google / medium=cpc` — so you
  can prove which channel brings buyers. Test it: open your own UTM URL and watch GA4 **Realtime → by
  source/medium**.
- **Why a plan, not a live campaign:** Google Ads requires a credit card at signup; the plan captures the
  full setup (goal, keywords, ad copy, landing URL) with zero cost.

---

# Social Media Audit — SAMPLE / reference (competitor: Daraz Nepal)

Use this as the model for the Q16 audit. Your own audit should analyse a competitor of *your* store and
end with 3 recommendations for *your* store.

> **Note:** figures below are **illustrative examples** of how to present an audit. Use the real numbers
> you observe on the competitor's page when you do the lab.

**Competitor:** Daraz Nepal · **Platforms:** Facebook, Instagram, TikTok

### Observations
- **Posting frequency:** ~2–3 posts/day (very active).
- **Content types:** product offers, flash-sale countdowns, festival campaigns, short reels, memes.
- **Engagement:** high on sale/festival posts, lower on plain product posts.
- **Responsiveness:** replies to comments and DMs, often redirecting to support.

### Engagement rate (worked example)
Take 5 recent posts, average `(likes + comments) ÷ followers × 100`:

| Post | Likes | Comments | Followers | Engagement % |
|------|-------|----------|-----------|--------------|
| 1 | 1,200 | 90 | 3,000,000 | 0.043% |
| 2 | 800 | 40 | 3,000,000 | 0.028% |
| 3 | 2,500 | 150 | 3,000,000 | 0.088% |
| 4 | 600 | 25 | 3,000,000 | 0.021% |
| 5 | 1,000 | 60 | 3,000,000 | 0.035% |

**Average engagement rate ≈ 0.043%** (typical for a very large page — big following, so % looks small).

### Strengths (2)
1. Consistent, high-volume posting keeps the brand top-of-mind.
2. Strong festival/sale campaigns that clearly drive engagement spikes.

### Weaknesses (2)
1. Plain product posts get little interaction.
2. High follower count dilutes engagement rate.

### Recommendations for LearningMart (3)
1. Post 3–4×/week (quality over quantity for a small store) with clear product + price.
2. Use short reels showing products in use (earbuds, smart watch) — reels out-engage static posts.
3. Run a small festival offer (Dashain/Tihar) with a countdown to create urgency, and always reply to
   comments to build trust.
