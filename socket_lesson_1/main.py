# import socket
#
# HOST = (socket.gethostname(), 10000)
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(HOST)
# s.listen()
# print('I am listening your connection')
#
# while True:
#     conn, addr = s.accept()
#     with open('people.txt', 'a') as file:
#         file.write(f'Connection - {addr} \n')
#     with open('people.txt') as file:
#         data = [line for line in file.readlines()]
#     for i in data:
#         conn.send(str.encode(i))
#         conn.send(str.encode('\n'))
#     print('\n'.join(data))

# ////////////////////////////

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
    res = b'Hello, my friend!'
    conn.send(res)

    conn.close()