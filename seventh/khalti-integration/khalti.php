<?php
/**
 * khalti.php — a tiny, self-contained Khalti e-Payment (KPG-2) helper.
 *
 * The ONLY file you must copy into another project. No database, no framework,
 * no globals — just PHP + cURL. Drop it in, `require` it, and use the class.
 *
 * The whole payment is 3 moves:
 *   1) initiate()  -> Khalti gives you a `payment_url` + `pidx`. Send the user to payment_url.
 *   2) user pays on Khalti, then Khalti redirects back to your `return_url?pidx=...`.
 *   3) lookup($pidx) -> you ask Khalti (server-to-server) if it's really 'Completed'.
 *
 * GOLDEN RULE: never trust the redirect alone. Only mark an order paid after
 * lookup() returns status 'Completed' AND the amount matches what you expected.
 */

class Khalti
{
    private string $secretKey;
    private string $baseUrl;

    /**
     * @param string $secretKey  Your Khalti *secret* key (server-side only — never expose it).
     * @param bool   $sandbox    true = test (dev.khalti.com), false = live (khalti.com).
     */
    public function __construct(string $secretKey, bool $sandbox = true)
    {
        $this->secretKey = $secretKey;
        $this->baseUrl   = $sandbox
            ? 'https://dev.khalti.com/api/v2/epayment/'   // TEST
            : 'https://khalti.com/api/v2/epayment/';      // LIVE
    }

    /**
     * Step 1 — start a payment.
     * Returns the decoded Khalti response; on success it has 'pidx' and 'payment_url'.
     * On failure it has 'detail' (Khalti's message) or '_error' (network problem).
     *
     * @param array $params Required keys:
     *   return_url, website_url, amount (in PAISA), purchase_order_id, purchase_order_name
     *   Optional: customer_info => ['name'=>..., 'email'=>..., 'phone'=>...]
     */
    public function initiate(array $params): array
    {
        return $this->request('initiate/', $params);
    }

    /**
     * Step 3 — verify a payment on the server by its pidx.
     * Paid  => response['status'] === 'Completed'.
     * Also returns 'total_amount' (paisa) and 'transaction_id' — check the amount too.
     */
    public function lookup(string $pidx): array
    {
        return $this->request('lookup/', ['pidx' => $pidx]);
    }

    /** Convenience: Khalti works in PAISA, so Rs. 100 => 10000. */
    public static function toPaisa(float $rupees): int
    {
        return (int) round($rupees * 100);
    }

    // --- internal: POST JSON to a Khalti endpoint with the secret key ---
    private function request(string $endpoint, array $payload): array
    {
        $ch = curl_init($this->baseUrl . $endpoint);
        curl_setopt_array($ch, [
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_POST           => true,
            CURLOPT_HTTPHEADER     => [
                'Authorization: Key ' . $this->secretKey,
                'Content-Type: application/json',
            ],
            CURLOPT_POSTFIELDS     => json_encode($payload),
            CURLOPT_TIMEOUT        => 30,
        ]);
        $response = curl_exec($ch);
        $error    = curl_error($ch);
        curl_close($ch);

        if ($response === false) {
            // Network/cURL failure (e.g. some free hosts block outbound requests).
            return ['_error' => $error ?: 'Request to Khalti failed (is outbound cURL allowed?)'];
        }
        return json_decode($response, true) ?: ['_error' => 'Invalid response from Khalti'];
    }
}
