# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

string = input('Введите строку из нескольких слов: ')
my_word = []
number = 1

for element in range(string.count(' ') + 1):
    my_word = string.split()
    if len(str(my_word)) <= 10:
        print(f'{number} {my_word[element]}')
        number += 1
    else:
        print(f'{number} {my_word[element][0:10]}')
        number += 1
