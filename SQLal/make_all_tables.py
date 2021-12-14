import models
from utils import engine, Base


"""Create all tables"""
Base.metadata.create_all(engine)
