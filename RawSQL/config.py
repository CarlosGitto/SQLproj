"""Creates database if theres not a database with the specified name."""

import mysql.connector

host = "localhost"
user = "root"
password = "root2021"
db_name = "sql_challenge"


def connection_factory(server_host: str, server_user: str, server_password: str, server_database_name: str) -> object:
    """Establishes connection with MySQL server."""

    connection = mysql.connector.connect(
        host=server_host,
        user=server_user,
        password=server_password,
        database=server_database_name
    )

    return connection


def db_creator(database_name: str, engine: object) -> None:
    """Creates database in server using credentials."""

    engine.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")


my_conn = connection_factory(server_host=host, server_user=user,
                             server_password=password, server_database_name=db_name)

my_cursor = my_conn.cursor()

db_name = db_creator(database_name=db_name, engine=my_cursor)
