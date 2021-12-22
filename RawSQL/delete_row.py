"""Delete a row base on the given id"""
from functions.delete_row import delete_row
import sys
arguments = sys.argv
if __name__ == "__main__":
    delete_row(arguments=arguments)