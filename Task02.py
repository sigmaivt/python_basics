class Road:
    weigth_square_meter = 25
    thickness = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weigth_calculate(self):
        return self._length * self._width * Road.weigth_square_meter / 1000 * Road.thickness


road1 = Road(20, 5000)
print(f"Требуется асфальт весом = {road1.weigth_calculate()} тонн")
