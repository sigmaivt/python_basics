initial_list = [300, 2, 12, 44, 1, 1, 4, 10, 11, 1, 78, 77, 155]
final_list = [initial_list[i] for i in range(1, len(initial_list)) if initial_list[i-1] < initial_list[i]]
print(final_list)
