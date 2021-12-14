from config import user,db_name,host,password
import mysql.connector

mydb = mysql.connector.connect(
        host = host,
        user = user,
        passwd = password,
        database = db_name
    )
    
mycursor = mydb.cursor()
