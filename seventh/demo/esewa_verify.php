<?php
// esewa_verify.php — eSewa redirects here after payment (success_url).
// We verify the signed 'data' on the server before marking the order paid.
include 'base/connect.php';
include 'base/functions.php';
require_once 'base/payment.php';

if (!isLoggedIn()) {
    redirect('login.php');
}

$user   = currentUser();
$data   = $_GET['data'] ?? '';
$reason = 'Payment was not completed.';

if ($data !== '') {
    $resp = esewa_verify_data($data);   // null if the signature doesn't check out

    if ($resp && ($resp['status'] ?? '') === 'COMPLETE') {
        $uuid = $resp['transaction_uuid'] ?? '';
        $pay  = payment_find_by_uuid($pdo, $uuid);   // our recorded attempt -> the order
        if ($pay) {
            finalize_paid_order($pdo, (int)$pay['order_id'], $user['id'], $uuid, $resp['transaction_code'] ?? '');
            redirect('order_success.php?order=' . (int)$pay['order_id']);
        }
    }
    $reason = 'eSewa verification failed or the payment was not completed.';
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
    <p class="mb-0"><?= htmlspecialchars($reason) ?></p>
  </div>
  <p>Your order is saved as <strong>pending</strong>. You can try again from your cart.</p>
  <a href="cart.php" class="btn btn-dark">Back to Cart</a>
  <a href="orders.php" class="btn btn-outline-dark">My Orders</a>
</main>

<?php include 'layout/footer.php'; ?>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
