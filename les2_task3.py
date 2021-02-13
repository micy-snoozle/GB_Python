# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

a_list = ['Зима', 'Весна', 'Лето', 'Осень']
a_dict = {0: 'Зима', 1: 'Весна', 2: 'Лето', 3: 'Осень'}
a = int(input('Введите порядковый номер месца в виде целого числа от 1 до 12: '))
if a == 1 or a == 2 or a == 12:
    print(a_list[0])
    print(a_dict[0])
elif a == 3 or a == 4 or a == 5:
    print(a_list[1])
    print(a_dict[1])
elif a == 6 or a == 7 or a == 8:
    print(a_list[2])
    print(a_dict[2])
elif a == 9 or a == 10 or a == 11:
    print(a_list[3])
    print(a_dict[3])
else:
    print('Ошибка.')

# ___ Попробовала сделать тоже самое с месяцами.

m_list = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
          'Декабрь']
m_dict = {0: 'Январь', 1: 'Февраль', 2: 'Март', 3: 'Апрель', 4: 'Май', 5: 'Июнь', 6: 'Июль', 7: 'Август', 8: 'Сентябрь',
          9: 'Октябрь', 10: 'Ноябрь', 11: 'Декабрь'}
m = int(input('Введите порядковый номер месца в виде целого числа от 1 до 12: '))
if m == 1:
    print(m_list[0])
    print(m_dict[0])
elif m == 2:
    print(m_list[1])
    print(m_dict[2])
elif m == 3:
    print(m_list[3])
    print(m_dict[3])
elif m == 4:
    print(m_list[4])
    print(m_dict[4])
elif m == 5:
    print(m_list[5])
    print(m_dict[5])
elif m == 6:
    print(m_list[6])
    print(m_dict[6])
elif m == 7:
    print(m_list[7])
    print(m_dict[7])
elif m == 8:
    print(m_list[8])
    print(m_dict[8])
elif m == 9:
    print(m_list[9])
    print(m_dict[9])
elif m == 10:
    print(m_list[10])
    print(m_dict[10])
elif m == 11:
    print(m_list[11])
    print(m_dict[11])
elif m == 12:
    print(m_list[12])
    print(m_dict[12])
else:
    print('Ошибка.')