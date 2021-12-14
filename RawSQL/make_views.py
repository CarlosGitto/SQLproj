from connection import mycursor

create_all_views_month = open("RawSQL/select_and_views/income_statement_by_month.sql", "r").read().split(";")
create_all_views_year = open("RawSQL/select_and_views/income_statement_by_year.sql", "r").read().split(";")
def create_views():
    """Create all views"""
    try:
        create_all_views_month.remove("")
        create_all_views_year.remove("")
    except:
        pass
    for line in create_all_views_month:
        line = line.strip("\n")
        mycursor.execute(line)

    for line in create_all_views_year:
        line = line.strip("\n")
        mycursor.execute(line)
