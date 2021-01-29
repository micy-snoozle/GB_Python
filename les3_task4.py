# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

# Первый способ:

def my_func(x, y):
    result = x ** y
    return result


print(f"Результат: {my_func(int(input('Введите положительное число: ')), int(input('Введите отрицательное число: ')))}")


# Второй способ:

def my_func(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    if y >= 0:
        return result
    else:
        return 1 / result


print(f"Результат: {my_func(int(input('Введите положительное число: ')), int(input('Введите отрицательное число: ')))}")


# правильный вариант решения (после разбора на уроке)

# Вариант 1
def my_pow_fun(x, y):
    try:
        res = x ** y
    except TypeError:
        return 'Enter a float number and negative power'
    return res


print(my_pow_fun(5, -2))


# Вариант 2
def my_func2(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return 'Не выполнено условие ввода данных:\nх должен быть больше 0\nу должен быть меньше 0'
        else:
            result = 1
            for _ in range(abs(y)):
                result /= x
            return f'Результат возведения х в степень y: {round(result, 6)}'
    except ValueError:
        return 'Программа работает только с числами'


number1 = input('Введите положительное число, x = ')
number2 = input('Введите отрицательное число, y = ')

print(my_func2(number1, number2))


# Вариант 3 c использованием рекурсии
def i_involve_r(x, y):
    return 1 if y == 0 else i_involve_r(x, y + 1) * 1 / x


a = 2
b = -4

print(f'Solved via recursion {a} raised to power {b} = {i_involve_r(a, b)}')
