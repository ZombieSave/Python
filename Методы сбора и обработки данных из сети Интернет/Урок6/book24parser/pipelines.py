from book24parser.DataAccess import DataAccess
import traceback


class Book24ParserPipeline:
    __name_field = "name"
    __link_field = "link"
    __discount_price_field = "discount_price"
    __price_field = "price"
    __rating_field = "rating"
    __authors_field = "authors"
    __category_field = "category"

    def __init__(self):
        self.__da = DataAccess(db_name="book24", host="127.0.0.1", port=27017)

    def process_item(self, item, spider):
        try:
            data = self.__prepare_data(item)
            self.__da.save_to_db(collection_name=item[self.__category_field], item=data)
        except Exception as ex:
            print(f"Ошибка сохранения в БД: {ex.msg}\n{traceback.format_exc()}")

        return item

    def __prepare_data(self, item):
        name = item[self.__name_field].strip()
        link = item[self.__link_field]

        if item[self.__discount_price_field]:
            discount_price_str = item[self.__discount_price_field].strip().split(" ")[0].replace("\xa0", "")
            discount_price = float(discount_price_str)
        else:
            discount_price = 0

        if item[self.__price_field]:
            price_str = item[self.__price_field].strip().split(" ")[0].replace("\xa0", "")
            price = float(price_str)
        else:
            price = 0

        rating = float(item[self.__rating_field].strip().replace(",", "."))
        authors = list(map(lambda x: x.strip(), item[self.__authors_field]))

        data = {self.__name_field: name,
                self.__link_field: link,
                self.__discount_price_field: discount_price,
                self.__price_field: price,
                self.__rating_field: rating,
                self.__authors_field: authors}

        return data