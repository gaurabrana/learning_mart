# LearningMart — E-Commerce Demo (PHP + MySQL + PDO)

The reference store for **IT 247**. All teaching material (guides, lab questions, marketing, deployment)
is in **[`../docs`](../docs)** — start at [`../docs/README.md`](../docs/README.md).

## Run it locally
1. Start **XAMPP** or **MAMP** (Apache + MySQL).
2. In phpMyAdmin, **import `database/schema.sql`** (creates the `demo` database + 15 sample products).
3. Open **`http://localhost/demo/`** (XAMPP) or **`http://localhost:8888/demo/`** (MAMP).

`base/connect.php` auto-detects XAMPP (root / empty pass) vs MAMP (root / `root`). For hosting and all
production settings, see [`../docs/DEPLOY.md`](../docs/DEPLOY.md) — you only edit `config.php`.

## What's inside
| Area | Files |
|------|-------|
| Catalog | `index.php`, `product.php`, `product_detail.php`, `category.php` |
| Auth | `register.php`, `login.php`, `logout.php` |
| Cart | `cart.php` (+ cart helpers in `base/functions.php`) — persistent for logged-in users |
| Checkout / payment | `checkout.php`, `pay.php`, `payment_verify.php`, `esewa_verify.php`, `order_success.php`, `orders.php` |
| Payment layer | `base/payment.php`, `base/khalti.php`, `base/esewa.php` |
| Shared | `base/connect.php`, `base/functions.php`, `layout/header.php`, `layout/footer.php` |
| SEO | `sitemap.php`, `robots.txt`, meta/OG/JSON-LD in the pages |
| Config | `config.php` — DB, payment keys, GA4 id, base URL |
| Database | `database/schema.sql` — tables + seed data |

## Payment sandboxes
- **eSewa** works out of the box (public test creds in `config.php`).
- **Khalti** needs a test key from test-admin.khalti.com in `config.php`.

Test-login credentials and the full teaching flow are in [`../docs/IT247_Teaching_Plan.md`](../docs/IT247_Teaching_Plan.md).
