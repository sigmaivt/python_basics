class Matrix:

    def __init__(self, *args):
        self.data = args
        self.number_of_lines = len(self.data)
        self.number_of_columns = len(self.data[0])
        self.is_data_correct = True
        for el in self.data:
            if len(el) == self.number_of_columns:
                continue
            else:
                self.is_data_correct = False
                self.number_of_columns = 0
                print("Данные при создании объекта таблица некорректные")
                break

    def __str__(self):
        if self.is_data_correct is True:
            list_of_strings = []
            for el in self.data:
                row_of_strings = [str(i) for i in el]
                list_of_strings.append("\t".join(row_of_strings))
            return "\n".join(list_of_strings)
        else:
            return "Данные об объекте таблица некорректные"

    def __add__(self, other):
        if self.is_data_correct is True and other.is_data_correct is True and \
                self.number_of_columns == other.number_of_columns and \
                self.number_of_lines == other.number_of_lines:
            add_result = []
            for row_item in range(self.number_of_lines):
                new_row = [self.data[row_item][column_item] + other.data[row_item][column_item]
                            for column_item in range(self.number_of_columns)]
                add_result.append(new_row)
            return Matrix(*add_result)
        else:
            print("Сложение невозможно из-за некорректных данных")
        return -1


matrix1 = Matrix([24, 35, 65], [120, 41, 17], [1, 2, 3])
print(matrix1, end="\n\n")
matrix2 = Matrix([2, 325, 6], [12, 4, 7], [30, 20, 10])
print(matrix2, end="\n\n")
matrix3 = matrix1 + matrix2
print(matrix3, end="\n\n")
print(matrix2 + matrix3)
