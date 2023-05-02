import requests
from bs4 import BeautifulSoup
from core.config import *
from core.utils import *
from database.dbpars import add_information_event

def get_html(URL, HEADER):
    response = requests.get(url=URL, headers=HEADER)
    if response.status_code != 200:
        return f"Ошибка: код {response.status_code}"
    return response.text

def processing_html(response):
    soup = BeautifulSoup(response, 'lxml').find("div", {'class': 'impression-items'}).find_all(\
        "div", {'class': 'impression-card'})

    for item in soup:
        title_event = str(item.get('data-title')).replace("'", "")
        cotigory_event = item.get("data-category")
        url_event = item.find("a", {"class": "impression-card-title"}).get("href")
        info_event = str(item.find('div', {
            'class': 'impression-card-info'}).text
            ).replace("\n    ", "").strip().replace("'", "")

        photo_event = DOMAIN + item.find(
            'div', {'class': 'impression-card-image'}
            ).find('img').get('src')
        db_time = search_datatime(info_event)

        add_information_event(cotigory_event, title_event, info_event, db_time, url_event, photo_event)        


# 2023-04-26 10:00
def start_parser():
    count_page = 0
    for page in range(1, 35):
        res = get_html(URL + str(page), HEADERS)
        processing_html(res)
        count_page += 1
        print("Страница готово:",count_page)

start_parser()