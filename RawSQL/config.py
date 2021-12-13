import mysql.connector

host = "localhost"
user = "root"
password = "123456"
db_name = "SQLproj"

def db_creator(database_name):
    mydb = mysql.connector.connect(
        host = host,
        user = user,
        passwd = password
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(database_name))
    return database_name


db_name = db_creator(db_name)
print(db_name)


