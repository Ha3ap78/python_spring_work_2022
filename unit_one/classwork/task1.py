# todo: Дано целое число. Если оно является положительным, то прибавить к нему 1;
# если отрицательным, то вычесть из него 2; если нулевым, то заме# нить его на 10.
# Вывести полученное число.

print("Введите целое число")
experimental = input()
experimental = int(experimental)
if experimental > 0:
    experimental = experimental + 1
elif experimental < 0:
    experimental = experimental - 2
elif experimental == 0:
    experimental = 10
print("Результат =", experimental)
