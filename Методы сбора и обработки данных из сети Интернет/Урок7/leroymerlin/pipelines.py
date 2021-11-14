import hashlib
from scrapy.utils.python import to_bytes
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from leroymerlin.DataAccess import DataAccess
from leroymerlin.Fields import Fields
import logging
#pip install Pillow !


class LeroymerlinDataPipeline:
    def __init__(self):
        self.__da = DataAccess(db_name="LeroyMerlin", host="127.0.0.1", port=27017)
        self.__logger = logging.getLogger()

    def process_item(self, item, spider):
        try:
            details = self.__get_details(item[Fields.details])
            data = {Fields.name: item[Fields.name],
                    Fields.article_number: item[Fields.article_number],
                    Fields.link: item[Fields.link],
                    Fields.price: item[Fields.price],
                    Fields.image_paths: item[Fields.image_paths],
                    Fields.details: details}
            # категория товара = имя коллекции в БД
            self.__da.save_to_db(item[Fields.category], data)
        except Exception as ex:
            self.__logger.error(f"Ошибка сохранения в БД: {ex}")

        return item

    def __get_details(self, detail_list: []):
        result = []

        for i in range(0, len(detail_list)-1, 2):
            result.append({Fields.param_name: detail_list[i],
                           Fields.param_value: detail_list[i+1]})

        return result


class LeroymerlinImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        if item[Fields.image_links]:
            for image in item[Fields.image_links]:
                try:
                    yield scrapy.Request(image)
                except Exception as ex:
                    logger = logging.getLogger()
                    logger.error(f"Ошибка получения изображения {ex}")

    def item_completed(self, results, item, info):
        # нам нужнен только путь
        item[Fields.image_paths] = list(map(lambda x: x[1]["path"], results))

        return item

    def file_path(self, request, response=None, info=None, *, item=None):
        image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        # 3)Реализовать хранение скачиваемых файлов в отдельных папках, каждая из которых должна соответствовать собираемому товару
        # папка "категория", подпапка "article_number" для каждого товара
        return f"full/{item[Fields.category]}/{item[Fields.article_number]}/{image_guid}.jpg"

