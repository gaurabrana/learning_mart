<?php
// base/functions.php
// Small shared helpers for sessions and auth.
// login.php, register.php, cart.php, checkout.php and logout.php all include this.

if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

function isLoggedIn(): bool
{
    return isset($_SESSION['user']);
}

function currentUser(): ?array
{
    return $_SESSION['user'] ?? null;
}

function redirect(string $path): void
{
    header("Location: $path");
    exit;
}

// Flash messages: set one before a redirect, shown once on the next page (see layout/header.php).
function set_flash(string $msg, string $type = 'success'): void
{
    $_SESSION['flash'][] = ['msg' => $msg, 'type' => $type];
}

// Mark a verified order as paid, mark its payment row, reduce stock, and clear the cart.
// Used by BOTH gateways. Idempotent: if the order is already paid, it does nothing.
//   $txnUuid   = the reference we sent the gateway (identifies the payment row)
//   $gatewayRef = the gateway's own transaction id (stored for the record)
function finalize_paid_order(PDO $pdo, int $orderId, int $userId, string $txnUuid, string $gatewayRef): void
{
    $pdo->beginTransaction();

    $stmt = $pdo->prepare("SELECT status FROM orders WHERE id = ? AND user_id = ? FOR UPDATE");
    $stmt->execute([$orderId, $userId]);
    $order = $stmt->fetch();

    if ($order && $order['status'] !== 'paid') {
        $pdo->prepare("UPDATE orders SET status='paid' WHERE id=?")->execute([$orderId]);
        $pdo->prepare("UPDATE payments SET status='paid', gateway_ref=? WHERE transaction_uuid=?")
            ->execute([$gatewayRef, $txnUuid]);

        $items = $pdo->prepare("SELECT product_id, quantity FROM order_items WHERE order_id = ?");
        $items->execute([$orderId]);
        $dec = $pdo->prepare("UPDATE products SET stock = GREATEST(stock - ?, 0) WHERE id = ?");
        foreach ($items->fetchAll() as $it) {
            $dec->execute([(int)$it['quantity'], (int)$it['product_id']]);
        }
    }

    $pdo->commit();
    cart_clear($pdo);
}

// ---- Cart: persistent (DB `cart` table) for logged-in users, session for guests ----

// Return the cart as [product_id => quantity].
function cart_get(PDO $pdo): array
{
    if (isLoggedIn()) {
        $stmt = $pdo->prepare("SELECT product_id, quantity FROM cart WHERE user_id = ?");
        $stmt->execute([currentUser()['id']]);
        $map = [];
        foreach ($stmt->fetchAll() as $r) {
            $map[(int)$r['product_id']] = (int)$r['quantity'];
        }
        return $map;
    }
    return $_SESSION['cart'] ?? [];
}

// Number of distinct products in the cart (used by the header badge).
function cart_count(PDO $pdo): int
{
    return count(cart_get($pdo));
}

// Set an exact quantity for a product (0 or less removes it).
function cart_set_qty(PDO $pdo, int $productId, int $qty): void
{
    if (isLoggedIn()) {
        $uid = currentUser()['id'];
        if ($qty <= 0) {
            $pdo->prepare("DELETE FROM cart WHERE user_id = ? AND product_id = ?")->execute([$uid, $productId]);
        } else {
            $pdo->prepare("INSERT INTO cart (user_id, product_id, quantity) VALUES (?, ?, ?)
                           ON DUPLICATE KEY UPDATE quantity = ?")
                ->execute([$uid, $productId, $qty, $qty]);
        }
    } else {
        if ($qty <= 0) unset($_SESSION['cart'][$productId]);
        else $_SESSION['cart'][$productId] = $qty;
    }
}

// Add quantity to a product, never exceeding available stock.
function cart_add(PDO $pdo, int $productId, int $qty, int $stock): void
{
    $current = cart_get($pdo)[$productId] ?? 0;
    cart_set_qty($pdo, $productId, min($current + $qty, max(1, $stock)));
}

// Remove one product from the cart.
function cart_remove(PDO $pdo, int $productId): void
{
    cart_set_qty($pdo, $productId, 0);
}

// Empty the cart (DB rows for logged-in users, and the session copy).
function cart_clear(PDO $pdo): void
{
    if (isLoggedIn()) {
        $pdo->prepare("DELETE FROM cart WHERE user_id = ?")->execute([currentUser()['id']]);
    }
    $_SESSION['cart'] = [];
}

// On login, move any guest (session) cart items into the user's persistent cart.
function cart_merge_session_to_db(PDO $pdo): void
{
    foreach (($_SESSION['cart'] ?? []) as $pid => $qty) {
        $stmt = $pdo->prepare("SELECT stock FROM products WHERE id = ?");
        $stmt->execute([(int)$pid]);
        $stock = (int)($stmt->fetchColumn() ?: 0);
        if ($stock > 0) {
            cart_add($pdo, (int)$pid, (int)$qty, $stock);
        }
    }
    $_SESSION['cart'] = [];
}

// Load the cart with product details. Returns ['items' => [...], 'total' => float].
// Each item has: id, title, price, image, qty, subtotal.
function cart_summary(PDO $pdo): array
{
    $cart = cart_get($pdo);
    if (!$cart) {
        return ['items' => [], 'total' => 0];
    }

    $ids          = array_keys($cart);
    $placeholders = implode(',', array_fill(0, count($ids), '?'));
    $stmt = $pdo->prepare("SELECT id, title, price, image FROM products WHERE id IN ($placeholders)");
    $stmt->execute($ids);

    $items = [];
    $total = 0;
    foreach ($stmt->fetchAll() as $p) {
        $qty           = (int) $cart[$p['id']];
        $p['qty']      = $qty;
        $p['subtotal'] = $p['price'] * $qty;
        $total        += $p['subtotal'];
        $items[]       = $p;
    }
    return ['items' => $items, 'total' => $total];
}
