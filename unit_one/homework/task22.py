# todo: Шифр Цезаря
#Описание шифра.
#В криптографии шифр Цезаря, также известный шифр сдвига, код Цезаря или сдвиг Цезаря,
#является одним из самых простых и широко известных методов шифрования.
#Это тип подстановочного шифра, в котором каждая буква в открытом тексте заменяется буквой на некоторое
#фиксированное количество позиций вниз по алфавиту. Например, со сдвигом влево 3, D будет заменен на A,
#E станет Б, и так далее. Метод назван в честь Юлия Цезаря, который использовал его в своей частной переписке.

#Задача.
#Считайте файл message.txt и зашифруйте  текст шифром Цезаря, при этом символы первой строки файла должны
#циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
#В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
#В каждой строчке содержатся различные символы. Шифровать нужно только буквы латинского алфавита.

def char_encrypte(letter, offset):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    if letter in alphabet:
        return alphabet[alphabet.index(letter) - offset]
    else:
        return letter

str_num = 1
str_encode = ''
f = open("message.txt", "rt", encoding="utf-8")

for i in f:
    count = 1
    while count <= len(i):
        str_encode += char_encrypte(i[count-1], str_num)
        count += 1
print(str_encode)
str_num += 1

f.close()


