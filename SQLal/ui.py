from utils import engine
from tabulate import tabulate
from sqlalchemy.orm import sessionmaker
from models import Product, Sale, AssignedExpenseItem, ExpenseFamily, ExpenseItem
from datetime import datetime

session = sessionmaker(engine)()

income_statement_by_month = "/Users/juanpena/Desktop/SQL_pr/SQLproj/SQLal/SQL_commands/view_generators/income_statement_by_month.sql"
income_statement_by_year = "/Users/juanpena/Desktop/SQL_pr/SQLproj/SQLal/SQL_commands/view_generators/income_statement_by_year.sql"


def sql_parser(file_path: str) -> list[str]:
    """Takes .sql file and returns a list of statements in it."""
    statements = open(file_path).read()
    statement_list = []

    for statement in statements.split('#'):
        corrected = statement.replace('\n', ' ')
        statement_list.append(corrected)

    return statement_list


def view_generator() -> None:
    """Creates or updates views inside the dbrm."""
    with engine.connect() as conn:
        for i in [income_statement_by_month, income_statement_by_year]:
            print(f'...creating or updating view for {i}')
            for s in sql_parser(i):
                conn.execute(s)
            print(f'{i} view created or updated successfully\n')


def main() -> None:
    """Main command line ui application."""

    tables = engine.connect().execute('SHOW TABLES;')
    table_list = []
    n = 1
    for table in tables:
        table_list.append([n, table[0]])
        n += 1

    table_index = tabulate(table_list, headers=tables.keys())

    user_input_n1 = input(
        'Would you like to read (1), insert (2) or delete (3) data? please choose by id: ')

    if user_input_n1 == '1':

        print('\n')
        print(table_index)
        print('\n')

        id = input('Select table by id number: ')

        for i in table_list:
            if id == str(i[0]):

                select = open(
                    f'/Users/juanpena/Desktop/SQL_pr/SQLproj/SQLal/SQL_commands/queries/{i[-1]}.sql').read()
                r = engine.connect().execute(select)

                query = []
                keys = r.keys()
                for row in r:
                    query.append(list(row))

                print('\n')
                print(tabulate(query, headers=keys))

                print('\n')
                main()

    if user_input_n1 == '2':
        models_list = [
            ['1', 'product', Product],
            ['2', 'sale', Sale],
            ['3', 'assigned_expense_item', AssignedExpenseItem],
            ['4', 'expense_family', ExpenseFamily],
            ['5', 'expense_item', ExpenseItem]
        ]

        print('\n')
        print(tabulate([[i[0], i[1]]
              for i in models_list], headers=['id', 'table']))
        print('\n')
        id = input('Select table to insert data into by id number: ')

        for i in models_list:
            if id == '1':
                price = int(input('Input price: '))
                cost = int(input('Input cost: '))
                stock = int(input('Input stock: '))

                engine.execute(
                    f"INSERT INTO product (price, cost, stock) VALUES ({price},{cost},{stock});")
                print('New row added successfully. \n')

                main()

            if id == '2':

                created_at = datetime(
                    input('Input date in Y, M, D, H, M, S format: '))
                product_id = input('Input product id: ')

                engine.execute(
                    f"INSERT INTO sale (created_at, product_id) VALUES ({created_at},{product_id});")
                print('New row added successfully. \n')

                main()

            if id == '3':
                created_at = datetime(
                    input('Input date in Y, M, D, H, M, S format: '))
                item_id = int(input('Input product id: '))
                state = input(
                    'Input state, either "pagado" or "no pagado": ')
                sale_id = int(input('Input sale id if applies: '))

                engine.execute(
                    f" INSERT INTO assigned_expense_item (created_at, item_id, state, sale_id) VALUES ({created_at}, {item_id}, {state}, {sale_id});")
                print('New row added successfully. \n')

                main()

            if id == '4':
                service_name = input('Input new expense family: ')

                engine.execute(
                    f"INSERT INTO expense_family (service_name) VALUES ({service_name});")
                print('New row added successfully. \n')

                main()

            if id == '5':

                item_name = input('Input new item name: ')
                family_id = input('Input family id: ')
                cost = int(input('Input cost: '))

                engine.execute(
                    f"INSERT INTO expense_item (item_name, family_id, cost) VALUES ({item_name}, {family_id}, {cost})")
                print('New row added successfully. \n')

                main()

            if id not in ['1', '2', '3', '4', '5']:
                print('Command not recognized. \n')

                main()

    if user_input_n1 == '3':
        models_list = [
            ['1', 'product', Product],
            ['2', 'sale', Sale],
            ['3', 'assigned_expense_item', AssignedExpenseItem],
            ['4', 'expense_family', ExpenseFamily],
            ['5', 'expense_item', ExpenseItem]
        ]

        print('\n')
        print(tabulate([[i[0], i[1]]
              for i in models_list], headers=['id', 'table']))
        print('\n')

        id = input('Select table by id number: ')

        for i in models_list:
            if id == str(i[0]):

                select = open(
                    f'/Users/juanpena/Desktop/SQL_pr/SQLproj/SQLal/SQL_commands/queries/{i[1]}.sql').read()
                r = engine.connect().execute(select)

                query = []
                keys = r.keys()
                for row in r:
                    query.append(list(row))

                print('\n')
                print(tabulate(query, headers=keys))

                print('\n')
                id_to_delete = input('Input id to delete: ')

                engine.execute(
                    f"DELETE FROM {i[1]} WHERE id = {id_to_delete};")

                print('Row has been deleted successfully.\n')

                main()

    if user_input_n1 not in ['1', '2', '3']:
        print('Command not recognized.\n')

        main()
