english_russian_vocab = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

try:
    with open("english_numbers.txt") as eng_numbers_file:
        rus_numbers = [[english_russian_vocab.get(line.split(" ")[0]), "-", line.split(" ")[2]] for line in
                       eng_numbers_file]
except IOError:
    print("Ошибка открытия файла")
finally:
    eng_numbers_file.close()
    try:
        with open("russian_numbers.txt", "w", encoding='utf-8') as rus_numbers_file:
            for line in rus_numbers:
                rus_numbers_file.write(" ".join(line))
    except IOError:
        print("Ошибка записи в файл")
