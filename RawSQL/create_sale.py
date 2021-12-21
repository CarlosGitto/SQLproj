"""Create a sale from CLI and affect all the related tables"""
import sys
from functions.create_sale import sale_creator

if __name__ == "__main__":
    """
    list_of_argumments: 
            .product_id
            .quantity
            .customer_id
    """
    list_of_argumments = sys.argv
    sale_creator(argumments=list_of_argumments)