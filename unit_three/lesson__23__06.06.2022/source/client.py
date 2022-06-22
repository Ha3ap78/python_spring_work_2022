# Echo client program
import socket

HOST = '127.0.0.1'    # The remote host
PORT = 50008              # The same port as used by the server

with open('ava.JPEG', 'rb') as f:
    ava = f.read()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(ava)
    data = s.recv(102400)
print('Received', repr(data))