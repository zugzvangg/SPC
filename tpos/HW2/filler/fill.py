import pandas as pd
import os
import pymysql

TABLE_NAME = os.getenv("TABLE_NAME")
MARIADB_DATABASE = os.getenv("MARIADB_DATABASE")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv('DB_PORT'))
MARIADB_ROOT_USER = os.getenv("MARIADB_ROOT_USER")
MARIADB_ROOT_PASSWORD = os.getenv("MARIADB_ROOT_PASSWORD")
# MYSQL_ROOT_USER = os.getenv("MYSQL_ROOT_USER")
# MYSQL_ROOT_PASSWORD = os.getenv('MYSQL_ROOT_PASSWORD')

def get_connection():
    try:
        connection = pymysql.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=MARIADB_ROOT_USER,
            password=MARIADB_ROOT_PASSWORD,
        )
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {MARIADB_DATABASE}")
        cursor.execute(f"USE {MARIADB_DATABASE}")
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} (name VARCHAR(50), age INTEGER)")
        cursor.execute("FLUSH TABLES")
    except Exception as e:
        raise e
    return connection, cursor


if __name__ == "__main__":
    connection, cursor = get_connection()
    data = pd.read_csv("data.csv")
    # Write info to DB
    for index, row in data.iterrows():
        cursor.execute(
            f"INSERT INTO {TABLE_NAME} (name, age) VALUES (%s, %s)",
            (row["name"], row["age"]),
        )
    # Check that info is in table
    print("Check that db is filled:")
    cursor.execute(f"SELECT * FROM {TABLE_NAME}")
    results = cursor.fetchall()
    for row in results:
        print(row)
    # Close connection
    connection.commit()
    cursor.close()
    connection.close()
    







