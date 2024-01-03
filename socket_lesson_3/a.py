import pickle
import socket

HOST = (socket.gethostname(), 10000)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(HOST)
print('Connected to', HOST)

resp = client.recv(4096)
print(resp)
print(pickle.loads(resp))