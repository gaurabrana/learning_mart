<?php
// Log the user out and return to the home page.
require 'base/functions.php';

$_SESSION = [];          // clear session data (keeps the cart? no — clears everything)
session_destroy();

redirect('index.php');
