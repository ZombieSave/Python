# 1. Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB и реализовать функцию, которая будет добавлять
# только новые вакансии/продукты в вашу базу.


import requests
from pymongo import MongoClient
from bs4 import BeautifulSoup
import codecs

client = MongoClient("127.0.0.1", 27017)
db = client["HeadHunter"]
#db.vacancies.delete_many({})


# функция по заданию к уроку 3
def add_vacancy(data):
    name = "vacancy_name"
    exists = db.vacancies.count_documents({name: data[name]}) > 0

    if not exists:
        db.vacancies.insert_one(data)

    return not exists  # если True значит запись была добавлена


def number_from_navigate_string(inp):
    return int(inp.replace("\u202f", ""))


# код получения данных о вакансиях с hh.ru из Урока2
page = 0
base_url = "https://hh.ru"
search_url = f"{base_url}/search/vacancy"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
result = []

print(f"Поиск вакансий на {base_url}")
search_text = input("Профессия: ")
pages_count = input(f"Количество страниц в выдаче: ")

while True:
    params = {"clusters": True,
              "area": 1,
              "ored_clusters": True,
              "enable_snippets": True,
              "salary": None,
              "text": search_text,
              "page": page}
    response = requests.get(search_url, params=params, headers=headers)

    if response.ok:
        dom = BeautifulSoup(response.text, "html.parser")
        vacancies = dom.find_all("div", {"class": "vacancy-serp-item"})

        for vacancy in vacancies:
            vacancy_data = {}
            vacancy_link_tag = vacancy.find("a", {"class": "bloko-link"})
            vacancy_name = vacancy_link_tag.text
            vacancy_link = vacancy_link_tag["href"]

            company_link_tag = vacancy.find("a", {"class": "bloko-link bloko-link_secondary"})

            if company_link_tag is not None:
                company = company_link_tag.text
            else:
                company = ""

            salary_span_tag = vacancy.find(attrs={"data-qa": "vacancy-serp__vacancy-compensation"})
            salary_from = salary_to = "не указана"

            if salary_span_tag is not None:
                try:
                    salary = salary_span_tag.text.split(" ")

                    if "от" in salary:
                        salary_from = number_from_navigate_string(salary[1])  # зарплата от
                        salary_to = None  # зарплата до
                    else:
                        salary_from = number_from_navigate_string(salary[0])  # зарплата от
                        salary_to = number_from_navigate_string(salary[2])  # зарплата до
                except:
                    pass

            vacancy_data = {"vacancy_name": vacancy_name,
                            "company": company,
                            "vacancy_link": vacancy_link,
                            "salary_from": salary_from,
                            "salary_to": salary_to,
                            "from_site": base_url}
            result.append(vacancy_data)

        # выходим если достигнуто количество стрниц либо запрос ничего не выдаёт
        if page == int(pages_count) - 1 or not vacancies or len(vacancies) == 0:
            break
        else:
            page += 1
            print(f"Получение страницы {page}")
    else:
        break

# сохраняем в БД
count = 0

for item in result:
    success = False

    try:
        success = add_vacancy(item)
    except:
        print(f"Ошибка добавления вакансии {item['vacancy_name']}")

    if success:
        count += 1

print(f"Добавлено {count} новых записей")
