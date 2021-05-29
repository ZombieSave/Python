# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
# необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


def my_func1(x, y):
    """
    :param x:  действительное положительное число
    :param y: целое отрицательное число
    """
    try:
        denominator = x;

        for i in range(2, abs(y) + 1):
            denominator = denominator * x

        result = round(1 / denominator, 4)
        print(result)
    except ValueError as ex:
        print(ex)


def my_func2(x, y):
    try:
        denominator = x ** abs(y);
        result = round(1 / denominator, 4)
        print(result)
    except ValueError as ex:
        print(ex)


my_func1(2.2, -3)
my_func2(2, -3)
