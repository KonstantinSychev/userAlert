import socket
import os

# создадим клиентский сокет для TCP подключения по IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = '127.0.0.1'
port = 8888
sock.connect((ip, port))
sock.send(b'Hello')
sock.close()