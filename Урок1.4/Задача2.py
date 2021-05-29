# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
# элемента. Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать
# генератор. Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

import random

list_test = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list_result_test = [item for i, item in enumerate(list_test) if i > 0 and item > list_test[i-1]]

list_random = [random.randint(1, 300) for i in list(range(0, 20))]
list_result_random = [item for i, item in enumerate(list_random) if i > 0 and item > list_random[i-1]]

print(f"list_test: {list_test}")
print(f"list_result_test: {list_result_test}")

print(f"list_random: {list_random}")
print(f"list_result_random: {list_result_random}")


