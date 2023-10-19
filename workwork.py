"""
Реализуйте класс «Человек». Необходимо хранить в полях класса:
 ФИО, дату рождения, контактный телефон, город, страну, домашний адрес.
 Реализуйте методы класса для ввода данных, вывода данных,
 реализуйте доступ к отдельным полям через методы класса.
"""


class Human:
    name = "Иван"
    surname = "Иванов"
    date = "25.12.1986"
    phone = 89531542613
    city = "Псков"
    country = "Россия"
    address = "Яна Фабрициуса 38"

    def setName(self, name):
        self.name = name

    def setSurname(self, surname):
        self.surname = surname

    def setDate(self, date):
        self.date = date

    def setPhone(self, phone):
        self.phone = phone

    def setCity(self, city):
        self.city = city

    def setCountry(self, country):
        self.country = country

    def setAddress(self, address):
        self.address = address

    def Output(self):
        print(f"Имя: {self.name}\n"
              f"Фамилия: {self.surname} \n"
              f"Дата рождения: {self.date}\n"
              f"Номер телефона: {self.phone} \n"
              f"Город: {self.city}\n"
              f"Страна: {self.country}\n"
              f"Адрес: {self.address}")

    def Input(self, name, surname, date, phone, city, country, address):
        self.name = name
        self.surname = surname
        self.date = date
        self.phone = phone
        self.city = city
        self.country = country
        self.address = address


h1 = Human()
h1.Output()
h1.Input("Константин","Константинов","17.05.2003", "4563217889","Пинск", "Белоруссия", "Ленина 6 ")
h1.Output()
