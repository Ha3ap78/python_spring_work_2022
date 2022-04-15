#todo: Дан массив размера N. Найти индексы двух ближайших чисел из этого массива.

import random

N = int(input("Введите размер массива: "))
mass = [random.randint(0, 10) for i in range(N)]
print(mass)
number = int(input("Введите число для поиска: "))
for i in mass:
    if i == number:
        break
        print(i * 10)



