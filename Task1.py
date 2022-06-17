# пример на использование переменных
name = "Максим"
year_of_birth = 1973
married = True
average_school_grade = 4.75

print(type(name))
print(type(year_of_birth))
print(type(married))
print(type(average_school_grade))

print("\nимя:",name,"\nгод рождения:",year_of_birth,"\nженат:",married,"\nсредний бал:",average_school_grade)

name = input("\nвведите имя: ")
year_of_birth = int(input("введите год рождения: "))
if input("вы женаты: ") == "Да":
    married = True
else:
    married = False
average_school_grade = float(input("ваш средний бал в школе: "))

print("\nимя:",name,"\nгод рождения:",year_of_birth,"\nженат:",married,"\nсредний бал:",average_school_grade)