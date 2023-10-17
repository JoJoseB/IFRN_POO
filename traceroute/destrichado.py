import socket
import struct
import sys
import netifaces
import time

# gerar um checksum em bytes apartir de uma string
def checksum(source_bytes):
    sum = 0
    countTo = (len(source_bytes)/2)*2
    count = 0
    while count<countTo:
        thisVal = source_bytes[count + 1] * 256 + source_bytes[count]
        sum = sum + thisVal
        sum = sum & 0xffffffff
        count = count + 2

    if countTo<len(source_bytes):
        sum = sum + source_bytes[len(source_bytes) - 1]
        sum = sum & 0xffffffff

    sum = (sum >> 16)  +  (sum & 0xffff)
    sum = sum + (sum >> 16)
    answer = ~sum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8)
    return answer & 0xFFFF

# destino google, protocolos e TTL
dest_addr = socket.gethostbyname('google.com')
protocol     = socket.getprotobyname('icmp')
proto2    = socket.getprotobyname('udp')
ttl = 1

# adquirindo IP padrão da interface ethernet
def_gw = netifaces.gateways()['default'][netifaces.AF_INET][1]
print(def_gw)
def_ip = netifaces.ifaddresses(def_gw)[netifaces.AF_INET][0]['addr']
print(def_ip)

#criando socket 
sock = socket.socket(socket.AF_INET,socket.SOCK_RAW,protocol)
print(sock)

# bind socket com o ip da inteface
sock.bind((def_ip,0))
print(sock)

# configurando a função ioctlsocket controla o modo de E/S de um soquete.
sock.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
print(sock)

# Definindo o valor da opção de soquete fornecida. As constantes simbólicas necessárias são definidas no módulo soquete (SO_* etc.). O valor pode ser um número inteiro, None ou um objeto semelhante a bytes representando um buffer. No último caso, cabe ao chamador garantir que a bytestring contenha os bits apropriados (consulte a estrutura do módulo integrado opcional para obter uma maneira de codificar estruturas C como bytestrings). Quando o valor é definido como Nenhum, o argumento optlen é necessário
sock.setsockopt(socket.SOL_SOCKET, socket.IP_TTL,ttl)
print(sock)

#utilizando funcao para criar um checksum
my_checksum = 0
a = checksum(b'jose')

#usando biblioteca struct para converter valores do python em valores da estrutura C
header = struct.pack('bbHHh',8,0,my_checksum,a,1)
print(header)

# Retorna o tamanho da estrutura (e, portanto, do objeto bytes produzido por pack(format, ...)) correspondente ao formato da string de formato
bytesInDouble = struct.calcsize("d")
print(bytesInDouble)
data = (192 - bytesInDouble) * "."
print(data)

# Colocando o tempo no checksum
#data = struct.pack("d", time.time()) + data.encode()
#print(data)

data = data.encode()
my_checksum = checksum(header + data)
print(my_checksum)

# Formatando o cabeçalho da requisição icmp
header = struct.pack(
    "bbHHh", 8, 0, socket.htons(my_checksum), a, 1
)
print(header)

# Pacote com completo com header e data
packet = header + data
print(packet)

# Enviando a requisição icmp para o destino
sock.sendto(packet,(dest_addr,0))
print(sock)

#recebendo resposta do destino
pacote_recebido,addr = sock.recvfrom(1024)
print(pacote_recebido,addr)

#destrinchando o icmp de resposta
icmpHeader = pacote_recebido[20:28]
print(icmpHeader)
type, code, checksoma, packetID, sequence = struct.unpack(
    "bbHHh", icmpHeader
)
print(type, code, checksoma, packetID, sequence)
print(pacote_recebido[12:16])
res = socket.inet_ntoa(pacote_recebido[12:16])
print(res)