# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
# чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
# чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
# программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих
# чисел к полученной ранее сумме и после этого завершить программу.


def current_sum(input_str):
    """
    Возвращает сумму введённых чисел.
    Выход - "q"
    """
    exit_symbol = 'q'
    array = input_str.split()
    result = sum(list(map(int, filter(lambda x: x.isnumeric(), array))))

    return result, input_str[-1].lower() == exit_symbol


total_sum = 0
stop = False

while not stop:
    x_str = input("Введите ряд чисел или 'q' для выхода: ")
    result = current_sum(x_str)
    total_sum += result[0]
    stop = result[1]

    if not stop:
        print(f"{result[0]}({total_sum})")

print(f"Итоговая сумма: {total_sum}")
