import socket

HOST = (socket.gethostname(), 10000)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(HOST)
s.listen()
print("I am listening your connections")

while True:
    conn, addr = s.accept()
    print("Connected -", addr)
    print('\n')
    msg = ''
    while True:
        data = conn.recv(4096)
        if not len(data):
            break
        msg += data.decode('UTF-8')

    print(msg)
    conn.close()