import threading,socket,json,time

def sniffer():
    sock = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_TCP)
    sock.bind(('127.0.0.1',socket.IPPROTO_TCP))
    data = {}
    for a in range(15):
        chave = f'#{a}'
        data[chave] = {"pacote":[],"origem":[]}
        recebido = sock.recvfrom(65536)
        data[chave]["pacote"].append(str(recebido[0]))
        data[chave]['origem'].append(str(recebido[1]))
        time.sleep(1)
        print(data)
    with open('packets.json','w') as f:
        json.dump(data,f)
        

def client():
    sock2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock2.bind(('127.0.0.1',8000))
    s_sniffer = threading.Thread(target=sniffer)
    while True:
        comm = sock2.recv(64).decode()
        print(comm)
        if comm == 'capturar':
            if s_sniffer.is_alive() == True:
                print('alive')
                pass
            else:    
                s_sniffer.start()
        if comm == 'alive':
            print(s_sniffer.is_alive())
            
s_client  = threading.Thread(target=client)
s_client.start()