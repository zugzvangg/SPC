from flask import Flask
import mariadb
import os
import requests

TABLE_NAME = os.getenv('TABLE_NAME')

def get_connection():
    conn = mariadb.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv("MARIADB_USER"),
        password=os.getenv("MARIADB_PASSWORD"),
        database=os.getenv("MARIADB_DATABASE")
    )
    return conn

app = Flask(__name__)

@app.route("/")
def all_data():
    cursor = get_connection().cursor()
    cursor.execute(f"SELECT * FROM {TABLE_NAME}")
    result = []
    for (name, age) in cursor:
        result.append((f"Name: {name}, age: {age}"))
    return result

@app.route("/health")
def health():
    return {}