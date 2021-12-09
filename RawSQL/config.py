import mysql.connector

host = "localhost"
user = "root"
passwd = "123456"
database = "SQLproj"

mydb = mysql.connector.connect(
        host = host,
        user = user,
        passwd = passwd,
        database = database
    )

mycursor = mydb.cursor()