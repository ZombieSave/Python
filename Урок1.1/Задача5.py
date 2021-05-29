# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

proceedsString = input("Введите значение выручки: ")
costString = input("Введите значение издержек: ")
proceeds = float(proceedsString)
cost = float(costString)

if proceeds > cost:
    numberOfEmployeesString = input("Введите количество сотрудников фирмы: ")
    numberOfEmployees = int(numberOfEmployeesString)

    profit = proceeds - cost  # прибыль
    profitability = profit / proceeds  # рентабельность
    profitPerEmployee = profit / numberOfEmployees  # прибыль в расчете на одного сотрудника

    print("Фирма отработала с прибылью {:.2f}".format(proceeds - cost))
    print("Рентабельность: {:.2f}".format(profitability))
    print("Прибыль на одного сотрудника: {:.2f}".format(profitPerEmployee))
elif proceeds < cost:
    print("Фирма отработала в убыток {:.2F}".format(proceeds - cost))
else:
    print("Фирма отработала в 0")
