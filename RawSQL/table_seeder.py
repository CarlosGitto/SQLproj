"""Seeds table with random data for testing purposes."""

import datetime
from os import stat
import random
import string
from config import my_cursor, my_conn


def seed_tables(products_num: int, sales_num: int, expense_items_num: int, assigned_expense_items_num: int, customer_num: int, purchase_num: int) -> None:
    """Creates and uploads randomly created rows for testing purposes."""

    """ Read a file of SQL statements and split them by ';' """

    insert_file = open("SQL_statements/insert_queries/insert.sql",
                       "r").read().split("#")

    for sql_statement in insert_file:

        """Select the correct data for the correct table to seed"""

        if "product" in sql_statement and "product_id" not in sql_statement:
            for i in range(products_num):
                price = random.randint(0, 100000)
                values = f"({price})"

                statement = sql_statement.replace('vals', values)
                my_cursor.execute(statement)
                my_conn.commit()

        if 'customer' in sql_statement and 'customer_id' not in sql_statement:

            for i in range(customer_num):
                name = ''.join(random.choices(string.ascii_letters, k=10))
                surname = ''.join(random.choices(string.ascii_letters, k=10))
                phone_number = int(''.join(
                    random.choices(
                        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], k=9)
                ))
                email = ''.join(random.choices(string.ascii_letters, k=10))

                values = f'("{name}", "{surname}", {phone_number}, "{email}")'

                statement = sql_statement.replace('vals', values)
                my_cursor.execute(statement)
                my_conn.commit()

        if "purchase" in sql_statement and "purchase_id" not in sql_statement:
            for i in range(sales_num):
                product_id = random.randint(1, products_num)

                created_at = datetime.datetime(
                    random.randint(2010, 2021),
                    random.randint(1, 12),
                    random.randint(1, 28),
                    random.randint(1, 23),
                    random.randint(1, 59),
                    random.randint(1, 59)
                )

                cost = random.randint(1, 2000)
                quantity = random.randint(1, 200)
                in_stock = quantity

                values = f'({product_id}, {quantity}, {cost}, {in_stock}, "{created_at}")'

                statement = sql_statement.replace('vals', values)
                my_cursor.execute(statement)
                my_conn.commit()

        # if "sale" in sql_statement and "sale_id" not in sql_statement:
        #     for i in range(sales_num):
        #         purchase_id = random.randint(1, purchase_num)

        #         created_at = datetime.datetime(
        #             random.randint(2010, 2021),
        #             random.randint(1, 12),
        #             random.randint(1, 28),
        #             random.randint(1, 23),
        #             random.randint(1, 59),
        #             random.randint(1, 59)
        #         )
        #         customer_id = random.randint(1, client_num)
        #         quantity = random.randint(1, 5)

        #         values = f'({purchase_id}, "{created_at}", {quantity}, {customer_id})'

        #         statement = sql_statement.replace('vals', values)
        #         my_cursor.execute(statement)
        #         my_conn.commit()

        if "expense_family" in sql_statement:
            for i in ['("hr")', '("others")', '("fianance")', '("marketing")']:
                statement = sql_statement.replace('vals', i)
                my_cursor.execute(statement)
                my_conn.commit()

        if "expense_item" in sql_statement and "assigned" not in sql_statement:
            for i in range(expense_items_num):
                item_name = ''.join(random.choices(string.ascii_letters, k=10))
                item_family = random.randint(1, 4)
                item_cost = random.uniform(0.0, 20000.0)
                values = f'("{item_name}", {item_family}, {item_cost})'

                statement = sql_statement.replace('vals', values)
                my_cursor.execute(statement)
                my_conn.commit()

        if "assigned_expense_item" in sql_statement:

            for i in range(assigned_expense_items_num):
                item_id = random.randint(1, expense_items_num)
                state = random.choice(["pagado", "no pagado"])
                created_at = datetime.datetime(
                    random.randint(2010, 2021),
                    random.randint(1, 12),
                    random.randint(1, 28),
                    random.randint(1, 23),
                    random.randint(1, 59),
                    random.randint(1, 59)
                )
                values = f'({item_id}, "{state}", "{created_at}")'

                statement = sql_statement.replace('vals', values)
                my_cursor.execute(statement)
                my_conn.commit()


if __name__ == "__main__":

    seed_tables(products_num=10, sales_num=200,
                expense_items_num=20, assigned_expense_items_num=200, customer_num=20, purchase_num=12)
