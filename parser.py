from datetime import datetime
import requests, csv
from config import *


def take_posts():
    token = TOKEN
    version = VERSION
    domain = DOMAIN
    offset = 0
    all_posts = []

    while offset < 2200:
        response = requests.get(URL_API, params={
            "access_token": token,
            "v": version,
            "domain": domain,
            "count": 100,
            "offset": offset
        })
        data = response.json()['response']['items']
        offset += 100
        all_posts.extend(data)
    return all_posts


def file_writer(data):
    with open(f'{DOMAIN}.csv', 'w', encoding="utf-8") as file:
        a_pen = csv.writer(file)
        a_pen.writerows(("date", "text"))
        count = 0
        for post in data:
            count += 1
            timestamp = int(post['date'])
            datetime_obj = str(datetime.fromtimestamp(timestamp))[:10]
            a_pen.writerow((datetime_obj, post['text'][:500]))
            print(f"Пройдено постов: {count}")


if __name__ == '__main__':
    file_writer(take_posts())
