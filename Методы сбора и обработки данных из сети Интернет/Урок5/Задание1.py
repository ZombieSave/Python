# Вариант I
# Написать программу, которая собирает входящие письма из своего или тестового почтового ящика и сложить данные о
# письмах в базу данных (от кого, дата отправки, тема письма, текст письма полный)
# Логин тестового ящика: study.ai_172@mail.ru
# Пароль тестового ящика: NextPassword172#


from selenium import webdriver
from pymongo import MongoClient
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
import traceback
from selenium.common.exceptions import StaleElementReferenceException


letter_data = []
login = "study.ai_172"
password = "NextPassword172#"
url = "https://mail.ru/"

from_address_field = "from_address"
subject_field = "subject"
received_at_field = "received_at"
body_field = "body"

options = Options()
# options.add_argument("--headless")
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
driver.maximize_window()

try:
    print("Подключение к mail.ru")
    driver.get(url)

    print("Ожидание поля login")
    login_input = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.NAME, "login")))
    login_input.send_keys(login)

    print("Нажатие \"Ввести пароль\"")
    input_password_button = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@data-testid='enter-password']")))
    input_password_button.click()

    print("Ожидание поля password")
    # presence_of_element_located почему-то не всегда срабатывает здесь, поэтому visibility_of_element_located
    password_input = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.NAME, "password")))
    password_input.send_keys(password)

    print("Ожидание кнопки \"Войти\"")
    login_button = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@data-testid='login-to-mail']")))
    login_button.click()

    print("Ожидание появления списка сообщений папки \"Входящие\"")
    # ждём появления первого элемента списка
    first_letter = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//div[@class='dataset__items']//a[contains(@class, 'js-letter-list-item')][1]")))
    # после получаем все элементы списка

    print("Сбор ссылок на сообщения")
    letter_links = []  # итоговый список ссылок на сообщения
    y_position = 0
    count = 0

    while True:
        current_links = []
        letters = driver.find_elements(By.XPATH, "//div[@class='dataset__items']//a[contains(@class, 'js-letter-list-item')]")

        # после прокрутки и выборки некоторые элементы, ушедшие вверх под невидимую область, могут быть удалены из DOM
        # так что получим StaleElementReferenceException. Но они уже добавлены в letter_links так что pass в except.
        for letter in letters:
            try:
                href = letter.get_attribute("href")
                current_links.append(href)
            except StaleElementReferenceException:
                pass

        # проверяем на дубли и добавляем в итоговый список ссылок
        for link in current_links:
            if link not in letter_links:
                letter_links.append(link)

        # если скролить некуда, y-позиция элемента перемещается вниз
        if y_position >= 500:
            break

        # скролим к последнему видимому элементу списка сообщений. (кнопками не скролится)
        scroll_position = letters[len(letters)-1].location_once_scrolled_into_view
        y_position = scroll_position["y"]
        print(f"Scroll {count}")  # для наглядности процесса
        count += 1

    print("Получение данных сообщений")

    for link in letter_links:
        driver.get(link)
        # если появился subject значит письмо открылось
        subject_tag = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, "thread__subject")))
        # собираем данные
        subject = subject_tag.text
        from_address = driver.find_element(By.CLASS_NAME, "letter-contact").get_attribute("title")
        received_at = driver.find_element(By.CLASS_NAME, "letter__date").text
        body = driver.find_element(By.CLASS_NAME, "letter__body").text
        letter_data.append({from_address_field: from_address,
                            subject_field: subject,
                            received_at_field: received_at,
                            body_field: body})
except Exception as e:
    print(f"Ошибка парсинга: {e.msg}\n{traceback.format_exc()}")
finally:
    print("Выход из почтового ящика")
    menu_button = driver.find_elements(By.XPATH, "//span[contains(@class, 'ph-dropdown-icon')]")  # без выпадения списка меню не существует

    if len(menu_button) != 0:
        menu_button[0].click()

    menu = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//div[contains(@class, 'ph-accounts')]")))
    menu_items = driver.find_elements(By.XPATH, "//a[contains(@class, 'ph-item')]")
    menu_items[2].click()  # жмём "Выйти"


print("Сохранение данных в БД")
client = MongoClient("127.0.0.1", 27017)
db = client["MailRu"]
new_records = 0

for data in letter_data:
    if db.letters.count_documents({"$and": [{from_address_field: data[from_address_field]},
                                            {subject_field: data[subject_field]},
                                            {received_at_field: data[received_at_field]}]}) == 0:
        new_records += 1
        db.letters.insert_one(data)

if new_records > 0:
    print(f"Добавлено {new_records} записей")
else:
    print("Нет новых писем")






