<?php
// payment_verify.php — Khalti redirects here after payment.
// We look up the payment we recorded, VERIFY with Khalti on the server, then finalize the order.
include 'base/connect.php';
include 'base/functions.php';
require_once 'base/payment.php';

if (!isLoggedIn()) {
    redirect('login.php');
}

$user   = currentUser();
$pidx   = $_GET['pidx'] ?? '';
$reason = 'Payment was not completed.';

if ($pidx !== '') {
    $look = khalti_lookup($pidx);                // ask Khalti to confirm the payment
    $pay  = payment_find_by_uuid($pdo, $pidx);   // the attempt we recorded -> tells us the order

    if ($pay && ($look['status'] ?? '') === 'Completed') {
        finalize_paid_order($pdo, (int)$pay['order_id'], $user['id'], $pidx, $look['transaction_id'] ?? $pidx);
        redirect('order_success.php?order=' . (int)$pay['order_id']);
    }
    $reason = 'Khalti status: ' . htmlspecialchars($look['status'] ?? ($look['_error'] ?? 'unknown'));
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Payment - LearningMart</title>
  <link href="assets/css/style.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="d-flex flex-column min-vh-100">

<?php include 'layout/header.php'; ?>

<main class="container py-5 flex-grow-1" style="max-width:640px">
  <div class="alert alert-danger">
    <h4 class="alert-heading">Payment not confirmed</h4>
    <p class="mb-0"><?= $reason ?></p>
  </div>
  <p>Your order is saved as <strong>pending</strong>. You can pay it anytime from your orders.</p>
  <a href="orders.php" class="btn btn-dark">My Orders</a>
  <a href="product.php" class="btn btn-outline-dark">Continue shopping</a>
</main>

<?php include 'layout/footer.php'; ?>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
