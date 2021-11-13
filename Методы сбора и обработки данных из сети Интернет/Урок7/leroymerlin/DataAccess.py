from pymongo import MongoClient
from leroymerlin.Fields import Fields


class DataAccess:
    def __init__(self, db_name, host, port):
        client = MongoClient(host, port)
        self.__db = client[db_name]

    def save_to_db(self, collection_name, item):
        collection = self.__db[collection_name]

        if collection.count_documents({Fields.name: item[Fields.name]}) == 0:
            collection.insert_one(item)
