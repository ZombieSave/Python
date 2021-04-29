class Worker:
    def __init__(self, name, middle_name, surname, position, wage, bonus):
        self._name = name
        self._surname = surname
        self._middle_name = middle_name
        self._position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, middle_name, surname, position, wage, bonus):
        super().__init__(name, middle_name, surname, position, wage, bonus)

    def get_full_name(self):
        return f"{self._surname} {self._name} {self._middle_name}, {self._position}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


p = Position("Виктор", "Робертович", "Цой", "кочегар", 80, 10)
print(f"Полное имя: {p.get_full_name()}")
print(f"Доход: {p.get_total_income()}")

p = Position("Юрий", "Юлианович", "Шевчук", "учитель рисования", 100, 20)
print(f"Полное имя: {p.get_full_name()}")
print(f"Доход: {p.get_total_income()}")