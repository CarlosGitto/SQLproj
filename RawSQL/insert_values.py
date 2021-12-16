"""Used to insert values into tables."""

import sys
from config import my_cursor, my_conn

table = sys.argv[1]
values = sys.argv[-1]

insert_statements = open(
    'SQL_statements/insert_queries/insert.sql').read().split('#')

if __name__ == '__main__':

    if table == 'sale':
        pass

    else:
        statement = f"INSERT INTO {table} VALUES {values};"

        my_cursor.execute(statement)
        my_conn.commit()
