import socket, threading

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock.connect(('127.0.0.1',8000))

while True:
    sock.send(input('>').encode())
