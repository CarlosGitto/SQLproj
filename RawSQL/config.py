"""Creates database if theres not a database with the specified name."""

import mysql.connector

host = "localhost"
user = "root"
password = "123456"
db_name = "sql_challenge"




def connection_factory(server_host: str, server_user: str, server_password: str, server_database_name: str) -> tuple[object,object]:
    """Establishes connection with MySQL server."""

    connection = mysql.connector.connect(
        host=server_host,
        user=server_user,
        password=server_password
    )

    my_cursor = connection.cursor()

    my_cursor.execute(f"CREATE DATABASE IF NOT EXISTS {server_database_name}")
    my_cursor.close()
    connection.close()

    final_connection = mysql.connector.connect(
        host = server_host,
        user = server_user,
        password = server_password,
        database = server_database_name
    )
    my_cursor = final_connection.cursor()

    return final_connection, my_cursor


connection_db, my_cursor = connection_factory(
                                                server_host=host, 
                                                server_user=user,
                                                server_password=password, 
                                                server_database_name=db_name)

