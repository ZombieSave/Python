from pymongo import MongoClient


class DataAccess:
    def __init__(self, db_name, host, port):
        client = MongoClient(host, port)
        self.__db = client[db_name]

    def save_user(self, user_id, username, full_name):
        """данные пользователей в коллекции users
           _id - id пользователя
           username - login
           full_name - имя в профиле
        """
        data = {"_id": user_id,
                "username": username,
                "full_name": full_name}

        if self.__db.users.count_documents({"_id": data["_id"]}) == 0:
            self.__db.users.insert_one(data)

    def save_friendship(self, user_id, friend_id):
        """коллекция friendships хранит данные о подписках
           user_id - кто подписан
           friend_id - на кого подписан
        """
        data = {"user_id": user_id,
                "friend_id": friend_id}

        if self.__db.friendships.count_documents({"$and": [{"user_id": user_id},
                                                           {"friend_id": friend_id}]}) == 0:
            self.__db.friendships.insert_one(data)

    #  6) Написать запрос к базе, который вернет список профилей, на кого подписан указанный пользователь
    def get_followings(self, user_id):
        # для получения подписок пользователя, ищем его в user_id коллекции friendships
        followings = self.__db.friendships.find({"user_id": user_id})
        user_filter = [x["friend_id"] for x in followings]

        return self.__db.users.find({"_id": {"$in": user_filter}})

    #  5) Написать запрос к базе, который вернет список подписчиков только указанного пользователя
    def get_followers(self, user_id):
        # для получения подписчиков пользователя, ищем его в friend_id коллекции friendships
        followers = self.__db.friendships.find({"friend_id": user_id})
        user_filter = [x["user_id"] for x in followers]

        return self.__db.users.find({"_id": {"$in": user_filter}})
