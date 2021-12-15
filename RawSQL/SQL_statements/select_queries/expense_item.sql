#
SELECT * FROM expense_item AS i
JOIN expense_family AS f
ON i.family_id = f.id;