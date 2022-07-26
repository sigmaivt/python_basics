class WrongMonthNumber(Exception):
    pass


class WrongNumberOfDaysInMonth(Exception):

    def __init(self, txt):
        self.txt = txt


class Date:

    def __init__(self, date_string):
        self.date_string = date_string

    @classmethod
    def date_extraction(cls, date_string):
        date_list = date_string.split("-")
        print(cls)
        print(f"Год = {int(date_list[2])}\nМесяц = {int(date_list[1])}\nДень = {int(date_list[0])}")

    @staticmethod
    def date_validation(date_string):
        date_month_check_list = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 20, 12: 31}
        date_list = date_string.split("-")
        print(f"Проверка {date_string}")
        try:
            date_list_int = [int(el) for el in date_list]
            day = date_list_int[0]
            month = date_list_int[1]
            year = date_list_int[2]
            if month > 12:
                raise WrongMonthNumber
            elif day > date_month_check_list[month]:
                raise WrongNumberOfDaysInMonth(f"В месяце {month} должно быть меньше дней")
            elif year % 4 != 0 and month == 2 and day == 29:
                raise WrongNumberOfDaysInMonth(f"Только в високосном году в феврале может быть 29 дней")
            print("Все Ок")
        except ValueError:
            print("дата, месяц и год должны быть целыми числами")
        except WrongMonthNumber:
            print("Месяц должен быть от 1 до 12")
        except WrongNumberOfDaysInMonth as err:
            print(err)


Date.date_extraction("31-12-2022")
date1 = Date("31-07-2010")
date1.date_extraction("31-01-2009")
Date.date_validation("31-03-1973")
Date.date_validation("31-13-1973")
Date.date_validation("31-04-1973")
Date.date_validation("29-02-2008")
Date.date_validation("29-02-2009")

