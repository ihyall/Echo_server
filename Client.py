import socket


sock = socket.socket()
sock.connect(('localhost', 1))
host_name = input('Input a host name: ')
# host_name = '127.0.0.1'
port = input('Input a port: ')
assert 0 < int(port) <= 65535, 'Incorrect port number'
sock.send(host_name.encode())
sock.send(port.encode())
sock.close()
sock = socket.socket()
sock.connect((host_name, int(port)))

while True:
    msg = input('Input a message: ')
    sock.send(msg.encode())
    data = sock.recv(1024)
    print(data.decode())
    if msg.lower() in ('exit', 'close'):
        break
sock.close()
