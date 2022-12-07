import socket
import os
# import Scanner


def log(logs):
    with open('Log.txt', mode='a') as f:
        f.write(logs+'\n')
    return logs


open('Log.txt', mode='w').close()

port = int(input('Input a port: '))
sock = socket.socket()
sock.bind(('', port))
print(log('Server start on: {}.\nPort: {}'.format(*sock.getsockname())))
sock.listen(1)
fl = False

while True:
    print(log('Waiting for connection.....'))
    conn, addr = sock.accept()
    print(log('Connected: {}. Port: {}'.format(*addr)))
    while True:
        data = conn.recv(1024)
        print(log(f'Data received.'))
        print(log(f'Data: {data.decode()}'))
        if data.decode().upper() == 'EXIT':
            conn.close()
            print(log('Connection closed.'))
            break
        elif data.decode().upper() == 'CLOSE':
            fl = True
            conn.close()
            break
        else:
            conn.send(data.upper())
            print(log('Data sent.'))
    if fl:
        sock.close()
        print(log('Socket closed'))
        break


