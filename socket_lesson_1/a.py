import socket

HOST = (socket.gethostname(), 10000)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(HOST)
print('Connected to', HOST)

msg = ''
while True:
    data = client.recv(8)
    msg += data.decode()
    if not len(data):
        break

print(msg)
