"""Select and print income_statement_by_year view."""

from config import my_cursor

if __name__ == '__main__':
    statement = open(
        'SQL_statements/select_queries/yearly_tables.sql', 'r').read()

    my_cursor.execute(statement)
    r = my_cursor.fetchall()

    for row in r:
        print(row)
