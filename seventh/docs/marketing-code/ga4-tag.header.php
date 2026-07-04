<?php
// ─────────────────────────────────────────────────────────────────────────────
// EXTRACT (not a standalone file). This is the GA4 tracking tag that loads on
// EVERY page, because it lives in the shared header include.
//
// Real location:  demo/layout/header.php   (lines 12–23)
// Turned on by:   $GA4_ID in config.php (see config.marketing.php)
//
// How it works: if $GA4_ID is set, this prints the standard Google gtag.js snippet
// into the <head> of every page (header.php is included by all pages). That single
// snippet is what makes page_view / users / source-medium / Realtime work.
// If $GA4_ID is empty, nothing is printed — analytics is simply off.
// ─────────────────────────────────────────────────────────────────────────────
?>
<?php
// Google Analytics 4 (Session 5): enabled site-wide when $GA4_ID is set in config.php.
// (Search Console: for a PHP site, verify with the HTML-FILE method — upload google<...>.html to the site root.)
if (!empty($GA4_ID)): ?>
<script async src="https://www.googletagmanager.com/gtag/js?id=<?= htmlspecialchars($GA4_ID) ?>"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', '<?= htmlspecialchars($GA4_ID) ?>');
</script>
<?php endif; ?>
