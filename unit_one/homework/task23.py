#todo: Взлом шифра
#Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
#Попробуйте все возможные сдвиги и расшифруйте фразу.

alphabet = "abcdefghijklmnopqrstuvwxyz"

code = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."
count = 1


def decode(letter, offset):
    if letter in alphabet and offset <= len(alphabet):
        return alphabet[alphabet.index(letter)-int(offset)]
    else:
        return letter

while count <= len(alphabet):
    str_decode = ''
    for i in code:
        str_decode += decode(i, count)
    print("Вариант расшифровки:", str_decode)
    count += 1
