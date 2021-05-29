# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте
# цикл while и арифметические операции.

inputString = input("Введите целое число: ")
value = int(inputString)
maxDigit = 0

while value > 0:
    currentDigit = value % 10
    value = value // 10

    if currentDigit == 9:
        maxDigit = currentDigit
        break

    if currentDigit > maxDigit:
        maxDigit = currentDigit

print("Самая большая цифра в числе: {0}".format(maxDigit))
