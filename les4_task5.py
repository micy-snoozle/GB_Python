# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


# print(reduce(my_func, [100, 1000]))
print(f'Список всех четных чисел: {[el for el in range(100, 1000) if el % 2 == 0]}')
print(
    f'Результат вычисления произведения всех элементов списка: '
    f'{reduce(my_func, [el for el in range(100, 1000) if el % 2 == 0])}')

# правильный вариант решения (после разбора на уроке)

from functools import reduce

print(reduce(lambda a, b: a * b, [x for x in range(100, 1001, 2)]))
