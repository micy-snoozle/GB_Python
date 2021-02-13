# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class Exception:
    def __init__(self, a, b):
        self.divider = a
        self.denominator = b

    @staticmethod
    def divide(a, b):
        try:
            result = round(a / b, 2)
        except:
            return f'{a} / {b} - Cannot be divided by zero! \n'
        else:
            print(f'{a} / {b} = {result} \n')


my_result = Exception(1, 100)
print(Exception.divide(10, 0))
print(Exception.divide(9, 2))
print(my_result.divide(8, 0))
print(my_result.divide(7, 2))
