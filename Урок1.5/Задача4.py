# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

try:
    source = open("source_4.txt", "r")
    target = open("target_4.txt", "w", encoding="utf-8")
    count = 0

    while count < 4:
        current = source.readline().split()

        if int(current[2]) == 1:
            current[0] = "Один"
        elif int(current[2]) == 2:
            current[0] = "Два"
        elif int(current[2]) == 3:
            current[0] = "Три"
        elif int(current[2]) == 4:
            current[0] = "Четыре"

        target.write(f"{' '.join(current)}\n")
        count += 1

except IOError:
    print("Ошибка чтения/записи")
finally:
    if not source.closed:
        source.close()

    if not target.closed:
        target.close()




