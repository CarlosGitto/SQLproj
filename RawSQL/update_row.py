"""Update a row taking values to update as args"""

from functions.update_row import update_row
import sys

arguments = sys.argv

if __name__ == "__main__":
    update_row(arguments=arguments)