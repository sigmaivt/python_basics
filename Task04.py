class Car:

    def __init__(self, speed, color, name, is_police, direction):
        self.current_speed = 0
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = bool(is_police)
        self.direction = direction

    def go(self):
        if self.current_speed == 0:
            self.current_speed = self.speed
            print(f"Машина {self.name} цвета {self.color} поехала со скоростью ", end="")
            print(f"{self.current_speed} км/ч в направлении {self.direction}")
        else:
            print(f"Машина {self.name} цвета {self.color} и так уже едет")

    def stop(self):
        if self.current_speed == 0:
            print(f"Машина {self.name} цвета {self.color} и так уже стоит")
        else:
            self.current_speed = 0
            print(f"Машина {self.name} цвета {self.color} остановилась")

    def turn(self, direction):
        if self.current_speed == 0:
            print(f"Машина {self.name} цвета {self.color} не может повернуть, так как она стоит")
        elif self.direction == direction:
            print(f"Машина {self.name} цвета {self.color} уже едет на {self.direction}")
        else:
            self.direction = direction
            print(f"Машина {self.name} цвета {self.color} повернула на {self.direction}")

    def show_speed(self):
        print(f"Текущая скорость машины {self.name} цвета {self.color} - {self.current_speed} км/ч")


class TownCar(Car):

    def __init__(self, speed, color, name, direction):
        super().__init__(speed, color, name, False, direction)

    def show_speed(self):
        print(f"Текущая скорость машины {self.name} цвета {self.color} - {self.current_speed} км/ч")
        if self.current_speed > 60:
            print(f"Внимание! Превышение максимальной скорости 60 км/ч")


class Sport(Car):

    def __init__(self, speed, color, name, direction):
        super().__init__(speed, color, name, False, direction)


class WorkCar(Car):

    def __init__(self, speed, color, name, direction):
        super().__init__(speed, color, name, False, direction)

    def show_speed(self):
        print(f"Текущая скорость машины {self.name} цвета {self.color} - {self.current_speed} км/ч")
        if self.current_speed > 40:
            print(f"Внимание! Превышение максимальной скорости 40 км/ч")


class Police(Car):

    def __init__(self, speed, color, name, direction):
        super().__init__(speed, color, name, True, direction)


workcar1 = WorkCar(50, "синий", "лада приора", "юг")
print(workcar1.name, workcar1.speed, workcar1.current_speed)
workcar1.stop()
workcar1.go()
workcar1.stop()
workcar1.turn("север")
workcar1.go()
workcar1.turn("юг")
workcar1.turn("север")
workcar1.show_speed()
workcar1.stop()

towncar1 = TownCar(55, "красный", "мерседес", "запад")
print(towncar1.name, towncar1.is_police, towncar1.current_speed, towncar1.color)
towncar1.stop()
towncar1.go()
towncar1.go()
towncar1.turn("восток")
towncar1.go()
towncar1.turn("юг")
towncar1.turn("север")
towncar1.show_speed()
towncar1.stop()
