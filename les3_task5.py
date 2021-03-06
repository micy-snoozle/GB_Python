# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def my_func():
    sum_res = 0
    exit = False
    while exit == False:
        number = input('Введите числа через проблел, либо введите exit - для выхода:  ').split()
        result = 0
        for el in range(len(number)):
            if number[el] == 'exit':
                exit = True
                break
            else:
                result = result + int(number[el])
        sum_res = sum_res + result
        print(f'Сумма введенных чисел равна: {sum_res}')
    print(f'Итоговая сумма чисел равна: {sum_res}')
my_func()


# правильный вариант решения (после разбора на уроке)

# Вариант 1
def sum_num():
    s = 0
    while True:
        in_list = input('Enter a number, input q to exit: ').split()
        for num in in_list:
            if num == 'q':
                return s
            else:
                try:
                    s += int(num)
                except ValueError:
                    print('To exit the program, enter - "q".')
        print(f'Sum of numbers = {s}')


print(sum_num())

# Вариант 2
num = 0
try:
    while num != '#':
        for i in map(int, input('Для выхода наберите "#"\nВведите числа, используя пробел\n').split()):
            num += i
        print(num)
except ValueError:
    print(num)