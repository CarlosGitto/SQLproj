from connection import mycursor

create_all_tables = open("RawSQL/create_drop_querys/create_all.sql", "r").read().split(";")


def create_tables():
    """Create all tables"""
    for line in create_all_tables:
        mycursor.execute(line)

create_tables()