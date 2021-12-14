"""Creates database if theres not a database with the specified name."""

import mysql.connector

host = "localhost"
user = "root"
password = "root2021"
db_name = "sql_challenge"


def db_creator(database_name: str) -> str:
    """Creates database in server using credentials."""

    mydb = mysql.connector.connect(
        host=host,
        user=user,
        passwd=password
    )
    mycursor = mydb.cursor()
    mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
    return database_name


db_name = db_creator(db_name)
print(db_name)
