"""This file selects table/s to show"""
from utils import session
from models import Product, Sale, ExpenseFamily, ExpenseItem
from models import AssignedExpenseItem
import sys
import pandas as pd


def select_product():
    s = session.query(Product.id, Product.price,
                      Product.cost, Product.stock).all()
    return s


def select_family():
    s = session.query(ExpenseFamily.id, ExpenseFamily.service_name).all()
    return s


def select_item():
    s = session.query(ExpenseItem.id, ExpenseItem.item_name,
                      ExpenseItem.family_id, ExpenseItem.cost).all()
    return s


def select_assigned():
    s = session.query(AssignedExpenseItem.id, AssignedExpenseItem.item_id, AssignedExpenseItem.state,
                      AssignedExpenseItem.created_at, AssignedExpenseItem.sale_id).all()
    return s


def select_sale():
    s = session.query(Sale.id, Sale.product_id, Sale.created_at).all()
    return s


list_of_select = [
    select_product,
    select_sale,
    select_family,
    select_item,
    select_assigned
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
        print("PRODUCT TABLE")
        show_table(select_product())

    if tag == "sale":
        print("SALE TABLE")
        show_table(select_sale())

    if tag == "item":
        print("EXPENSE ITEM TABLE")
        show_table(select_item())

    if tag == "family":
        print("EXPENSE FAMILY TABLE")
        show_table(select_family())

    if tag == "assei":
        print("ASSIGNED EXPENSE ITEM TABLE")
        show_table(select_assigned())

    if tag == "all":
        print("ALL tables")
        circular()
