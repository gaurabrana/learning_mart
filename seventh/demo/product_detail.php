<?php
include 'base/connect.php';

$id = $_GET['id'] ?? null;

if (!$id) {
    die("Product not found");
}

$stmt = $pdo->prepare("
    SELECT 
        products.*,
        categories.name AS category_name
    FROM products
    LEFT JOIN categories
    ON products.category_id = categories.id
    WHERE products.id = ?
");

$stmt->execute([$id]);
$product = $stmt->fetch(PDO::FETCH_ASSOC);

if (!$product) {
    die("Product not found");
}

$image = $product['image']
    ? 'uploads/' . $product['image']
    : 'https://placehold.co/600x400';

// Related products from the same category (exclude this one).
$relStmt = $pdo->prepare(
    "SELECT id, title, price, image FROM products WHERE category_id = ? AND id <> ? ORDER BY id DESC LIMIT 4"
);
$relStmt->execute([$product['category_id'], $product['id']]);
$related = $relStmt->fetchAll();

// SEO / social values for this product.
require_once __DIR__ . '/config.php';                       // $APP_BASE
$ogImage  = $product['image'] ? $APP_BASE . '/uploads/' . $product['image'] : 'https://placehold.co/600x400';
$metaDesc = trim(mb_substr((string)$product['description'], 0, 150));
$pageUrl  = $APP_BASE . '/product_detail.php?id=' . (int)$product['id'];
?>

<!DOCTYPE html>
<html>
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

  <link href="assets/css/style.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
</head>

<body class="d-flex flex-column min-vh-100">

<?php include 'layout/header.php'; ?>

<main class="container py-4 flex-grow-1">

  <div class="row g-4">

    <div class="col-md-6">
      <img src="<?= $image ?>" class="img-fluid rounded shadow">
    </div>

    <div class="col-md-6">

      <span class="badge bg-primary mb-2">
        <?= htmlspecialchars($product['category_name']) ?>
      </span>

      <h2 class="fw-bold">
        <?= htmlspecialchars($product['title']) ?>
      </h2>

      <p class="text-muted">
        <?= htmlspecialchars($product['description']) ?>
      </p>

      <h4 class="text-dark mb-2">
        Rs. <?= number_format($product['price']) ?>
      </h4>

      <p class="mb-4">
        <?php if ((int)$product['stock'] > 0): ?>
          <span class="badge bg-success">In stock: <?= (int)$product['stock'] ?></span>
        <?php else: ?>
          <span class="badge bg-secondary">Out of stock</span>
        <?php endif; ?>
      </p>

      <?php if ((int)$product['stock'] > 0): ?>
        <form method="get" action="cart.php" class="d-flex gap-2" style="max-width:300px">
          <input type="hidden" name="action" value="add">
          <input type="hidden" name="id" value="<?= (int)$product['id'] ?>">
          <input type="number" name="qty" value="1" min="1" max="<?= (int)$product['stock'] ?>"
                 class="form-control" style="max-width:90px" aria-label="Quantity">
          <button class="btn btn-dark btn-lg flex-grow-1" type="submit">Add to Cart</button>
        </form>
      <?php else: ?>
        <button class="btn btn-secondary btn-lg w-100" disabled>Out of Stock</button>
      <?php endif; ?>

    </div>

  </div>

  <?php if ($related): ?>
    <hr class="my-5">
    <h4 class="mb-3">Related products</h4>
    <div class="row g-3">
      <?php foreach ($related as $r):
        $rImg = $r['image'] ? 'uploads/' . $r['image'] : 'https://placehold.co/600x400?text=Product';
      ?>
        <div class="col-6 col-md-3">
          <div class="card product-card border-0 shadow-sm h-100">
            <img src="<?= htmlspecialchars($rImg) ?>" class="product-image w-100" alt="">
            <div class="card-body">
              <h6 class="fw-bold"><?= htmlspecialchars($r['title']) ?></h6>
              <div class="fw-bold mt-1">Rs. <?= number_format($r['price']) ?></div>
              <a href="product_detail.php?id=<?= (int)$r['id'] ?>" class="btn btn-outline-dark btn-sm mt-2 w-100">View</a>
            </div>
          </div>
        </div>
      <?php endforeach; ?>
    </div>
  <?php endif; ?>

</main>

<?php include 'layout/footer.php'; ?>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
<script src="assets/js/script.js"></script>
</body>
</html>