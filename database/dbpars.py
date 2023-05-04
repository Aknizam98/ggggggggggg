import psycopg2
from os import getenv
from dotenv import load_dotenv
from random import randint
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


def get_cotegory_events():
    cursor = connection.cursor()
    cursor.execute("SELECT cotigory from events")
    all_events = cursor.fetchall()

    data = set()

    for i in all_events:
        data.add(i[0])
    return data


def check_title():
    cursor = connection.cursor()
    cursor.execute(f"SELECT title FROM events")
    all_titles = cursor.fetchall()
    
    data = set()
    for i in all_titles:
        data.add(i[0])
    
    return data



def get_values_category_events(text):
    cursor = connection.cursor()
    cursor.execute(f"SELECT title FROM events WHERE cotigory = '{text}'")
    all_events = cursor.fetchall()

    data = set()
    
    for i in all_events:
        data.add(i[0])
    
    return data


def get_title_category_events(text):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM events WHERE title = '{text}'")
    event = cursor.fetchone()
    # (id, category, title, information, data, url, photo, createt)
    event_information_text = f"\n<b>Заголовок:</b> <a href='{event[6]}'>{event[2]}</a>\n<b>Котегория:</b> {event[1]}\n<b>Информация:</b> {event[3]}\n<b>Дата:</b> {event[4]}\n<b>Подробнее:</b> <a href='{event[5]}'>Нажмите тут</a>"

    return event_information_text


# ----------------------------------------------------------------

def add_information_location(title, info, url, photo):
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS location (id SERIAL PRIMARY KEY,\
        title VARCHAR(255) NOT NULL,\
        information VARCHAR(255) NOT NULL,\
        url TEXT NOT NULL,\
        photo TEXT DEFAULT NULL,\
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
    )
    cursor.execute(f"SELECT * FROM location WHERE title = '{title}'\
        and information = '{info}' \
        and url = '{url}' and photo = '{photo}'")
    check_one = cursor.fetchone()

    if check_one is None:
        cursor.execute("INSERT INTO location (title, information, url, photo)\
            VALUES(%s, %s, %s, %s)", (title, info, url, photo))
    else:
        pass

    connection.commit()
    cursor.close()


def get_location() -> list:
    cursor = connection.cursor()
    data = []
    for location in range(1, 11):
        cursor.execute(f"SELECT * FROM location WHERE id = {randint(1, 1800)}")
        one_location = cursor.fetchone()
        data.append(one_location)

    return data