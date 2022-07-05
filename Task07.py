import json

try:
    with open("Firms.txt", encoding='utf-8') as firms_file:
        firms_profit_vocabulary = {line.split(" ")[0]: (float(line.split(" ")[1]) - float(line.split(" ")[2])) for line
                                   in firms_file}
        firms_average_vocabulary = firms_profit_vocabulary
        sum_profit = 0.0
        count_profit_firms = 0
        for item in firms_profit_vocabulary.values():
            print(item)
            if item >= 0:
                sum_profit += item
                count_profit_firms += 1
        try:
            average_profit = sum_profit / count_profit_firms
        except ZeroDivisionError:
            average_profit = 0
except IOError:
    print("Ошибка при доступе к файлу")
finally:
    firms_file.close()
    firms_list = [firms_profit_vocabulary, {"average_profit": average_profit}]
    print(firms_list)
    try:
        with open("firms.json", "w", encoding='utf-8') as firms_json_file:
            json.dump(firms_list, firms_json_file)
    except IOError:
        print("Ошибка при сохранении файла")
    finally:
        firms_json_file.close()
