# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, p_1, p_2):
        self.p_1 = p_1
        self.p_2 = p_2

    def __add__(self):
        matrix = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]

        for i in range(len(self.p_1)):
            for el in range(len(self.p_2)):
                matrix[i][el] = self.p_1[i][el] + self.p_2[i][el]

        return str('\n'.join(['\t'.join([str(el) for el in i]) for i in matrix]))


my_matrix = Matrix([[1, 12, 3],
                    [14, 5, 6],
                    [7, 8, 19]],
                   [[9, 8, 17],
                    [6, 15, 4],
                    [13, 2, 1]])

print('Result: \n', my_matrix.__add__())
