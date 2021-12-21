DELIMITER //

CREATE PROCEDURE sql_challenge.spAlterStock(IN product_id INT, IN stock_to_buy INT, IN sale_id INT)
BEGIN
	
	DECLARE actual_stock INT;
    DECLARE stock_bough INT;
    DECLARE n INT DEFAULT 1;
    
	WHILE stock_to_buy > 0 DO 
    
		call spPurchaseId(n, product_id, @purchase_id);
        
		SELECT purchase.in_stock INTO actual_stock FROM purchase
		WHERE purchase.id = @purchase_id 
		AND purchase.product_id = product_id;
    
		WHILE actual_stock > 0 AND stock_to_buy> 0 DO
			CASE 
				WHEN actual_stock <= stock_to_buy THEN
				
				UPDATE purchase SET purchase.in_stock = 0
				WHERE purchase.id = @purchase_id;
				SET stock_to_buy = stock_to_buy - actual_stock;
                SET stock_bough =	actual_stock;
                SET actual_stock = 0;
				
				
				
				WHEN actual_stock > stock_to_buy THEN
				
				UPDATE purchase SET purchase.in_stock = actual_stock - stock_to_buy
				WHERE purchase.id = @purchase_id;
				SET stock_bough =	stock_to_buy;
				SET stock_to_buy = 0;
				
			END CASE;
			
			call spSaleToPur(@sale_id, @purchase_id, stock_bough);
		END WHILE;
        SET n = n + 1;
	END WHILE;
        
END //

DELIMITER ;