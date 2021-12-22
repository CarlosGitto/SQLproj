"""Seeds table with random data for testing purposes."""

from functions.random_table_seeder import seed_tables
from functions.random_sale_creator import random_sale_creator

if __name__ == "__main__":

    seed_tables(products_num=10, sales_num=200,
                expense_items_num=20, assigned_expense_items_num=200, customer_num=20, purchase_num=12)
    random_sale_creator(sale_num=20, product_num=10, customer_num=20)