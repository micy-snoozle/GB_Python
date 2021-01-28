# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_func(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return 'Делитель не может быть нулем.'
    except ValueError:
        return 'Введите число.'


print(my_func(int(input('Введите делимое число: ')), int(input('Введите делитель: '))))