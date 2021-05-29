class Complex:
    def __init__(self, x, y=1):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __add__(self, other):
        return Complex(self.__x + other.x, self.__y + other.y)

    def __mul__(self, other):
        x = self.__x * other.x - self.__y * other.y
        y = self.__x * other.y + self.__y * other.x

        return Complex(x, y)

    def __str__(self):
        return f"{self.__x} {'+' if self.__y > 0 else '-'} {abs(self.__y) if self.__y != 1 else ''}i"


v1 = Complex(2)
v2 = Complex(3, 5)
v3 = v1 + v2
print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2 = {v3}")
print()
v1 = Complex(3)
v2 = Complex(2, -3)
v3 = v1 * v2
print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 * v2 = {v3}")
