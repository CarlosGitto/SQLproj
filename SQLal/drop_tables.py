"""Remove all tables and views."""

from utils import engine, Base
import models


if __name__ == "__main__":
    Base.metadata.drop_all(engine)
