from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine

user = 'root'
password = 'root2021'
host = 'localhost'
port = '3306'
db_name = 'sql_challenge'

engine = create_engine(
        f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db_name}'
)

Base = declarative_base()
