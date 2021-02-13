# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3,
# а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие,
# при котором повторение элементов списка будет прекращено.


def my_count_func(start_number, stop_number):
    for el in count(start_number):
        if el > stop_number:
            break
        else:
            print(el)


my_count_func(start_number=int(input('Введите первое число: ')), stop_number=int(input('Введите последнее число: ')))


def my_cycle_func(my_list, iteration):
    i = 0
    iter = cycle(my_list)
    while i < iteration:
        print(next(iter))
        i += 1


my_cycle_func(my_list=[1, 2, 3, 4], iteration=int(input('Введите количество итераций: ')))

# правильный вариант решения (после разбора на уроке)

from itertools import count, cycle

# a)
iterator = count(int(input('Введите целое число, начиная с которого будут генерироваться числа: ')))
print('Первые десять чисел начинаяс введенного вами числа: ')
for i in range(10):
    print(next(iterator), end=' ')

# b)
print('/n- cycle -')
lst = ['string', 101, 3.1415, 15.145]
iterator = cycle(lst)
for i in range(len(lst) * 2):
    print(next(iterator), end=' ')



