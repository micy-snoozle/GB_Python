# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('file_name.txt', 'r', encoding='utf-8') as file_obj:
    content = file_obj.read().split('\n')
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('file_name.txt', 'w', encoding='utf-8') as file_obj_2:
    file_obj_2.writelines(new_file)

# правильный вариант решения (после разбора на уроке)

rus_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('text_44.txt', 'w', encoding='utf-8') as new_file:
    with open('text_4.txt', encoding='utf-8') as my_file:
        new_file.writelines([line.replace(line.split()[0], rus_dict.get(line.split()[0])) for line in my_file])

# Вариант 2

from googletrans import Translator

with open('text_4_translate.txt', 'w', encoding='utf-8') as f:
    with open('text_4.txt', 'r', encoding='utf-8') as f1:
        text = f1.read()
    try:
        f.write(Translator().translate(text, dest='ru').text)
    except AttributeError:
        print('Error')
