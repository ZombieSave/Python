# 2. Написать функцию, которая производит поиск и выводит на экран вакансии с заработной платой больше введённой суммы
# (необходимо анализировать оба поля зарплаты). Для тех, кто выполнил задание с Росконтролем - напишите запрос для
# поиска продуктов с рейтингом не ниже введенного или качеством не ниже введенного (то есть цифра вводится одна,
# а запрос проверяет оба поля)


from pymongo import MongoClient
from pprint import pprint


def find_vacancy_by_sum(sum):
    return db.vacancies.find({"salary_from": {"$gt": int(sum)}})


client = MongoClient("127.0.0.1", 27017)
db = client["HeadHunter"]


try:
    sum = input("Введите сумму: ")
    vacancies = find_vacancy_by_sum(sum)
    vacancy_list = list(vacancies)
    print(f"Получено {len(vacancy_list)} записей")
    pprint(vacancy_list)
except:
    print("Ошибка обращения к БД")
