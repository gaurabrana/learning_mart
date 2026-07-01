<?php
// Shopping cart — persistent (DB `cart` table) for logged-in users, session for guests.
// The cart helpers in base/functions.php pick DB or session automatically.
include 'base/connect.php';
include 'base/functions.php';

$action = $_GET['action'] ?? null;
$id     = isset($_GET['id']) ? (int)$_GET['id'] : 0;

// --- Handle cart actions, then redirect (Post/Redirect/Get) so refresh won't re-add ---
if ($action === 'add' && $id > 0) {
    $qty  = max(1, (int)($_GET['qty'] ?? 1));
    $stmt = $pdo->prepare("SELECT title, stock FROM products WHERE id = ?");
    $stmt->execute([$id]);
    $row = $stmt->fetch();
    if ($row) {
        cart_add($pdo, $id, $qty, (int)$row['stock']);   // stock-capped; DB or session
        set_flash('Added to cart: ' . $row['title']);
    } else {
        set_flash('Product not found.', 'danger');
    }
    // Return to the page the user came from (fallback to the product list).
    redirect($_SERVER['HTTP_REFERER'] ?? 'product.php');
}

if ($action === 'remove' && $id > 0) {
    cart_remove($pdo, $id);
    redirect('cart.php');
}

if ($_SERVER['REQUEST_METHOD'] === 'POST' && ($_POST['action'] ?? '') === 'update') {
    foreach (($_POST['qty'] ?? []) as $pid => $qty) {
        cart_set_qty($pdo, (int)$pid, (int)$qty);   // qty 0 removes the item
    }
    redirect('cart.php');
}

// --- Load the cart for display ---
$cart  = cart_summary($pdo);
$items = $cart['items'];
$total = $cart['total'];
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Your Cart - LearningMart</title>
  <link href="assets/css/style.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="d-flex flex-column min-vh-100">

<?php include 'layout/header.php'; ?>

<main class="container py-4 flex-grow-1">

  <h2 class="mb-4">Your Cart</h2>

  <?php if (!$items): ?>
    <div class="alert alert-info">
      Your cart is empty. <a href="product.php">Browse products</a>.
    </div>
  <?php else: ?>
    <form method="post" action="cart.php">
      <input type="hidden" name="action" value="update">
      <div class="table-responsive">
        <table class="table align-middle">
          <thead>
            <tr><th>Product</th><th>Price</th><th style="width:120px">Qty</th><th>Subtotal</th><th></th></tr>
          </thead>
          <tbody>
            <?php foreach ($items as $c):
              $img = $c['image'] ? 'uploads/' . $c['image'] : 'https://placehold.co/80x80?text=%20';
            ?>
              <tr>
                <td class="d-flex align-items-center gap-3">
                  <img src="<?= htmlspecialchars($img) ?>" width="60" height="60" style="object-fit:cover" class="rounded" alt="">
                  <span><?= htmlspecialchars($c['title']) ?></span>
                </td>
                <td>Rs. <?= number_format($c['price']) ?></td>
                <td>
                  <input type="number" min="0" name="qty[<?= (int)$c['id'] ?>]" value="<?= (int)$c['qty'] ?>" class="form-control form-control-sm">
                </td>
                <td class="fw-bold">Rs. <?= number_format($c['subtotal']) ?></td>
                <td><a href="cart.php?action=remove&id=<?= (int)$c['id'] ?>" class="btn btn-sm btn-outline-danger">Remove</a></td>
              </tr>
            <?php endforeach; ?>
          </tbody>
        </table>
      </div>

      <div class="d-flex justify-content-between align-items-center flex-wrap gap-2">
        <button type="submit" class="btn btn-outline-dark">Update Cart</button>
        <h4 class="mb-0">Total: Rs. <?= number_format($total) ?></h4>
      </div>
    </form>

    <div class="text-end mt-3">
      <a href="checkout.php" class="btn btn-success btn-lg">Proceed to Checkout</a>
    </div>
  <?php endif; ?>

</main>

<?php include 'layout/footer.php'; ?>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
<script src="assets/js/script.js"></script>
</body>
</html>
