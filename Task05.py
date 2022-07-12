class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def draw(self):
        print("Запуск отрисовки для класса Pen")


class Pencil(Stationery):

    def draw(self):
        print("Запуск отрисовки для класса Pencil")


class Handle(Stationery):

    def draw(self):
        print("Запуск отрисовки для класса Handle")


pen1 = Pen("ручка красная")
pencil1 = Pencil("карандаш зеленый")
handle1 = Handle("маркер синий")
pen1.draw()
pencil1.draw()
handle1.draw()
