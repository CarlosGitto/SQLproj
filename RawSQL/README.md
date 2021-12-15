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

If this is the first time using the application, run both _make_tables.py_ and _make_views.py_ file to create database (if there is none with the database name provided), tables and views inside such database.

For testing purposes, run the file _table_seeder.py_ to fill tables with random data. This is useful for debugging SQL queries.

### SELECT Statements

To view data from the reports previously introduced in this document's introduction:
* To view monthly income reports, run _select_views_month.py_
* To view yearly income reports, run _select_views_year.py_
