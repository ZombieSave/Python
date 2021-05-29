# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

try:
    with open("Задача1.dat", "r", encoding="utf-8") as f:
        data = [i for i in f]
except IOError:
    print("Ошибка при чтении файла")

print(f"Строк в файле: {len(data)}\n")

for i, item in enumerate(data):
    print(f"Строка {i+1} слов {len(item.split())}")


