from pymongo import MongoClient


class DataAccess:
    def __init__(self, db_name, host, port):
        client = MongoClient(host, port)
        self.__db = client[db_name]

    def save_to_db(self, collection_name, item):
        name = "name"
        collection = self.__db[collection_name]

        # дубли ищем по наименованию книги
        if collection.count_documents({name: item[name]}) == 0:
            collection.insert_one(item)
