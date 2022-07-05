try:
    with open("my_file.txt", 'w') as file_obj:
        input_line = input("Введите строк для записи в файл: ")
        while input_line != "":
            file_obj.write(f'{input_line}\n')
            input_line = input("Введите строк для записи в файл: ")
            continue
except IOError:
    print("Ошибка при создании файла")
finally:
    file_obj.close()
    print("Файл создан")
