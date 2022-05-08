#todo: Для игры "Отгадай число от 0 до 100" реализованной на занятии 4 homework/task3
#написать Save Game по следующему сценарию:
#В запущенной игре по нажатию клавиши S появляется вывод:
#1. Продолжить
#2. Сохранить игру

#При выборе пункта 1. игра продолжается.
#При выборе пункта 2. пользователю предлагается ввести название для
#сохранения, после чего нужно сделать сериализацию состояния игры.
#Законсервировать все объекты которые отвечают за состоянии игры в файл
#game_dump.pkl   Сериализацию и десериализацию сделать на базе библиотеки pickle.

#При старте игры пользователю должен предлагатся выбор
#1. Новая игра
#2. Восстановить игру
#При выборе 1. начинается новая игра.
#При выборе 2. пользователю выводится список всех сохраненных игр(происходит десериализация).
#Из них он выберает нужную, после чего загружается состояние игры на момент сохранения.
import random, pickle

data = {'number': random.randint(0, 100),  # Случайное число
        'answer': 0,      # текущий ответ
        'guesses': 10,   # количество попыток
        'guess': 0,    # Текущая попытка
        'answers': [],  # Введенные ответы
        'save_name': 0}  # Имя игры для сохранения
saved_games = []  # Список сохраненных игр


def new_game():
    global data
    while data['guess'] != data['guesses']:
        data['answer'] = input('Введите число: ')

        if data['answer'] == str(data['number']):
            print(f"Поздравляю! Вы угадали загаданное число c {data['guess'] + 1} попытки!")
            break
        elif data['answer'] == 'S' or data['answer'] == 's':
            print("1. Продолжить\n2. Сохранить игру")
            act = input("Выберите дальнейшее действие:")
            match act:
                case "1":
                    continue
                case "2":
                    save_game(data, 'game_dump.pkl')
                    continue
        else:
            if data['answer'].isdigit():
                if data['answer'] in data['answers']:
                    print("Вы уже вводили данное число")
                data['guess'] += 1
                if int(data['answer']) > data['number']:
                    data['answers'].append(data['answer'])
                    print("Загаданное число меньше введенного."
                          "У вас осталось", data['guesses'] - data['guess'], "попыток")
                else:
                    data['answers'].append(data['answer'])
                    print("Загаданное число больше введенного."
                          "У вас осталось", data['guesses'] - data['guess'], "попыток")
                if data['guess'] == data['guesses']:
                    print(f"К сожалению у Вас закончились попытки. Вы проиграли.\n"
                          f"Загаданное число было {data['number']}. До свидания.")
            else:
                print("Введите числовое значение или нажмите клавишу S")
                continue


def save_game(object, file):
    global data
    data['save_name'] = input("Введите название для сохранения: ")
    with open(file, 'ab') as f:
        pickle.dump(object, f)
    print(f"Игра {data['save_name']} сохранена. Продолжим")


def load_game(object: list, file):
    global data
    try:
        with open(file, "rb") as f:
            while True:  # читаем pkl файл до конца
                try:
                    object.append(pickle.load(f))  # добавляем сохранение в список
                except EOFError:  # исключение конец файла
                    break
    except FileNotFoundError:  # исколючение - если файл не найден
        print('Сохраненные игры отсутствуют. Начинаем новую игру')
        return -1

    for i in object:  # выводим на экран список всех сохраненных игр
        print(str((object.index(i) + 1)) + '.', object[object.index(i)]['save_name'])

    num_save = int(input('Введите номер сохраненной игры для загрузки: '))
    if 0 <= num_save <= len(object):
        data = object[num_save - 1]
    else:
        print('Введен неверный номер сохраненной игры. Загружено последнее сохранение')
        data = object[len(object) - 1]

    print('Загружена игра:', data['save_name'])
    print('Использовано попыток:', data['guess'])
    print('Осталось попыток:', data['guesses'] - data['guess'])
    answers = ''
    for i in data['answers']:
        answers += i + ' '
    print('Ранее введенные ответы:', answers)


print("Добрый день. Загадано число от 1 до 100. Попробуйте отгадать за 10 попыток")
print("1. Новая игра \n2. Восстановить игру")
game_type = input("Выберите тип игры:")

if game_type == '1':
    new_game()
elif game_type == '2':
    load_game(saved_games, 'game_dump.pkl')
    new_game()
else:
    print("Введен некорректный ответ")



