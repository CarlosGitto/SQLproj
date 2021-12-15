"""Drops all tables if necessary."""

from config import my_cursor

drop_table_statements = open(
    "SQL_statements/create_and_drop_queries/drop_all.sql", "r").read().split(";")

drop_views_statements = open(
    'SQL_statements/create_and_drop_queries/drop_views.sql', 'r').read().split(';')


def drop_tables() -> None:
    """Drop all tables"""
    for line in drop_table_statements:
        my_cursor.execute(line)


def drop_views() -> None:
    """Drop all views"""

    for line in drop_views_statements:
        my_cursor.execute(line)


if __name__ == "__main__":

    drop_tables()
    drop_views()
