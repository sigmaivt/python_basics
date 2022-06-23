def my_func(x, y, type_of_calculation):
    try:
        x = float(x)
    except ValueError:
        print("Первый аргумент должен быть действительным числом")
        return -1, None
    try:
        y = int(y)
    except ValueError:
        print("Второй аргумент должен быть целым числом")
        return -1, None
    if x < 0:
        print("Первое число должен быть положительным")
        return -1, None
    elif y >= 0:
        print("Второе число должно быть отрицательным")
        return -1, None
    else:
        if type_of_calculation == 1:
            Local_result= x**y
        else:
            Local_result = 1/x
            for i in range(-1,y,-1):
                Local_result = Local_result/x
        return 1, Local_result


while input("Для окончания работы с программой введите Q, иначе любой другой символ: ").upper() != "Q":
    print("----------------------------------")
    x = input("введите 1-ое число: ")
    y = input("введите 2-ое число: ")
    result = my_func(x, y, 2)
    if result[0] == 1:
        print(f"{x} в степени {y} = {result[1]:e}")
    else:
        print("попробуйте еще раз")
    print("----------------------------------")
    continue
print("До новых встреч!")