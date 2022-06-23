def my_func(prev_sum, local_str):
    local_sum = prev_sum
    my_list = local_str.split(" ")
    for i in range(len(my_list)):
        if my_list[i].upper() == "Q":
            return -1, local_sum
        else:
            try:
                add_element = float(my_list[i])
                local_sum += add_element
                continue
            except:
                break
    return 1, local_sum


global_sum = 1, 0.0
while global_sum[0] == 1:
    global_sum = my_func(global_sum[1], input("Введите строку для суммирования (Q - для окончания расчета): "))
    print(f"Текущая сумма = {global_sum[1]}")
    continue
print(f"Итоговая сумма = {global_sum[1]}")