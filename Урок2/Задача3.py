# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

monthString = input("Введите месяц: ")
month = int(monthString)
seasons = {"зима": [1, 2, 12],
           "весна": [3, 4, 5],
           "лето": [6, 7, 8],
           "осень": [9, 10, 11]}

for key in seasons.keys():
    if month in seasons[key]:
        print(f"Это {key}")
        break

print(seasons.values())
