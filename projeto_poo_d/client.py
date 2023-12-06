import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('localhost',8001))
while True:
    comando = input('>')
    s.send(comando.encode())
    if comando == 'sair':
        s.close()
        break