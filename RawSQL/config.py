"""Creates database if theres not a database with the specified name."""

import mysql.connector

from SQLproj.RawSQL import connection

host = "localhost"
user = "root"
password = "root2021"
db_name = "sql_challenge"


def connection_factory(server_host: str, server_user: str, server_password: str, server_database_name: str) -> object:
    """Establishes connection with MySQL server."""

    my_database = mysql.connector.connect(
        server_host,
        server_user,
        server_password,
        server_database_name
    )

    return connection


def db_creator(database_name: str) -> None:
    """Creates database in server using credentials."""

    engine = connection_factory(host, user, password, db_name)

    engine.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

    print('Database now exists in server.')


db_name = db_creator(db_name)

my_conn = connection_factory(server_host=host, server_user=user,
                             server_password=password, server_database_name=db_name)

my_cursor = my_conn.cursor()
