class Stationery:
    def __init__(self, title):
        self._title = title

    def draw(self):
        print(f"Запуск отрисовки")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Пишет {self._title}")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Чертит {self._title}")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Красит {self._title}")


pen = Pen("Красная ручка")
pen.draw()

pencil = Pencil("Чёрный карандаш")
pencil.draw()

handle = Handle("Синий маркер")
handle.draw()


