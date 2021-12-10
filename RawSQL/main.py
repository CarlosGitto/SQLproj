from RawSQL.selec_table import select_table
from config import mycursor
from RawSQL.make_tables import create_tables
from RawSQL.drop_tables import drop_tables
"""
expenseitems = cablevision
expensefamily = internet
assignedexpense = 2 unidades de cablevision
"""
drop_tables()
create_tables()
select_table()

mycursor.execute("")