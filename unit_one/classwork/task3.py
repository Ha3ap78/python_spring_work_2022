#todo 3.1: Получите заданное количество N (например, 20) различных
# случайных целых чисел в диапазоне от 0 до N-1. Найдите их
# сумму.


#todo 3.2:  Известно, что сейф открывается при правильном вводе
# кода из 3 цифр 0...9. Задайте код и затем откройте сейф, ис-
# пользуя метод перебора с помощью нескольких операторов
# цикла for.

#3.1
import random
N = int(input("Введите размер массива: "))
mass = [random.randint(0, N-1) for i in range(N)]
print("Последовательность чисел: ", mass)
print("Сумма чисел: ", sum(mass))

#3.2
password = [random.randint(0, 9) for i in range(3)]
print(password)
for j in range(9):
    if j == password[0]:
        continue
for k in range(9):
    if k == password[1]:
        continue
for l in range(9):
    if l == password[2]:
        break
print("Сейф взломан! Пароль:", password)



