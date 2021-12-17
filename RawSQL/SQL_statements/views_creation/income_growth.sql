CREATE OR REPLACE VIEW revenue_growth AS 
SELECT year(sale.created_at) AS 'year_income', 
    month(sale.created_at) AS 'month_income', 
    SUM(sale_to_purchase.quantity * product.price) AS 'income',
    (
    SUM(sale_to_purchase.quantity * product.price) - 
    LAG(SUM(sale_to_purchase.quantity * product.price), 1) OVER (
        PARTITION BY month(sale.created_at)) /
    LAG(SUM(sale_to_purchase.quantity * product.price), 1) OVER (
        PARTITION BY month(sale.created_at))
    ) AS 'revenue_evolution'
    FROM sale
    JOIN sale_to_purchase
    ON sale_to_purchase.sale_id = sale.id
    JOIN product
    ON sale.product_id = product.id
    GROUP BY sale_to_purchase.sale_id, 1, 2
    ORDER BY 1, 2;