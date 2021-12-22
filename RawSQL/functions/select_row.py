"""Function that take an id and a table to select a row"""

from config import my_cursor, my_conn
import pandas as pd

def select_row(arguments: list[int, str]) -> None:
    table_name = arguments[1]
    row_id = arguments[2]
    
    df = pd.read_sql(f"SELECT * FROM {table_name} WHERE {table_name}.id = {row_id};", con=my_conn)

    print (df)
    