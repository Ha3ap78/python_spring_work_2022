# II вариант (алгоритм сортировки слиянием)
# Реализовать на Python алгоритм сортировки слиянием представленный в псевдокоде
# в учебнике “Introduction to Algorithms”  на стр. 71 - 77.
#
# Задача.
# Перепишите процедуру  MERGE_SORT и отсортируйте последовательность
A = [31, 41, 9, 26, 41, 58, -1, 6, 101, 13]  # по возрастанию

import math

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)
    return A

def merge(A, p, q, r):
    n1 = q - p + 1  # вычисляем длину левого и правого массива
    n2 = r - q
    L = [0] * (n1 + 1)   # создаем массив их нулей чтобы заполнить соотв числами из основного массива
    R = [0] * (n2 + 1)
    for i in range(n1):
        L[i] = A[p + i - 1]  # заполняем
    for j in range(n2):
        R[j] = A[q + j]
    L[n1] = math.inf
    R[n2] = math.inf
    i = 0
    j = 0
    for k in range(p - 1, r):  # заходим в цикл где будем сравнивать левый и правый массивы
        if L[i] <= R[j]:  # если след. число из левого массива меньше правого, ставим левое
            A[k] = L[i]
            i += 1  # увеличиваем счетчик - переходим на след. число ЛЕВОГО массива
        else:
            A[k] = R[j]  # иначе добавляем правое и переходим на след число ПРАВОГО массива
            j += 1
    return A


print(merge_sort(A, 1, len(A)))
