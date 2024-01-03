import socket

s = socket.socket()
s.bind((socket.gethostname(), 10000))
s.listen()

print('Сервер запущен!')
name = input("Введите имя: ")
conn, addr = s.accept()

client = (conn.recv(1024)).decode()
print(client, 'Присоединился')
conn.send(name.encode())

while True:
    msg = input('Я: ')
    conn.send(msg.encode())
    msg = conn.recv(1024)
    msg = msg.decode()
    print(client, ":", msg)