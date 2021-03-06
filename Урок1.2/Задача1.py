# Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
# элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

miscellaneous = ["Str",
                 20,
                 3.1,
                 False,
                 ("i", 13, True, ["1", "22"]),
                 [1, 2, 3],
                 {11, 12, 13},
                 dict(key1=1000),
                 bytes("bytes", encoding='utf-8'),
                 bytearray(123456),
                 None]

for item in miscellaneous:
    print(type(item))
