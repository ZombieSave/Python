class DivisionByZeroError(Exception):
    def __init__(self):
        print("Error: попытка деления на 0")


aStr = input("Введите делимое: ")
bStr = input("Введите делитель: ")

try:
    a = int(aStr)
    b = int(bStr)

    if b == 0:
        raise DivisionByZeroError

    print(f"Частное: {a / b}")
except ValueError as ex:
    print("Введены некорректные данные")
except DivisionByZeroError as ex:
    print(ex)
