"""This file is used to create tables in the database."""

from connection import mycursor

create_table_queries = open(
    "SQL_statements/create_and_drop_queries/create_all.sql", "r").read().split(";")


def create_tables() -> None:
    """Create all tables"""

    for line in create_table_queries:
        mycursor.execute(line)


if __name__ == "__main__":

    create_tables()