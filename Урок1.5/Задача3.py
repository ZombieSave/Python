# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
# дохода сотрудников.

try:
    with open("text_3.txt", "r", encoding="utf-8") as f:
        data = f.readlines()

    print("Сотрудники с окладом менее 20 т.р.:")

    for item in list(map(lambda x: x, filter(lambda x: float(x.split()[1]) < 20000, data))):
        print(item, end="")

    salary_list = list(map(lambda x: float(x.split()[1]), data))
    average_salary = sum(salary_list) / len(salary_list)
    print(f"\nСредняя величина дохода сотрудников: {average_salary}")
except IOError:
    print("Ошибка чтения файла")
except Exception as ex:
    print(ex)
