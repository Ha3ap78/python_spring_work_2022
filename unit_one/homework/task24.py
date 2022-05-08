#todo: Числа в буквы
#Замените числа, написанные через пробел, на буквы. Не числа не изменять.

#Пример.
#Input	                            Output
#8 5 12 12 15	                    hello
#8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

def create_dict(alfa):
    dict = {}
    count = 1
    for i in alfa:
        dict[count] = i
        count += 1
    return dict

def insert_digit(dict, insert):
    l2 = list(insert.split(" "))
    index = 0
    for i in l2:
        for key in dict.keys():
            if i == str(key):
                l2[index] = dict[key]
            elif i == "0":
                l2[index] = " "
                break
        index += 1
    insert = "".join(l2)
    return insert

alphabet = "abcdefghijklmnopqrstuvwxyz"

numbers = input("Введите числа для замены на буквы: ")

dict = create_dict(alphabet)

print(insert_digit(dict, numbers))
