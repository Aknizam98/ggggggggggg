import psycopg2
from core.config import *

connection = psycopg2.connect(
    host = PGHOST, 
    database = PGDATABASE,
    user = PGUSER, 
    password = PGPASSWORD, 
    port = PGPORT
)

def check_users(user_id):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users(id SERIAL PRIMARY KEY,\
        user_id BIGINT,\
        username VARCHAR(45) DEFAULT NULL,\
        first_name VARCHAR(225) DEFAULT NULL,\
        last_name VARCHAR(225) DEFAULT NULL,\
        phone VARCHAR(225) DEFAULT NULL,\
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
    
    cursor.execute(f"SELECT * FROM users WHERE user_id = {user_id}")

    check = cursor.fetchone()
    if check is not None:
        return check
    else:
        return None


def registrstion_users(user_id, username, first_name, last_name, phone):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users(id SERIAL PRIMARY KEY,\
        user_id BIGINT,\
        username VARCHAR(45) DEFAULT NULL,\
        first_name VARCHAR(225) DEFAULT NULL,\
        last_name VARCHAR(225) DEFAULT NULL,\
        phone VARCHAR(225) DEFAULT NULL,\
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
    
    cursor.execute("INSERT INTO users(user_id, username,\
        first_name, last_name, phone) VALUES(%s, %s, %s, %s, %s)", 
        (user_id, username, first_name, last_name, phone))
    connection.commit()
    cursor.close()


def search_inline_mode(text):
    cursor = connection.cursor()
    cursor.execute(
    f"SELECT * FROM events WHERE title LIKE '{text}%' or title LIKE '%{text}%'"
    )
    all_events = cursor.fetchall()

    return all_events