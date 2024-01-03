import socket

HOST = (socket.gethostname(), 10000)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(HOST)
print('Connected to', HOST)

msg = b'HELLO MY FRIEND SOCKET'
client.sendall(msg)

print('send msg')