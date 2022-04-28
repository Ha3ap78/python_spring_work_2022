#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
#– id - номер по порядку (от 1 до 10);
#– текст из списка algoritm
#Каждое значение из списка должно находится на отдельной строке.

algoritm = ["C4.5", "k - means", "Метод опорных векторов", "Apriori",
"EM", "PageRank", "AdaBoost", "kNN", "Наивный байесовский классификатор", "CART"]


f = open("algoritm.csv", "wt", encoding="cp1251")

counter = 1

for line in algoritm:

    f.write(str(counter) + "," + line + '\n')
    counter += 1
f.close()

