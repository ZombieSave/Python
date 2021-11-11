import scrapy
from scrapy.http import HtmlResponse
import traceback
import urllib.parse
from book24parser.items import Book24ParserItem


class Book24Spider(scrapy.Spider):
    name = 'book24'
    allowed_domains = ['book24.ru']
    # меню "Каталог" (только книги)
    start_urls = ["https://book24.ru/catalog/knigi-s-avtografom-4435/",  # Книги с автографом 16 страниц
                  # "https://book24.ru/catalog/fiction-1592/",  # Художественная литература 2099 страниц
                  # "https://book24.ru/catalog/detskie-knigi-1159/",  # Детские книги 1299 страниц
                  "https://book24.ru/catalog/knigi-dlya-podrostkov-3351/",  # Книги для подростков 40 страниц
                  "https://book24.ru/catalog/business-1671/",  # Бизнес-литература 93 страницы
                  "https://book24.ru/catalog/samoobrazovanie-i-razvitie-4560/",  # Самообразование и развитие 78 страниц
                  # "https://book24.ru/catalog/khobbi-i-dosug-4056/",  # Хобби и досуг 485 страниц
                  # "https://book24.ru/catalog/school-1492/",  # Учебная литература 468 страниц
                  "https://book24.ru/catalog/pedagogika-i-vospitanie-4743/",  # Педагогика и воспитание 35 страниц
                  # "https://book24.ru/catalog/estestvennye-nauki-1347/",  # Научно-популярная литература 467 страниц
                  # "https://book24.ru/catalog/publitsistika-1426/",  # Публицистика 144 страницы
                  "https://book24.ru/catalog/religiya-1437/",  # Религия 44 страницы
                  "https://book24.ru/catalog/knizhnyy-razval-3646/",  # Книжный развал 45 страниц
                  "https://book24.ru/catalog/knigi-v-kozhanom-pereplete-2729/",  # Книги в кожаном переплете 21 страница
                  "https://book24.ru/catalog/novyy-god-4771/"]  # Новый год 16 страниц

    def parse(self, response: HtmlResponse):
        try:
            next_page, log_url = self.__get_next_page_url(response)
            print(f"Получение данных {log_url}")
            yield response.follow(next_page, self.parse)
            # получаем ссылки на книги текущей страницы
            links = response.xpath("//div[@class='catalog__product-list-holder']//a[contains(@class, 'product-card__name')]/@href").getall()
            # по каждой категории будет создана отдельная коллекция
            category = self.__get_category_from_url(response.url)

            for link in links:
                url = urllib.parse.urljoin(response.url, link)
                yield response.follow(url, self.__callback, meta={"category": category})

        except Exception as ex:
            print(f"Ошибка парсинга: {ex.msg}\n{traceback.format_exc()}")

    def __callback(self, response: HtmlResponse):
        category = response.meta.get("category")
        name = response.xpath("//h1[@class='product-detail-page__title']/text()").get().strip()
        link = response.url
        discount_price = response.xpath("//div[contains(@class, 'product-sidebar-price__main-price')]//span[contains(@class, 'product-sidebar-price__price')]/text()").get()
        price = response.xpath("//span[contains(@class, 'product-sidebar-price__price-old')]/text()").get()
        rating = response.xpath("//div[contains(@class, 'rating-widget')]//span[contains(@class, 'rating-widget__main-text')]/text()").get()
        authors = response.xpath("//li[contains(@class, 'product-characteristic__item-holder')][1]//a/text()").getall()

        yield Book24ParserItem(category=category, name=name, link=link, authors=authors, price=price, discount_price=discount_price, rating=rating)

    def __get_next_page_url(self, response: HtmlResponse):
        pos = response.url.rfind("page-")

        # url первой страницы каждой категории не имеет page-n
        if pos != -1:
            pos = response.url.rfind('-')
            page_number = int(response.url[pos + 1:-1]) + 1
            next_page = urllib.parse.urljoin(response.url[0:pos + 1], f"page-{page_number}")
            log_url = response.url
        else:
            next_page = urllib.parse.urljoin(response.url, "page-2")
            log_url = f"{response.url}page-1/"

        return next_page, log_url

    def __get_category_from_url(self, url):
        """ получение категории из url """
        start = url.rfind("catalog")+8
        end = url.rfind("page")

        return url[start:end-1] if end != -1 else url[start:-1]
