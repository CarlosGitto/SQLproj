from connection import mycursor

file_of_views_month = open("RawSQL/select_and_views/select_views_month.sql", "r").read().split(";")
file_of_views_year = open("RawSQL/select_and_views/select_views_year.sql", "r").read().split(";")

def select_views_month():
    file_of_views_month.remove("")
    for index,line in enumerate(file_of_views_month):
        line = line.strip("\n")
        print(str(index+1),". ",line)
    try:  
        pick = input("pick one [1-3]: ")
        print("query: ",file_of_views_month[int(pick)-1])
    except (IndexError, ValueError):
        print("Incorrect index value")
    mycursor.execute(file_of_views_month[int(pick)-1])



def select_views_year():
    file_of_views_year.remove("")
    for index,line in enumerate(file_of_views_year):
        line = line.strip("\n")
        print(str(index+1),". ",line)
    try:  
        pick = input("pick one [1-3]: ")
        print("query: ",file_of_views_year[int(pick)-1])
    except (IndexError, ValueError):
        print("Incorrect index value")
    mycursor.execute(file_of_views_year[int(pick)-1])