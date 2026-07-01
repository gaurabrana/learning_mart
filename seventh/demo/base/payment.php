<?php
// base/payment.php — shared payment layer used by checkout.php and pay.php.
// Records each attempt in the `payments` table, then hands off to the chosen gateway.
require_once __DIR__ . '/khalti.php';
require_once __DIR__ . '/esewa.php';

// Start a payment for an existing order via the chosen gateway.
// $order = ['id' => int, 'total' => float, 'name' => string, 'email' => string]
// On success this redirects/exits (to the gateway). On failure it returns an error string.
function payment_start(PDO $pdo, array $order, string $gateway): string
{
    if ($gateway === 'esewa') {
        // Our unique reference for this attempt (eSewa rejects duplicate UUIDs).
        $uuid = 'ORDER-' . $order['id'] . '-' . time();
        $pdo->prepare(
            "INSERT INTO payments (order_id, gateway, amount, status, transaction_uuid)
             VALUES (?, 'esewa', ?, 'initiated', ?)"
        )->execute([$order['id'], $order['total'], $uuid]);

        esewa_redirect_to_payment((float) $order['total'], $uuid);   // renders form + exits
        return '';                                                   // unreachable
    }

    // default: Khalti
    $resp = khalti_initiate($order);
    if (!empty($resp['payment_url'])) {
        $pdo->prepare(
            "INSERT INTO payments (order_id, gateway, amount, status, transaction_uuid)
             VALUES (?, 'khalti', ?, 'initiated', ?)"
        )->execute([$order['id'], $order['total'], $resp['pidx'] ?? null]);

        redirect($resp['payment_url']);   // exits
    }
    return htmlspecialchars($resp['detail'] ?? $resp['_error'] ?? 'Khalti could not start the payment.');
}

// Find a payment attempt by the reference we sent the gateway (esewa uuid / khalti pidx).
function payment_find_by_uuid(PDO $pdo, string $uuid): ?array
{
    $stmt = $pdo->prepare("SELECT * FROM payments WHERE transaction_uuid = ? ORDER BY id DESC LIMIT 1");
    $stmt->execute([$uuid]);
    return $stmt->fetch() ?: null;
}
