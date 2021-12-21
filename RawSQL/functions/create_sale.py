"""Defines sale creation function and links it to a batch utilizing FIFO exit method."""
from config import my_cursor, my_conn



def argument_parser_sales(argv: list[str]) -> list[int, str]:
    """
    Prepares sys.argv to be fed to other functions.

    Position 1: product_id
    Position 2: quantity
    Position 3: customer_id
    """

    parsed_arguments = argv[1:]
    return [int(i) for i in parsed_arguments]

def sale_creator(argumments: list[int, str]) -> None:
    product_id, quantity, customer_id = argument_parser_sales(argv=argumments)
    args_from_cli = (product_id, quantity, customer_id)
    my_cursor.callproc("spSaleWorker",args_from_cli)
    my_conn.commit()
