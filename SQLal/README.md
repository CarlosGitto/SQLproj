# Raw SQL challenge - SQLAlchemy

The objective of this challenge was to create a command line application simulating a regular business's activity. The resulting application runs on MySQL and uses SQLAlchemy's library for interacting with such database manager using the Python programming language.

## Run with perzonaliced settings

First define your user, password, host, port and database name (db_name) for your server by changeing the variables in "utils.py" file or you can use the default values

Then follow the steps


## Step 1
### Build the database, tables and views

python make_all_tables.py
python create_views.py

## Step 2
### Fill tables with random Data

python seed_table.py

## Step 3
### Select the table or the view you want to see

python select_table.py <arg>*

or

pyhton select_view.py <arg1> <arg2>**

*  <arg> is the name of the table you wish to see:
    
    command  -  table

    product  >> product 
    sale     >> sale 
    item     >> expense_item 
    family   >> expense_family
    assei    >> assigned_expense_item 

    all      >> all tables

**  <arg1> Can be "month" or "year"
    <arg2> Is to know wich of the views releated to <arg1> you want to see

    command  -  view table

    1   >>  income_by_month / income_by_year
    2   >>  expenses_by_month / expenses_by_year
    3   >>  income_statement_by_month /income_statement_by_year

    If you wish to see all of them, only use <arg1> like all

    command  --  view table

    all     >>  all views

## Restart

python drop_all_tables.py
python make_all_tables.py
python create_views.py
python seed_table.py

# Go to Step 3