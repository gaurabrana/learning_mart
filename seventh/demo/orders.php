<?php
// My Orders — lists the logged-in user's orders.
include 'base/connect.php';
include 'base/functions.php';

if (!isLoggedIn()) {
    redirect('login.php');
}

$user = currentUser();
$stmt = $pdo->prepare("SELECT * FROM orders WHERE user_id = ? ORDER BY created_at DESC, id DESC");
$stmt->execute([$user['id']]);
$orders = $stmt->fetchAll();
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Orders - LearningMart</title>
  <link href="assets/css/style.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="d-flex flex-column min-vh-100">

<?php include 'layout/header.php'; ?>

<main class="container py-4 flex-grow-1">

  <h2 class="mb-4">My Orders</h2>

  <?php if (!$orders): ?>
    <div class="alert alert-info">You have no orders yet. <a href="product.php">Start shopping</a>.</div>
  <?php else: ?>
    <div class="table-responsive">
      <table class="table align-middle">
        <thead><tr><th>Order #</th><th>Date</th><th>Total</th><th>Status</th><th></th></tr></thead>
        <tbody>
          <?php foreach ($orders as $o): ?>
            <tr>
              <td>#<?= (int)$o['id'] ?></td>
              <td><?= htmlspecialchars(date('Y-m-d', strtotime($o['created_at']))) ?></td>
              <td>Rs. <?= number_format($o['total']) ?></td>
              <td>
                <span class="badge bg-<?= $o['status'] === 'paid' ? 'success' : 'secondary' ?>">
                  <?= htmlspecialchars($o['status']) ?>
                </span>
              </td>
              <td>
                <a href="order_success.php?order=<?= (int)$o['id'] ?>" class="btn btn-sm btn-outline-dark">View</a>
                <?php if ($o['status'] !== 'paid'): ?>
                  <a href="pay.php?order=<?= (int)$o['id'] ?>" class="btn btn-sm btn-success">Pay now</a>
                <?php endif; ?>
              </td>
            </tr>
          <?php endforeach; ?>
        </tbody>
      </table>
    </div>
  <?php endif; ?>

</main>

<?php include 'layout/footer.php'; ?>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
