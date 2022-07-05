try:
    with open("salary.txt", encoding='utf-8') as salary_file:
        salary_data_refined = [[line.split(" ")[0], float(line.split(" ")[1])]
                               for line in salary_file if float(line.split(" ")[1]) > 20000.00]
        sum_salary = 0.00
        count_employees = 0
        salary_file.seek(0)
        for line in salary_file:
            sum_salary += float(line.split(" ")[1])
            count_employees += 1
        average_salary = sum_salary / count_employees
except IOError:
    print("Ошибка открытия файла")
finally:
    salary_file.close()
    print(f"Средняя зарплата сотрудников = {average_salary:,.2f}".replace(",", " "))
    print(f"Сотрудники с зарплатой больше 20 000:\n{salary_data_refined}")
