# 1. Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB и реализовать функцию, которая будет добавлять
# только новые вакансии/продукты в вашу базу.
# 2. Написать функцию, которая производит поиск и выводит на экран вакансии с заработной платой больше введённой суммы
# (необходимо анализировать оба поля зарплаты). Для тех, кто выполнил задание с Росконтролем - напишите запрос для
# поиска продуктов с рейтингом не ниже введенного или качеством не ниже введенного (то есть цифра вводится одна,
# а запрос проверяет оба поля)

import requests
from pymongo import MongoClient


client = MongoClient("127.0.0.1", 27017)
db = client["HeadHunter"]


def add_vacancy(data):
    exists = db.vacancies.count_documents({"data": "asdfasdf"}) > 0

    if not exists:
        db.vacancies.insert_one(data)


vacancy = {"data": "asdfasdf"}
#add_vacancy(vacancy)


vacancies = db.vacancies.find({})
print(list(vacancies))
size = db.vacancies.count_documents({"data": "asdfasdf"})
print(size)

