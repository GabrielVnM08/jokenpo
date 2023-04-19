import socket
import threading

sock = socket.socket()
sock.connect(('localhost', 6060))

def receive():
    while True:
        data = sock.recv(1024)
        if not data:
            break
        print(f'>> {data}')

threading.Thread(target=receive).start()

while True:
    data = input()
    # sock.send(b'hello server')
    sock.send(bytes(data, 'ascii'))