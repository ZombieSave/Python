# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

inputString = input("Введите целое число: ")

n1 = int(inputString)
n2 = int(inputString + inputString)
n3 = int(inputString + inputString + inputString)
result = n1 + n2 + n3

print("Сумма равна {0}".format(result))
