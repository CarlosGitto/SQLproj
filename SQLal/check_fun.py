"""This file have a function that check stock, quantity, and product"""

from typing import Dict, List

from sqlalchemy.orm import with_expression
import models
from utils import engine, session

def product_checker(product_id : int) -> List[Dict]:

    """Use the product_id to return the stock and quantity of it"""

    my_list = [product_id]

    result = session.query(models.Purchase.in_stock, models.Purchase.quantity).filter(
        models.Purchase.product_id == product_id
    ).one()

    for i, value in enumerate(result):
        my_list.append(value)

    return my_list

"""quantity -> sale ->update with_expression

4 -> purchase_id
costo 400

client -> sale product_id ->""" 