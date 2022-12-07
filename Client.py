import socket

def ip_check(ip):
    q = ip.split('.')
    if q == ['localhost']:
        return True
    elif len(q) == 4:
        q1 = list(map(lambda x: True if 0 <= int(x) <= 255 else False, q))
        if not False in q1:
            return True
    else:
        return False

while True:
    host_name = input('Input a host name: ')
    port = int(input('Input a port: '))
    if ip_check(host_name):
        break
    else:
        print('Host name is not an ip-address or "localhost". Try again.')
sock = socket.socket()
sock.connect((host_name, port))

while True:
    msg = input('Input a message: ')
    sock.send(msg.encode())
    data = sock.recv(1024)
    print(data.decode())
    if msg.lower() in ('exit', 'close'):
        break
sock.close()
