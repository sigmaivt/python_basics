class ComplexNumber:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        if self.imaginary < 0:
            return f"{self.real} - {abs(self.imaginary)}i"
        else:
            return f"{self.real} + {self.imaginary}i"

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary, self.real * other.imaginary + \
                             self.imaginary * other.real)


complex_number1 = ComplexNumber(1, -2)
print(complex_number1)
complex_number2 = ComplexNumber(2, 5)
print(complex_number2)
print("Сложение:")
print(complex_number1 + complex_number2)
print("Умножение")
print(complex_number1 * complex_number2)
