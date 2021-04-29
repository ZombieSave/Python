import random


class Car:
    def __init__(self, color, model, is_police):
        self.__turn_on = ["налево", "направо"]
        self._speed = 0
        self._color = color
        self._model = model
        self._is_police = is_police

    def go(self):
        print(f"{self._color} {self._model}: начато движение")
        self._speed = random.randint(1, 140)

    def stop(self):
        print(f"{self._color} {self._model}: остановка")
        self._speed = 0

    def turn(self):

        print(f"{self._color} {self._model}: поворот {self.__turn_on[random.randint(0, 1)]}")

    def show_speed(self):
        print(f"{self._color} {self._model}: текущая скорость {self._speed}")


class TownCar(Car):
    def __init__(self, color, name, is_police):
        super().__init__(color, name, is_police)

    def show_speed(self):
        super().show_speed()

        if self._speed > 60:
            print(f"{self._model}: скорость превышена")


class SportCar(Car):
    def __init__(self, color, name, is_police):
        super().__init__(color, name, is_police)


class WorkCar(Car):
    def __init__(self, color, name, is_police):
        super().__init__(color, name, is_police)

    def show_speed(self):
        super().show_speed()

        if self._speed > 40:
            print(f"Скорость превышена")


class PoliceCar(Car):
    def __init__(self, color, name, is_police):
        super().__init__(color, name, is_police)


town_car = TownCar("Серый", "Hyunday", False)
town_car.show_speed()
town_car.go()
town_car.show_speed()
town_car.turn()
town_car.turn()
town_car.stop()
town_car.show_speed()
town_car.go()
town_car.show_speed()

work_car = WorkCar("Крвсный", "Renault", False)
work_car.show_speed()
work_car.go()
work_car.show_speed()
work_car.turn()
work_car.turn()
work_car.stop()
work_car.show_speed()
work_car.go()
work_car.show_speed()

work_car = WorkCar("Белый", "Renault", False)
work_car.show_speed()
work_car.go()
work_car.show_speed()
work_car.turn()
work_car.turn()
work_car.stop()
work_car.show_speed()
work_car.go()
work_car.show_speed()


police_car = PoliceCar("Коричневый", "ZAZ", True)
police_car.show_speed()
police_car.go()
police_car.show_speed()
police_car.turn()
police_car.turn()
police_car.stop()
police_car.show_speed()
police_car.go()
police_car.show_speed()
