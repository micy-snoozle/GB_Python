# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

custom_value = int(input("Введите время в секундах: "))

hour = custom_value // 3600
minute = (custom_value - hour * 3600) // 60
second = custom_value - (hour * 3600 + minute * 60)

print('Время в формате чч:мм:сс', hour, ':', + minute, ':', + second)
print('Время в формате чч:мм:сс %s : %d : %f' % (hour, minute, second))
print(f'Время в формате чч:мм:сс {hour} : {minute} : {second}')
