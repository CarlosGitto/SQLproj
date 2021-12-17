"""Select and show tables views"""
from utils import engine
import pandas as pd
import sys

list_of_views = [
    ['1', "income_by_month"],
    ['2', "expenses_by_month"],
    ['3', "income_statement_by_month"],
    ['4', "income_by_year"],
    ['5', "expenses_by_year"],
    ['6', "income_statement_by_year"],
    ['7', "revenue_growth"]
]


if __name__ == "__main__":

    """Call a table view"""
    for id, table in list_of_views:

        if id == sys.argv[1]:
            df = pd.read_sql(f'SELECT * FROM {table};', con=engine)

            print(df)

    if sys.argv not in [i[0] for i in list_of_views]:
        print('Id not recognized.')
