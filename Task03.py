class Cell:

    def __init__(self, number_of_cells):
        self.number_of_cells = number_of_cells

    def __str__(self):
        return f"{self.number_of_cells:d} яч."

    def __add__(self, other):
        return Cell(self.number_of_cells + other.number_of_cells)

    def __sub__(self, other):
        if self.number_of_cells > other.number_of_cells:
            return Cell(self.number_of_cells - other.number_of_cells)
        else:
            print("Вычитание невозможно")

    def __mul__(self, other):
        return Cell(self.number_of_cells * other.number_of_cells)

    def __truediv__(self, other):
        return Cell(self.number_of_cells // other.number_of_cells)

    def make_order(self, number_in_row):
        output_str = ("*" * number_in_row + "\n") * (self.number_of_cells // number_in_row)\
                     + ("*" * (self.number_of_cells % number_in_row))
        return output_str


cell1 = Cell(7)
cell2 = Cell(2)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell2 - cell1)
print(cell1 * cell2)
print(cell2 / cell1)
print(cell1.make_order(4))
