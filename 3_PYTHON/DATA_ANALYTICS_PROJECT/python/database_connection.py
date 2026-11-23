"""
MySQL connection setup for the analytics project.
"""
import os
from getpass import getpass
from urllib.parse import quote_plus

import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", "3306"))
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "india_population")
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")


def get_mysql_password() -> str:
    global MYSQL_PASSWORD
    if MYSQL_PASSWORD is None:
        MYSQL_PASSWORD = getpass(f"MySQL password for {MYSQL_USER}: ")
    return MYSQL_PASSWORD


def get_connection():
    server_connection = mysql.connector.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        password=get_mysql_password(),
    )
    cursor = server_connection.cursor()
    cursor.execute(
        f"CREATE DATABASE IF NOT EXISTS `{MYSQL_DATABASE}` "
        "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
    )
    cursor.close()
    server_connection.close()

    return mysql.connector.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        database=MYSQL_DATABASE,
        user=MYSQL_USER,
        password=get_mysql_password(),
    )


def get_sqlalchemy_engine():
    password = quote_plus(get_mysql_password())
    url = (
        f"mysql+pymysql://{MYSQL_USER}:{password}"
        f"@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
    )
    return create_engine(url)


def save_dataframe(engine: Engine, table_name: str, dataframe) -> None:
    dataframe.to_sql(table_name, con=engine, if_exists="replace", index=False)


if __name__ == "__main__":
    try:
        connection = get_connection()
        print(
            f"MySQL connected: {MYSQL_USER}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
        )
        connection.close()
    except mysql.connector.Error as error:
        print(f"MySQL connection failed: {error}")

