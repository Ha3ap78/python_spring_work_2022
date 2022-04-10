print('Для определения четности/нечетности введите целое число')
even_or_odd = input()
even_or_odd = int(even_or_odd)
if even_or_odd % 2 == 0:
    print('Число четное')
else:
    print('Число нечетное')