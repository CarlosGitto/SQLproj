"""Select queries by table."""

import sys
from config import my_cursor

flag = sys.argv[1]

possible_arguments = [
    ['1', 'product'],
    ['2', 'sale'],
    ['3', 'expense_family'],
    ['4', 'expense_item'],
    ['5', 'assigned_expense_item']
]

if __name__ == "__main__":

    for i in possible_arguments:
        if i[0] == flag:

            statement = open(
                f'SQL_statements/select_queries/{i[1]}.sql', 'r').read()

            my_cursor.execute(statement)

            query = my_cursor.fetchall()

            for row in query:
                print(row)

        elif flag not in [i[0] for i in possible_arguments]:

            print('Flag not recognized.')
