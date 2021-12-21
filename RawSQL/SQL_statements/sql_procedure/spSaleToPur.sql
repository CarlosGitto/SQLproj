DELIMITER //

CREATE PROCEDURE spSaleToPur(IN sale_id INT, IN purchase_id INT, IN quantity INT)
BEGIN

	INSERT INTO sale_to_purchase(sale_id, purchase_id, quantity)
    VALUES (sale_id, purchase_id, quantity);
    
END //

DELIMITER ;