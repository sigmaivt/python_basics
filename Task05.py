sum_numbers = 0
try:
    with open("sum_numbers.txt", "w+") as sum_numbers_file:
        input_string = input("Введите строку целых чисел разделенных пробелами: ")
        sum_numbers_file.write(input_string)
        sum_numbers_file.seek(0)
        numbers_list = sum_numbers_file.read().split(" ")
        for item in numbers_list:
            sum_numbers += int(item)
except IOError:
    print("Ошибка доступа к файлу")
finally:
    sum_numbers_file.close()
    print(f"Сумма чисел = {sum_numbers:,d}")
