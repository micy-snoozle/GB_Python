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

# правильный вариант решения (после разбора на уроке)

def div(s_1, s_2):
    try:
        s_1, s_2 = int(s_1), int(s_2)
        div_num = s_1 / s_2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return 'division by zero forbidden'
    return round(div_num, 4)

print(div(input('enter first number: '), input('enter second number: ')))