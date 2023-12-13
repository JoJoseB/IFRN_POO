from objetos import *
import socket, threading
'''
# cria o objeto que faz sniffing do servidor django
teste = SNIFFER()
# guarda os pacotes
teste.getpacket()
# lê os pacotes
#todo: aprimorar esse método
teste.packet_unpack()
'''

def achar_ip_porta():
    pid = os.popen(f'ps aux').readlines()
    for a in pid:
        if 'runserver' in a:
            index_process = pid.index(a)+1
            break
    pid = pid[index_process].split()[1]
    process = (os.popen(f'lsof -i | grep {pid}').readlines()[-1]).split()[-2]
    ip,port = process.split(':',1)
    return ip,port

def client(conn):
    sniffer = SNIFFER()
    while True:
        comando = conn.recv(64).decode()
        print(comando)
        if comando == 'sair':
            print('conexao fechada')
            conn.close()
            break
        if comando == 'pacote':
            pacotes = sniffer.getpacket()
            #sniffer.packet_unpack()
            conn.send(str(pacotes).encode())

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip,port = achar_ip_porta()
print(port)
s.bind((ip,int(port)+1))
s.listen()

while True:
    conn,addr = s.accept()
    print(f'Cliente {addr} aceita')
    t_client = threading.Thread(target=client,args=(conn,))
    t_client.start()
    print('thread no ar')