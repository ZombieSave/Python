# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
# ввода данных свидетельствует пустая строка.

data = []

while True:
    current_string = input("Введите строку: ")

    if current_string != "":
        data.append(f"{current_string}\n")
    else:
        break;

if len(data) != 0:
    try:
        with open("Задача1.dat", "w") as f:
            f.writelines(data)
    except IOError as ex:
        print("Ошибка при записи в файл")
else:
    print("Нет данных для сохранения.")
