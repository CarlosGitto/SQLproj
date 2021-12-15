"""File that create tables in the database"""
from utils import engine, Base
import models

"""Create all tables"""
Base.metadata.create_all(engine)
