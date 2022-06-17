time_in_seconds = int(input("введите время в секундах:"))
hours = time_in_seconds // 3600
minutes = (time_in_seconds % 3600) // 60
seconds = (time_in_seconds % 3600) % 60
print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')