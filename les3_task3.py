# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg_1, arg_2, arg_3):
    if arg_1 >= arg_3 and arg_2 >= arg_3:
        return arg_1 + arg_2
    elif arg_1 > arg_2 and arg_1 < arg_3:
        return arg_1 + arg_3
    else:
        return arg_2 + arg_3


print(
    f"Результат: {my_func(int(input('Введите первый аргумент: ')), int(input('Введите второй аргумент: ')), int(input('Введите третий аргумент: ')))}")

# правильный вариант решения (после разбора на уроке)

# Вариант 1
def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    try:
        my_list.remove(min(my_list))
        return sum(my_list)
    except TypeError:
        return 'Enter only numbers'

print(my_func(3, 15, -20))

# Вариант 2
def my_func(arg_1, arg_2, arg_3):
    return sum((sorted([arg_1, arg_2, arg_3])[1:]))

print(my_func(150, 50, 40))

# Вариант 3
my_func = lambda arg_1, arg_2, arg_3: (arg_1 + arg_2 + arg_3) - min(arg_1, arg_2, arg_3)

print(my_func(10, 20, 30))