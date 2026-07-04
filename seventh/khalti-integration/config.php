<?php
/**
 * config.php — your Khalti settings. This is the only file you edit.
 *
 * Get a TEST secret key: https://test-admin.khalti.com  (log in → your merchant →
 * Settings → Keys → copy the "Secret Key", looks like `live_secret_key_xxxxxxxx`).
 * The word "live" in the test key name is normal — it's still a sandbox key.
 */

return [
    // Paste your Khalti SECRET key here (server-side only — do NOT put it in JavaScript/HTML).
    'secret_key' => 'PASTE_YOUR_KHALTI_SECRET_KEY_HERE',

    // true  = sandbox / testing (no real money) — use this for the lab.
    // false = live (real money) — only when you go to production with a live key.
    'sandbox'    => true,

    // Where Khalti sends the user back after payment. Must be a URL on YOUR site.
    // Change the host to match where you run this (localhost / your domain).
    'return_url'  => 'http://localhost/khalti-integration/verify.php',
    'website_url' => 'http://localhost/khalti-integration/',
];
