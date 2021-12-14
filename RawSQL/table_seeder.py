import datetime
import random
import string
from connection import mycursor, mydb


def seed_tables(products_num: int, sales_num: int, expense_items_num: int, assigned_expense_items_num: int) -> None:
    """Creates and uploads randomly created rows for testing purposes."""

    """ Read a file of SQL statements and split them by ';' """

    insert_file = open("SQL_statements/insert_queries/insert.sql",
                       "r").read().split(";")

    for sql_statement in insert_file:

        """Select the correct data for the correct table to seed"""

        if "product" in sql_statement and "product_id" not in sql_statement:
            for i in range(products_num):
                price = random.randint(0, 100000)
                cost = random.randint(0, price)
                stock = random.randint(1, 100)
                values = (price, cost, stock)
                mycursor.execute(sql_statement, values)
                mydb.commit()

        if "sale" in sql_statement and "sale_id" not in sql_statement:
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
                values = (product_id, created_at)
                mycursor.execute(sql_statement, values)
                mydb.commit()

        if "expense_family" in sql_statement:
            for i in range(4):
                values = [("hr",), ("others",), ("fianance",), ("marketing",)]
                mycursor.execute(sql_statement, values[i])
                mydb.commit()

        if "expense_item" in sql_statement and "assigned" not in sql_statement:
            for i in range(expense_items_num):
                item_name = ''.join(random.choices(string.ascii_letters, k=10))
                item_family = random.randint(1, 4)
                item_cost = random.randint(1, 20000)
                values = (item_name, item_family, item_cost)
                mycursor.execute(sql_statement, values)
                mydb.commit()

        if "assigned_expense_item" in sql_statement:
            def get_random_saleid(min_val: int, max_val: int, none_probability: float):
                if random.random() < none_probability:
                    return None
                else:
                    return random.randint(min_val, max_val)
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
                sale_id = get_random_saleid(1, sales_num, 0.8)
                values = (item_id, state, created_at, sale_id)
                mycursor.execute(sql_statement, values)
                mydb.commit()


if __name__ == "__main__":

    seed_tables(products_num=10, sales_num=200,
                expense_items_num=20, assigned_expense_items_num=200)
