"""This file is used to create tables in the database."""
from functions.create_tables import create_tables, create_table_queries

if __name__ == "__main__":
    create_tables(create_table_queries)
