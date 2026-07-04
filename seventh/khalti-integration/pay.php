<?php
/**
 * pay.php — start a Khalti payment for an existing PENDING order.
 *
 * This mirrors the course demo store, so it assumes the SAME setup you already have:
 *   - base/connect.php   → gives you $pdo (a PDO connection) and starts the session
 *   - base/functions.php → gives you isLoggedIn(), currentUser(), redirect()
 *   - an `orders` table with columns: id, user_id, total, status
 *
 * Copy khalti.php + config.php + this file into your store's web root (next to base/).
 * If your folders differ, adjust the two include paths below.
 */
require_once __DIR__ . '/khalti.php';
$config = require __DIR__ . '/config.php';

include 'base/connect.php';     // your project — provides $pdo (and session_start)
include 'base/functions.php';   // your project — isLoggedIn(), currentUser(), redirect()

$khalti = new Khalti($config['secret_key'], $config['sandbox']);

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
    redirect('verify.php?order=' . $orderId);   // already paid
}

$error = null;
if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    $resp = $khalti->initiate([
        'return_url'          => $config['return_url'],
        'website_url'         => $config['website_url'],
        'amount'              => Khalti::toPaisa($order['total']),   // rupees → paisa
        'purchase_order_id'   => (string) $orderId,
        'purchase_order_name' => 'Order #' . $orderId,
        'customer_info'       => ['name' => $user['name'], 'email' => $user['email']],
    ]);

    if (!empty($resp['payment_url'])) {
        // Remember what we charged so verify.php can reconcile it after the redirect.
        $_SESSION['khalti_expected_paisa'] = Khalti::toPaisa($order['total']);
        $_SESSION['khalti_order_id']       = $orderId;

        header('Location: ' . $resp['payment_url']);   // send the user to Khalti
        exit;
    }
    $error = 'Payment could not start: ' . ($resp['detail'] ?? $resp['_error'] ?? 'unknown error');
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pay for Order #<?= (int)$orderId ?></title>
  <style>
    body { font-family: system-ui, sans-serif; max-width: 460px; margin: 60px auto; padding: 0 16px; }
    .card { border: 1px solid #ddd; border-radius: 12px; padding: 24px; }
    .btn { background: #5c2d91; color: #fff; border: 0; padding: 12px 20px; border-radius: 8px;
           font-size: 16px; cursor: pointer; width: 100%; }
    .err { background: #fdecea; color: #b71c1c; padding: 12px; border-radius: 8px; margin-bottom: 16px; }
    .muted { color: #666; font-size: 14px; }
  </style>
</head>
<body>
  <div class="card">
    <h2>Pay for Order #<?= (int)$orderId ?></h2>
    <?php if ($error): ?>
      <div class="err"><?= htmlspecialchars($error) ?></div>
    <?php endif; ?>
    <p>Amount due: <strong>Rs. <?= number_format($order['total']) ?></strong></p>
    <form method="post" action="pay.php?order=<?= (int)$orderId ?>">
      <button class="btn" type="submit">Pay with Khalti</button>
    </form>
    <p class="muted" style="margin-top:16px">
      Sandbox test login → Khalti ID <code>9800000000</code>, MPIN <code>1111</code>, OTP <code>987654</code>.
    </p>
  </div>
</body>
</html>
