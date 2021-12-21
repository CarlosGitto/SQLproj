"""Drops views from de database."""
from config import my_cursor


drop_views_statements = open(
    'SQL_statements/create_and_drop_queries/drop_views.sql', 'r').read().split(';')

def drop_views() -> None:
    """Drop all views"""

    for line in drop_views_statements:
        try:
            my_cursor.execute(line)
        except:
            pass
