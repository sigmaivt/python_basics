def func(arg1, arg2, arg3):
    try:
        return (max(arg1+arg2, arg2+arg3, arg3+arg1))
    except:
        print("ошибка")


print(func(1, 2, 3))