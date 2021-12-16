"""This file take a product id and return purchase id"""
from re import M
from typing import Dict, List
from utils import engine, session
import models

def product_id_in_purchase(sale_quantity: int, product_id : int) -> List[Dict]:

    result = session.query(models.Purchase.id, models.Purchase.in_stock, models.Purchase.cost).filter(
        models.Purchase.product_id == product_id
    ).all()

    stock_to_buy = sale_quantity
    my_purchase_list = []

     

    for purchase in result:
        if purchase[1] < stock_to_buy and purchase[1] > 0:
            stock_to_buy = stock_to_buy - purchase[1]

            my_purchase_list.append({
                "purchase_id": purchase[0],
                "cost": purchase[2]*purchase[1],
                "quantity":purchase[1]
                })
            
            session.query(models.Purchase).filter(
                models.Purchase.id == purchase[0]
            ).update({"in_stock": 0})
            session.commit()

        else:
            my_purchase_list.append({
                "purchase_id": purchase[0],
                "cost": purchase[2]*stock_to_buy,
                "quantity":stock_to_buy
                })
            session.query(models.Purchase).filter(
                models.Purchase.id == purchase[0]
            ).update({"in_stock": f'{purchase[1] - stock_to_buy}'})
            session.commit()
            break
    

        
    return my_purchase_list


#x = product_id_in_purchase(474, 1)

#print(x)
