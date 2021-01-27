# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def get_person(name, surname, year, city, email, number):
    return ' '.join(name, surname, year, city, email, number)


name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')
year = int(input('Введите год вашего рождения: '))
city = input('Введите город проживания: ')
email = input('Введите ваш email: ')
number = int(input('Введите номер вашего телефона: '))

print(
    'Имя: {name}, Фамилия: {surname}, Год рождения: {year}, Город: {city}, Email: {email}, Номер телефона: {number}'.format(
        name=name, surname=surname, year=year, city=city, email=email, number=number))
