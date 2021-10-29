# Необходимо собрать информацию о вакансиях на вводимую должность (используем input или через аргументы получаем должность)
# с сайтов HH(обязательно) и/или Superjob(по желанию). Приложение должно анализировать несколько страниц сайта
# (также вводим через input или аргументы). Получившийся список должен содержать в себе минимум:
# 1. Наименование вакансии.
# 2. Предлагаемую зарплату (разносим в три поля: минимальная и максимальная и валюта. цифры преобразуем к цифрам).
# 3. Ссылку на саму вакансию.
# 4. Сайт, откуда собрана вакансия.
# По желанию можно добавить ещё параметры вакансии (например, работодателя и расположение). Структура должна быть
# одинаковая для вакансий с обоих сайтов. Общий результат можно вывести с помощью dataFrame через pandas.
# Сохраните в json либо csv.


import requests
from bs4 import BeautifulSoup


page = 0
base_url = "https://hh.ru"
search_url = f"{base_url}/search/vacancy"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
result = []

print(f"Поиск вакансий на {base_url}")
search_text = input("Профессия: ")
pages_count = input(f"Количество страниц в выдаче: ")

while True:
    print(f"Get page {page+1}")
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
            vacancy_link = vacancy.find("a", {"class": "bloko-link"})
            vacancy_name = vacancy_link.text
            vacancy_link = vacancy_link["href"]

            company_link = vacancy.find("a", {"class": "bloko-link bloko-link_secondary"})

            if company_link is not None:
                company = company_link.text
            else:
                company = ""

            salary_span = vacancy.find(attrs={"data-qa": "vacancy-serp__vacancy-compensation"})

            if salary_span is not None:
                salary = salary_span.text
            else:
                salary = "не указана"

            vacancy_data = {"vacancy_name": vacancy_name,
                            "company": company,
                            "vacancy_link": vacancy_link,
                            "salary": salary}
            result.append(vacancy_data)

        if page == int(pages_count) - 1:
            break
        else:
            page += 1
    else:
        break

for item in result:
    print(f"Наименование вакансии: {item['vacancy_name']}")
    print(f"Работодатель: {item['company']}")
    print(f"Ссылка: {item['vacancy_link']}")
    print(f"Зарплата: {item['salary']}\n\r")