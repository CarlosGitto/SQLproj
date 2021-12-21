from config import my_cursor
sp_alter_stock = open("SQL_statements/sql_procedure/spAlterStock.sql", "r").read()
"""sp_new_sale = open("SQL_statements/sql_procedure/spNewSale.sql", "r").read()
sp_sale_to_purchase = open("SQL_statements/sql_procedure/spSaleToPur.sql", "r").read()
sp_sale_worker = open("SQL_statements/sql_procedure/spSaleWorker.sql", "r").read()"""

list_of_procedures =[
     sp_alter_stock
     #sp_new_sale,
     #sp_sale_to_purchase,
     #sp_sale_worker
]

my_cursor.execute(sp_alter_stock)
