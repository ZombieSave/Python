# 1. Написать приложение, которое собирает основные новости с сайта на выбор news.mail.ru, lenta.ru, yandex-новости.
# Для парсинга использовать XPath. Структура данных должна содержать:
# название источника;
# наименование новости;
# ссылку на новость;
# дата публикации.
# 2. Сложить собранные новости в БД
# Минимум один сайт, максимум - все три

import requests
from lxml import html
from pprint import pprint
import datetime
from pymongo import MongoClient


# получаем список новостей
articles = []
url = "https://yandex.ru/news"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
response = requests.get(url, headers=headers)
dom = html.fromstring(response.text)
items = dom.xpath("//article")
missing_count = 0

for item in items:
    try:
        article_link_tag = item.xpath(".//a[@class='mg-card__link']")[0]
        article_link = article_link_tag.xpath("./@href")[0]
        article_header = article_link_tag.xpath(".//h2[@class='mg-card__title']/text()")[0]

        source = item.xpath(".//a[@class='mg-card__source-link']/text()")[0]
        publish_time = item.xpath(".//span[@class='mg-card-source__time']/text()")[0]
        publish_date_time = datetime.datetime.strptime(f"{datetime.datetime.now().date()} {publish_time}", '%Y-%m-%d %H:%M')

        articles.append({"article_header": article_header,
                         "article_link": article_link,
                         "source": source,
                         "time": publish_date_time})
    except:
        missing_count += 1
        print(f"Ошибка получения данных со страницы")

print(f"Получено {len(items)} записей")
print(f"Пропущено {missing_count} записей")

# сохраняем в БД
client = MongoClient("127.0.0.1", 27017)
db = client["YandexNews"]
new_records = 0

for article in articles:
    article_header = "article_header"

    if db.articles.count_documents({article_header: article[article_header]}) == 0:
        db.articles.insert_one(article)
        new_records += 1

if new_records != 0:
    print(f"Добавлено {new_records} новых записей")
else:
    print(f"Нет новых записай")


