"""This file deletes tables from the database"""

from utils import engine, Base
import models

"""Drop all tables"""
Base.metadata.drop_all(engine)
