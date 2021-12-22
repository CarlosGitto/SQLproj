#
UPDATE
    expense_item
SET
    expense_item.item_name = val2,
    expense_item.family_id = val3,
    expense_item.cost = val4
WHERE
    customer.id = val1;