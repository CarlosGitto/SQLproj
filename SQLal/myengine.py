from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine


engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/SQLproj')
Base = declarative_base()
