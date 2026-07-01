<?php
// bootstrap.php
// Entry point bootstrap (foundation) for the learning ecommerce.
// Later we will add routing and controllers.

require __DIR__ . '/base/connect.php';

// A simple helper for students: consistent escaping.
function e(string $value): string
{
  return htmlspecialchars($value, ENT_QUOTES, 'UTF-8');
}

