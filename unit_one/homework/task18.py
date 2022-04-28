#todo:Создайте программу, которая будет выводить все возможные комбинации при броске 2 игральных костей
#и сумму их значений. У игральной кости стороны пронумерованы от 1 до 6.

#Пример вывода:
#Сумма 2   комбинация [(1,1)]
#Сумма 3   комбинация [(1,2),(2,1)]
#Сумма 4   комбинация [(1,3),(3,1),(2,2)]
#........................................
#Выводы комбинаций оформить в список кортежей.

dice_1 = (1, 2, 3, 4, 5, 6)
dice_2 = (1, 2, 3, 4, 5, 6)
all_options = []
options = []
summa = 1
number = 2



while summa < 13:
    summa = summa + 1
    for i in dice_1:
        for j in dice_2:
            if i + j == summa:
                var = (i, j)
                all_options.append(var)
                break
while number < 13:
    for i in all_options:
        if sum(i) == number:
            options.append(i)
    print("Сумма", number, "перечень комбинаций", options)
    options.clear()
    number += 1










