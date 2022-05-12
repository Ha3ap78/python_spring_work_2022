# II вариант (алгоритм сортировки слиянием)
# Реализовать на Python алгоритм сортировки слиянием представленный в псевдокоде
# в учебнике “Introduction to Algorithms”  на стр. 71 - 77.
#
# Задача.
# Перепишите процедуру  MERGE_SORT и отсортируйте последовательность
A = [31, 41, 9, 26, 41, 58, -1, 6, 101, 13]  # по возрастанию

def merge_sort (numbers):
    if len(numbers) > 1:
        a = numbers[:len(numbers)//2]  # первая половина массива
        b = numbers[len(numbers)//2:]  # вторая половина массива
        merge_sort(a)
        merge_sort(b)

        i = j = k = 0  # индексы в списках a, b, numbers
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                numbers[k] = a[i]
                i += 1
            else:
                numbers[k] = b[j]
                j += 1
            k += 1

        while i < len(a):
            numbers[k] = a[i]
            i += 1
            k += 1
        while j < len(b):
            numbers[k] = b[j]
            j += 1
            k += 1


merge_sort(A)
print(A)
