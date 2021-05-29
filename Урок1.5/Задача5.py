# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random

try:
    f = open("Задача5.dat", "w+")

    for item in range(0, 10):
        f.write(f"{str(random.randint(0, 100))} ")

    f.flush()
    f.seek(0)
    result = sum(list(map(int, f.read().split())))
    print(f"Сумма записаных чисел: {result}")
except IOError:
    print("Ошибка чтения/записи")
finally:
    if not f.closed:
        f.close()

