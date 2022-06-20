working_list = [1, 2.0, None, True, "test", [2, 1.2], (23, "тест")]
print(working_list)
for i in range(len(working_list)):
    print(f"{working_list[i]} - {type(working_list[i])}")