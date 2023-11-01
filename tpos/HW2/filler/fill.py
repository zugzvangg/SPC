import mariadb
import pandas as pd
import os
import time

TABLE_NAME = os.getenv("TABLE_NAME")

if __name__ == "__main__":
    # Connect to MariaDB
    time.sleep(5)
    conn = mariadb.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("MARIADB_USER"),
        password=os.getenv("MARIADB_PASSWORD"),
        database=os.getenv("MARIADB_DATABASE"),
    )
    cursor = conn.cursor()
    # cursor.execute(f"DROP TABLE IF EXISTS {TABLE_NAME}")
    try:
        cursor.execute(f"CREATE TABLE {TABLE_NAME}  (name VARCHAR(50), age INT)")
    except mariadb.OperationalError:
        print(f"Table {TABLE_NAME} already exists, fill it")
        pass

    data = pd.read_csv("data.csv")
    # Write info to DB
    for index, row in data.iterrows():
        cursor.execute(
            f"INSERT INTO {TABLE_NAME} (name, age) VALUES (?, ?)",
            (row["name"], row["age"]),
        )
    conn.commit()
    # Check that info is in table
    print("Check that db is filled:")
    cursor.execute(f"SELECT * FROM {TABLE_NAME}")
    for name, age in cursor:
        print(f"Name: {name}, age: {age}")
    # Close connection
    conn.close()
