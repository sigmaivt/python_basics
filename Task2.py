number = int(input("введите размер списка: "))
working_list = list()
i = 1
while i <= number:
    working_list.append(input(f"введите {i+1}-ый элемент списка из {number}: "))
    i = i + 1
print(working_list)
i = 0
while (i + 1) < len(working_list):
    temp_str = working_list[i]
    working_list[i] = working_list[i+1]
    working_list[i+1] = temp_str
    i = i + 2
print(working_list)
