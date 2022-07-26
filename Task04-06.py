class NotEnoughEquipmentError(Exception):
    pass


class NoSuchDepartment(Exception):
    pass


class Store:
    department_list = {"Офис", "Производство", "Финотдел"}

    def __init__(self, name, address, capacity):
        self.name = name
        self.address = address
        self.capacity = int(capacity)
        self.store_items = {}

    def __str__(self):
        return f"Склад - {self.name}\nАдрес склада - {self.address}\nВместимость склада - {self.capacity}"

    def recieve_equipment(self, equipment, number):
        try:
            number_old = self.store_items.pop(equipment)
            number += number_old
            self.store_items[equipment] = number
        except KeyError:
            self.store_items[equipment] = number

    def give_equimpent(self, equipment, department, number):

        try:
            if department not in Store.department_list:
                raise NoSuchDepartment
            else:
                number_old = self.store_items.pop(equipment)
                if number_old < number:
                    self.store_items[equipment] = number_old
                    raise NotEnoughEquipmentError
                else:
                    if number_old > number:
                        number = number_old - number
                        self.store_items[equipment] = number
        except NoSuchDepartment:
            print(f"Нет такого отдела - {department}")
        except NotEnoughEquipmentError:
            print(f"Нет в наличие столько техники {equipment.model}")
        except KeyError:
            print(f"Техники {equipment.model} нет на складе")

    def print_store(self):
        for el in self.store_items.keys():
            print(f"{el.equipment_type}, модель {el.model}, на складе - {self.store_items[el]} шт")


class OfficeEquipment:

    def __init__(self, model, production_firm, equipment_type):
        self.model = model
        self.firm = production_firm
        self.equipment_type = equipment_type

    def __str__(self):
        return f"Модель техники - {self.model}\nТип техники - {self.equipment_type}\n"\
                f"Фирма-производитель - {self.firm}"

    def short_print(self):
        return f"Модель техники - {self.model}; Тип техники - {self.equipment_type}"


class Printer(OfficeEquipment):

    def __init__(self, model, production_firm, paper_size, speed):
        super().__init__(model, production_firm, "принтер")
        self.paper_size = paper_size
        try:
            self.speed = int(speed)
        except ValueError:
            print("Ошибка !!! Скорость должна быть числом")

    def __str__(self):
        return f"{super().__str__()}\nФормат бумаги - {self.paper_size}\nСкорость печати - {self.speed}"


class Scanner(OfficeEquipment):

    def __init__(self, model, production_firm, paper_size, dpi):
        super().__init__(model, production_firm, "сканнер")
        self.paper_size = paper_size
        try:
            self.dpi = int(dpi)
        except ValueError:
            print("Ошибка !!! Разрешение должно быть числом")

    def __str__(self):
        return f"{super().__str__()}\nФормат бумаги - {self.paper_size}\nРазрешение - {self.dpi}"


class Zerox(OfficeEquipment):

    def __init__(self, model, production_firm, paper_size, sides):
        super().__init__(model, production_firm, "Ксерокс")
        self.paper_size = paper_size
        self.sides = sides

    def __str__(self):
        return f"{super().__str__()}\nФормат бумаги - {self.paper_size}\nКоличество сторон - {self.sides}"


store1 = Store("store1", "Moscow", 32)
print(store1)
office_equipment1 = OfficeEquipment("С_Sh_1", "Cannon", "шредер")
printer0 = Printer("HP_P_2", "HP", "A3", "аб")  # выдает ошибку - скорость не число
printer1 = Printer("HP_P_2", "HP", "A3", 120)
printer2 = Printer("Cn_P_1", "Canon", "A2", 200)
scanner1 = Scanner("Z_S_1", "Zerox", "А4", 1200)
zerox1 = Zerox("Z_Z_1", "Zerox", "A3", 2)
print(office_equipment1)
print(printer1)
print(scanner1)
store1.recieve_equipment(printer1, 2)
store1.recieve_equipment(printer1, 3)
store1.recieve_equipment(scanner1, 3)
store1.recieve_equipment(printer2, 10)
print("Остатки на складе после оприходования:")
store1.print_store()
store1.give_equimpent(printer1, "Офис", 4)
store1.give_equimpent(scanner1, "Производство", 4)  # ошибка - нет такого количества на складе
store1.give_equimpent(zerox1, "Финотдел", 4)  # ошибка - нет такого оборудования на складе
store1.give_equimpent(scanner1, "head office", 4)  # ошибка - нет такого подразделения
print("Остатки на складе после списания принтера HP_P_2 (4 шт) :")
store1.print_store()
store1.give_equimpent(scanner1, "Финотдел", 3)  # списание под 0
print("Остатки на складе после списания сканера Z_S_1 под ноль:")
store1.print_store()
