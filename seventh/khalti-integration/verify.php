<?php
/**
 * verify.php — Khalti redirects here after payment (this is your return_url).
 *
 * Same setup assumptions as pay.php:
 *   - base/connect.php   → $pdo (and session_start)
 *   - base/functions.php → isLoggedIn(), currentUser(), redirect()
 *   - an `orders` table with columns: id, user_id, status
 *
 * Khalti appends ?pidx=...&status=... to the URL, but we IGNORE those for the
 * decision and ask Khalti directly via lookup() — the only trustworthy check.
 */
require_once __DIR__ . '/khalti.php';
$config = require __DIR__ . '/config.php';

include 'base/connect.php';     // your project — provides $pdo (and session_start)
include 'base/functions.php';   // your project — isLoggedIn(), currentUser(), redirect()

$khalti = new Khalti($config['secret_key'], $config['sandbox']);

if (!isLoggedIn()) {
    redirect('login.php');
}
$user = currentUser();

$pidx    = $_GET['pidx'] ?? '';
$paid    = false;
$message = 'No payment reference (pidx) found.';

if ($pidx !== '') {
    $look   = $khalti->lookup($pidx);          // SERVER-SIDE verification
    $status = $look['status'] ?? '';

    // Confirm the amount and order match what we started (guards against tampering).
    $expected = $_SESSION['khalti_expected_paisa'] ?? null;
    $amountOk = ($expected === null) || ((int)($look['total_amount'] ?? 0) === (int)$expected);
    $orderId  = (int) ($_SESSION['khalti_order_id'] ?? 0);

    if ($status === 'Completed' && $amountOk && $orderId) {
        // ✅ CONFIRMED — mark the order paid. IDEMPOTENT: only flip a still-pending
        // order, so a second redirect from Khalti can't double-process it.
        $upd = $pdo->prepare(
            "UPDATE orders SET status = 'paid' WHERE id = ? AND user_id = ? AND status <> 'paid'"
        );
        $upd->execute([$orderId, $user['id']]);

        $paid    = true;
        $txn     = $look['transaction_id'] ?? $pidx;
        $message = "Payment confirmed for order #$orderId. Transaction ID: $txn";
        unset($_SESSION['khalti_expected_paisa'], $_SESSION['khalti_order_id']);
    } elseif ($status === 'Completed' && !$amountOk) {
        $message = 'Amount mismatch — payment rejected.';
    } else {
        // Other statuses: Pending, Initiated, Refunded, Expired, User canceled, ...
        $message = 'Payment not completed. Khalti status: ' . ($status ?: ($look['_error'] ?? 'unknown'));
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Payment result</title>
  <style>
    body { font-family: system-ui, sans-serif; max-width: 460px; margin: 60px auto; padding: 0 16px; }
    .card { border: 1px solid #ddd; border-radius: 12px; padding: 24px; }
    .ok  { background: #e8f5e9; color: #1b5e20; padding: 14px; border-radius: 8px; }
    .no  { background: #fdecea; color: #b71c1c; padding: 14px; border-radius: 8px; }
  </style>
</head>
<body>
  <div class="card">
    <?php if ($paid): ?>
      <div class="ok"><h3>✅ Success</h3><p><?= htmlspecialchars($message) ?></p></div>
    <?php else: ?>
      <div class="no"><h3>❌ Not confirmed</h3><p><?= htmlspecialchars($message) ?></p></div>
    <?php endif; ?>
    <p><a href="orders.php">← Back to My Orders</a></p>
  </div>
</body>
</html>
