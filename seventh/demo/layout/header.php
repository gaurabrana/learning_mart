<?php
// Header include - navbar with dark mode, cart count and auth links.
require_once __DIR__ . '/../base/functions.php';    // cart + auth helpers
require_once __DIR__ . '/../config.php';            // $GA4_ID for analytics

$currentPage = basename($_SERVER['PHP_SELF']);
$cartCount   = cart_count($pdo);                     // distinct products (DB cart if logged in, else session)
$user        = $_SESSION['user'] ?? null;
$searchTerm  = $_GET['q'] ?? '';
?>

<?php
// Google Analytics 4 (Session 5): enabled site-wide when $GA4_ID is set in config.php.
// (Search Console: for a PHP site, verify with the HTML-FILE method — upload google<...>.html to the site root.)
if (!empty($GA4_ID)): ?>
<script async src="https://www.googletagmanager.com/gtag/js?id=<?= htmlspecialchars($GA4_ID) ?>"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', '<?= htmlspecialchars($GA4_ID) ?>');
</script>
<?php endif; ?>

<nav class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top glass">
  <div class="container-fluid">

    <a class="navbar-brand fw-bold" href="index.php">LearningMart</a>

    <button class="navbar-toggler" type="button"
      data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
      aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">

      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link <?= ($currentPage === 'index.php') ? 'active' : '' ?>" href="index.php">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link <?= ($currentPage === 'category.php') ? 'active' : '' ?>" href="category.php">Categories</a>
        </li>
        <li class="nav-item">
          <a class="nav-link <?= ($currentPage === 'product.php') ? 'active' : '' ?>" href="product.php">Products</a>
        </li>
      </ul>

      <!-- Search -->
      <form class="d-flex me-2" role="search" method="get" action="product.php">
        <input class="form-control me-2" type="search" name="q"
               value="<?= htmlspecialchars($searchTerm) ?>"
               placeholder="Search products..." aria-label="Search">
        <button class="btn btn-outline-light" type="submit">Search</button>
      </form>

      <!-- Cart -->
      <a class="btn btn-outline-light me-2 position-relative" href="cart.php">
        Cart
        <?php if ($cartCount > 0): ?>
          <span class="badge bg-warning text-dark rounded-pill"><?= $cartCount ?></span>
        <?php endif; ?>
      </a>

      <!-- Auth -->
      <?php if ($user): ?>
        <a class="btn btn-outline-light me-2" href="orders.php">My Orders</a>
        <span class="navbar-text text-light me-2">Hi, <?= htmlspecialchars($user['name']) ?></span>
        <a class="btn btn-outline-light me-2" href="logout.php">Logout</a>
      <?php else: ?>
        <a class="btn btn-outline-light me-2" href="login.php">Login</a>
        <a class="btn btn-light me-2" href="register.php">Register</a>
      <?php endif; ?>

      <!-- Dark Mode Toggle -->
      <button id="darkModeToggle" class="btn btn-outline-light" type="button" title="Toggle dark mode">🌙</button>

    </div>
  </div>
</nav>

<?php // Flash messages (set via set_flash() before a redirect) — shown once.
$flashes = $_SESSION['flash'] ?? [];
unset($_SESSION['flash']);
if ($flashes): ?>
  <div class="container mt-3">
    <?php foreach ($flashes as $f): ?>
      <div class="alert alert-<?= htmlspecialchars($f['type']) ?> alert-dismissible fade show" role="alert">
        <?= htmlspecialchars($f['msg']) ?>
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
      </div>
    <?php endforeach; ?>
  </div>
<?php endif; ?>
