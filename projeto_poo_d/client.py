import socket, threading

def client_send(s):
    while True:
        comando = input('>')
        s.send(comando.encode())
        if comando == 'sair':
            s.close()
            break

def client_recv():
    pass
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('localhost',8001))

tclient_send = threading.Thread(target=client_send,args=(s,))
tclient_send.start()
'''tclient_recv = threading.Thread(target=client_recv)'''

'''
while True:
    comando = input('>')
    s.send(comando.encode())
    if comando == 'sair':
        s.close()
        break
        '''