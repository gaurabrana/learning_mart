<?php
// Home page — now loads categories and products from the database (PDO).
include 'base/connect.php';

$categories = $pdo->query("SELECT * FROM categories ORDER BY name")->fetchAll();
$products   = $pdo->query("SELECT p.*, c.name AS category_name
                           FROM products p
                           JOIN categories c ON p.category_id = c.id
                           ORDER BY p.created_at DESC, p.id DESC
                           LIMIT 8")->fetchAll();
?>
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LearningMart - Buy Gadgets, Electronics & Accessories Online in Nepal</title>
  <meta name="description" content="Shop smart gadgets, laptops, audio, wearables and accessories at LearningMart — fast delivery across Nepal, pay with Khalti or eSewa.">

  <link href="assets/css/style.css" type="text/css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
</head>

<body class="d-flex flex-column min-vh-100">
  <?php include 'layout/header.php'; ?>

  <main class="container py-4 flex-grow-1">

    <!-- Hero -->
    <section class="hero-section glass rounded-4 overflow-hidden p-5 text-white">
      <div class="row align-items-center">
        <div class="col-lg-6">
          <span class="badge bg-warning text-dark mb-3">Big Sale — Up To 50% OFF</span>
          <h1 class="display-4 fw-bold mb-3">Discover Premium Tech Products</h1>
          <p class="lead text-light mb-4">Shop smart gadgets, accessories, electronics and more.</p>
          <div class="d-flex gap-3">
            <a href="product.php" class="btn btn-light btn-lg px-4">Shop Now</a>
            <a href="category.php" class="btn btn-outline-light btn-lg px-4">Browse Categories</a>
          </div>
        </div>
        <div class="col-lg-6 text-center mt-4 mt-lg-0">
          <img src="https://images.unsplash.com/photo-1498049794561-7780e7231661?w=900"
               class="img-fluid rounded-4 shadow-lg" alt="Hero Banner">
        </div>
      </div>
    </section>

    <!-- Categories (from DB) -->
    <section class="mt-4">
      <div class="d-flex align-items-center justify-content-between mb-3">
        <h2 class="h4 mb-0">Shop by Category</h2>
        <a href="category.php" class="small">View all</a>
      </div>
      <div class="row g-3">
        <?php foreach ($categories as $c): ?>
          <div class="col-6 col-md-3">
            <a href="product.php?cat=<?= (int)$c['id'] ?>" class="text-decoration-none text-dark">
              <div class="card border-0 shadow-sm h-100 category-card">
                <div class="card-body">
                  <div class="fs-3">📦</div>
                  <h5 class="mt-2"><?= htmlspecialchars($c['name']) ?></h5>
                  <p class="text-muted small mb-0"><?= htmlspecialchars($c['description']) ?></p>
                </div>
              </div>
            </a>
          </div>
        <?php endforeach; ?>
      </div>
    </section>

    <!-- Featured products (from DB) -->
    <section class="mt-4 pb-4">
      <div class="d-flex align-items-center justify-content-between mb-3">
        <h2 class="h4 mb-0">Featured Products</h2>
        <a href="product.php" class="small">See all products</a>
      </div>

      <?php if (!$products): ?>
        <div class="alert alert-info">No products yet. Add some in phpMyAdmin (table <code>products</code>).</div>
      <?php else: ?>
        <div class="row g-3">
          <?php foreach ($products as $p):
            $img = $p['image'] ? 'uploads/' . $p['image'] : 'https://placehold.co/600x400?text=Product';
          ?>
            <div class="col-6 col-md-3">
              <div class="card product-card border-0 shadow-sm h-100">
                <img src="<?= htmlspecialchars($img) ?>" class="product-image w-100" alt="">
                <div class="card-body">
                  <span class="badge text-bg-primary mb-2"><?= htmlspecialchars($p['category_name']) ?></span>
                  <h6 class="fw-bold"><?= htmlspecialchars($p['title']) ?></h6>
                  <div class="fw-bold mt-1">Rs. <?= number_format($p['price']) ?></div>
                  <div class="mt-3 d-grid gap-2">
                    <a href="product_detail.php?id=<?= (int)$p['id'] ?>" class="btn btn-outline-dark btn-sm">View</a>
                    <a href="cart.php?action=add&id=<?= (int)$p['id'] ?>" class="btn btn-dark btn-sm">Add to Cart</a>
                  </div>
                </div>
              </div>
            </div>
          <?php endforeach; ?>
        </div>
      <?php endif; ?>
    </section>
  </main>

  <?php include 'layout/footer.php'; ?>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
  <script src="assets/js/script.js"></script>
</body>

</html>
