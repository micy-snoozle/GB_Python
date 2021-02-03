# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_ = [num for el, num in enumerate(my_list) if el > 0 and my_list[el] > my_list[el - 1]]

print(new_)

# правильный вариант решения (после разбора на уроке)

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
more_then = [my_list[num] for num in range(1, len(my_list)) if  my_list[num] > my_list[num - 1]]
print(more_then)

# Вариант 2
import random

original_list = [random.randint(0, 1000) for _ in list(range(0, random.randint(2, 20)))]
answer_list = [i for num, i in enumerate(original_list[1:]) if i > original_list[num]]

print(original_list)
print(answer_list)
