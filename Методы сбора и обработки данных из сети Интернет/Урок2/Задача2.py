# Необходимо собрать информацию по продуктам питания с сайта: Список протестированных продуктов на сайте Росконтроль.рф
# Приложение должно анализировать несколько страниц сайта (вводим через input или аргументы).
# Получившийся список должен содержать:

# Наименование продукта.
# Все параметры (Безопасность, Натуральность, Пищевая ценность, Качество) Не забываем преобразовать к цифрам
# Общую оценку
# Сайт, откуда получена информация.
# Общий результат можно вывести с помощью dataFrame через Pandas. Сохраните в json либо csv.


import requests
from bs4 import BeautifulSoup
import pandas as pd


page = 1
base_url = "http://Росконтроль.рф"
search_url = f"{base_url}/testlab/search"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
result = []

print(f"Поиск продуктов на {base_url}")
search_text = input("Продукт: ")
pages_count = input(f"Количество страниц в выдаче: ")

while True:
    params = {"keyword": search_text,
              "page": page}
    response = requests.get(search_url, params=params, headers=headers)

    if response.ok:
        dom = BeautifulSoup(response.text, "html.parser")
        products = dom.find_all("div", {"class": "wrap-product-catalog__item"})

        for product in products:
            product_data = {}
            product_name = product.find("div", {"class": "product__item-link"}).text
            product_rate_text = product.find("div", {"class": "rate"}).text
            product_rate = int(product_rate_text) if product_rate_text != "" else 0

            rating_blocks_tag = product.find("div", {"class": "rating-block"}).find_all("div", {"class": "row"})

            if rating_blocks_tag:
                safety = int(rating_blocks_tag[0].find("div", {"class": "right"}).text)
                naturally = int(rating_blocks_tag[1].find("div", {"class": "right"}).text)
                nutritional_value = int(rating_blocks_tag[2].find("div", {"class": "right"}).text)
                quality = int(rating_blocks_tag[3].find("div", {"class": "right"}).text)
                note = ""
            else:
                safety = naturally = nutritional_value = quality = 0
                note = product.find("div", {"class": "blacklist-desc-full-inner"}).text.replace("\n", "").strip()

            product_data = {"product_name": product_name,
                            "product_rate": product_rate,
                            "safety": safety,
                            "naturally": naturally,
                            "nutritional_value": nutritional_value,
                            "quality": quality,
                            "note": note}
            result.append(product_data)

        # выходим если достигнуто количество стрниц либо запрос ничего не выдаёт
        if page == int(pages_count) or not products or len(products) == 0:
            break
        else:
            print(f"Got page {page}")
            page += 1
    else:
        break

if result:
    with open("roscontrol_result.json", 'w') as file:
        file.write(str(result))

    table = pd.DataFrame(result, columns=["product_name", "product_rate", "safety", "naturally", "nutritional_value", "quality", "note"])
    print(table)
else:
    print("Ничего не найдено")

print(result)
