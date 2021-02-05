# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа,
# а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.


def factorial(n):
    result = 1
    el = 1
    while (el < n):
        result = result * el
        yield result
        el += 1


gen = factorial(10)
for i in gen:
    print(i)


# правильный вариант решения (после разбора на уроке)

def fact_gen(number):
    f_num = 1
    if number == 0:
        yield f'{number}! = 1'
    for i in range(1, number + 1):
        f_num *= i
        yield f'{i}! = {f_num}'


for el in fact_gen(int(input('Factorial number: '))):
    print(el)
