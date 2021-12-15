SELECT * FROM assigned_expense_item AS a
JOIN expense_item AS e
ON a.item_id = e.id
JOIN expense_family AS f
ON f.id = e.family_id;