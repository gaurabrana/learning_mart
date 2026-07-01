<?php
// base/khalti.php — minimal Khalti e-Payment helpers (initiate + verify).
// Flow: initiate() gets a payment_url -> send the user there -> after payment Khalti
// redirects back to return_url -> lookup() confirms the payment on the server.
require_once __DIR__ . '/../config.php';

// Low-level: POST JSON to a Khalti endpoint with your secret key. Returns the decoded response.
function khalti_request(string $endpoint, array $payload): array
{
    global $KHALTI;

    $ch = curl_init($KHALTI['base'] . $endpoint);
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST           => true,
        CURLOPT_HTTPHEADER     => [
            'Authorization: Key ' . $KHALTI['secret_key'],
            'Content-Type: application/json',
        ],
        CURLOPT_POSTFIELDS     => json_encode($payload),
        CURLOPT_TIMEOUT        => 30,
    ]);
    $response = curl_exec($ch);
    $error    = curl_error($ch);
    curl_close($ch);

    if ($response === false) {
        return ['_error' => $error ?: 'Request to Khalti failed'];
    }
    return json_decode($response, true) ?: ['_error' => 'Invalid response from Khalti'];
}

// Start a payment. On success the response contains 'pidx' and 'payment_url'.
function khalti_initiate(array $order): array
{
    global $KHALTI;
    return khalti_request('initiate/', [
        'return_url'          => $KHALTI['return_url'],
        'website_url'         => $KHALTI['website_url'],
        'amount'              => (int) round($order['total'] * 100), // amount is in paisa
        'purchase_order_id'   => (string) $order['id'],
        'purchase_order_name' => 'Order #' . $order['id'],
        'customer_info'       => [
            'name'  => $order['name'],
            'email' => $order['email'],
        ],
    ]);
}

// Verify a payment by its pidx. When paid, the response 'status' is 'Completed'.
function khalti_lookup(string $pidx): array
{
    return khalti_request('lookup/', ['pidx' => $pidx]);
}
