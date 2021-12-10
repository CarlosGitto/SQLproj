from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine

user = 'root'
password = '123456'
host = 'localhost'
port = '3306'
db_name = 'SQLproj'

engine = create_engine(
        f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db_name}'
)

Base = declarative_base()