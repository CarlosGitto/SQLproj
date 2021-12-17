from utils import engine

list_of_views = [
    "income_by_month",
    "expenses_by_month",
    "income_statement_by_month",
    "income_by_year",
    "expenses_by_year",
    "income_statement_by_year",
    "revenue_growth"
]


def drop_all_views():
    with engine.connect():
        for i in list_of_views:
            engine.execute("DROP VIEW {}".format(i))


if __name__ == "__main__":
    drop_all_views()
