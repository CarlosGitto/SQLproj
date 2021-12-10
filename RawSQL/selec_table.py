from config import mycursor

select_all_from_table = open("RawSQL/querys/select_table.sql", "r").read().split(";")

def select_table():
    for index,line in enumerate(select_all_from_table):
        line = line.strip("\n")
        print(str(index+1),". ",line)
        
    pick = input("pick one [1-5]")
    mycursor.execute(select_all_from_table[int(pick)-1])
    mycursor.commit()

select_table()
