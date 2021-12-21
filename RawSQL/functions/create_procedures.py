"""Define a function that read and execute files that create procedures"""

from config import my_cursor, my_conn

sp_alter_stock = open("SQL_statements/sql_procedure/spAlterStock.sql", "r").read().split("#")
sp_new_sale = open("SQL_statements/sql_procedure/spNewSale.sql", "r").read().split("#")
sp_sale_to_purchase = open("SQL_statements/sql_procedure/spSaleToPur.sql", "r").read().split("#")
sp_sale_worker = open("SQL_statements/sql_procedure/spSaleWorker.sql", "r").read().split("#")
sp_purchase_id = open("SQL_statements/sql_procedure/spPurchaseID.sql", "r").read().split("#")

list_of_procedures = [
    sp_alter_stock,
    sp_new_sale,
    sp_sale_to_purchase,
    sp_sale_worker,
    sp_purchase_id
]

def create_procedures() -> None:
    """Create all procedures"""
    for procedure in list_of_procedures:
        try:
            procedure.remove("")
        except:
            pass
        for line in procedure:
            line = line.strip("\n")
            my_cursor.execute(line)
            my_conn.commit()
