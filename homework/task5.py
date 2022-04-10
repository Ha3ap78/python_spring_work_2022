print('Введите значение точки А на числовой оси')
dot_A = input()
dot_A = float(dot_A)
print('Введите значение точки В на числовой оси')
dot_B = input()
dot_B = float(dot_B)
print('Введите значение точки С на числовой оси')
dot_C = input()
dot_C = float(dot_C)
line_segment_AC = dot_C-dot_A
line_segment_BC = dot_C-dot_B
print('Длина отрезка АС равна', line_segment_AC)
print('Длина отрезка ВС равна', line_segment_BC)
print('Сумма отрезков АС и ВС равна', line_segment_AC+line_segment_BC)