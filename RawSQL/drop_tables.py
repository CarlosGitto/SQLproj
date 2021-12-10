from config import mycursor

drop_all_tables = open("RawSQL/querys/drop_all.sql", "r").read().split(";")

def drop_tables():
    """Drop all tables"""
    for line in drop_all_tables:
        mycursor.execute(line)
        mycursor.commit()

