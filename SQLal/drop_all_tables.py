from sqlalchemy.engine import base
import models
from utils import engine, Base


"""Drop all tables"""
Base.metadata.drop_all(engine)
