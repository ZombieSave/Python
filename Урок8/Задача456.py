# Склад оргтехники
from abc import ABC, abstractmethod


class Storage:
    """
    склад
    """
    def __init__(self):
        self.__identity = 0  # счётчик id
        self.__items = {}  # хранилище товаров
        self.__departments = {1: "Отдел технического контроля", 2: "Отптовый отдел", 3: "Розничный отдел", 4: "Отдел б/у"}

    @property
    def all_items(self):
        return self.__items

    @property
    def departments(self):
        return self.__departments

    def incoming(self, equipment, department_id, price):
        """
        метод оприходования товара на склад
        :param equipment: товар
        :param department_id: id отдела
        :param price: цена
        """
        self.__identity += 1 # счётчик id товаров
        new_item = Item(self.__identity, department_id, equipment, price)

        if self.__items.get(equipment.equipment_type) is None:
            self.__items[equipment.equipment_type] = [new_item]
        else:
            self.__items[equipment.equipment_type].append(new_item)

        return new_item.id

    def move_to_department(self, item_id, new_department_id):
        """
        метод перевода товараа в другой отдел
        :param item_id: id товара
        :param new_department_id: id отдела
        """
        item = self.get_item(item_id)

        if item is not None:
            item.department_id = new_department_id
        else:
            raise StorageOperationError(f"Товар Id = {item_id} не найден")

    def get_item(self, item_id):
        """
        получение товара по id
        :param item_id: id
        :return: товар с заданным id
        """
        find_result = list(filter(lambda z: z != [],
                           list(map(lambda x:
                                    list(filter(lambda y: y.id == item_id, x)), self.__items.values()))))

        return find_result[0][0] if len(find_result) != 0 else None
# end class


class Item:
    """
    единица хранения
    """
    def __init__(self, item_id, department_id, equipment, price):
        self.__id = item_id
        self.__department_id = department_id
        self.__price = price
        self.__equipment = equipment

    @property
    def id(self):
        return self.__id

    @property
    def department_id(self):
        return self.__department_id

    @department_id.setter
    def department_id(self, value):
        self.__department_id = value

    @property
    def equipment(self):
        return self.__equipment

    @property
    def price(self):
        return self.__price
# end class


class Equipment(ABC):
    """
    Базовый клас товара
    """
    def __init__(self, equipment_type, brand):
        """
        :param equipment_type: принтер, сканер, копир
        :param brand: бренд производителя
        """
        self.__brand = brand
        self.__type = equipment_type

    def __str__(self):
        return f"{self.__type} \"{self.__brand}\""

    @property
    def equipment_type(self):
        return self.__type

    @property
    def brand(self):
        return self.__brand

    @staticmethod
    def get_equipment_type():
        return {1: "принтер", 2: "сканер", 3: "копир"}
# end class


class Printer(Equipment):
    def __init__(self, brand, printing_speed, print_type):
        super().__init__("Принтер", brand)
        self.__printing_speed = printing_speed
        self.__print_type = print_type

    def __str__(self):
        description = super().__str__()
        return f"{description}\nСкорость печати {self.__printing_speed} в минуту\nТип {Printer.print_types()[self.__print_type]}"

    @staticmethod
    def print_types():
        return {0: "Лазерный", 1: "Струйный"}
# end class


class Scaner(Equipment):
    def __init__(self, brand, scanning_speed):
        super().__init__("Сканер", brand)
        self.__scanning_speed = scanning_speed

    def __str__(self):
        description = super().__str__()
        return f"{description}\nСкорость сканирования {self.__scanning_speed} в минуту"
# end class


class Xerox(Equipment):
    def __init__(self, brand, copy_speed):
        super().__init__("Копировальный аппарат", brand)
        self.__copy_speed = copy_speed

    def __str__(self):
        description = super().__str__()
        return f"{description}\nСкорость копирования {self.__copy_speed} в минуту"
# end class


class WorkingStorage:
    """
    UI пользователя для работы со складом
    """
    def __input_department(self, departments):
        print("---------- Выберите код отдела: ", end="")

        for dep in departments.items():
            print(f"{dep[1]} {dep[0]}, ", end="")

        department_id_str = input()
        department_id = int(department_id_str)

        if department_id not in departments.keys():
            raise StorageOperationError("Неверный отдел")

        return department_id

    def __init__(self):
        print("---------- Операции складского учёта")
        self.__storage = Storage()

        p = Printer("HP", 3, 1)
        s1 = Scaner("Canon", 11)
        s2 = Scaner("Nikon", 22)
        x1 = Xerox("Rikoh", 12)

        self.__storage.incoming(p, 1, 200)
        self.__storage.incoming(s1, 2, 45)
        self.__storage.incoming(s2, 2, 22.1)
        self.__storage.incoming(x1, 4, 11.50)

    def start(self):
        while True:
            command_string = input(f"---------- Выберите операцию: "
                                   f"просмотр товаров - 1, "
                                   f"приход - 2, "
                                   f"передать в подразделение - 3, "
                                   f"выход - 0 ----------")
            try:
                try:
                    command = int(command_string)

                    if command == 0:
                        print("---------- Работа со складом завершена")
                        break
                    elif command == 1:
                        for key in self.__storage.all_items.keys():
                            print(f"*** Товары в категории {key}:")

                            for item in self.__storage.all_items[key]:
                                print(f"Id: {item.id}\n{item.equipment}\nЦена: {item.price}\nОтдел: {self.__storage.departments[item.department_id]}\n")

                    elif command == 2:
                        brand_str = input(">>>>> бренд производителя: ")
                        price_str = input(">>>>> цена: ")
                        price = float(price_str)
                        department_id = self.__input_department(self.__storage.departments)

                        equipment_type_str = input(">>>>> категория: 1 - принтер, 2 - сканер, 3 - копир")
                        equipment_type = int(equipment_type_str)

                        if equipment_type not in Equipment.get_equipment_type().keys():
                            raise StorageOperationError("Неверная категория товара")

                        new_equipment = None

                        if equipment_type == 1:
                            printing_speed_str = input(">>>>> дополнительный параметр: скорость печати ")
                            printing_speed = int(printing_speed_str)

                            print(">>>>> дополнительный параметр: тип принтера", end="")

                            for print_type in Printer.print_types().items():
                                print(f"{print_type[1]} {print_type[0]}, ", end="")

                            print_type_str = input()
                            print_type = int(print_type_str)

                            if print_type not in Printer.print_types().keys():
                                raise StorageOperationError("Неверный тип принтера")

                            new_equipment = Printer(brand_str, printing_speed, print_type)
                        elif equipment_type == 2:
                            scaning_speed_str = input(">>>>> дополнительный параметр: скорость сканирования ")
                            scaning_speed = int(scaning_speed_str)
                            new_equipment = Scaner(brand_str, scaning_speed)
                        elif equipment_type == 3:
                            coping_speed_str = input(">>>>> дополнительный параметр: скорость копирования ")
                            coping_speed = int(coping_speed_str)
                            new_equipment = Xerox(brand_str, coping_speed)

                        new_id = self.__storage.incoming(new_equipment, department_id, price)
                        item = self.__storage.get_item(new_id)
                        print("---------- Занесено на склад:")
                        print(f"Id: {item.id}\n{item.equipment}\nВ отдел: {self.__storage.departments[item.department_id]}")

                    elif command == 3:
                        item_id_str = input("Id товара: ")
                        item_id = int(item_id_str)
                        department_id = self.__input_department(self.__storage.departments)
                        self.__storage.move_to_department(item_id, department_id)
                        print(f"Товар Id = {item_id} передан в отдел {department_id}")
                except ValueError:
                    raise StorageOperationError("Неверный ввод")
            except StorageOperationError as ex:
                print(ex)

# end class


class StorageOperationError(Exception):
    def __init__(self, message="нет данных"):
        self.__message = message

    def __str__(self):
        return f"####### Ошибка операции со складом: {self.__message}"
# end class


w = WorkingStorage()
w.start()

