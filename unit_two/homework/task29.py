#todo Задача 2. Транспонирование матрицы, transpose(matrix)
# Написать функцию transpose(matrix), которая выполняет транспонирование матрицы. Решить с использованием списковых включений.
#
#
# Пример:
# >>> transpose([[1, 2, 3], [4, 5, 6]])
#
# [[1, 4], [2, 5], [3, 6]]
#
#
# ||1 2 3||      ||1 4||
# ||4 5 6||  =>  ||2 5||
#                ||3 6||

matrix = [[1, 2, 3], [4, 5, 6]]

def transpose(matrix):
        return [[i, j] for i in matrix[0] for j in matrix[1] if matrix[0].index(i) == matrix[1].index(j)]

print(transpose(matrix))