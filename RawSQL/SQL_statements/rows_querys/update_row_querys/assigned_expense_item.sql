#
UPDATE
    assigned_expense_item
SET
    assigned_expense_item.item_id = val2,
    assigned_expense_item.state = val3,
    assigned_expense_item.created_at = NOW()
WHERE
    assigned_expense_item.id = val1;