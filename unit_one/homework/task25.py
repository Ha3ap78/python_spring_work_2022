#todo: Убрать повторяющиеся буквы и лишние символы
#Построить по ключевой фразе часть алфавита. Взять все буквы по одному разу. Не буквы убрать.
#Буквы должны идти в том порядке, в котором встретились во фразе в первый раз.

#Input             	            Output
#apple	                        aple
#25.04.2022 Good morning !!	    godmrni

word = "apple"
phrase = "25.04.2022 Good morning !!"
english = ''.join([chr(i) for i in range(ord("a"), ord("a") + 26)])

def lines(letter, eng):
    letter = letter.lower()
    l = []
    index = 0
    for i in letter:
        if i in eng:
            if i not in l:
                l.append(i)
        index += 1
    text = "".join(l)
    return text


print((lines(word, english)))
print(lines(phrase, english))
