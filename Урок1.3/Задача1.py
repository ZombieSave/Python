# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
# у пользователя, предусмотреть обработку ситуации деления на ноль.


def division(v_x, v_y):
    try:
        x = int(v_x)
        y = int(v_y)

        return x / y
    except (ZeroDivisionError, ValueError) as ex:
        print(f"v_y: {v_x}; v_y: {v_y}; exception: {ex}")


xStr = input("Введите делимое: ")
yStr = input("Введите делитель: ")
z = division(xStr, yStr)
print(f"Частное: {z}")
