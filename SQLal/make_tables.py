import models
from utils import engine, Base


Base.metadata.create_all(engine)
