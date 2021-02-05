# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_number = int(input('Введите целое положительное число: '))
max_number = 0
while user_number > 0:
    value = user_number % 10
    if value >= max_number: max_number = value
    user_number //= 10
print(max_number)
