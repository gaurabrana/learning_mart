<?php
// base/esewa.php — eSewa ePay v2 helpers (signature + form + verify).
// Flow: POST a signed form to eSewa -> user pays -> eSewa redirects to success_url with a base64 'data'
// param -> we decode it and check the signature on the server before marking the order paid.
require_once __DIR__ . '/../config.php';

// eSewa signs/verifies with base64(HMAC-SHA256(message, secret)).
function esewa_signature(string $message): string
{
    global $ESEWA;
    return base64_encode(hash_hmac('sha256', $message, $ESEWA['secret'], true));
}

// Build the hidden fields (with signature) to POST to eSewa's payment form.
// $uuid is our unique transaction reference (created + stored by payment_start()).
function esewa_fields(float $total, string $uuid): array
{
    global $ESEWA;
    $totalStr = number_format($total, 2, '.', '');   // exact string that must match the signature
    $message  = "total_amount=$totalStr,transaction_uuid=$uuid,product_code={$ESEWA['product_code']}";

    return [
        'amount'                  => $totalStr,
        'tax_amount'              => '0',
        'total_amount'            => $totalStr,
        'transaction_uuid'        => $uuid,
        'product_code'            => $ESEWA['product_code'],
        'product_service_charge'  => '0',
        'product_delivery_charge' => '0',
        'success_url'             => $ESEWA['success_url'],
        'failure_url'             => $ESEWA['failure_url'],
        'signed_field_names'      => 'total_amount,transaction_uuid,product_code',
        'signature'               => esewa_signature($message),
    ];
}

// Render a self-submitting form that sends the user to eSewa, then stop.
function esewa_redirect_to_payment(float $total, string $uuid): void
{
    global $ESEWA;
    $fields = esewa_fields($total, $uuid);
    echo '<!doctype html><html><body onload="document.forms[0].submit()">';
    echo '<form method="POST" action="' . htmlspecialchars($ESEWA['form_url']) . '">';
    foreach ($fields as $k => $v) {
        echo '<input type="hidden" name="' . htmlspecialchars($k) . '" value="' . htmlspecialchars($v) . '">';
    }
    echo '<p style="font-family:sans-serif;padding:2rem">Redirecting to eSewa…</p></form></body></html>';
    exit;
}

// Verify the base64 'data' eSewa returns. Returns the decoded array if the signature is valid, else null.
function esewa_verify_data(string $data): ?array
{
    $json = json_decode(base64_decode($data), true);
    if (!$json || empty($json['signed_field_names'])) {
        return null;
    }
    // Rebuild the signed message from exactly the fields eSewa listed, in order.
    $parts = [];
    foreach (explode(',', $json['signed_field_names']) as $field) {
        $parts[] = "$field=" . ($json[$field] ?? '');
    }
    $expected = esewa_signature(implode(',', $parts));

    return hash_equals($expected, $json['signature'] ?? '') ? $json : null;
}
