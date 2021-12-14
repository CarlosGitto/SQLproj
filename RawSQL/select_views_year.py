"""This file is used to invoke the income_statement_by_year view."""

from connection import mycursor

if __name__ == '__main__':
    statement = open(
        'SQL_statements/yearly_tables.sql', 'r').read()

    mycursor.execute(statement)
    r = mycursor.fetchall()

    for row in r:
        print(row)
