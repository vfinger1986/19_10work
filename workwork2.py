"""
Создайте класс для подсчета максимума из четырех аргументов,
 минимума из четырех аргументов, средне-арифметического из четырех аргументов,
  факториала аргумента. Функциональность необходимо реализовать в
   виде статических методов.

"""
import math


class Count:
    @staticmethod
    def find_max(a, b, c, d):
        return max(a, b, c, d)

    @staticmethod
    def find_min(a, b, c, d):
        return min(a, b, c, d)

    @staticmethod
    def find_avg(a, b, c, d):
        return (a + b + c + d) / 4

    @staticmethod
    def find_factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            p = 1
            for i in range(1, n + 1):
                p *= i
            return p


print("Максимальное:", Count.find_max(2, 3, 5, 6))
print("Минимальное:", Count.find_min(7, 336, 852, 11))
print("Среднее-арифметическое:", Count.find_avg(5, 6, 158, 3))
print("Факториал:", Count.find_factorial(7))


