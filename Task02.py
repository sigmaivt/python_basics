class MyZeroDivsionError(Exception):

    def __init__(self):
        print("Ошибка! Деление на ноль!")


try:
    dividend = float(input("Введите делимое - "))
    divider = float(input("Введите делитель - "))
    if divider == 0:
        raise MyZeroDivsionError
    else:
        quotient = dividend / divider
        print(f"Делимое / делитель = {quotient:.2f}")
except MyZeroDivsionError as err:
    print(err)
except ValueError:
    print("Были неправильно введены числа")
