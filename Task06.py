from sys import argv
from itertools import count, cycle


script_name, initial_number1, max_number1, max_number2 = argv
for el in count(int(initial_number1)):
    if el > int(max_number1):
        break
    else:
        print(el)

my_list = [1, "текст", [2, 3]]
i = 0

# print(cycle(my_list))

for el in cycle(my_list):
    if i > int(max_number2):
        break
    print(el)
    i += 1
