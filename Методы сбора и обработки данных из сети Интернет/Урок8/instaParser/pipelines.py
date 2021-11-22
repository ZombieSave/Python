import logging
from instaParser import settings
from instaParser.dataAccess import DataAccess
from instaParser.fields import Fields
from scrapy.pipelines.images import ImagesPipeline
import scrapy


class InstaparserDataPipeline:
    def __init__(self):
        self.__logger = logging.getLogger()
        self.__da = DataAccess(db_name=settings.DB_NAME, host=settings.HOST, port=settings.PORT)

    def process_item(self, item, spider):
        try:
            # сохраняем пользователя
            self.__da.save_user(item[Fields.friend_id], item[Fields.username], item[Fields.full_name])

            # сохраняем подписку/подписчика
            if item[Fields.userId] != item[Fields.friend_id]:
                self.__da.save_friendship(item[Fields.userId], item[Fields.friend_id])
        except Exception as ex:
            self.__logger.error(f"Ошибка сохранения в БД: {ex}")

        return item


class InstaparserImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item[Fields.profile_pic_url]:
            try:
                yield scrapy.Request(item[Fields.profile_pic_url])
            except Exception as ex:
                logger = logging.getLogger()
                logger.error(f"Ошибка получения изображения {ex}")

    def item_completed(self, results, item, info):
        return item

    def file_path(self, request, response=None, info=None, *, item=None):
        return f"full/avatars/{item[Fields.friend_id]}.jpg"


