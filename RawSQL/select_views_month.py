"""Select and print income_statement_by_month view."""

import pandas as pd
from config import my_conn

if __name__ == '__main__':
    statement = open(
        'SQL_statements/select_queries/monthly_tables.sql', 'r').read()

    df = pd.read_sql(statement, my_conn)

    print(df)
