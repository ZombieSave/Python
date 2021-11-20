from pymongo import MongoClient


class DataAccess:
    def __init__(self, db_name, host, port):
        client = MongoClient(host, port)
        self.__db = client[db_name]

    def save_user(self, user_id, username, full_name):
        data = {"_id": user_id,
                "username": username,
                "full_name": full_name}

        if self.__db.users.count_documents({"_id": data["_id"]}) == 0:
            self.__db.users.insert_one(data)

    def save_friendship(self, user_id, friend_id):
        data = {"user_id": user_id,
                "friend_id": friend_id}

        if self.__db.friendships.count_documents({"$and": [{"user_id": user_id},
                                                           {"friend_id": friend_id}]}) == 0:
            self.__db.friendships.insert_one(data)

    #  6) Написать запрос к базе, который вернет список профилей, на кого подписан указанный пользователь
    def get_followings(self, user_id):
        followings = self.__db.friendships.find({"user_id": user_id})
        user_filter = list(map(lambda x: {"_id": x["friend_id"]}, followings))

        return self.__db.users.find({"$or": user_filter})

    #  5) Написать запрос к базе, который вернет список подписчиков только указанного пользователя
    def get_followers(self, user_id):
        followers = self.__db.friendships.find({"friend_id": user_id})
        user_filter = list(map(lambda x: {"_id": x["user_id"]}, followers))

        return self.__db.users.find({"$or": user_filter})
