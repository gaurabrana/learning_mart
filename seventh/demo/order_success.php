<?php
// Order confirmation — shows one order that belongs to the logged-in user.
include 'base/connect.php';
include 'base/functions.php';

if (!isLoggedIn()) {
    redirect('login.php');
}

$user    = currentUser();
$orderId = (int) ($_GET['order'] ?? 0);

$stmt = $pdo->prepare("SELECT * FROM orders WHERE id = ? AND user_id = ?");
$stmt->execute([$orderId, $user['id']]);
$order = $stmt->fetch();

if (!$order) {
    http_response_code(404);
    $orderMissing = true;
} else {
    $itemsStmt = $pdo->prepare(
        "SELECT oi.quantity, oi.price_at_purchase, p.title
         FROM order_items oi JOIN products p ON oi.product_id = p.id
         WHERE oi.order_id = ?"
    );
    $itemsStmt->execute([$orderId]);
    $items = $itemsStmt->fetchAll();

    // The successful payment for this order (if any).
    $payStmt = $pdo->prepare(
        "SELECT gateway, gateway_ref FROM payments WHERE order_id = ? AND status='paid' ORDER BY id DESC LIMIT 1"
    );
    $payStmt->execute([$orderId]);
    $payment = $payStmt->fetch();
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Order Confirmation - LearningMart</title>
  <link href="assets/css/style.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="d-flex flex-column min-vh-100">

<?php include 'layout/header.php'; ?>

<main class="container py-4 flex-grow-1" style="max-width:720px">

  <?php if (!empty($orderMissing)): ?>
    <div class="alert alert-danger">Order not found.</div>
    <a href="product.php" class="btn btn-dark">Continue shopping</a>
  <?php else: ?>
    <div class="alert alert-success">
      <h4 class="alert-heading">Thank you! Order #<?= (int)$order['id'] ?> placed.</h4>
      <p class="mb-0">Status: <strong><?= htmlspecialchars($order['status']) ?></strong>
        <?php if ($payment): ?>
          · Paid via <?= htmlspecialchars(ucfirst($payment['gateway'])) ?><?php if ($payment['gateway_ref']): ?> (ref: <?= htmlspecialchars($payment['gateway_ref']) ?>)<?php endif; ?>
        <?php endif; ?>
      </p>
    </div>

    <table class="table">
      <thead><tr><th>Product</th><th>Qty</th><th class="text-end">Price</th></tr></thead>
      <tbody>
        <?php foreach ($items as $it): ?>
          <tr>
            <td><?= htmlspecialchars($it['title']) ?></td>
            <td><?= (int)$it['quantity'] ?></td>
            <td class="text-end">Rs. <?= number_format($it['price_at_purchase'] * $it['quantity']) ?></td>
          </tr>
        <?php endforeach; ?>
        <tr class="fw-bold"><td colspan="2">Total</td><td class="text-end">Rs. <?= number_format($order['total']) ?></td></tr>
      </tbody>
    </table>

    <p class="text-muted">
      Ship to: <?= htmlspecialchars($order['shipping_name']) ?>,
      <?= htmlspecialchars($order['shipping_address']) ?> (<?= htmlspecialchars($order['shipping_phone']) ?>)
    </p>

    <a href="product.php" class="btn btn-dark">Continue shopping</a>
    <a href="orders.php" class="btn btn-outline-dark">My Orders</a>
  <?php endif; ?>

</main>

<?php include 'layout/footer.php'; ?>

<?php // GA4 e-commerce: record the purchase (only when GA4 is on and the order is actually paid).
if (!empty($GA4_ID) && !empty($payment) && !empty($order) && !empty($items)): ?>
<script>
  gtag('event', 'purchase', {
    transaction_id: '<?= (int)$order['id'] ?>',
    value: <?= (float)$order['total'] ?>,
    currency: 'NPR',
    items: [
      <?php foreach ($items as $it): ?>
      { item_name: <?= json_encode($it['title']) ?>, price: <?= (float)$it['price_at_purchase'] ?>, quantity: <?= (int)$it['quantity'] ?> },
      <?php endforeach; ?>
    ]
  });
</script>
<?php endif; ?>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
