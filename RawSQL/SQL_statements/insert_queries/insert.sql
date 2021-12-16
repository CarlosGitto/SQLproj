#
INSERT INTO product
    (price)
VALUES
    vals;
#
INSERT INTO customer
    (name, surname, phone_number, email)
VALUES
    vals;
#
INSERT INTO expense_family
    (service_name)
VALUES
    vals;
#
INSERT INTO purchase
    (product_id, quantity, cost, in_stock, created_at)
VALUES
    vals;
#
INSERT INTO client_table
    (name, surname, phone_number, email)
VALUES
    vals;
#
INSERT INTO sale
    (purchase_id, created_at, quantity, client_table_id)
VALUES
    vals;
#
INSERT INTO expense_item
    (item_name, family_id, cost)
VALUES
    vals;
#
INSERT INTO assigned_expense_item
    (item_id, state, created_at)
VALUES
    vals;
