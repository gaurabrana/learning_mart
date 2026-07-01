<?php
// config.php — app + payment settings.
// Get TEST keys from your Khalti test/merchant account (see docs.khalti.com).
// NEVER put a live secret key in a teaching project.

// Base URL of your app (used to build the payment return URLs). No trailing slash.
//   XAMPP: http://localhost/demo
//   MAMP:  http://localhost:8888/demo
// Change to your live https URL after you deploy.
$APP_BASE = 'http://localhost:8888/demo';

// Google Analytics 4 (Session 5): set your Measurement ID (e.g. 'G-XXXXXXXXXX') to enable
// site-wide tracking. Leave empty to turn analytics off.
$GA4_ID = '';

// Database connection.
// Local dev: leave $DB = null — base/connect.php auto-detects XAMPP (root / empty) and MAMP (root / 'root').
// Production (e.g. InfinityFree): fill in your host's MySQL details from its control panel:
//   $DB = ['host' => 'sqlXXX.infinityfree.com', 'port' => 3306,
//          'name' => 'epiz_XXXXXXXX_demo', 'user' => 'epiz_XXXXXXXX', 'pass' => 'your-db-password'];
$DB = null;

$KHALTI = [
    // SANDBOX base (dev.khalti.com). Production is a.khalti.com — using it with a test key = "Invalid token".
    'base'        => 'https://dev.khalti.com/api/v2/epayment/',
    // Your test secret key from test-admin.khalti.com (shown there as live_secret_key_xxxxxxxx).
    'secret_key'  => 'e12b594356eb4969afd07b288f9a8c03',
    'return_url'  => $APP_BASE . '/payment_verify.php',
    'website_url' => $APP_BASE . '/',
];

// eSewa ePay v2 SANDBOX — these test values are public/documented (sandbox only, no real money).
// Confirm the current test values/endpoints at developer.esewa.com.np if payments stop working.
$ESEWA = [
    'product_code' => 'EPAYTEST',                                          // test merchant code
    'secret'       => '8gBm/:&EnhH.1/q',                                   // test signing secret
    'form_url'     => 'https://rc-epay.esewa.com.np/api/epay/main/v2/form', // rc = sandbox
    'status_url'   => 'https://rc.esewa.com.np/api/epay/transaction/status/',
    'success_url'  => $APP_BASE . '/esewa_verify.php',
    'failure_url'  => $APP_BASE . '/checkout.php?pay=failed',
];
