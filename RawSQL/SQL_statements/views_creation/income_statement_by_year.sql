

CREATE OR REPLACE VIEW income_by_year AS
SELECT year(created_at) AS 'year_income', 
    SUM(price) AS 'sales', 
    SUM(cost) AS 'cost_of_goods_sold', 
    (SUM(price) - SUM(cost)) AS 'gross_profit'
    FROM sale
    JOIN product ON sale.product_id = product.id
    GROUP BY 1
    ORDER BY 1;


CREATE OR REPLACE VIEW expenses_by_year AS
SELECT year(created_at) AS 'year_expense', 
	SUM(IF(service_name = 'marketing', cost, 0)) AS 'marketing',
    SUM(IF(service_name = 'hr', cost, 0)) AS 'human_resources',
    SUM(IF(service_name = 'finance', cost, 0)) AS 'finance',
    SUM(IF(service_name = 'others', cost, 0)) AS 'other_expenses',
    (
    SUM(IF(service_name = 'marketing', cost, 0)) +
    SUM(IF(service_name = 'hr', cost, 0)) +
    SUM(IF(service_name = 'finance', cost, 0)) +
    SUM(IF(service_name = 'others', cost, 0))
    ) AS 'total_expenses'
    FROM assigned_expense_item AS a
    JOIN expense_item AS e 
    ON a.item_id = e.id
    JOIN expense_family AS f
    ON e.family_id = f.id
    GROUP BY 1
    ORDER BY 1;


CREATE OR REPLACE VIEW income_statement_by_year AS
SELECT year_income AS 'year', 
    sales, 
    cost_of_goods_sold, 
    gross_profit,
    marketing,
    human_resources,
    finance,
    other_expenses,
    total_expenses,
    (gross_profit - total_expenses) AS 'profits'
    FROM income_by_year AS i
    JOIN expenses_by_year AS e 
    ON i.year_income = e.year_expense AND i.year_income = e.year_expense
    GROUP BY 1
    ORDER BY 1;