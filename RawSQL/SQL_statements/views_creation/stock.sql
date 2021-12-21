#
CREATE OR REPLACE VIEW stock AS
SELECT product_id, SUM(in_stock)
FROM purchase
GROUP BY product_id;