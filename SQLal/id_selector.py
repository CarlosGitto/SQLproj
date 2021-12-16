"""This file takes a product id and returns purchase id"""
from utils import engine, session
import models


def product_id_in_purchase(sale_quantity: int, product_id: int) -> None:
    """Links sale to purchase for accounting purposes."""

    result = session.query(models.Purchase.id, models.Purchase.in_stock, models.Purchase.cost).filter(
        models.Purchase.product_id == product_id
    ).all()

    stock_to_buy = sale_quantity
    my_purchase_list = []

    print(result)

    for purchase in result:
        if purchase[1] < stock_to_buy:
            stock_to_buy = stock_to_buy - purchase[1]

            my_purchase_list.append(purchase[0])

            session.query(models.Purchase).filter(
                models.Purchase.id == purchase[0]
            ).update({"in_stock": 0})
            session.commit()

        else:

            session.query(models.Purchase).filter(
                models.Purchase.id == purchase[0]
            ).update({"in_stock": f'{purchase[1] - stock_to_buy}'})
            session.commit()
            my_purchase_list.append(purchase[0])
            break

    print(my_purchase_list)


"""def func():
    cost_sale = product_id_in_purchase()

    engine.execute("INSERT INTO VIEW sale_cost (cost) value cost_sale
    where id_ssale == 1")"""


product_id_in_purchase(sale_quantity=107, product_id=4)
