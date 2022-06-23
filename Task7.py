def int_func(local_str):
    for i in range(len(local_str)):
        if ord(local_str[i]) < 97 or ord(local_str[i]) > 122:
            print("есть латинские непрописные или нелатинские символы")
            return local_str
        else:
            continue
    return local_str.capitalize()


initial_str = input("Введите строку: ")
initial_list = initial_str.split(" ")
final_list = []
for i in range(len(initial_list)):
    final_list.append(int_func(initial_list[i]))
    continue
final_str = " ".join(final_list)
print(final_str)
