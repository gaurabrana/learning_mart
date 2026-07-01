<?php
// Category listing — from the database using PDO.
include 'base/connect.php';

$categories = $pdo->query("SELECT * FROM categories ORDER BY name")->fetchAll();
?>
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Categories - LearningMart</title>
  <link href="assets/css/style.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
</head>

<body class="d-flex flex-column min-vh-100">

<?php include 'layout/header.php'; ?>

<main class="container py-4 flex-grow-1">

  <h1 class="mb-4">Categories</h1>

  <div class="row g-4">
    <?php foreach ($categories as $c): ?>
      <div class="col-6 col-md-3">
        <a href="product.php?cat=<?= (int)$c['id'] ?>" class="text-decoration-none text-dark">
          <div class="card border-0 shadow-sm p-3 category-card h-100">
            <div class="fs-1 mb-2">📦</div>
            <h5><?= htmlspecialchars($c['name']) ?></h5>
            <p class="text-muted small mb-0"><?= htmlspecialchars($c['description']) ?></p>
          </div>
        </a>
      </div>
    <?php endforeach; ?>
  </div>

</main>

<?php include 'layout/footer.php'; ?>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
<script src="assets/js/script.js"></script>
</body>
</html>
