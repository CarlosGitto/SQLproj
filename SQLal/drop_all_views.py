from select_view import list_of_views
from utils import engine

def drop_all_views():
    with engine.connect():
        for i in list_of_views:
            engine.execute("DROP VIEW {}".format(i))

if __name__ == "__main__":
    drop_all_views()