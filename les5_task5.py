# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def summary():
    try:
        with open('file_2.txt', 'w+', encoding='utf-8') as file_obj:
            line = input('Введите цифры через пробел: ')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле.')
    except ValueError:
        print('Неправильно набран номер.')


summary()

# правильный вариант решения (после разбора на уроке)

from random import randint

with open('text.txt', 'w', encoding='utf-8') as my_file:
    my_list = [randint(1, 100) for _ in range(100)]
    my_file.write(' '.join(map(str, my_list)))

print(f'Sum of elements - {sum(my_list)}')

# Вариант 2

from random import randint

with open('text_5.txt', 'w+', encoding='utf-8') as the_file:
    the_file.write(' '.join([str(randint(1, 1000)) for _ in range(100000)]))
    the_file.seek(0)
    print(sum(map(int, the_file.readline().split())))
