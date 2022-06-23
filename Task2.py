def print_user_data(func_name, func_surname, func_year, func_town, func_email, func_telephone):
    try:
        print(" ".join([func_name, func_surname, func_year, func_town, func_email, func_telephone]))
        return 1
    except:
        print("произошла ошибка")
        return -1

first_name = input("введите ваше имя: ")
last_name = input("введите вашу фамилию: ")
year_of_birth = input("введите год рождения: ")
town_of_birth = input("введите город рождения: ")
email = input("введите email: ")
telephone = input("введите телефон: ")
print_user_data(func_name=first_name, func_surname=last_name, func_year=year_of_birth, func_town=town_of_birth,
                func_email=email, func_telephone=telephone)
