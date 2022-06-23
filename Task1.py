def divide(a, b):
    try:
        return 1, float(a)/float(b)
    except ZeroDivisionError:
        return -1, None
    except ValueError:
        return -2, None


while input("Для окончания работы с программой введите Q, иначе любой другой символ: ").upper() != "Q":
    print("----------------------------------")
    divisible = input("Введите делимое: ")
    divider = input("Введите делитель: ")
    result = divide(divisible, divider)
    print(type(result))
    if result[0] == -1:
        print("Ошибка - деление на ноль. Попробуйте еще раз")
    elif result[0] == -2:
        print("Ошибка - неправильно введены числа. Попробуйте еще раз")
    elif result[0] == 1:
        print(f"Результат деления {float(divisible):f} на {float(divider):f} = {result[1]:f}")
    else:
        print("Ошибка. Попробуйте еще раз")
    print("----------------------------------")
    continue
print("До новых встреч!")
