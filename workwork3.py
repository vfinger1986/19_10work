"""
Создать базовый класс Employer (служащий) с функцией Print().
 Она должна выводить информацию о служащем.
  В случае базового класса это может быть строка Создайте от него три производных
   класса: President, Manager, Worker. Переопределите функцию Print() для
вывода информации, соответствующей каждому типу служащего.
"""


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        pass


class Manager(Employee):
    def __init__(self, name, age):
        super().__init__(name, age)

    def print(self):
        print (f"Менеджер {self.name} возраст {self.age}")


    def __str__(self):
        return f"Менеджер {self.name} возраст {self.age}"

    def __int__(self):
        return int(self.age)


class President(Employee):
    def __init__(self, name, age):
        super().__init__(name, age)

    def print(self):
        print (f"Президент {self.name} возраст {self.age}")


    def __str__(self):
        return f"Президент {self.name} возраст {self.age}"

    def __int__(self):
        return int(self.age)


class Worker(Employee):
    def __init__(self, name, age):
        super().__init__(name, age)

    def print(self):
        print (f"Рабочий {self.name} возраст {self.age}")

    def __str__(self):
        return f"Рабочий {self.name} возраст {self.age}"

    def __int__(self):
        return int(self.age)


m1 = Manager("Иванов", 25)
m1.print()
p1 = President("Петров", 48)
p1.print()
w1 = Worker("Сидоров", 37)
w1.print()
print("Возраст", int(w1))
print("Возраст", int(p1))
print("Возраст", int(m1))
