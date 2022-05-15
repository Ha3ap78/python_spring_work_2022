#todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения
# Пример:
# render, 10,  12.05.2022 12:00
# show,    5,  12.05.2022 12:02
# render, 15,  12.05.2022 12:07
#
# Декоратор должен применяться для различных функций с переменным числом аргументов.
# Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.


from datetime import datetime

log = {}  # {функция:количество вызовов}

def decorator_catch(func):  # декоратор-счетчик
    def wrapper(*args, **kwargs):
        global log
        if func.__name__ in log.keys():
            log[func.__name__] += 1
        else:
            log[func.__name__] = 1
        return func(*args, **kwargs)
    return wrapper


def save(log: dict):  # запись данных в файл
    time = datetime.now()
    with open('debug.log', 'at') as f:
        for i in log.keys():
            print(f'{i}, {log[i]}, {time.strftime("%d.%m.%Y, %H:%M:%S")}')
            f.write(f'{i}, {log[i]}, {time.strftime("%d.%m.%Y, %H:%M:%S")}\n')


@decorator_catch
def render(text):
    text = text.upper()
    return text

@decorator_catch
def summa(x, y):
    sum = x + y
    return sum

@decorator_catch
def exponent(x, y):
    exp = x ** y
    return exp

summa(115, 22)

exponent(10, 3)

print(render('hello'))

render('summertime')

print(f'Сумма 256 и 785 равна {summa(256, 785)}')

summa(2, 2)

save(log)
