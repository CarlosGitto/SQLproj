#
CREATE TABLE customer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR (225),
    surname VARCHAR (225),
    phone_number INT,
    email VARCHAR (225)
);
#
CREATE TABLE expense_family (
    id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR (225)
);
#
CREATE TABLE product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    price INT
);
#
CREATE TABLE expense_item (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR (225),
    family_id INT,
    cost INT,
    FOREIGN KEY (family_id) REFERENCES expense_family (id)
);
#
CREATE TABLE purchase (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    FOREIGN KEY (product_id) REFERENCES product (id),
    quantity INT,
    cost INT,
    in_stock INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
#
CREATE TABLE sale (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES product (id),
    quantity INT,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customer (id)
);
#
CREATE TABLE assigned_expense_item (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_id INT,
    FOREIGN KEY (item_id) REFERENCES expense_item (id),
    state VARCHAR (225),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE sale_to_purchase (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sale_id INT,
    FOREIGN KEY (sale_id) REFERENCES sale (id),
    purchase_id INT,
    FOREIGN KEY (purchase_id) REFERENCES purchase (id),
    quantity INT
    );