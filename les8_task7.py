# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение
# и умножение созданных экземпляров. Проверьте корректность полученного результата.

# a = 1 + 2j
# b = 3 + 4j
# print('Addition =', a + b, '\n', 'Subtraction =', a - b, '\n',
#       'Multiplication =', a * b, '\n', 'Division =', a / b, '\n')

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Сумма комплексных чисел: ')
        return f' {self.a + other.a} + {self.b + other.b} * j'

    def __mul__(self, other):
        print(f'Произведение комплексных чисел: ')
        return f'{self.a * other.a - (self.b * other.b)} + {self.b * other.a} * j'

    def __str__(self):
        return f'z = {self.a} + {self.b} * j'


addition = ComplexNumber(3, 4)
multiplication = ComplexNumber(5, 6)

print(addition + multiplication)
print(addition * multiplication)
