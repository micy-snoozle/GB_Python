# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date(object):

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def date_str(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date_count = cls(day, month, year)
        print(cls, date_as_string)
        return date_count

    @staticmethod
    def date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        if day <= 31 and day != 0 and month <= 12 and month != 0 and year <= 3000:
            print(day, month, year)
        else:
            print('Error. Please enter a valid value.')


a = '12-12-2012'
date_class = Date.date_str(a)
date_static = Date.date_valid(a)

b = '32-13-3001'
date_class = Date.date_str(b)
date_static = Date.date_valid(b)
