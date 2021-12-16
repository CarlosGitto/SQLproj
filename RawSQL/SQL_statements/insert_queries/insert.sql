#
INSERT INTO product
    (price, cost, stock)
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
INSERT INTO sale
    (product_id, created_at, quantity, customer_id)
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