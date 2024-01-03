import socket

HOST = (socket.gethostname(), 10000)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
s.bind(HOST)
s.listen()
print('I am listening your connections')

while True:
    conn, addr = s.accept()
    print('Connected -', addr)
    print('Waiting for request!')

    req = ''
    while True:
        data = conn.recv(4096)
        if not len(data):
            break
        req += data.decode('UTF-8')

    print(req)
    conn.close()