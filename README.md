# SQL Challenge

SQL challenge developed for company purposes. The objective lies in creating a database system using only SQL and Python code. The database created consists on several normalized tables inspired by a business's regular activity. Tables contain:

* Product: details different products on sale, along their price, cost and stock volume.
* Sale: registre of sales, containing both a timestamp and product sold.
* Expense_item: list of different expense items, containing a description, cost associated and a column named "family", to help taxonomize expenses by type.
* Expense_family: list of different categories, to help understand taxonomy of Expense_item registres.
* Assigned_expense_item: registre of expenses, detailing the item expended, state of expense, timestamp and an associated sale, if expense was directly related to a sale.

## Usage

The relational database management system of choice is MySQL. Please refer to requirements.txt file before attempting to use.

First open utils.py file and detail your own MySQL server configurations in string format (listed in lines 5 through 8) and save the file:

```
user = YOUR_USER
password = YOUR_PASSWORD
port = YOUR_PORT
db_name = YOUR_DATABASE_NAME
```

This step is to connect the SQLAlchemy engine to the host's database.

Once completed run both make_tables.py and seed_table.py (in that specific order) to both generate tables in the database, and also populating such tables with randomly generated data for exposing purposes.
