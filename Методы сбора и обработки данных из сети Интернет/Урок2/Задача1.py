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
import pandas as pd


page = 0
base_url = "https://hh.ru"
search_url = f"{base_url}/search/vacancy"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
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

            if salary_span_tag is not None:
                salary = salary_span_tag.text
            else:
                salary = "не указана"

            vacancy_data = {"vacancy_name": vacancy_name,
                            "company": company,
                            "vacancy_link": vacancy_link,
                            "salary": salary,
                            "from_site": base_url}
            result.append(vacancy_data)

        # выходим если достигнуто количество стрниц либо запрос ничего не выдаёт
        if page == int(pages_count) - 1 or not vacancies or len(vacancies) == 0:
            break
        else:
            page += 1
            print(f"Got page {page}")
    else:
        break

if result:
    with open("hh_result.json", 'w') as file:
        file.write(str(result))

    table = pd.DataFrame(result, columns=["vacancy_name", "company", "vacancy_link", "salary", "from_site"])
    print(table)
else:
    print("Ничего не найдено")
