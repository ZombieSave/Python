# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
# собственности, выручка, издержки.

import json

result = []

with open("text_7.txt", "r", encoding="utf-8") as f:
    result_dict = {i.split()[0]: float(i.split()[2]) - float(i.split()[3]) for i in f.readlines()}

profit_list = list(filter(lambda x:
                          x > 0,
                          map(float,
                              result_dict.values())))

average_profit = sum(profit_list) / len(profit_list)
result.append(result_dict)
result.append({"average_profit": average_profit})

with open("Задача7.json", "w", encoding="utf8") as jf:
    json.dump(result, jf, ensure_ascii=False, indent=4)





