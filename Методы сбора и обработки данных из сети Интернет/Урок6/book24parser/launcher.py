from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from book24parser.spiders.book24 import Book24Spider
from book24parser import settings


if __name__ == "__main__":
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(crawler_settings)
    process.crawl(Book24Spider)
    process.start()
