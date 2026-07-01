<?php
/**
 * Database Connection File
 *
 * Provides BOTH connections so students can compare:
 *   $conn -> MySQLi (older style)
 *   $pdo  -> PDO (modern style) — we use this for most features (prepared statements = safer).
 *
 * Runs on either local server WITHOUT edits by trying the common setups in order:
 *   XAMPP -> user 'root', empty password, MySQL port 3306
 *   MAMP  -> user 'root', password 'root', MySQL port 8889
 * On a live host, replace $db_setups with the host's single set of credentials.
 */

if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

date_default_timezone_set("Asia/Kathmandu");

require_once __DIR__ . '/../config.php';   // optional production DB override ($DB)

if (isset($DB) && is_array($DB)) {
    // Production: use the single set of credentials from config.php.
    $db_name   = $DB['name'];
    $db_setups = [[
        'host' => $DB['host'],
        'port' => $DB['port'] ?? 3306,
        'user' => $DB['user'],
        'pass' => $DB['pass'] ?? '',
    ]];
} else {
    // Local: auto-detect XAMPP or MAMP.
    $db_name   = 'demo';
    $db_setups = [
        ['host' => '127.0.0.1', 'port' => 3306, 'user' => 'root', 'pass' => ''],     // XAMPP
        ['host' => '127.0.0.1', 'port' => 8889, 'user' => 'root', 'pass' => 'root'], // MAMP
    ];
}

// --- PDO connection (find the setup that works) ---
$pdo    = null;
$active = null;
foreach ($db_setups as $setup) {
    try {
        $pdo = new PDO(
            "mysql:host={$setup['host']};port={$setup['port']};dbname=$db_name;charset=utf8mb4",
            $setup['user'],
            $setup['pass']
        );
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
        $active = $setup;
        break;
    } catch (PDOException $e) {
        $pdo = null; // try the next setup
    }
}

if (!$pdo) {
    die(
        "Database connection failed. Check: "
        . "(1) MySQL is started in XAMPP/MAMP, "
        . "(2) the database '$db_name' exists in phpMyAdmin, "
        . "(3) you imported database/schema.sql. "
        . "If your MySQL user/password/port differ, edit \$db_setups in base/connect.php."
    );
}

// --- MySQLi connection (same settings that worked for PDO) ---
$conn = mysqli_connect($active['host'], $active['user'], $active['pass'], $db_name, $active['port']);
if (!$conn) {
    die("MySQLi connection failed: " . mysqli_connect_error());
}
