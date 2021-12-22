"""Function that take a table and insert a new row"""
from config import my_conn, my_cursor

def insert_row(arguments: list[int, str]) -> None:
    """
    list of arguments:
        table_name
        row_id
        val_col1
        val_col2
        ...
    """
    table_name = arguments[1]
    dict_values = {}
    for i in range(len(arguments[2:])):
        dict_values[f"val{i+1}"] = f"'{arguments[i+2]}'"

    update_file = open(f"SQL_statements/rows_querys/insert_row_querys/{table_name}.sql", "r").read().split("#")
    values = []
    for i in dict_values.values():
        values.append(i)
    
    values = f'({",".join([i for i in values])})'

    for line in update_file:
        statement = line.replace('vals', values)
        
        my_cursor.execute(statement)
        my_conn.commit()

    
        
