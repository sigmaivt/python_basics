my_list = [7, 5, 3, 3, 2]
number = int(input("введите число: "))
if my_list[0] < number:
    my_list.insert(0, number)
else:
    i = 1
    number_inserted = False
    while i < len(my_list):
        if my_list[i-1] >= number and my_list[i] < number:
            my_list.insert(i, number)
            number_inserted = True
            break
        i = i + 1
        continue
    if number_inserted == False:
        my_list.append(number)
print(my_list)
