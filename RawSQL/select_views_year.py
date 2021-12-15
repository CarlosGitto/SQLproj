"""Select and print income_statement_by_year view."""

import pandas as pd
from config import my_conn

if __name__ == '__main__':
    statement = open(
        'SQL_statements/select_queries/yearly_tables.sql', 'r').read()

    df = pd.read_sql(statement, my_conn)

    print(df)
