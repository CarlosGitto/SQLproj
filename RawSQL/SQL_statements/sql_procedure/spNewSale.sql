#
CREATE PROCEDURE spNewSale(
    IN product_id INT,
    IN stock_to_buy INT,
    IN customer_id INT,
    OUT sale_id INT
) BEGIN
INSERT INTO
    sale(product_id, created_at, quantity, customer_id)
VALUES
    (product_id, NOW(), stock_to_buy, customer_id);

SELECT
    LAST_INSERT_ID() into sale_id;

END;