<?php
// ─────────────────────────────────────────────────────────────────────────────
// EXTRACT (not a standalone file). This is the on-page SEO + social + rich-result
// markup that goes in the <head> of each product page.
//
// Real location:  demo/product_detail.php   (variables at lines 40–42, <head> at 47–83)
// Depends on:     $APP_BASE (config.php) + $product (row from the DB).
//
// What each block does:
//   • <title> + <meta description>  → the text Google shows in search results.
//   • <link rel="canonical">        → tells Google the one true URL (avoids dupes).
//   • Open Graph (og:*)             → the image/title/desc shown when the link is
//                                     shared on Facebook/Instagram/WhatsApp (and in
//                                     Meta ads). VERIFIED readable by Meta's crawler.
//   • JSON-LD Product schema        → lets Google show price/stock rich results.
// Put your keyword-rich text into the product title/description (in the DB) and it
// flows into all of these automatically.
// ─────────────────────────────────────────────────────────────────────────────

// --- values built before <head> (product_detail.php lines 40–42) ---
$ogImage  = $product['image'] ? $APP_BASE . '/uploads/' . $product['image'] : 'https://placehold.co/600x400';
$metaDesc = trim(mb_substr((string)$product['description'], 0, 150));
$pageUrl  = $APP_BASE . '/product_detail.php?id=' . (int)$product['id'];
?>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title><?= htmlspecialchars($product['title']) ?> - LearningMart</title>

  <!-- On-page SEO -->
  <meta name="description" content="<?= htmlspecialchars($metaDesc) ?>">
  <link rel="canonical" href="<?= htmlspecialchars($pageUrl) ?>">

  <!-- Open Graph — controls how the product looks when shared on social media -->
  <meta property="og:type" content="product">
  <meta property="og:title" content="<?= htmlspecialchars($product['title']) ?>">
  <meta property="og:description" content="<?= htmlspecialchars($metaDesc) ?>">
  <meta property="og:image" content="<?= htmlspecialchars($ogImage) ?>">
  <meta property="og:url" content="<?= htmlspecialchars($pageUrl) ?>">

  <!-- Structured data (schema.org Product) — helps Google show rich results -->
  <script type="application/ld+json">
  <?= json_encode([
      '@context'    => 'https://schema.org',
      '@type'       => 'Product',
      'name'        => $product['title'],
      'description' => $metaDesc,
      'image'       => $ogImage,
      'offers'      => [
          '@type'         => 'Offer',
          'price'         => (string)$product['price'],
          'priceCurrency' => 'NPR',
          'availability'  => ((int)$product['stock'] > 0)
              ? 'https://schema.org/InStock' : 'https://schema.org/OutOfStock',
      ],
  ], JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT) ?>
  </script>
</head>
