import socket

# создадим серверный сокет для TCP подключения по IP V4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# займем порт и адрес
ip = '127.0.0.1'
port = 8888
sock.bind((ip, port))
sock.listen(5)
sock.setblocking(False)

while True:
    try:
        client, addr = sock.accept()
    except socket.error:
        print('no clients')
    except KeyboardInterrupt:
        break
    else:
        client.setblocking(True)
        result = client.recv(1024)  # узнать размер буфера
        client.close()
        print('Message', result.decode('utf-8'))

