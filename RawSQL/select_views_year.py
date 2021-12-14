"""Select and print income_statement_by_year view."""

from connection import mycursor

if __name__ == '__main__':
    statement = open(
        'SQL_statements/select_queries/yearly_tables.sql', 'r').read()

    mycursor.execute(statement)
    r = mycursor.fetchall()

    for row in r:
        print(row)
