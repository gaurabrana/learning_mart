<?php
// router.php
// Very simple routing for learning.
// Usage examples:
//   /demo/router.php?page=home
//   /demo/router.php?page=cart

// Import base bootstrap
require __DIR__ . '/bootstrap.php';

$page = $_GET['page'] ?? 'home';

// In Phase 1/2 we still keep pages simple.
// We will move to views/controllers later.
if ($page === 'home') {
  require __DIR__ . '/index.php';
  exit;
}

if ($page === 'cart') {
  require __DIR__ . '/cart.php';
  exit;
}

// Default: show home
require __DIR__ . '/index.php';

