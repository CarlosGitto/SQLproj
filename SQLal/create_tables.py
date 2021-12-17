"""File that create tables in the database"""
from utils import engine, Base

"""Create all tables"""

if __name__ == '__main__':
    Base.metadata.create_all(engine)
