<?php
// ─────────────────────────────────────────────────────────────────────────────
// EXTRACT (not a standalone file). These are the marketing-relevant settings that
// live inside the real  demo/config.php.  Everything marketing "turns on" from here.
//
// Real location:  demo/config.php   (lines 10 and 14)
// ─────────────────────────────────────────────────────────────────────────────

// Base URL of the site, no trailing slash. Used to build sitemap URLs, canonical
// URLs, Open Graph URLs, and payment return URLs.
//   Local:  http://localhost:8888/demo
//   Live:   https://your-store.example.com   ← set this after you deploy
$APP_BASE = 'http://localhost:8888/demo';

// Google Analytics 4 Measurement ID. LEAVE EMPTY to keep analytics OFF.
// Set it to your real 'G-XXXXXXXXXX' and the gtag snippet (see ga4-tag.header.php)
// renders on every page automatically — nothing else to wire up.
$GA4_ID = '';

// (Optional / advanced) Meta Pixel — NOT in the shipped code. If a student wants
// Facebook/Instagram conversion tracking, add a variable like this and guard the
// pixel snippet with it, exactly like $GA4_ID guards the GA4 snippet:
// $META_PIXEL_ID = '';
