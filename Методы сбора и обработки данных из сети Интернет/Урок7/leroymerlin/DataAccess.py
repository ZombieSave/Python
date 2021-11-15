from pymongo import MongoClient
from leroymerlin.Fields import Fields


class DataAccess:
    def __init__(self, db_name, host, port):
        client = MongoClient(host, port)
        self.__db = client[db_name]

    def save_to_db(self, collection_name, item):
        collection = self.__db[collection_name]

        # проверка уже существующего товара по арт. номеру
        if collection.count_documents({Fields.article_number: item[Fields.article_number]}) == 0:
            collection.insert_one(item)
