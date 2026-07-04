# Khalti Payment — drop-in module (PHP)

A tiny Khalti **e-Payment (KPG-2)** integration for PHP. The `Khalti` class itself is
**self-contained** — no database, no framework, no Composer, just PHP + cURL. The two example
pages (`pay.php`, `verify.php`) plug straight into a store like the course demo.

## What's in here
| File | What it is | Copy it? |
|------|-----------|----------|
| **`khalti.php`** | The `Khalti` class (initiate + verify). DB-free, reusable anywhere. **The core — always copy this.** | ✅ always |
| `config.php` | Your key + settings (the one file you edit) | ✅ (or inline the values) |
| `pay.php` | Template: fetch a pending order + start the payment | 📄 copy & adapt |
| `verify.php` | Template: the return page — verifies, then marks the order paid | 📄 copy & adapt |

> **`pay.php` / `verify.php` assume the same setup as the course demo store:** a `base/connect.php`
> that gives you `$pdo` (and starts the session), a `base/functions.php` with `isLoggedIn()` /
> `currentUser()` / `redirect()`, and an **`orders`** table (`id, user_id, total, status`). If your
> project differs, only the includes + the two SQL queries need editing — the Khalti calls stay the same.

## How Khalti works (the whole flow)
```
[your pay page]                 [Khalti]                    [your return_url]
   initiate()  ── amount ──►  gives payment_url  
   redirect user to payment_url ─────────────────►  user logs in & pays
                                                     redirects back with ?pidx=...
   lookup(pidx) ◄── "is it really paid?" ──────────  ✔ status = "Completed"
   → mark order paid
```
**Golden rule:** the redirect back is *not* proof of payment. Only trust `lookup($pidx)` returning
`status === 'Completed'` **and** the amount matching what you charged.

---

## Set it up in 3 steps
1. **Get a test key** — log in at **https://test-admin.khalti.com** → your merchant → **Settings → Keys**
   → copy the **Secret Key** (it looks like `live_secret_key_xxxx`; the word "live" in a test key is normal).
2. **Paste it** into `config.php` → `'secret_key'`. Leave `'sandbox' => true`. Set `return_url` to your
   `verify.php` URL and `website_url` to your site (e.g. `http://localhost/yourstore/verify.php`).
3. **Drop the files into your store** (next to `base/`), then — logged in, with a pending order — open
   `pay.php?order=<id>` and click **Pay with Khalti**. It redirects to Khalti; after paying you land on
   `verify.php`, which confirms the payment and flips the order to `paid`.

**Sandbox test login (on Khalti's payment page):**
- Khalti ID: `9800000000` (also `...001`–`...005`)  ·  MPIN: `1111`  ·  OTP: `987654`

---

## Integrate into YOUR project (3 things)
1. **Copy `khalti.php`** into your project and create the object with your key:
   ```php
   require_once 'khalti.php';
   $khalti = new Khalti('your_secret_key', true /* sandbox */);
   ```
2. **Start the payment** where your "Pay" button posts — build the params from *your* order, then redirect:
   ```php
   $resp = $khalti->initiate([
       'return_url'          => 'https://yoursite/verify.php',
       'website_url'         => 'https://yoursite/',
       'amount'              => Khalti::toPaisa($order['total']),   // rupees → paisa
       'purchase_order_id'   => (string) $order['id'],
       'purchase_order_name' => 'Order #' . $order['id'],
       'customer_info'       => ['name' => $user['name'], 'email' => $user['email']],
   ]);
   if (!empty($resp['payment_url'])) {
       $_SESSION['expected_paisa'] = Khalti::toPaisa($order['total']); // to check later
       header('Location: ' . $resp['payment_url']); exit;
   }
   // else: show $resp['detail'] ?? $resp['_error']
   ```
3. **Verify on your return page** (`return_url`) and update your DB:
   ```php
   $look = $khalti->lookup($_GET['pidx'] ?? '');
   $amountOk = (int)($look['total_amount'] ?? 0) === (int)($_SESSION['expected_paisa'] ?? -1);
   if (($look['status'] ?? '') === 'Completed' && $amountOk) {
       // mark the order paid — IDEMPOTENTLY (check it isn't already paid first)
   }
   ```

That's the whole integration. The `Khalti` class never touches your database — *you* decide what
"paid" means in your own tables.

---

## Response fields you'll use
- **`initiate()` success:** `pidx` (payment id — store it), `payment_url` (send the user here).
- **`lookup()`:** `status` (`Completed` = paid), `total_amount` (in paisa — verify it), `transaction_id`.
- **On error:** `detail` (Khalti's message, e.g. "Invalid token") or `_error` (network/cURL problem).

## Sandbox vs Live
| | Sandbox (testing) | Live (real money) |
|--|--|--|
| `new Khalti($key, $sandbox)` | `true` | `false` |
| Key from | test-admin.khalti.com | admin.khalti.com |
| Base URL (handled for you) | `dev.khalti.com` | `khalti.com` |

**Never mix them:** a test key on the live URL (or vice-versa) → `"Invalid token"`.

## Common errors
- **`Invalid token`** → wrong key ↔ environment. Test key needs `sandbox = true`; live key needs `false`.
- **`_error: Request to Khalti failed`** → your server can't make outbound requests. Many **free hosts
  block outbound cURL** — test on localhost/XAMPP, or use a host that allows it.
- **Amount looks 100× off** → Khalti uses **paisa**. Always send `Khalti::toPaisa($rupees)`.
- **Payment shows paid but order isn't** → you didn't call `lookup()` on the return page, or didn't
  update your DB there. The redirect alone never updates anything.

## Security notes (say these in your viva)
- The **secret key stays on the server** — never in JavaScript, HTML, or a public repo.
- **Always verify with `lookup()`** server-side before granting anything; don't trust the redirect URL.
- **Check the amount** (`total_amount`) matches what you charged.
- **Be idempotent** when marking paid — Khalti can hit your return_url more than once.
