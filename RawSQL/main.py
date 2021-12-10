from config import mycursor
from make_tables import create_tables
from drop_tables import drop_tables
"""
expenseitems = cablevision
expensefamily = internet
assignedexpense = 2 unidades de cablevision
"""
drop_tables()
create_tables()

mycursor.execute("")