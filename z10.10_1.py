"""
Задание 1
Создайте класс Circle (окружность). Для данного
класса реализуйте ряд перегруженных операторов:
■ Проверка на равенство радиусов двух окружностей
(операция ==);
■ Сравнения длин двух окружностей (операции >, <,
<=,>=);
■ Пропорциональное изменение размеров окружности,
путем изменения ее радиуса (операции + - += -=).
"""
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circleLen(self):
        return self.radius * math.pi * 2

    def __str__(self):
        return "Радиус окружности {0}, длина окружности {1:.5f}".format(self.radius, self.circleLen())

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        return self.circleLen() > other.circleLen()

    def __lt__(self, other):
        return self.circleLen() < other.circleLen()

    def __ge__(self, other):
        return self.circleLen() <= other.circleLen()

    def __le__(self, other):
        return self.circleLen() >= other.circleLen()

    def __add__(self, other):
        return self.radius + other

    def __sub__(self, other):
        return self.radius - other

    def __iadd__(self, other):
        self.radius += other
        return self

    def __isub__(self, other):
        self.radius -= other
        return self

c1 = Circle(5)
c2 = Circle(6)
# Проверка на равенство радиусов двух окружностей (операция ==)
if c1==c2:
    print("Радиусы равны")
else:
    print("Радиусы не равны")
print(c1)
print(c2)
# Сравнения длин двух окружностей (операции >, <, <=, >=)
print("Вызывается магический метод __gt__", c1 > c2) # Вызывается магический метод __gt__
print("Вызывается магический метод __lt__", c1 < c2) # Вызывается магический метод __lt__
print("Вызывается магический метод __ge__", c1 <= c2) # Вызывается магический метод __ge__
print("Вызывается магический метод __le__", c1 >= c2) # Вызывается магический метод __le__
# Пропорциональное изменение размеров окружности, путем изменения ее радиуса (операции + - += -=)
print("Изменили радиус:", c1+3)
print("Изменили радиус:", c1-5)

c1 += 3
print("Увеличиваем радиус на 3")
print(c1)

print("Уменьшаем радиус на 8")
c1 -= 8
print(c1)

