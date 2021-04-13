# Для списка реализовать обмен значений соседних элементов. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний
# сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию input().

inputString = input("Введите ряд чисел через пробел: ")
inputList = inputString.split()
print(inputList)

for (i, item) in enumerate(inputList):
    if i % 2 != 0:
        inputList[i-1], inputList[i] = inputList[i], inputList[i-1]

print(inputList)



