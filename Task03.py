class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


Position1 = Position("Максим", "Сигачев", "аналитик", 100000, 20000)
print(Position1.get_full_name())
print(Position1.get_total_income())
