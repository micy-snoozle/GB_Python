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
