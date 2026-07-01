# Deploying LearningMart to InfinityFree (free PHP + MySQL host)

Develop on XAMPP/MAMP; deploy once to a public host so the marketing tools (Search Console, Google Ads,
live GA4) have a real URL. Netlify **cannot** run this — it's static only. InfinityFree runs PHP + MySQL
free with HTTPS. (Alternatives: 000webhost, AwardSpace.)

> **Good news:** all deploy settings now live in **`config.php`** — you don't edit `connect.php` anymore.

## Steps

1. **Sign up** at [infinityfree.com](https://infinityfree.com) → create a site. You get a free subdomain
   like `https://learningmart.infinityfreeapp.com`.

2. **Create a MySQL database** (control panel → *MySQL Databases*). Note the four values it gives you:
   **DB host** (e.g. `sqlXXX.infinityfree.com`), **DB name** (e.g. `epiz_1234_demo`),
   **DB user**, **DB password**.

3. **Import the schema.** Open the host's **phpMyAdmin** → select your database → **Import** →
   upload `database/schema.sql`.
   > ⚠️ First delete the top two lines `CREATE DATABASE IF NOT EXISTS demo;` and `USE demo;` — on shared
   > hosting you import into the database the host already created for you. Keep everything else.

4. **Upload the files.** File Manager (or FTP) → put all `demo/` files into **`htdocs/`**.

5. **Edit `config.php`** — this is the only file you change for production:
   ```php
   $APP_BASE = 'https://learningmart.infinityfreeapp.com';   // your live URL, no trailing slash

   $DB = [                                   // from step 2
       'host' => 'sqlXXX.infinityfree.com',
       'port' => 3306,
       'name' => 'epiz_1234_demo',
       'user' => 'epiz_1234',
       'pass' => 'your-db-password',
   ];

   // optional: your real Khalti test key, and GA4 id
   $KHALTI['secret_key'] = 'your_khalti_test_secret';
   $GA4_ID = 'G-XXXXXXXXXX';
   ```

6. **Update `robots.txt`** — change the `Sitemap:` line to your live URL
   (`https://learningmart.infinityfreeapp.com/sitemap.php`). On a real domain, `robots.txt` and the Search
   Console verification file belong at the **domain root**.

7. **Open the live URL**, confirm the **HTTPS padlock**, and test: browse → register → cart → checkout.

## Known limits of free hosting (tell students)
- HTTPS/SSL may take a few minutes to activate after first deploy.
- Some free hosts **block outbound requests** (the cURL call to Khalti/eSewa verification). If a live
  payment fails for that reason, demo the payment on XAMPP/MAMP and use the live site for browse + SEO +
  analytics. This is a hosting limit, not a code bug.
- Free hosts can be slow / throttle new accounts — retry if a deploy stalls.
