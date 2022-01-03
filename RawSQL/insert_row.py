"""Used to insert values into tables."""
from functions.insert_row import insert_row
import sys

arguments = sys.argv

if __name__ == "__main__":
    """
    list of arguments:
        table_name
        row_id
        val_col1
        val_col2
        ...
    """
    insert_row(arguments=arguments)
