"""
Задание 2
Создайте класс Complex (комплексное число).
Создайте перегруженные операторы для реализации
арифметических операций для по работе с комплексными
числами (операции +, -, *, /).
"""
class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a}+{self.b}i"

    # Сложение комплексных чисел определяется правилом:
    # (a1 + b1i) + (a2 + b2i) = (a1 + a2) + (b1 + b2) i
    def __add__(self, other):
        return f"{self.a + other.a} + {self.b + other.b}i"

    # Вычитание комплексных чисел определяется правилом:
    # (a1 + b1i) - (a2 + b2i) = (a1 - a2) + (b1 - b2) i
    def __sub__(self, other):
        return f"{self.a - other.a} + {self.b - other.b}i"

    #  Умножение комплексных чисел определяется правилом:
    #  (a1 + b1i) (a2 + b2i) = (a1a2 - b1b2) + (a1b2 + a2b1) i.
    def __mul__(self, other):
        return f"{self.a * other.a - self.b * other.b} + {self.a * other.b + other.a * self.b}i"

    def __truediv__(self, other):
        r1 = (self.a * other.a + self.b * other.b) / (pow(other.a, 2) + pow(other.b, 2))
        r2 = (other.a * self.b - self.a * other.b) / (pow(other.a, 2) + pow(other.b, 2))
        return f"{r1} + {r2}i"

c1 = Complex(1, 2)
c2 = Complex(2, 1)
print(c1)
print(c2)
print("Сложение: ", c1 + c2)
print("Вычитание: ", c1 - c2)
print("Учножение: ", c1 * c2)
print("Деление: ", c1 / c2)
