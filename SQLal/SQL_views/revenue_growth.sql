CREATE OR REPLACE VIEW revenue_evolution AS
SELECT month(created_at) AS 'revenue_month',
    year(created_at) AS 'revenue_year',
    SUM(price) AS 'revenue',
    FROM sale;
