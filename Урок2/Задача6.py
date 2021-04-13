# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.

list = []
userChoice = input("Хотите добавить товар (д/н)? ")

if userChoice.lower() == "д":
    index = 0

    while userChoice == "д":
        name = input("Наименование: ")
        price = input("Цена: ")
        amount = input("Количество: ")
        units = input("Единицы: ")

        index += 1
        list.append((index, {"наименование": name, "цена": float(price), "количество": int(amount), "eд": units}))
        userChoice = input("Добавить ещё товар (д/н)? ").lower()

    resultDict = dict()

    for item in list:
        for key in item[1]:
            if resultDict.get(key) is None:
                resultDict[key] = [item[1][key]]
            elif item[1][key] not in resultDict[key]:
                resultDict[key].append(item[1][key])

    print("Итог: ")
    print(resultDict)
print("Работа завершена")
