"insertar datos sqlal"
from utils import engine
import models
from sqlalchemy.orm import sessionmaker
from values_to_seed.seed_dict_values import expense_family_values, expense_item_values, assigned_expense_values, product_values, sale_values


Session = sessionmaker(engine)
session = Session()

"This lists bring a table CLASS and some values from 'seed_dict_values.py' in the folder 'values_to_seed' "

expense_item_seed = [   {"class":models.ExpenseItem, "values":expense_item_values}  ]


expense_family_seed = [ {"class":models.ExpenseFamily, "values":expense_family_values}   ]


assigned_expense_seed = [   {"class":models.AssignedExpenseItem, "values": assigned_expense_values}    ]


product_seed = [    {"class":models.Product, "values":product_values}   ]


sale_seed = [   {"class":models.Sale, "values":sale_values} ]



def seeder(dict_seed):
    "using for loop to seed each table in the database"
    for item in dict_seed:
        table_class = item["class"]
        row_to_add = []
        for value in item["values"]:
            new_row = table_class(**value)
            row_to_add.append(new_row)
        session.add_all(row_to_add)
        session.commit()

"a list with the right order to seed the tables"
list_of_seed = [
    product_seed,
    sale_seed,
    expense_family_seed,
    expense_item_seed,
    assigned_expense_seed
]


for seed in list_of_seed:
    seeder(seed)