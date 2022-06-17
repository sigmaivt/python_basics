y = (n := int(input("введите положительное целое число: ")))
max_digit = y % 10
while y > 10 and max_digit < 9:
    y = y // 10
    max_digit = max(max_digit, y % 10)
    continue
print(f"максимальная цифра числа {n} - {max_digit}")