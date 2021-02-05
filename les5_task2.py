# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

# Первый способ (выводит все строки)
count = 0
with open('file_name.txt', 'r', encoding='utf-8') as file:
    for line in file:
        count += 1
        print(count)

# Второй способ (общее количество строк)
with open('file_name.txt', 'r', encoding='utf-8') as file:
    print(len(file.readlines()))

# Вывод количества слов в строке:
with open('file_name.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for index, value in enumerate(lines):
        number_of_words = len(value.split())
        print('В {} строке написано {} слов.\n'.format(index + 1, number_of_words))
