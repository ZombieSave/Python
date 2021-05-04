import math


class Citos:
    def __init__(self, number_of_cells):
        self.__number_of_cells = number_of_cells

    @property
    def number_of_cells(self):
        return self.__number_of_cells

    def __add__(self, other):
        return Citos(self.__number_of_cells + other.number_of_cells)

    def __sub__(self, other):
        return Citos(abs(self.__number_of_cells - other.number_of_cells))

    def __mul__(self, other):
        return Citos(self.__number_of_cells * other.number_of_cells)

    def __truediv__(self, other):
        return Citos(math.floor(self.__number_of_cells / other.number_of_cells))

    def make_order(self, cols_count):
        if cols_count != [0]:
            for i in range(1, self.__number_of_cells + 1):
                print("*", end="")

                if i % cols_count == 0:
                    print("\n", end="")
        else:
            print("".join(["*" for i in range(self.__number_of_cells)]))

        print()


c1 = Citos(15)
c2 = Citos(10)

print("Сложение")
c3 = c1 + c2
c3.make_order(4)

print("Вычитание")
c3 = c1 - c2
c3.make_order(4)

print("Умножение")
c3 = c1 * c2
c3.make_order(20)

print("Деление")
c3 = c1 / c2
c3.make_order(4)


