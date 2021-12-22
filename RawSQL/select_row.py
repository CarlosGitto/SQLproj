"""Select a row base on the given id"""

from functions.select_row import select_row
import sys

arguments = sys.argv

if __name__ == "__main__":
    select_row(arguments=arguments)