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

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def transpose(matrix):
    columns = len(matrix)
    strings = len(matrix[1])
    transp_matrix = [[matrix[j][i] for j in range(columns)] for i in range(strings)]
    return transp_matrix


print(f'Исходная матрица {matrix}')

print(f'Транспонированная матрица {transpose(matrix)}')
