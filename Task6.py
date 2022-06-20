number = int(input("введите количество элементов: "))
working_list = list()
i = 1
while i <= number:
    print(f"ввод {i}-го элемента из {number}")
    name = input("название: ")
    price = float(input("цена: "))
    quantity = int(input("количество: "))
    unit = input("ед. измерения: ")
    list_item_dict = {"название": name, "цена": price, "количество": quantity, "ед": unit}
    working_list.append((i, list_item_dict))
    i = i + 1
print(working_list)

name_set = set()
price_set = set()
quantity_set = set()
unit_set = set()

for i in range(len(working_list)):
    name_set.add((working_list[i])[1].get("название"))
    price_set.add((working_list[i])[1].get("цена"))
    quantity_set.add((working_list[i])[1].get("количество"))
    unit_set.add((working_list[i])[1].get("ед"))

analytic_dict = {"название": name_set, "цена": price_set, "количество": quantity_set, "ед": unit_set}

print(analytic_dict)