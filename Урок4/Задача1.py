# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.

from sys import argv
from decimal import Decimal


def parse_input(func, value):
    """
    Функция валидации и преобразования строки в число
    :param func: преобразователи строки в число int(), float()
    :param value: строка преобразования
    :return: (<int, float>, <True, False>)
    """

    try:
        val = func(value.replace(",", "."))
        result = (val, True)
    except ValueError:
        result = (0, False)

    return result


input_valid = True
s_name, input_hh, input_tariff, input_award = "x000"

try:
    s_name, input_hh, input_tariff, input_award = argv
except ValueError as ex:
    input_valid = False
    print(f"Ошибка ввода: {ex}")

if input_valid:
    hh, is_valid = parse_input(int, input_hh)

    if not is_valid:
        input_valid = False
        print(f"Ошибка ввода выработки: {input_hh}. Значение должно быть целым числом.")

    tariff, is_valid = parse_input(Decimal, input_tariff)

    if not is_valid:
        input_valid = False
        print(f"Ошибка ввода ставки: {input_tariff}. Значение должно быть целым или дробным числом.")

    award, is_valid = parse_input(Decimal, input_award)

    if not is_valid:
        input_valid = False
        print(f"Ошибка ввода премии: {input_award}. Значение должно быть целым или дробным числом.")

    if input_valid:
        salary = round(hh * tariff + award, 2)
        print(f"Заработная плата: {salary} р.")


# python Задача1.py 10 2.5 3,5
# Заработная плата: 28.5 р.

