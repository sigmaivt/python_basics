from functools import reduce


def multiple(el_prev, el):
    return el_prev * el


my_list = [el for el in range(10, 1001) if el % 2 == 0]
print(my_list)
print(reduce(multiple, my_list))
