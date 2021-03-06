from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
import logging
from leroymerlin.spiders.leroy import LeroySpider
from leroymerlin import settings

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(LeroySpider, category="unitazy-kompakt")  # передаём категорию товара

    logger = logging.getLogger()
    logger.info("*** Начало работы LeroySpider ***")
    process.start()
    logger.info("*** LeroySpider работу завершил ***")

