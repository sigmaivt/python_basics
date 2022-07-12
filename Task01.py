from itertools import cycle
from time import sleep


class TrafficLight:
    __color = "No color"
    __color_codes = {"red": 31, "yellow": 33, "green": 32}
    __color_modes = ()

    def __init__(self, red_time, yellow_time, green_time):
        self.__color_modes = (
            ("red", red_time), ("yellow", yellow_time), ("green", green_time), ("yellow", yellow_time))

    def running(self):
        for __color, counter_max in cycle(self.__color_modes):
            for counter in range(counter_max):
                print(f"\r\033[{self.__color_codes[__color]}m\033[1m{__color} {counter + 1}/{counter_max}\033[0m", end="")
                sleep(1)
#            print("\n")


TrafficLight1 = Traff   icLight(7, 2, 5)
try:
    TrafficLight1.running()
except KeyboardInterrupt:
    print("\rРабота завершена")

