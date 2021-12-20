"""This file selects table/s to show"""
from utils import engine,session

import sys
import pandas as pd


list_of_select = [
    "product",
    "customer",
    "sale_to_purchase",
    "sale",
    "expense_family",
    "expense_item",
    "assigned_expense_item"
]




if __name__ == "__main__":

    tag = sys.argv[1]

    if tag == "product":
        df = pd.read_sql(f"SELECT * FROM {tag};", con=engine)
        print(df)

    if tag == "sale":
        df = pd.read_sql(f"SELECT * FROM {tag};", con=engine)
        print(df)

    if tag == "item":
        df = pd.read_sql(f"SELECT * FROM {tag};", con=engine)
        print(df)

    if tag == "family":
        df = pd.read_sql(f"SELECT * FROM {tag};", con=engine)
        print(df)

    if tag == "assei":
        df = pd.read_sql(f"SELECT * FROM {tag};", con=engine)
        print(df)

    if tag == "stp":
        df = pd.read_sql(f"SELECT * FROM {tag};", con=engine)
        print(df)
    if tag == "cust":
        df = pd.read_sql(f"SELECT * FROM {tag};", con=engine)
        print(df)

    if tag == "all":
        for table in list_of_select:
            df = pd.read_sql(f"SELECT * FROM {table};", con=engine)
            print(table.upper(),"\n\n",df , "\n\n\n")
    