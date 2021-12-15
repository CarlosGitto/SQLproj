"""Select and print income_statement_by_month view."""

from config import my_cursor

if __name__ == '__main__':
    statement = open(
        'SQL_statements/select_queries/monthly_tables.sql', 'r').read()

    my_cursor.execute(statement)
    r = my_cursor.fetchall()

    for row in r:
        print(row)
