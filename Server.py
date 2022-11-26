import socket
import os


def log(logs):
    with open('Log.txt', mode='a') as f:
        f.write(logs+'\n')


if 'Log.txt' in os.listdir(os.getcwd()):
    os.remove(os.getcwd()+'\\Log.txt')

while True:
    if not 'Log.txt' in os.listdir(os.getcwd()):
        open('Log.txt', mode='w').close()
    sock1 = socket.socket()
    sock1.bind(('localhost', 1))
    while True:
        sock1.listen(1)
        conn, addr = sock1.accept()
        try:
            host_name = conn.recv(1024).decode()
            port = int(conn.recv(1024).decode())
        except:
            continue
        conn.close()
        sock1.close()
        if 0 < port <= 65535:
            break
    print(host_name, port)
    fl = False
    sock2 = socket.socket()
    sock2.bind((host_name, port))
    log(f'Server start on: {host_name}.\nPort: {port}')
    sock2.listen(1)
    log('Waiting for connection.....')
    conn, addr = sock2.accept()

    log('Connected: {}. Port: {}'.format(*addr))

    while True:
        data = conn.recv(1024)
        log(f'Data received.')
        log(f'Data: {data.decode()}')
        if data.decode().upper() == 'EXIT':
            conn.close()
            break
        elif data.decode().upper() == 'CLOSE':
            conn.close()
            fl = True
            break
        else:
            conn.sendall(data.upper())
            log('Data sent.')
    log('Connection closed')
    if fl:
        break
sock2.close()
