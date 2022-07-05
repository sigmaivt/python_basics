try:
    with open("my_file.txt") as file_obj:
        report = [0]
        count_number = 0
        for line in file_obj:
            count_number += 1
            word_count = 0
            line = line.expandtabs(1) 
            line = line.strip()
            while "  " in line:
                line = line.replace("  ", " ")
            print(line)
            for word in line.split(" "):
                word_count += 1
            report.append([count_number, word_count])
        report.pop(0)
        report.insert(0, count_number)
except IOError:
    print("Ошибка при открытии файла")
finally:
    file_obj.close()
    print(f"Отчет о содержимом файла:\n{report}")
