"""This file take a product id and return purchase id"""
from SQLal.models import Purchase
from utils import engine, session
import models

def product_id_in_purchase(product_id : int) -> int:

    result = session.query(models.Purchase.id).filter(
        models.Purchase.product_id == product_id
    ).fetchone()

    return result
