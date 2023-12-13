import socket, threading

def client_send(s):
    while True:
        comando = input('>')
        s.send(comando.encode())
        if comando == 'sair':
            s.close()
            break

def client_recv(s):
    while True:
        print(s.recv(65535))
        
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('localhost',8001))

tclient_send = threading.Thread(target=client_send,args=(s,))

tclient_recv = threading.Thread(target=client_recv,args=(s,))

tclient_send.start()
print('iniciou')
tclient_recv.start()
print('iniciou')
'''
while True:
    comando = input('>')
    s.send(comando.encode())
    if comando == 'sair':
        s.close()
        break
        '''