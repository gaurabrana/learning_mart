<?php
require 'base/connect.php';
require 'base/functions.php';

$error = null;

if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    $email    = trim($_POST['email'] ?? '');
    $password = $_POST['password'] ?? '';

    $stmt = $pdo->prepare("SELECT * FROM users WHERE email = ?");
    $stmt->execute([$email]);
    $user = $stmt->fetch(PDO::FETCH_ASSOC);

    if ($user && password_verify($password, $user['password'])) {
        session_regenerate_id(true);   // security: new session id on login
        $_SESSION['user'] = [
            'id'    => $user['id'],
            'name'  => $user['name'],
            'email' => $user['email'],
            'role'  => $user['role'],
        ];
        cart_merge_session_to_db($pdo);   // carry a guest cart into the user's saved cart
        set_flash('Welcome back, ' . $user['name'] . '!');
        redirect("index.php");
    } else {
        $error = "Invalid email or password";
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Login - LearningMart</title>
  <link href="assets/css/style.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="d-flex flex-column min-vh-100">

<?php include 'layout/header.php'; ?>

<main class="container flex-grow-1">
  <div class="card shadow-sm auth-card">
    <div class="card-body p-4">
      <h2 class="mb-4">Login</h2>

      <?php if ($error): ?>
        <div class="alert alert-danger"><?= htmlspecialchars($error) ?></div>
      <?php endif; ?>

      <form method="POST">
        <div class="mb-3">
          <label class="form-label">Email</label>
          <input class="form-control" name="email" type="email" required>
        </div>
        <div class="mb-3">
          <label class="form-label">Password</label>
          <input class="form-control" name="password" type="password" required>
        </div>
        <button class="btn btn-dark w-100">Login</button>
      </form>

      <p class="mt-3 mb-0 text-center">No account? <a href="register.php">Register</a></p>
    </div>
  </div>
</main>

<?php include 'layout/footer.php'; ?>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
<script src="assets/js/script.js"></script>
</body>
</html>
