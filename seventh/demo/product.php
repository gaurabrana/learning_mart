<?php
// Product listing — from the database using PDO prepared statements.
// Supports optional category filter (?cat=) and search (?q=).
include 'base/connect.php';

$cat = isset($_GET['cat']) ? (int)$_GET['cat'] : 0;
$q   = trim($_GET['q'] ?? '');

$sql = "SELECT p.id, p.title, p.description, p.price, p.image, c.name AS category_name
        FROM products p
        JOIN categories c ON p.category_id = c.id
        WHERE 1=1";
$params = [];

if ($cat > 0) {
    $sql .= " AND p.category_id = :cat";
    $params[':cat'] = $cat;
}
if ($q !== '') {
    $sql .= " AND (p.title LIKE :q OR p.description LIKE :q)";
    $params[':q'] = '%' . $q . '%';
}
$sort    = $_GET['sort'] ?? '';
$orderBy = match ($sort) {          // whitelist — never put user input directly in ORDER BY
    'price_asc'  => 'p.price ASC',
    'price_desc' => 'p.price DESC',
    default      => 'p.id DESC',
};
$sql .= " ORDER BY $orderBy";

$stmt = $pdo->prepare($sql);
$stmt->execute($params);
$products = $stmt->fetchAll();
?>
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Products - LearningMart</title>
  <link href="assets/css/style.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
</head>

<body class="d-flex flex-column min-vh-100">

<?php include 'layout/header.php'; ?>

<main class="container py-4 flex-grow-1">

  <div class="d-flex justify-content-between align-items-center mb-3">
    <h3 class="mb-0">
      Products
      <?php if ($q !== ''): ?>
        <small class="text-muted">— results for "<?= htmlspecialchars($q) ?>"</small>
      <?php endif; ?>
    </h3>
    <span class="text-muted small"><?= count($products) ?> item(s)</span>
  </div>

  <!-- Search + sort filter -->
  <form method="get" action="product.php" class="row g-2 align-items-center mb-4">
    <?php if ($cat > 0): ?><input type="hidden" name="cat" value="<?= (int)$cat ?>"><?php endif; ?>
    <div class="col-sm-6 col-md-5">
      <input type="search" name="q" value="<?= htmlspecialchars($q) ?>" class="form-control" placeholder="Search products…">
    </div>
    <div class="col-sm-4 col-md-4">
      <select name="sort" class="form-select">
        <option value="" <?= $sort === '' ? 'selected' : '' ?>>Latest</option>
        <option value="price_asc" <?= $sort === 'price_asc' ? 'selected' : '' ?>>Price: Low to High</option>
        <option value="price_desc" <?= $sort === 'price_desc' ? 'selected' : '' ?>>Price: High to Low</option>
      </select>
    </div>
    <div class="col-sm-2 col-md-3 d-grid">
      <button class="btn btn-primary" type="submit">Apply</button>
    </div>
  </form>

  <?php if (!$products): ?>
    <div class="alert alert-info">No products found. <a href="product.php">Show all products</a>.</div>
  <?php else: ?>
    <div class="row g-4">
      <?php foreach ($products as $p):
        $img = $p['image'] ? 'uploads/' . $p['image'] : 'https://placehold.co/600x400?text=Product';
      ?>
        <div class="col-md-6 col-xl-3">
          <div class="card product-card border-0 shadow-sm h-100">
            <img src="<?= htmlspecialchars($img) ?>" class="product-image w-100" alt="">
            <div class="card-body d-flex flex-column">
              <span class="badge bg-primary mb-2 align-self-start"><?= htmlspecialchars($p['category_name']) ?></span>
              <h5 class="fw-bold"><?= htmlspecialchars($p['title']) ?></h5>
              <p class="text-muted small flex-grow-1">
                <?= htmlspecialchars(substr($p['description'], 0, 70)) ?><?= strlen($p['description']) > 70 ? '…' : '' ?>
              </p>
              <div class="fw-bold mb-3">Rs. <?= number_format($p['price']) ?></div>
              <div class="d-grid gap-2">
                <a href="product_detail.php?id=<?= (int)$p['id'] ?>" class="btn btn-outline-dark">View Details</a>
                <a href="cart.php?action=add&id=<?= (int)$p['id'] ?>" class="btn btn-dark">Add to Cart</a>
              </div>
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
