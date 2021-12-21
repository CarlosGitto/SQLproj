#
CREATE PROCEDURE spSaleWorker(
    IN product_id INT,
    INOUT stock_to_buy INT,
    IN customer_id INT
) BEGIN call spNewSale(product_id, stock_to_buy, customer_id, @sale_id);
call spAlterStock(product_id, stock_to_buy, @sale_id);
END;
