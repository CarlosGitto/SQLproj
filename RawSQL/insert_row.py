"""Used to insert values into tables."""
from functions.insert_row import insert_row
import sys

arguments = sys.argv

if __name__ == "__main__":
    insert_row(arguments=arguments)
