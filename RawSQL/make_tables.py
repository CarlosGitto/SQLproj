from config import mycursor

create_all_tables = open("RawSQL/querys/create_all.sql", "r").read().split(";")


def create_tables():
    """Create all tables"""
    for line in create_all_tables:
        mycursor.execute(line)
        mycursor.commit()


