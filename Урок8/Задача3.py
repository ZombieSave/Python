class WrongInputException(Exception):
    def __init__(self):
        print("Ошибка ввода. Допустимы только числа")


result_list = []

while True:
    input_str = input("Введите число или 'q' для завершения ввода: ")

    if input_str == "q":
        break
    else:
        try:
            if not input_str.replace(".", "", 1).replace("-", "", 1).isdigit():
                raise WrongInputException

            result_list.append(input_str)
        except WrongInputException as ex:
            print(ex)

print("Результат: ")
print("  ".join(result_list))
