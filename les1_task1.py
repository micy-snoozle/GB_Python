# 1. Поработайте с переменными, создайте несколько,
# выведите на экран, запросите у пользователя несколько чисел и строк
# и сохраните в переменные, выведите на экран.

# Вывод на экран несколько переменных
a = 'Hello'
print(a, type(a))
b = 10
print(b, type(b))
c = 33.3
print(c, type(c))
d = True
print(d, type(d))

# Запрос у ползователя нескольких чисел и строк, вывод данных на экран
name = input('Enter your name: ')
print('Name =', name, ' type:', type(name))

surname = input('Enter your surname: ')
print('Surname =', surname, ' type:', type(surname))

age = int(input('Enter your age: '))
print('Age =', age, ' type:', type(age))

years = age * 12.0
print(age, 'years =', years, ' month', ' type:', type(years))

# if age < 18:
#     print('You are underage')
# if age == 18:
#     print('You are adult')
# else:
#     print('You are adult')
