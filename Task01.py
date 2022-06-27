from sys import argv

script_name, working_time, wage_per_hour, bonus = argv
print(f"Зарплата = {int(working_time)*int(wage_per_hour) + int(bonus)}")
