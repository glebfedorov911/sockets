import socket

HOST = (socket.gethostname(), 10000)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(HOST)
print('Connected to', HOST)

sent = 0
req = b'GET / HTTP/1.1\r\nHost:localhost:10000\r\n\r\n'
# while sent < len(req): #socket.sendall()
#     sent += client.send(req[sent:])
client.sendall(req)

print('Send msg!')