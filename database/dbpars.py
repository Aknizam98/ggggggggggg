import psycopg2
from os import getenv
from dotenv import load_dotenv
load_dotenv()

connection = psycopg2.connect(
    host = getenv("PGHOST"), 
    database = getenv("PGDATABASE"),
    user = getenv("PGUSER"), 
    password = getenv("PGPASSWORD"), 
    port = getenv("PGPORT"),
)

def add_information_event(cotigory, title, info, date, url, photo):
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS events (id SERIAL PRIMARY KEY,\
        cotigory VARCHAR(255) NOT NULL,\
        title VARCHAR(255) NOT NULL,\
        information VARCHAR(255) NOT NULL,\
        event_data VARCHAR(100) NOT NULL,\
        url TEXT NOT NULL,\
        photo TEXT DEFAULT NULL,\
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
    )
    cursor.execute(f"SELECT * FROM events WHERE title = '{title}'\
        and information = '{info}' and event_data = '{date}'\
        and url = '{url}' and photo = '{photo}'")
    check_one = cursor.fetchone()

    if check_one is None:
        cursor.execute("INSERT INTO events (cotigory, title, information, event_data, url, photo)\
            VALUES(%s, %s, %s, %s, %s, %s)", (cotigory, title, info, date, url, photo))
    else:
        pass

    connection.commit()
    cursor.close()
