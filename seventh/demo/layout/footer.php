<?php
// Shared footer
?>

<footer class="bg-dark text-white mt-5">
  <div class="container py-4">

    <div class="row">

      <!-- Brand -->
      <div class="col-md-4">
        <div class="fw-bold">LearningMart</div>
        <div class="small text-white-50">
          Teaching project: PHP + MySQL (PDO) + Bootstrap 5
        </div>
      </div>

      <!-- Quick Links -->
      <div class="col-md-4">
        <div class="fw-bold">Quick Links</div>
        <ul class="list-unstyled small text-white-50">
          <li><a href="index.php" class="text-white-50 text-decoration-none">Home</a></li>
          <li><a href="category.php" class="text-white-50 text-decoration-none">Categories</a></li>
          <li><a href="product.php" class="text-white-50 text-decoration-none">Products</a></li>
          <li><a href="#" class="text-white-50 text-decoration-none">Cart (later)</a></li>
        </ul>
      </div>

      <!-- Newsletter -->
      <div class="col-md-4">
        <div class="fw-bold">Newsletter</div>
        <div class="small text-white-50 mb-2">
          Subscribe for updates (UI only)
        </div>

        <form class="d-flex gap-2">
          <input type="email" class="form-control form-control-sm" placeholder="Email">
          <button class="btn btn-primary btn-sm" disabled>Join</button>
        </form>
      </div>

    </div>

    <hr class="border-secondary">

    <div class="text-center small text-white-50">
      © <?= date('Y') ?> LearningMart. All rights reserved.
    </div>

  </div>
</footer>