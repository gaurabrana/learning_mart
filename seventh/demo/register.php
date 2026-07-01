<?php
require 'base/connect.php';
require 'base/functions.php';

$error = null;

if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    $name     = trim($_POST['name'] ?? '');
    $email    = trim($_POST['email'] ?? '');
    $password = $_POST['password'] ?? '';

    if (!$name || !$email || !$password) {
        $error = "All fields are required";
    } elseif (strlen($password) < 6) {
        $error = "Password must be at least 6 characters";
    } else {
        // check existing user
        $stmt = $pdo->prepare("SELECT id FROM users WHERE email = ?");
        $stmt->execute([$email]);

        if ($stmt->fetch()) {
            $error = "Email already exists";
        } else {
            $hashedPassword = password_hash($password, PASSWORD_BCRYPT);
            $pdo->prepare("INSERT INTO users (name, email, password) VALUES (?, ?, ?)")
                ->execute([$name, $email, $hashedPassword]);
            set_flash('Account created. Please log in.');
            redirect("login.php");
        }
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Register - LearningMart</title>
  <link href="assets/css/style.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="d-flex flex-column min-vh-100">

<?php include 'layout/header.php'; ?>

<main class="container flex-grow-1">
  <div class="card shadow-sm auth-card">
    <div class="card-body p-4">
      <h2 class="mb-4">Create Account</h2>

      <?php if ($error): ?>
        <div class="alert alert-danger"><?= htmlspecialchars($error) ?></div>
      <?php endif; ?>

      <form method="POST">
        <div class="mb-3">
          <label class="form-label">Name</label>
          <input class="form-control" name="name" required>
        </div>
        <div class="mb-3">
          <label class="form-label">Email</label>
          <input class="form-control" name="email" type="email" required>
        </div>
        <div class="mb-3">
          <label class="form-label">Password</label>
          <input class="form-control" name="password" type="password" minlength="6" required>
        </div>
        <button class="btn btn-primary w-100">Register</button>
      </form>

      <p class="mt-3 mb-0 text-center">Already have an account? <a href="login.php">Login</a></p>
    </div>
  </div>
</main>

<?php include 'layout/footer.php'; ?>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
<script src="assets/js/script.js"></script>
</body>
</html>
