def fact(number):
    n = 1
    for i in range(1, number+1):
        n *= i
        yield n


for el in fact(int(input("Введите число: "))):
    print(el)
