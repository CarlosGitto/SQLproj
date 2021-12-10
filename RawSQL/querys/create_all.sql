create table expense_family (id INT AUTO_INCREMENT PRIMARY KEY,service_name VARCHAR(225));

create table product (id INT AUTO_INCREMENT PRIMARY KEY,price INT, cost INT, stock INT );

create table expense_item (id INT AUTO_INCREMENT PRIMARY KEY,item_name VARCHAR(225), 
                            family_id INT, cost INT, FOREIGN KEY (family_id) REFERENCES expense_family(id));

create table sale (id INT AUTO_INCREMENT PRIMARY KEY,product_id INT, created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (product_id) REFERENCES product(id));

create table assigned_expense_item (id INT AUTO_INCREMENT PRIMARY KEY, 
                                    item_id INT, FOREIGN KEY (item_id) REFERENCES expense_item(id), 
                                    state VARCHAR(225), created_at DATETIME DEFAULT CURRENT_TIMESTAMP, 
                                    sale_id INT, FOREIGN KEY (sale_id) REFERENCES sale(id));