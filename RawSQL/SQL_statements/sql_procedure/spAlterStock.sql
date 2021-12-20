DELIMITER //
CREATE PROCEDURE sql_challenge.spAlterStock(IN purchase_id INT, IN product_id INT, INOUT stock_to_buy INT, OUT stock_bough INT)
BEGIN
	DECLARE actual_stock INT; 
	SELECT in_stock INTO actual_stock FROM purchase
    WHERE purchase.id = purchase_id 
    AND purchase.product_id = product_id;	
	CASE 
		WHEN actual_stock <= stock_to_buy THEN  
        UPDATE purchase SET purchase.in_stock = 0
		WHERE purchase.id = purchase_id;
        SET stock_to_buy = stock_to_buy - actual_stock;
        SET stock_bough =	actual_stock;        
		WHEN actual_stock > stock_to_buy THEN        
        UPDATE purchase SET purchase.in_stock = actual_stock - stock_to_buy
        WHERE purchase.id = purchase_id;
        SET stock_bough =	stock_to_buy;
		SET stock_to_buy = 0;      
    END CASE;
END //
DELIMITER ;