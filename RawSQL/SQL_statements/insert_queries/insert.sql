INSERT INTO product (price, cost, stock)
VALUES (%s,%s,%s);

INSERT INTO expense_family (service_name) 
VALUES (%s);

INSERT INTO sale (product_id, created_at)
VALUES (%s,%s);

INSERT INTO expense_item (item_name, family_id, cost)
VALUES (%s,%s,%s);

INSERT INTO assigned_expense_item(item_id, state, created_at, sale_id)
VALUES (%s,%s,%s,%s);