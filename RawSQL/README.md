# Raw SQL challenge using MySQL

This command line application consists of a series of Python files used to interact with a database. The database is made up of 5 different tables in a normalized manner. Two views were developed to summarize all tables, consisting of monthly and annually income reports.

## Usage

### Optional Step

Open the _config.py_ file in the editor of your choice. Modify lines 3 through 6 with your own MySQL server credentials:

```
host = YOUR_HOST                -> default = "localhost"
user = YOUR_USER                -> default = "root"
password = YOUR_PASSWORD        -> default = "123456"
db_name = YOUR_DATABASE_NAME    -> default = "sql_challenge"
```

### Step 1 - Create

To create all the tables, views and procedures in the database run:

```
python -m make_all_tables
python -m make_all_views
python -m make_procedures
```

### Step 2 - Populate

For testing purposes, you can populate the database with randomly created data. Open the CLI of your choice and run:

```
python -m table_seeder
```

### Step 3 - Select, Update, Insert or Delete
### View Selection Statements

To view data from the reports previously introduced in this document's introduction:

* To view monthly income reports:

```
python -m select_views_month
```

* To view yearly income reports, run _select_views_year.py_

```
python -m select_views_year
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
python -m select_table 1
```
### Row Selection Statements

To select a row you need to pass trough CLI flags the table name and the id of the row you wish to see:

```
python -m select_row <table_name> <row_id>
 ```

### Row Update Statements

To update a row you need to pass trough CLI flags the table name, the id of the row you wish to update and the values of each column:

```
python -m update_row <table_name> <row_id> <val_col1> <val_col2> ...
```

### Row Insert Statements

To insert a new row in a table of the followings
[
    product,
    customer,
    expense_family,
    purchase,
    expense_item,
    assigned_expense_item
]

You must do:
```
pyhton -m insert <table_name> <row_id> <val_col1> <val_col2> ...
```


# To insert a new row in the sale table you must do:
```
pyhton -m create_sale sale <product_id> <quantity> <customer_id> ...
```

### Row Delete Statements
If you wish to delete a specific row in a specific table you should run:

```
python -m delete_row <table_name> <row_id> 
```


### Step 3 - Reset database
### Drop tables

If for any reason you would like to reset the whole database, drop all tables by running:

```
python -m drop_tables
```

Once completed, please follow instructions again from the top.

### Drop views

If for any reason you would like to reset the whole database, drop all views by running:

```
python -m drop_views
```

Once completed, please follow instructions again from the top.

### Drop procedures

If for any reason you would like to reset the whole database, drop all tables by running:

```
python -m drop_procedures
```

Once completed, please follow instructions again from the top.