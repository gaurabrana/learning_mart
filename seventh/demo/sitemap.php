<?php
// sitemap.php — a dynamic XML sitemap of every public page, for Google Search Console.
// Submit its URL in Search Console (e.g. http://localhost:8888/demo/sitemap.php, or your live URL).
require __DIR__ . '/base/connect.php';
require __DIR__ . '/config.php';

header('Content-Type: application/xml; charset=utf-8');

$urls = [
    $APP_BASE . '/',
    $APP_BASE . '/product.php',
    $APP_BASE . '/category.php',
];
foreach ($pdo->query("SELECT id FROM products")->fetchAll() as $p) {
    $urls[] = $APP_BASE . '/product_detail.php?id=' . $p['id'];
}

echo '<?xml version="1.0" encoding="UTF-8"?>' . "\n";
echo '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' . "\n";
foreach ($urls as $u) {
    echo '  <url><loc>' . htmlspecialchars($u) . '</loc></url>' . "\n";
}
echo '</urlset>' . "\n";
