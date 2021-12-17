"""Select and show tables views"""
from utils import engine
import sys


def select_views(view_name):
    """Select a table view"""
    with engine.connect():
        y = engine.execute("SELECT * FROM {}".format(view_name)).fetchall()
        for item in y:
            print(item)
    print(view_name, "\n")


list_of_views = [
    "income_by_month",
    "expenses_by_month",
    "income_statement_by_month",
    "income_by_year",
    "expenses_by_year",
    "income_statement_by_year",
    "revenue_growth"
]


if __name__ == "__main__":

    """Call a table view"""
    if len(sys.argv) == 3:
        tag1 = sys.argv[1]
        tag2 = sys.argv[2]

        if tag1 == "year":
            if tag2 == "1":
                select_views("income_by_year")
            if tag2 == "2":
                select_views("expenses_by_year")
            if tag2 == "3":
                select_views("income_statement_by_year")

        if tag1 == "month":
            if tag2 == "1":
                select_views("income_by_month")
            if tag2 == "2":
                select_views("expenses_by_month")
            if tag2 == "3":
                select_views("income_statement_by_month")
    else:
        tag1 = sys.argv[1]
        if tag1 == "all":
            for vw_name in list_of_views:
                select_views(vw_name)
