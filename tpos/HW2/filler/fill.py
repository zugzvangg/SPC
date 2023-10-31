import mariadb
import pandas as pd
import os

TABLE_NAME = "TEST"

if __name__ == "__main__":
    # Connect to MariaDB 
    conn = mariadb.connect(
        host=os.getenv('DB_HOST'),
        user="user",
        password="password",
        database="database"
    )
    cursor = conn.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {TABLE_NAME}")
    cursor.execute(f"CREATE TABLE {TABLE_NAME}  (name VARCHAR(50), age INT)")

    data = pd.read_csv("data.csv")
    # Write info to DB
    for index, row in data.iterrows():
        cursor.execute(
        f"INSERT INTO {TABLE_NAME} (name, age) VALUES (?, ?)",
        (row["name"], row["age"]))

    #Check that info is in table
    cursor.execute(f"SELECT * FROM {TABLE_NAME}")
    for (name, age) in cursor:
        print(f"Name: {name}, age: {age}")
    # Close connection
    conn.close()
