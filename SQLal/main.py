from re import S
import sqlalchemy
from utils import engine
import time
from tabulate import tabulate

income_statement_by_month = "/Users/juanpena/Desktop/SQL_pr/SQLproj/SQLal/queries/income_statement_by_month.sql"
income_statement_by_year = "/Users/juanpena/Desktop/SQL_pr/SQLproj/SQLal/queries/income_statement_by_year.sql"


def sql_parser(file_path: str) -> list[str]:
    statements = open(file_path).read()
    statement_list = []

    for statement in statements.split('#'):
        corrected = statement.replace('\n', ' ')
        statement_list.append(corrected)

    return statement_list


if __name__ == "__main__":

    with engine.connect() as conn:
        for i in [income_statement_by_month, income_statement_by_year]:
            print(f'creating or updating view for {i}')
            for s in sql_parser(i):
                conn.execute(s)
            print(f'{i} view created or updated successfully')

    print('\n')

    user_input_n1 = input(
        'Would you like to read (1), insert (2) or delete (3) data?: ')

    if user_input_n1 == '1':

        user_input_n2 = input(
            'Would you like to read reports (1) or tables (2)? ')

        if user_input_n2 == '1':

            user_input_n3 = input(
                'Would you like monthly (1) or yearly (2) based reports?: ')

            if user_input_n3 == '1':

                r = engine.connect().execute('SELECT * FROM income_statement_by_month;')
                keys = r.keys()

                table = []

                for row in r:
                    table.append(list(row))

                print('\n')
                print(tabulate(table, headers=keys))

            elif user_input_n3 == '2':

                r = engine.connect().execute('SELECT * FROM income_statement_by_year;')
                keys = r.keys()

                table = []

                for row in r:
                    table.append(list(row))

                print('\n')
                print(tabulate(table, headers=keys))

            if user_input_n3 not in ['1', '2']:
                print('Command not recognized, please start again.')

        if user_input_n2 == '2':

            tables = engine.connect().execute('SHOW TABLES;')
            table_list = []

            print('\n')
            n = 1
            for table in tables:
                print(table[0])
                table_list.append((n, table[0]))
                n += 1

            print(table_list)

#            user_input_n4 = input('Please choose table id: ')

    if user_input_n1 == '2':
        pass
