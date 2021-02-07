# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


a = Position('Tuomas', 'Ottosson', 'Therapist', 56100, 15250)
print('Name: ', a.get_full_name(), '\n', 'Position: ', a.position, '\n', 'Salary: ', a.get_total_income(), '\n')

b = Position('Kira', 'Saari', 'Nurse', 43200, 5450)
print('Name: ', b.get_full_name(), '\n', 'Position: ', b.position, '\n', 'Salary: ', b.get_total_income(), '\n')

c = Position('Taru', 'Eklund', 'Surgeon', 81400, 12600)
print('Name: ', c.get_full_name(), '\n', 'Position: ', c.position, '\n', 'Salary: ', c.get_total_income(), '\n')

d = Position('Helena', 'Engberg', 'Dentist', 61300, 28500)
print('Name: ', d.get_full_name(), '\n', 'Position: ', d.position, '\n', 'Salary: ', d.get_total_income(), '\n')
