#todo: Создайте функцию compute_bill, считающаю итоговую сумму товаров в чеке.
#Функция должна принимать 1 параметр - словарь, в котором указано количество едениц товара.
#Цены хранятся в словаре:

def compute_bill(dic1, dic2):
  dic3 = dict()
  for k in dic1:
    if k in dic2:
      dic3[k] = dic1[k] * dic2[k]
  return sum(dic3.values())


prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

amount = {
  "banana": 1,
  "apple": 3,
  "orange": 2,
  "pear": 4
}

bill = compute_bill(prices, amount)

print("Бананы:", amount.get('banana'), "кг *", prices.get('banana'), "$ = ",
      amount.get('banana') * prices.get('banana'), "$")
print("Яблоки:", amount.get('apple'), "кг *", prices.get('apple'), "$ = ",
      amount.get('apple') * prices.get('apple'), "$")
print("Апельсины:", amount.get('orange'), "кг *", prices.get('orange'), "$ = ",
      amount.get('orange') * prices.get('orange'), "$")
print("Груши:", amount.get('pear'), "кг *", prices.get('pear'), "$ = ",
      amount.get('pear') * prices.get('pear'), "$")
print("Итого: ", bill, "$")
