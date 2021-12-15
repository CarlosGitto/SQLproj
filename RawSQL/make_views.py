"""Creates or updates views in the database."""

from config import my_cursor

create_all_views_month = open(
    "SQL_statements/views_creation/income_statement_by_month.sql", "r").read().split(";")
create_all_views_year = open(
    "SQL_statements/views_creation/income_statement_by_year.sql", "r").read().split(";")


def create_views() -> None:
    """Create all views"""
    try:
        create_all_views_month.remove("")
        create_all_views_year.remove("")
    except:
        pass
    for line in create_all_views_month:
        line = line.strip("\n")
        my_cursor.execute(line)

    for line in create_all_views_year:
        line = line.strip("\n")
        my_cursor.execute(line)


if __name__ == "__main__":

    create_views()
