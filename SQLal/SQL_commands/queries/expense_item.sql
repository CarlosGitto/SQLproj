#
SELECT * FROM expense_item AS i
JOIN expense_family AS e
ON i.family_id = e.id;