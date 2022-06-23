def int_func(local_str):
    for i in range(len(local_str)):
        if ord(local_str[i]) < 97 or ord(local_str[i]) > 122:
            print("есть латинские непрописные или нелатинские символы")
            return local_str
        else:
            continue
    return local_str.capitalize()


print(int_func(input("Введите строку: ")))