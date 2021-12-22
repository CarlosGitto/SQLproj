"""A function that creates random sales"""
import random
from functions.create_sale import sale_creator

def random_sale_creator(sale_num: int, product_num: int, customer_num: int) -> list[int]:
    for i in range(sale_num):
        
        product_id = random.randint(1,product_num)
        quantity = random.randint(1,1000)
        customer_id = random.randint(1, customer_num)

        my_list = ["", product_id, quantity, customer_id]

        sale_creator(my_list)