# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

inputString = input("Введите количество секунд: ")
seconds = int(inputString)
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = (seconds % 3600) % 60

print("Время {h:0=2}:{m:0=2}:{s:0=2}".format(h=hours, m=minutes, s=seconds))
