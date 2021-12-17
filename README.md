# SQL Challenge

SQL challenge developed for company purposes. The objective lies in creating a database system using only SQL and Python code. The database created consists on several normalized tables inspired by a business's regular activity. Tables contain:

* Product: details different products on sale, along their price, cost and stock volume.
* Sale: registre of sales, containing both a timestamp and product sold.
* Expense_item: list of different expense items, containing a description, cost associated and a column named "family", to help taxonomize expenses by type.
* Expense_family: list of different categories, to help understand taxonomy of Expense_item registres.
* Assigned_expense_item: registre of expenses, detailing the item expended, state of expense, timestamp and an associated sale, if expense was directly related to a sale.
* Purchase: consists of a list of stock increments, specifying quantity acquired, product cost and date. Used to calculate cost of sales with either FIFO or LIFO methods.
* Sale_to_purchase: links sales to purchase for calculating cost of sales.
