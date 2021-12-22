"""Function that take an id and a table to update the row"""

from config import my_cursor, my_conn

def update_row(arguments: list[int, str]) -> None:
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

    update_file = open(f"SQL_statements/rows_querys/update_row_querys/{table_name}.sql", "r").read().split("#")
                    
   
    for line in update_file:
        
        for i, j in dict_values.items():
            line = line.replace(i,j)
        print(line)
        my_cursor.execute(line)
        my_conn.commit()