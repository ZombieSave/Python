# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год»


class Data:
    def __init__(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year

    @classmethod
    def extract_date_parts(cls, date_str):
        try:
            dates = date_str.split("-")
            return cls(int(dates[0]), int(dates[1]), int(dates[2]))
        except:
            raise

    @staticmethod
    def validate(date_string):
        try:
            obj = Data.extract_date_parts(date_string)
            months_with_31_days = {1, 3, 5, 7, 8, 10, 12}

            if not (1990 < obj.__year <= 9999):
                raise

            if not (0 < obj.__month <= 12):
                raise

            if (obj.__month in months_with_31_days and not (0 < obj.__day <= 31)) or \
               (obj.__month not in months_with_31_days and not (0 < obj.__day <= 30)) or \
               (obj.__month == 2 and not (0 < obj.__day <= 28)):
                raise

            print(f"Результат валидации '{date_string}': \nдень: {obj.__day}, месяц: {obj.__month}, год {obj.__year}")
        except:
            print(f"Строка '{date_string}' не распознана как корректная дата")


Data.validate("28-2-2021")
Data.validate("31-6-2021")
