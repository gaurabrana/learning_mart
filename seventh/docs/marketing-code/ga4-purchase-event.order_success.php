<?php
// ─────────────────────────────────────────────────────────────────────────────
// EXTRACT (not a standalone file). This is the GA4 e-commerce CONVERSION event.
// It fires once, on the order-confirmation page, only for a real paid order.
//
// Real location:  demo/order_success.php   (lines 92–106)
// Depends on:     $GA4_ID set (so the gtag() function from ga4-tag.header.php exists),
//                 plus $order / $items / $payment for the paid order.
//
// This is what turns GA4 from "counting visits" into "measuring revenue": the
// `purchase` event reports the transaction id, total value, currency, and line items,
// and shows up under GA4 → Realtime → Events and → Monetization.
// ─────────────────────────────────────────────────────────────────────────────
?>
<?php // GA4 e-commerce: record the purchase (only when GA4 is on and the order is actually paid).
if (!empty($GA4_ID) && !empty($payment) && !empty($order) && !empty($items)): ?>
<script>
  gtag('event', 'purchase', {
    transaction_id: '<?= (int)$order['id'] ?>',
    value: <?= (float)$order['total'] ?>,
    currency: 'NPR',
    items: [
      <?php foreach ($items as $it): ?>
      { item_name: <?= json_encode($it['title']) ?>, price: <?= (float)$it['price_at_purchase'] ?>, quantity: <?= (int)$it['quantity'] ?> },
      <?php endforeach; ?>
    ]
  });
</script>
<?php endif; ?>
