class NotNumberError(Exception):

    def __init__(self, txt):
        self.txt = txt


input_list = []
while (input_string := input("Введите число - ")) != "stop":
    try:
        if input_string.isdigit() is False:
            raise NotNumberError(f"Ошибка! Введенная информация '{input_string}' не является числом")
        else:
            input_number = int(input_string)
            input_list.append(input_number)
    except NotNumberError as err:
        print(err)
    continue
print("Список чисел:")
print(input_list)
