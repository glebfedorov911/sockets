import socket

socket_server = socket.socket()

name = input("Введите имя: ")
socket_server.connect((socket.gethostname(), 10000))
socket_server.send(name.encode())
socket_name = socket_server.recv(1024)
server_name = socket_name.decode()
print(server_name, 'Присоединился')

while True:
    msg = (socket_server.recv(1024)).decode()
    print(server_name, ':', msg)
    msg = input('Я: ')
    socket_server.send(msg.encode())