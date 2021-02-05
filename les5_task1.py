# 1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

file = open('file_1.txt', 'w', encoding='utf-8')
text = input('Введите текст: ')
while text:
    file.writelines(text)
    text = input('Введите текст: ')
    if not text:
        break

file.close()
file = open('file_1.txt', 'r', encoding='utf-8')
result = file.readlines()
print(result)

# правильный вариант решения (после разбора на уроке)

with open('text_1.txt', 'w', encoding='utf-8') as f:
    while True:
        line = input('input new string or empty string to done: ')
        if not line:
            break
        # f.write(f'{line}\n')
        print(line, file=f)

# Вариант 2

print('введите данные для записи в файл\n Для окончания ввода введите пустуюд строку')
with open('text_1.txt', 'w', encoding='utf-8') as my_file:
    while (line := input()) != '':
        my_file.write(f'{line}\n')

# Вариант 3

my_file = open('text_1.txt', 'w', encoding='utf-8')

line = ' '
while line:
    line = input('Enter something: ')
    my_file.write(f'{line}\n') if line != '' else my_file.close()
