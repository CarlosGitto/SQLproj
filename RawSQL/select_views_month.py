"""Select and print income_statement_by_month view."""

from connection import mycursor

if __name__ == '__main__':
    statement = open(
        'SQL_statements/select_queries/monthly_tables.sql', 'r').read()

    mycursor.execute(statement)
    r = mycursor.fetchall()

    for row in r:
        print(row)
