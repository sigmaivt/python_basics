try:
    with open("Lessons.txt", encoding='utf-8') as lessons_file:
        lessons_list = [line.split(" ") for line in lessons_file]
        print(lessons_list)
        lessons_vocabulary = {"0": 0}
        for item in lessons_list:
            lesson_name = item[0][0:-1]
            lesson_hours_1 = 0 if item[1] == "-" else int(item[1][0:item[1].find("(")])
            lesson_hours_2 = 0 if item[2] == "-" else int(item[2][0:item[2].find("(")])
            lesson_hours_3 = 0 if item[3] == "-" else int(item[3][0:item[3].find("(")])
            lesson_hours = lesson_hours_1 + lesson_hours_2 + lesson_hours_3
            lessons_vocabulary[lesson_name] = lesson_hours
        lessons_vocabulary.pop("0")
except IOError:
    print("Ошибка открытия файла")
finally:
    lessons_file.close()
    print(lessons_vocabulary)
