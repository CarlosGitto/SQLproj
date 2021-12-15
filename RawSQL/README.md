# Raw SQL challenge using MySQL

This command line application consists of a series of Python files used to interact with a database. The database is made up of 5 different tables in a normalized manner. Two views were developed to summarize all tables, consisting of monthly and annually income reports.

## Usage

Open the _config.py_ file in the editor of your choice. Modify lines 3 through 6 with your own MySQL server credentials:

```
host = YOUR_HOST
user = YOUR_USER
password = YOUR_PASSWORD
db_name = YOUR_DATABASE_NAME
```


If this is the first time using the application, the following command creates the database with the specified name (if it doesn't exist) and tables inside it. Open the CLI of your choice and run:



```
python make_tables.py
```

For testing purposes, you can populate the database with randomly created data. Open the CLI of your choice and run:

```
python table_seeder.py
```

### View Selection Statements

To view data from the reports previously introduced in this document's introduction:
* To view monthly income reports:

```
python select_views_month.py
```

* To view yearly income reports, run _select_views_year.py_

```
python select_views_year.py
```

### Table Selection Statements

To select a specific table (in denormalized format if it contains a foreign key) run the following command in the CLI of your choice along with a flag. List of possible flags:
* 1: Product
* 2: Sale
* 3: Expense_family
* 4: Expense_item
* 5: Assigned_expense_item

To select the product table, for example, run:

```
python select_table.py 1
```

### Drop tables

If for any reason you would like to reset the whole database, drop all tables by running:

```
python drop_tables.py
```

Once completed, please follow instructions again from the top.
