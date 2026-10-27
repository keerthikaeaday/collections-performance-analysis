SELECT
    DATE_TRUNC('month', CAST(event_at AS TIMESTAMP)) AS month,
    COUNT(*) AS total_transactions,
    SUM(CASE WHEN payment_status = 'SUCCESS' THEN 1 ELSE 0 END) AS successful_transactions,
    SUM(CASE WHEN payment_status = 'SUCCESS' THEN amount ELSE 0 END) AS successful_payment_amount,
    ROUND(
        100.0 * SUM(CASE WHEN payment_status = 'SUCCESS' THEN 1 ELSE 0 END)
        / NULLIF(COUNT(*), 0),
        2
    ) AS payment_success_rate_pct
FROM payments
GROUP BY DATE_TRUNC('month', CAST(event_at AS TIMESTAMP))
ORDER BY month;

SELECT
   payment_id,
   COUNT(*) AS row_count
FROM payments
GROUP BY payment_id
HAVING COUNT(*) > 1
ORDER BY row_count DESC;

SELECT
   COUNT(*) AS missing_payment_references
FROM payments
WHERE payment_reference IS NULL OR TRIM(payment_reference) = '';

SELECT
   p.borrower_id,
   COUNT(*) AS payment_records
FROM payments p
LEFT JOIN borrowers b
   ON p.borrower_id = b.borrower_id
WHERE b.borrower_id IS NULL
GROUP BY p.borrower_id
ORDER BY payment_records DESC;\n
