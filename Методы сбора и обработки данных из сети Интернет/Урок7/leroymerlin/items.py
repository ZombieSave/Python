import scrapy
from itemloaders.processors import MapCompose, TakeFirst


def process_price(value: str):
    try:
        # строка цены имеет вид "1234 Р шт.", в value приходит массив как после split(" ")
        # конвертим в float то что конвертится, остальное отбрасываем в except
        value = float(value.replace(" ", ""))
    except:
        value = None

    return value


def process_image_link(value: str):
    # ссылка на полноразмерную картинку содержит размеры по горизонтали и вертикали вида w_1200,h_1200
    # https://res.cloudinary.com/lmru/image/upload/f_auto,q_auto,w_1200,h_1200,c_pad,b_white,d_photoiscoming.png/LMCode/17988174.jpg
    # отфильтровываем ссылки, не содержащие w_1200,h_1200 (w_82,h_82)
    return value if "w_1200" in value else None


def process_article_number(value: str):
    return int(value.replace("Арт. ", ""))


def process_details(value: str):
    return value.replace("\n", "").strip()


class LeroymerlinItem(scrapy.Item):
    _id = scrapy.Field()
    category = scrapy.Field(output_processor=TakeFirst())
    name = scrapy.Field(output_processor=TakeFirst())
    link = scrapy.Field(output_processor=TakeFirst())
    article_number = scrapy.Field(input_processor=MapCompose(process_article_number), output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(process_price), output_processor=TakeFirst())
    image_links = scrapy.Field(input_processor=MapCompose(process_image_link))
    image_paths = scrapy.Field()
    details = scrapy.Field(input_processor=MapCompose(process_details))


