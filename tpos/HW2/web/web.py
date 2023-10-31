from flask import Flask
import mariadb
import os

TABLE_NAME = os.getenv('TABLE_NAME')

def get_connection():
    conn = mariadb.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv("MARIADB_USER"),
        password=os.getenv("MARIADB_PASSWORD"),
        database=os.getenv("MARIADB_DATABASE")
    )
    return conn

print(1)
connection = get_connection()
cursor = connection.cursor()
cursor.execute(f"SELECT * FROM {TABLE_NAME}")
for (name, age) in cursor:
    print(f"Name: {name}, age: {age}")
    
print(3)

app = Flask(__name__)









@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"