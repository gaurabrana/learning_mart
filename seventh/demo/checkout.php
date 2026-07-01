<?php
// Checkout — collects shipping details, saves the order (pending), then starts the chosen payment (Khalti/eSewa).
include 'base/connect.php';
include 'base/functions.php';
require_once 'base/payment.php';

// Checkout requires login (the cart itself does not).
if (!isLoggedIn()) {
    redirect('login.php');
}

$user  = currentUser();
$error = null;

// Shown when a gateway sends the user back after a cancelled/failed payment.
if (($_GET['pay'] ?? '') === 'failed') {
    $error = 'Payment was cancelled or failed. Your order was saved as pending — you can try again below.';
}

$cart  = cart_summary($pdo);
$items = $cart['items'];
$total = $cart['total'];

if ($_SERVER['REQUEST_METHOD'] === 'POST' && $items) {
    $name    = trim($_POST['name'] ?? '');
    $address = trim($_POST['address'] ?? '');
    $phone   = trim($_POST['phone'] ?? '');
    $method  = $_POST['method'] ?? 'khalti';

    if ($name === '' || $address === '' || $phone === '') {
        $error = 'Please fill in all shipping fields.';
    } else {
        // 1) Save the order (pending) and its items in ONE transaction.
        $pdo->beginTransaction();
        $pdo->prepare(
            "INSERT INTO orders (user_id, total, status, shipping_name, shipping_address, shipping_phone)
             VALUES (?, ?, 'pending', ?, ?, ?)"
        )->execute([$user['id'], $total, $name, $address, $phone]);
        $orderId = (int) $pdo->lastInsertId();

        $itemStmt = $pdo->prepare(
            "INSERT INTO order_items (order_id, product_id, quantity, price_at_purchase) VALUES (?, ?, ?, ?)"
        );
        foreach ($items as $it) {
            $itemStmt->execute([$orderId, $it['id'], $it['qty'], $it['price']]);
        }
        $pdo->commit();
        cart_clear($pdo);   // order placed — empty the cart

        // 2) Start the chosen payment (records a payments row, then hands off to the gateway).
        //    payment_start() redirects/exits on success; if it returns, it failed.
        $err = payment_start($pdo, [
            'id'    => $orderId,
            'total' => $total,
            'name'  => $user['name'],
            'email' => $user['email'],
        ], $method);

        $error = 'Order #' . $orderId . ' saved as pending, but payment could not start: ' . $err
               . ' You can pay it anytime from "My Orders".';
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Checkout - LearningMart</title>
  <link href="assets/css/style.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="d-flex flex-column min-vh-100">

<?php include 'layout/header.php'; ?>

<main class="container py-4 flex-grow-1" style="max-width:820px">

  <h2 class="mb-4">Checkout</h2>

  <?php if ($error): ?>
    <div class="alert alert-warning"><?= $error ?></div>
  <?php endif; ?>

  <?php if (!$items): ?>
    <div class="alert alert-info">Your cart is empty. <a href="product.php">Browse products</a>.</div>
  <?php else: ?>
    <div class="row g-4">

      <!-- Order summary -->
      <div class="col-md-5 order-md-2">
        <div class="card shadow-sm">
          <div class="card-body">
            <h5 class="card-title">Order Summary</h5>
            <ul class="list-group list-group-flush">
              <?php foreach ($items as $c): ?>
                <li class="list-group-item d-flex justify-content-between px-0">
                  <span><?= htmlspecialchars($c['title']) ?> × <?= (int)$c['qty'] ?></span>
                  <span>Rs. <?= number_format($c['subtotal']) ?></span>
                </li>
              <?php endforeach; ?>
              <li class="list-group-item d-flex justify-content-between px-0 fw-bold">
                <span>Total</span><span>Rs. <?= number_format($total) ?></span>
              </li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Shipping + payment form -->
      <div class="col-md-7 order-md-1">
        <form method="post" action="checkout.php" class="card shadow-sm">
          <div class="card-body">
            <h5 class="card-title mb-3">Shipping Details</h5>
            <div class="mb-3">
              <label class="form-label">Full name</label>
              <input class="form-control" name="name" value="<?= htmlspecialchars($user['name']) ?>" required>
            </div>
            <div class="mb-3">
              <label class="form-label">Delivery address</label>
              <input class="form-control" name="address" required>
            </div>
            <div class="mb-3">
              <label class="form-label">Phone</label>
              <input class="form-control" name="phone" required>
            </div>

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

            <button class="btn btn-success btn-lg w-100" type="submit">Place Order &amp; Pay</button>
          </div>
        </form>
      </div>

    </div>
  <?php endif; ?>

</main>

<?php include 'layout/footer.php'; ?>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
