import re

def search_datatime(text):
    # 26 апреля в 10:00
    regex = r'(\d{1,2})\s+([а-яА-Я]+)\s+в\s+(\d{1,2}):(\d{2})'
    
    match = re.search(regex, text)
    month_name = match.group(2)

    months = {
        'января': '01',
        'февраля': '02',
        'марта': '03',
        'апреля': "04",
        'мая': '05',
        'июня': '06',
        'июля': '07',
        'августа': '08',
        'сентября': '09',
        'октября': '10',
        'ноября': '11',
        'декабря': '12',
    }
    month = months[month_name.lower()]

    return f"2023-{month}-{match.group(1)} {match.group(3)}:{match.group(4)}"
