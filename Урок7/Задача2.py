from abc import ABC, abstractmethod


class Clothes(ABC):
    _name = ""

    @abstractmethod
    def calculate_consumption(self):
        pass

    @property
    def name(self):
        return self._name;


class Coat(Clothes):
    Clothes._name = "Пальто"
    __size = 0

    @property
    def size(self):
        return self.__size

    def __init__(self, size):
        Clothes.__init__(self)
        self.__size = size

    def calculate_consumption(self):
        return round(self.__size / 6.5 + 0.5)


class Suit(Clothes):
    Clothes._name = "Костюм"
    __height = 0

    @property
    def height(self):
        return self.__height

    def __init__(self, height):
        Clothes.__init__(self);
        self.__height = height

    def calculate_consumption(self):
        return round(self.__height * 2 + 0.3, 2)


c = Coat(12)
s = Suit(10)
print(f"Общий расход ткани для {c.name} размером {c.size}: {c.calculate_consumption()}")
print(f"Общий расход ткани для {s.name} ростом {s.height}: {s.calculate_consumption()}")
