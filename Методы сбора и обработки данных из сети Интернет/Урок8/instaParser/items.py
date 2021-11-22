import scrapy
from itemloaders.processors import TakeFirst


class InstaparserItem(scrapy.Item):
    userId = scrapy.Field(output_processor=TakeFirst())
    friend_id = scrapy.Field(output_processor=TakeFirst())
    username = scrapy.Field(output_processor=TakeFirst())
    full_name = scrapy.Field(output_processor=TakeFirst())
    profile_pic_url = scrapy.Field(output_processor=TakeFirst())
