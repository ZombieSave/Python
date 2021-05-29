# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
# числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce


def aggregate(previous, current):
    return previous * current


ev_list = [i for i in list(range(100, 1000+1)) if i % 2 == 0]
result = reduce(aggregate, ev_list)
print(result)


