"""Generate random values to be used for the 'seed_tables.py' file"""
import random
import string
import datetime
from typing import Dict, List, Union


def random_expense_family_engine(num_families: int) -> List[Dict]:
    """Creates list of json objects to seed expense_family table for testing purposes."""

    my_families = []

    for i in range(num_families):
        random_family = ''.join(random.choices(string.ascii_letters, k=6))
        my_families.append(random_family)

    my_list = [{"service_name": family} for family in my_families]

    return my_list


def random_expense_item_engine(num_expenses: int, families: List) -> List[Dict]:
    """Creates list of json objects to seed expense_item table for testing purposes."""

    my_list = []
    num_families = len(families)

    for i in range(num_expenses):
        item_name = ''.join(random.choices(string.ascii_letters, k=10))
        item_family = random.randint(1, num_families)
        item_cost = random.uniform(0.0, 20000.0)

        random_row = {
            "item_name": item_name,
            "family_id": item_family,
            "cost": item_cost
        }

        my_list.append(random_row)

    return my_list


def random_assigned_expense_item_engine(num_assigned_expenses: int, items: List, sales: List) -> List[Dict]:
    """Creates list of json objects to seed assigned_expense_item table for testing purposes."""

    my_list = []
    num_items = len(items)
    num_sales = len(sales)

    def get_random_sale_id(minval: int, maxval: int, none_probability: float) -> Union[int, None]:
        """Takes maximum, minimum and none probability, returns either an integer or none object."""

        if random.random() < none_probability:
            return None
        else:
            return random.randint(minval, maxval)

    for i in range(num_assigned_expenses):
        item_id = random.randint(1, num_items)

        created_at = datetime.datetime(
            random.randint(2010, 2021),
            random.randint(1, 12),
            random.randint(1, 28),
            random.randint(1, 23),
            random.randint(1, 59),
            random.randint(1, 59)
        )

        state = random.choice(['pagado', 'no pagado'])
        sale_id = get_random_sale_id(1, num_sales, 0.8)

        random_row = {
            "item_id": item_id,
            "state": state,
            "created_at": created_at,
            "sale_id": sale_id
        }

        my_list.append(random_row)

    return my_list


def random_product_engine(num_products: int) -> List[Dict]:
    """Creates list of json objects to seed product table for testing purposes."""

    my_list = []

    for i in range(num_products):
        price = random.randint(0, 100000)
        cost = random.randint(0, price)
        stock = random.randint(1, 100)

        random_row = {
            "price": price,
            "cost": cost,
            "stock": stock
        }

        my_list.append(random_row)

    return my_list


def random_sale_engine(num_sales: int, product: List) -> List[Dict]:
    """Creates list of json objects to seed sale table for testing purposes."""

    my_list = []
    num_products = len(product)

    for i in range(num_sales):
        product_id = random.randint(1, num_products)
        created_at = datetime.datetime(
            random.randint(2010, 2021),
            random.randint(1, 12),
            random.randint(1, 28),
            random.randint(1, 23),
            random.randint(1, 59),
            random.randint(1, 59)
        )

        random_row = {
            "product_id": product_id,
            "created_at": created_at
        }

        my_list.append(random_row)
    return my_list
