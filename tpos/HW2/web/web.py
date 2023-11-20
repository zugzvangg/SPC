from flask import Flask
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
        cursor.execute(f"USE {MARIADB_DATABASE}")
        cursor.execute("FLUSH TABLES")
    except Exception as e:
        raise e
    return connection, cursor

app = Flask(__name__)

@app.route("/")
def all_data():
    connection, cursor = get_connection()
    cursor.execute(f"SELECT * FROM {TABLE_NAME}")
    results = cursor.fetchall()
    json_res = {"result": []}
    for name, age in results:
        json_res["result"].append({name: age})
    connection.close()
    return json_res

@app.route("/health")
def health():
    return {"status": "OK"}

