# todo:  Даны три переменные: X, Y, Z. Их значения числа.
# Из данных произвольных чисел выбрать наибольшее.

# Пример:
# X = 5
# Y = 10
# Z = 3
# Ответ: Наибольшее число 10.
#
# X = 10
# Y = 12
# Z = -7
# Ответ: Наибольшее число 12.

print("Введите первое число")
number_one = input()
number_one = int(number_one)
print("Введите второе число")
number_two = input()
number_two = int(number_two)
print("Введите третье число")
number_three = input()
number_three = int(number_three)
maximum = number_one
if number_two > maximum:
    maximum = number_two
if number_three > maximum:
    maximum = number_three
print("Наибольшее число -", maximum)