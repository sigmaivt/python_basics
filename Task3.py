year_list = ["зима","зима","весна","весна","весна","лето","лето","лето","осень","осень","осень","зима"]
month_list = ["январь","февраль","март","апрель","май","июнь","июль","август","сентябрь","октябрь","ноябрь","декабрь"]

month_number = int(input("введите порядковый номер месяца: "))

print(f"время года {month_number}-го месяца ({month_list[month_number-1]}) - {year_list[month_number-1]}")

year_dict =  {1:"зима", 2:"зима", 3:"весна", 4:"весна", 5:"весна", 6:"лето", 7:"лето",
              8:"лето", 9:"осень", 10:"осень", 11:"осень", 12:"зима"}
month_dict =  {1:"январь", 2:"февраль", 3:"март", 4:"апрель", 5:"май", 6:"июнь", 7:"июль",
              8:"август", 9:"сентябрь", 10:"октябрь", 11:"ноябрь", 12:"декабрь"}

print(f"время года {month_number}-го месяца ({month_dict.get(month_number)}) - {year_dict.get(month_number)}")