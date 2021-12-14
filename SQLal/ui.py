from utils import engine
from tabulate import tabulate
from sqlalchemy.orm import sessionmaker
from models import Product, Sale, AssignedExpenseItem, ExpenseFamily, ExpenseItem

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
            if id == i[0]:
                model = i[1]

                possible_commands = [
                    {
                        "model": "product",
                        "attributes": [
                            "price",
                            "cost",
                            "stock"
                        ]
                    },
                    {
                        "model": "expense_family",
                        "attributes": [
                            "service_name"
                        ]
                    },
                    {
                        "model": "assigned_expense_item",
                        "attributes": [
                            "service_name"
                        ]
                    },
                    {
                        "model": "sale",
                        "attributes": [
                            "created_at",
                            "product_id"
                        ]
                    },
                    {
                        "model": "expense_item",
                        "attributes": [
                            "service_name"
                        ]
                    }
                ]

                for j in possible_commands:
                    if j["model"] == model:
                        attributes = {}
                        for at in j['attributes']:
                            attributes[f'{at}'] = input(
                                f'Please type {at} to insert: ')

                row = model(attributes)

                session.add(row)
                session.commit()

                main()

    if user_input_n1 == '3':
        pass

    if user_input_n1 not in ['1', '2', '3']:
        print('Command not recognized.\n')

        main()
