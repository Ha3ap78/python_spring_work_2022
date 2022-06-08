#  TODO: реализовать протокол
# https://docs.python.org/3/library/socket.html#module-socket
# https://pythonist.ru/rabota-s-setevymi-soketami-na-python/
import socket
# Дописать протокол передачи файла. Сперва разбираем
HOST = ''                 # Хост
PORT = 50008              # Порт сервера
# Создаем сокет
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # связываем сокет с хостом, функции bind передаем хост и порт
    s.bind((HOST, PORT))
    # запускаем режим прослушивания, передаваемый параметр определяет размер очереди.
    s.listen(1)
    # принимаем подключение с помощью метода accept, который возвращает кортеж с двумя элементами.
    conn, addr = s.accept()
    # Теперь мы установили с клиентом связь и можем с ним «общаться». Т.к. мы не можем точно знать,
    # что и в каких объемах клиент нам пошлет, то мы будем получать данные от него небольшими порциями.
    # Чтобы получить данные, нужно воспользоваться методом recv, который в качестве аргумента принимает
    # количество байт для чтения. Мы будем читать порциями по 1024 байт (или 1 кб):
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(102400)
            print(data)
            if not data: break
            conn.sendall(data)
            with open('ava_2.jpg', 'wb') as f:
                f.write(data)
