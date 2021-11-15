import scrapy


class Book24ParserItem(scrapy.Item):
    _id = scrapy.Field()
    name = scrapy.Field()
    link = scrapy.Field()
    authors = scrapy.Field()
    price = scrapy.Field()
    discount_price = scrapy.Field()
    rating = scrapy.Field()
    category = scrapy.Field()
