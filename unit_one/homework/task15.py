# Написать игру "Поле чудес"

#Отгадываемые слова и описание лежат в разных  массивах по одинаковому индексу.

##Слово из массива берется случайным порядком. Принимая из ввода букву мы ее открываем
#в случае успеха а в случае неуспеха насчитывам штрафные балы. Игра продолжается до 10 штрафных баллов
#либо победы.

#Пример вывода:

#"Это слово обозначает наименьшую автономную часть языка программирования"

#▒  ▒  ▒  ▒  ▒  ▒  ▒  ▒

#Введите букву: O

#O  ▒  ▒  ▒  ▒  ▒  O  ▒


#Введите букву: Я

#Нет такой буквы.
#У вас осталось 9 попыток !
#Введите букву:
import random
from random import choice

name = input("Представьтесь, пожалуйста: ")
print(name, ", добрый день! Итак, начинаем игру.")
words = ["какао", "пингвин", "самовар"]
desc = [ "Плоды этого дерева служат для приготовления шоколада.", "Южная нелетающая птица.",
          "Металлический сосуд для кипячения воды и приготовления чая." ]
r = choice(desc)
answer = list(words[desc.index(r)])
board = list("□" * len(answer))
print("Внимание! Вопрос: ", r, "Это слово из", len(answer),"букв.")
print(board)
guesses = 0
full_word = []

if full_word < answer:
    while guesses < 10:
        guess = input("Назовите букву: ")
        for i in answer:
            if guess in answer:
                if answer.count(guess) == 1:
                    full_word.insert(answer.index(guess), guess)
                    board[answer.index(guess)] = guess
                    print("Здорово! Есть такая буква! Откройте букву", guess,"на табло!")
                    print(board)
                    break
                if answer.count(guess) > 1:
                    indices = [i for i, x in enumerate(answer) if x == guess]
                    board[indices[0]] = guess
                    board[indices[1]] = guess
                    full_word.insert(indices[0], guess)
                    full_word.insert(indices[1], guess)
                    print("Здорово! Есть такая буква! Откройте букву", guess, "на табло!")
                    print(board)
                    break
            if guess not in answer:
                guesses = guesses + 1
                print("К сожалению, нет такой буквы! У вас осталось ", 10 - guesses, "попыток!")
                break
        else:
            print("Вы проиграли! Словов было -", words[desc.index(r)], ". Удачи в следующий раз! До свидания!")
            break
        if "□" not in board:
            print("Поздравляю,", name, "! Вы выиграли! Вы отгадали слово - это", words[desc.index(r)], "!")
            break
