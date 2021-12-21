"""Define a funtion that read a file with drop procedures sentences."""

from config import my_cursor, my_conn

drop_procedure_file = open("SQL_statements/sql_procedure/drop_procedures.sql", "r").read().split("#")

def drop_procedures() -> None:
    """Drop all procedures"""
    try:
        drop_procedure_file.remove("")
    except:
        pass
    for line in drop_procedure_file:
        line = line.strip("\n")
        my_cursor.execute(line)
        my_conn.commit()
