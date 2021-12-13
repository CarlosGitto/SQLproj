from utils import engine
import models
from values_to_seed.random_seed_generator import random_assigned_expense_item_engine, random_expense_family_engine, random_expense_item_engine, random_product_engine, random_sale_engine
from sqlalchemy.orm import sessionmaker
# from values_to_seed.seed_dict_values import expense_family_values, expense_item_values, assigned_expense_values, product_values, sale_values


Session = sessionmaker(engine)
session = Session()

"""Seeds database with random values used for testing purposes."""

families = [
    {
        "service_name": "marketing"
    },
    {
        "service_name": "finance"
    },
    {
        "service_name": "hr"
    },
    {
        "service_name": "others"
    }
]

expense_items = random_expense_item_engine(50, families=families)
products = random_product_engine(10)
sales = random_sale_engine(1000, product=products)
assigned_expenses = random_assigned_expense_item_engine(
    200, items=expense_items, sales=sales)

expense_item_seed = [
    {"class": models.ExpenseItem, "values": expense_items}]


expense_family_seed = [
    {"class": models.ExpenseFamily, "values": families}]


assigned_expense_seed = [
    {"class": models.AssignedExpenseItem, "values": assigned_expenses}]


product_seed = [{"class": models.Product, "values": products}]


sale_seed = [{"class": models.Sale, "values": sales}]


def seeder(dict_seed):
    """Using for loop to seed each table in the database"""
    for item in dict_seed:
        table_class = item["class"]
        row_to_add = []
        for value in item["values"]:
            new_row = table_class(**value)
            row_to_add.append(new_row)
        session.add_all(row_to_add)
        session.commit()


"""A list with the right order to seed the tables"""
list_of_seed = [
    product_seed,
    sale_seed,
    expense_family_seed,
    expense_item_seed,
    assigned_expense_seed
]


for seed in list_of_seed:
    seeder(seed)
