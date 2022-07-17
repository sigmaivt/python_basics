from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, clothes_name, clothes_type="одежда"):
        self.clothes_type = clothes_type
        self.clothes_name = clothes_name

    @abstractmethod
    def calculate_cloth_consumption(self):
        pass


class Coat(Clothes):

    def __init__(self, name, v):
        self.v = v
        super().__init__(name, "пальто")

    @property
    def calculate_cloth_consumption(self):
        return f"На пошив одежды {self.clothes_name} /типа {self.clothes_type}/ " \
               f"требуется {self.v / 6.5 + 0.5:.2f} м материи"


class Costume(Clothes):

    def __init__(self, name, h):
        self.h = h
        super().__init__(name, "костюм")

    @property
    def calculate_cloth_consumption(self):
        return f"На пошив одежды {self.clothes_name} /типа {self.clothes_type}/ " \
               f"требуется {self.h * 2 + 0.3:.2f} м материи"


coat1 = Coat("пальто Максима", 2)
print(coat1.calculate_cloth_consumption)
costume1 = Costume("костюм Николая", 3)
print(costume1.calculate_cloth_consumption)
