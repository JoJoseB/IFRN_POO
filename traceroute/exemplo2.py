'''
REFERENCIAS
https://itecnote.com/tecnote/python-raw-sockets-windows-sniffing-ethernet-frames/
'''

import socket
import time
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
s.bind(('127.0.0.1', socket.IPPROTO_ICMP))
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_MAX)
count = 0

while True:
    count += 1
    pkt,origem = s.recvfrom(1024)
    print(pkt)
    if count == 1:
        break


teste = struct.unpack('! 22B hhhhbb', pkt[:32])
print(teste)
cont = 0
#for a in teste:
    #print(bin(teste[cont]))
    #print(hex(teste[cont]))
    #cont += 1

print(hex(teste[-1]))
print(int(teste[-1]))
print(chr(teste[-1]))
print(chr(teste[-2]))