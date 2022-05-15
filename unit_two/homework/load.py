#todo Задача 1. Чтение матрицы, load_matrix(filename)
# Дан файл, содержащий таблицу целых чисел вида
# (в каждой строке через пробел записаны числа)
#
# 11 12 13 14 15 16
# 21 22 23 24 25 26
# 31 32 33 34 35 36
#
# Т.е. в каждой строке через пробел записаны числа.
# Требуется написать функцию load_matrix(filename) которая загружает эту таблицу из файла.
# Если в каждой строке находится одинаковое количество чисел, функция возвращает список списков целых чисел.
# В противном случае возвращает False.
#
# Задачу следует решить с использованием списковых включений, циклы использовать НЕЛЬЗЯ!

def load_matrix(filename):
    with open(filename, 'rt') as f:
        "читаем файл"
        mass = f.read()
        #print(f'mass =\n {mass}')
        "убираем \n из массива"
        mass = mass.split('\n')
        #print(f'mass = {mass}')
        "превращаем массив в строку с числами для того чтобы посчитать общее кол-во чисел в матрице"
        nums = ''.join([i + ' ' for i in mass])
        #print(f'nums = {nums}')
        "удаляем пробел в конце строки"
        nums = nums.rstrip(' ')
        #print(f'nums = {nums}')
        "переводим числа в массиве из str в int"
        nums = [int(i) for i in nums.split(' ')]
        #print(f'nums = {nums}')
        "получаем список списков целых чисел"
        matrix = [[int(x) for x in i.split(' ')] for i in mass]
        #print(f'matrix = {matrix}')
        "получаем список списков целых чисел если выполняется условие задачи. Если не выполняется получаем []"
        result = [i for i in matrix if len(i) == len(nums) / len(matrix)]
        "for debug"
        #print(f'mass = {mass}')
        #print(f'nums = {nums}')
        #print(f'matrix = {matrix}')
        " Если условие задачи выполняется возвращаем список списков целых чисел. Если нет возвращаем False "
    return result if len(result) > 0 else False

load_matrix('matrix.TXT')
