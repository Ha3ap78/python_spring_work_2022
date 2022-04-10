print('Для решения уравнения A * x + B = 0 ведите занчение А, не равное 0')
var_A = input()
var_A = float(var_A)
var_A = -var_A
print('Введите значение переменной B')
var_B = input()
var_B = float(var_B)
print('x =', var_B/var_A)
