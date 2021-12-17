"""This file selects table/s to show"""
from utils import engine,session
from models import Product, Sale, ExpenseFamily, ExpenseItem, Customer
from models import AssignedExpenseItem as assei
from models import SaleToPurchase as stp
import sys
import pandas as pd


def select_product():
    s = session.query(Product.id, Product.price).all()
    return s


def select_family():
    s = session.query(ExpenseFamily.id, ExpenseFamily.service_name).all()
    return s


def select_item():
    s = session.query(ExpenseItem.id, ExpenseItem.item_name,
                      ExpenseItem.family_id, ExpenseItem.cost).all()
    return s


def select_assigned():
    s = session.query(assei.id, assei.item_id, assei.state,
                      assei.created_at).all()
    return s


def select_sale():
    s = session.query(Sale.id, Sale.product_id, Sale.created_at).all()
    return s

def select_sale_to_purchase():
    s = session.query(stp.id, stp.purchase_id, stp.quantity, stp.sale_id).all()
    return s

def select_customer():
    s = session.query(Customer.id, Customer.name, Customer.surname, Customer.phone_number, Customer.email).all()
    return s


list_of_select = [
    "product",
    "customer",
    "sale_to_purchase",
    "sale",
    "expense_family",
    "expense_item",
    "assigned_expense_item"
]


def show_table(s):
    for item in s:
        print(item)


def circular():
    for func in list_of_select:
        s = func()
        for item in s:
            print(item)
        print("\n")


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
    