#
SELECT * FROM sale AS s
JOIN product AS p
ON p.id = s.product_id;