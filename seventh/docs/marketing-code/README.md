# Marketing code — everything in one place

All the code that makes the **marketing half** of LearningMart work, collected here so you can see it
without hunting through the app. Two of these are **real, runnable files** (copied verbatim); the rest are
**extracts** — the marketing-relevant lines lifted out of larger files, each with a header comment saying
exactly where the real code lives (`file` + line numbers).

> ⚠️ **Extracts are for reading, not running.** The `*.header.php`, `*.order_success.php`,
> `*.product_detail.php` and `config.marketing.php` files are snippets pulled out of bigger files — they
> won't run on their own. Edit the **real** files in `demo/` (paths below); this folder is a study/reference
> copy. The two standalone files (`sitemap.php`, `robots.txt`) ARE the real thing.

## What's in this folder

| File here | What it is | Real location in the app |
|-----------|------------|--------------------------|
| `config.marketing.php` | The two settings that turn marketing on: `$APP_BASE` (live URL) and `$GA4_ID` | `demo/config.php` (lines 10, 14) |
| `ga4-tag.header.php` | The GA4 **gtag.js** tracking snippet that loads on every page | `demo/layout/header.php` (lines 12–23) |
| `ga4-purchase-event.order_success.php` | The GA4 **`purchase`** conversion event (revenue tracking) | `demo/order_success.php` (lines 92–106) |
| `seo-tags.product_detail.php` | `<title>`, meta description, canonical, **Open Graph**, **JSON-LD** product schema | `demo/product_detail.php` (lines 40–42, 47–83) |
| `sitemap.php` | **Runnable** — dynamic XML sitemap of all public URLs | `demo/sitemap.php` (this is a copy) |
| `robots.txt` | **Runnable** — allows crawling + points to the sitemap | `demo/robots.txt` (this is a copy) |

## How the pieces connect (the marketing pipeline)

```
config.php  ($APP_BASE, $GA4_ID)
   │
   ├──► sitemap.php + robots.txt ───► submit in Google Search Console ──► get INDEXED (be found)
   │        (uses $APP_BASE to build live URLs)
   │
   ├──► seo-tags (product_detail.php) ─► good titles/descriptions in results
   │        + Open Graph ─────────────► nice link previews when shared / in Meta ads
   │        + JSON-LD ────────────────► price/stock rich results in Google
   │
   └──► ga4-tag (header.php, needs $GA4_ID) ─► tracks every visit (page_view, source, Realtime)
            │
            └──► ga4-purchase-event (order_success.php) ─► tracks REVENUE (the `purchase` conversion)
```

## To actually turn it all on

Everything above is either already written or a config value — there are **no structural code changes**:

1. **`demo/config.php`** — set `$GA4_ID` to your real `G-XXXXXXXXXX`, and `$APP_BASE` to your live HTTPS URL.
2. **`demo/robots.txt`** — update the `Sitemap:` line to your live URL.
3. Upload the Search Console `google<...>.html` verification file to the **site root**.
4. Put your keywords into product **titles/descriptions** (that's product **data** in the DB, not code) —
   they flow into the SEO tags automatically.

That's it. The gtag snippet, the `purchase` event, the sitemap, and all the SEO/OG/JSON-LD markup are
already in the code and switch on the moment `$GA4_ID` and `$APP_BASE` are set.

## Optional / advanced — Meta (Facebook/Instagram) Pixel

Not shipped in the code. If you want Meta conversion tracking, it mirrors the GA4 pattern in three spots:
add a `$META_PIXEL_ID` guard to `config.php`, put the Pixel base snippet in `layout/header.php` next to the
gtag block, and add one `fbq('track','Purchase', …)` line in `order_success.php` beside the GA4 purchase
event. See `MARKETING_GUIDE.md` §4 "Live option — Meta Ads Manager".

---

**Related docs:** `../MARKETING_GUIDE.md` (full how-to) · `../MARKETING_SAMPLES.md` (deliverable templates) ·
`../IT247_Marketing_Viva_Answers.md` (worked viva answers).
