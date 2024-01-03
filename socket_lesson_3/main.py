import pickle
import socket

HOST = (socket.gethostname(), 10000)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
s.bind(HOST)
s.listen()
print('I am listening your connections')

d = {
    'name': 'Amanda',
    'age': 50,
}

while True:
    conn, addr = s.accept()
    print('Connected from -', addr)
    resp = pickle.dumps(d)
    conn.send(resp)

    conn.close()