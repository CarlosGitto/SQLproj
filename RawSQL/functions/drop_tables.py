"""Drops tables from database."""
from config import my_cursor

drop_table_statements = open(
    "SQL_statements/create_and_drop_queries/drop_tables.sql", "r").read().split(";")



def drop_tables() -> None:
    """Drop all tables"""
    for line in drop_table_statements:
        try:
            my_cursor.execute(line)
        except:
            pass