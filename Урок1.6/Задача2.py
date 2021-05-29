class Road:
    def __init__(self, width, length):
        self._width = width
        self._length = length

    def asphalt_weight(self):
        return (self._width * self._length * 25 * 5) / 1000


r = Road(3, 5000)
print(f"Масса асфальта: {r.asphalt_weight()} тонн.")
