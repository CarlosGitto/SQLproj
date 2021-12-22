"""Function that take an id and a table to delete a row"""

from config import my_cursor, my_conn

def delete_row(arguments: list[int, str]) -> None:
    table_name = arguments[1]
    row_id = arguments[2]

    deleter_file = open(f"SQL_statements/rows_querys/delete_row_querys/{table_name}.sql", "r").read().split("#")

    for line in deleter_file:
        line = line.replace("val",row_id)
        my_cursor.execute(line)
        my_conn.commit()


