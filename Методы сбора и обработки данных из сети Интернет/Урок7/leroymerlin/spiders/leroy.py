import scrapy
from itemloaders import ItemLoader
from scrapy.http import HtmlResponse
import urllib.parse
from leroymerlin.Fields import Fields
from leroymerlin.items import LeroymerlinItem
import logging


class LeroySpider(scrapy.Spider):
    name = 'leroy'
    allowed_domains = ["leroymerlin.ru"]

    def __init__(self, category, **kwargs):
        super().__init__(**kwargs)
        self.__category = category
        self.start_urls = [f"https://leroymerlin.ru/catalogue/{self.__category}/"]
        self.__logger = logging.getLogger()

    def parse(self, response: HtmlResponse):
        try:
            self.__logger.info(f"Загрузка страницы {response.url}")
            next_page = self.__get_next_page_url(response.url)
            yield response.follow(next_page, self.parse)

            # если не делать /@href то почему-то в цикле из yield response.follow() не попадаем в callback
            links = response.xpath("//div[contains(@class, 'phytpj4_plp')]//div[contains(@class, 'c155f0re_plp')]//a[contains(@class, 'bex6mjh_plp')]/@href").getall()

            for link in links:
                url = urllib.parse.urljoin(response.url, link)
                self.__logger.info(f"Получение данных товара {url}")
                yield response.follow(url, self.__callback)

        except Exception as ex:
            self.__logger.error(f"Ошибка парсинга: {ex}")

    def __callback(self, response: HtmlResponse):
        item = LeroymerlinItem()
        loader = ItemLoader(item=item, selector=response)
        loader.add_xpath(Fields.name, "//h1/text()")
        loader.add_value(Fields.link, response.url)
        loader.add_xpath(Fields.article_number, "//span[@slot='article']/text()")
        loader.add_xpath(Fields.price, "//uc-pdp-price-view/span/text()")
        loader.add_xpath(Fields.image_links, "//uc-pdp-media-carousel//img/@src")
        loader.add_value(Fields.image_paths, [])
        loader.add_value(Fields.category, self.__category)

        # 2)Написать универсальный обработчик характеристик товаров, который будет формировать данные вне зависимости от их типа и количества.
        loader.add_xpath(Fields.details, "//dl[@class='def-list']//dt/text() | //dl[@class='def-list']//dd/text()")

        yield loader.load_item()

    def __get_next_page_url(self, url):
        pos = url.rfind('=')

        if pos != -1:
            page_number = int(url[pos+1:]) + 1
            new_url = f"{url[0:pos + 1]}{page_number}"
        else:
            new_url = f"{url}?page=2"

        return new_url
