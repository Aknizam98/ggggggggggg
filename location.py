import requests
from bs4 import BeautifulSoup
from core.config import *
from core.utils import *
from database.dbpars import add_information_location

def get_html(URL, HEADER):
    response = requests.get(url=URL, headers=HEADER)
    if response.status_code != 200:
        return f"Ошибка: код {response.status_code}"
    return response.text

def processing_html(response):
    soup = BeautifulSoup(response, 'lxml').find("div", {'class': 'impression-items'}).find_all(\
        "div", {'class': 'impression-card'})

    for item in soup:
        title_location = str(item.get('data-title')).replace("'", "")
        url_location = item.find("a", {"class": "impression-card-title"}).get("href")
        info_location = str(item.find('div', {
            'class': 'impression-card-info'}).text
            ).replace("\n    ", "").strip().replace("'", "")

        photo_location = DOMAIN + item.find(
            'div', {'class': 'impression-card-image'}
            ).find('img').get('src')
        

        add_information_location(title_location, info_location, url_location, photo_location)        


# 2023-04-26 10:00
def start_parser():
    count_page = 0
    location_url = "https://sxodim.com/almaty/places?page="
    for page in range(1, 120):
        res = get_html(location_url + str(page), HEADERS)
        processing_html(res)
        count_page += 1
        print("Страница готово:",count_page)

start_parser()