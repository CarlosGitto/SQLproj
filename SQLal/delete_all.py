from sqlalchemy.engine import base
import models
from utils import engine, Base


Base.metadata.drop_all(engine)
