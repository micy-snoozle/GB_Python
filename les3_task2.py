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


# правильный вариант решения (после разбора на уроке)

# Вариант 1
def personal_info(**kwargs):
    return ' '.join(kwargs.values())


print(personal_info(name=input('Введите ваше имя: '), surname=input('Введите вашу фамилию: '),
                    year=input('Введите год вашего рождения: '), city=input('Введите город проживания: '),
                    email=input('Введите ваш email: '), number=input('Введите номер вашего телефона: ')))


# Вариант 2
def person_inf(name, surname, year, city, email, number):
    return f'Имя: {name}; Фамилия: {surname}; Год рождения: {year}; \
    Город: {city}; Email: {email}; Номер телефона: {number}'


print(person_inf(name='Bill', surname='White', year='10.12.1986', city='Kilpisjärvi', email='name.surname@mail.ru',
                 number='+3-456-789-10-21'))
