from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
import logging
from instaParser.spiders.insta import InstaSpider
from instaParser import settings


if __name__ == "__main__":
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(InstaSpider)

    logger = logging.getLogger()
    logger.info("*** Начало работы InstaSpider ***")
    process.start()
    logger.info("*** InstaSpider работу завершил ***")



