<?php
// pay.php — pay for an existing PENDING order (reached from "Pay now" in My Orders).
include 'base/connect.php';
include 'base/functions.php';
require_once 'base/payment.php';

if (!isLoggedIn()) {
    redirect('login.php');
}

$user    = currentUser();
$orderId = (int) ($_GET['order'] ?? 0);

// The order must exist, belong to this user, and not already be paid.
$stmt = $pdo->prepare("SELECT * FROM orders WHERE id = ? AND user_id = ?");
$stmt->execute([$orderId, $user['id']]);
$order = $stmt->fetch();

if (!$order) {
    redirect('orders.php');
}
if ($order['status'] === 'paid') {
    redirect('order_success.php?order=' . $orderId);
}

$error = null;
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $method = $_POST['method'] ?? 'khalti';
    // payment_start() redirects/exits on success; if it returns, it failed.
    $err = payment_start($pdo, [
        'id'    => $orderId,
        'total' => $order['total'],
        'name'  => $user['name'],
        'email' => $user['email'],
    ], $method);
    $error = 'Payment could not start: ' . $err;
}

$itemsStmt = $pdo->prepare(
    "SELECT oi.quantity, oi.price_at_purchase, p.title
     FROM order_items oi JOIN products p ON oi.product_id = p.id
     WHERE oi.order_id = ?"
);
$itemsStmt->execute([$orderId]);
$items = $itemsStmt->fetchAll();
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pay for Order #<?= (int)$orderId ?> - LearningMart</title>
  <link href="assets/css/style.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="d-flex flex-column min-vh-100">

<?php include 'layout/header.php'; ?>

<main class="container py-4 flex-grow-1" style="max-width:600px">

  <h2 class="mb-4">Pay for Order #<?= (int)$orderId ?></h2>

  <?php if ($error): ?>
    <div class="alert alert-warning"><?= $error ?></div>
  <?php endif; ?>

  <ul class="list-group mb-3">
    <?php foreach ($items as $it): ?>
      <li class="list-group-item d-flex justify-content-between">
        <span><?= htmlspecialchars($it['title']) ?> × <?= (int)$it['quantity'] ?></span>
        <span>Rs. <?= number_format($it['price_at_purchase'] * $it['quantity']) ?></span>
      </li>
    <?php endforeach; ?>
    <li class="list-group-item d-flex justify-content-between fw-bold">
      <span>Total</span><span>Rs. <?= number_format($order['total']) ?></span>
    </li>
  </ul>

  <form method="post" action="pay.php?order=<?= (int)$orderId ?>">
    <label class="form-label d-block">Payment method</label>
    <div class="mb-3">
      <div class="form-check form-check-inline">
        <input class="form-check-input" type="radio" name="method" id="mKhalti" value="khalti" checked>
        <label class="form-check-label" for="mKhalti">Khalti</label>
      </div>
      <div class="form-check form-check-inline">
        <input class="form-check-input" type="radio" name="method" id="mEsewa" value="esewa">
        <label class="form-check-label" for="mEsewa">eSewa</label>
      </div>
    </div>
    <button class="btn btn-success btn-lg w-100" type="submit">Pay Now</button>
  </form>

</main>

<?php include 'layout/footer.php'; ?>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
