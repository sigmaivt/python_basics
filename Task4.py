str = input("введите строку: ")
list_str = str.split(" ")
print(list_str)
for i in range(len(list_str)):
    print(f"{i+1} - {list_str[i][0:10:1]}")
