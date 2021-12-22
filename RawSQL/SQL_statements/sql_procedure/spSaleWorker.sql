#
CREATE PROCEDURE spSaleWorker(
    IN product_id INT,
    INOUT stock_to_buy INT,
    IN customer_id INT
) BEGIN DECLARE `_rollback` BOOL DEFAULT 0;

DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
SET
    `_rollback` = 1;

SET
    autocommit = 0;

START TRANSACTION;

call spNewSale(product_id, stock_to_buy, customer_id, @sale_id);

call spAlterStock(product_id, stock_to_buy, @sale_id);

IF `_rollback` THEN ROLLBACK;

ELSE COMMIT;

END IF;

END;