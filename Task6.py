distance_in_first_day = float(input("введите пробег в 1-ый день (км): "))
target_distance = float(input("введите целевую дистанцию (км): "))
distance_runned = distance_in_first_day
number_of_days = 1
while distance_runned < target_distance:
    distance_runned = distance_runned * 1.1
    number_of_days = number_of_days + 1
    continue
print(f"чтобы пробежать {target_distance:.2f} км спортсмену потребуется {number_of_days:d} дн.")