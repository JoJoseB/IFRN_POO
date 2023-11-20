'''
REFERENCIAS
https://itecnote.com/tecnote/python-raw-sockets-windows-sniffing-ethernet-frames/
'''
import socket
import time
import struct

interface = '10.0.2.15'
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
s.bind((interface,socket.IPPROTO_TCP))
timeout = time.time() + 5

while True:
    pkt,origem = s.recvfrom(1024)
    print(pkt)
    if time.time() > timeout:
        break

tam = len(pkt)

version_ihl, dscp_ecn, t_len, id, flag_frag,ttl, proto, chksum, src_ip, src_ip2, src_ip3, src_ip4, dst_ip, dst_ip2, dst_ip3, dst_ip4 = struct.unpack(f'! 2b 3H B b H 8B', pkt[0:20])
print(version_ihl, dscp_ecn, t_len, id, flag_frag, ttl, proto, chksum, src_ip,src_ip2,src_ip3,src_ip4, dst_ip, dst_ip2, dst_ip3, dst_ip4)


'''rv_dest_ip = struct.pack(f'4B',dst_ip, dst_ip2, dst_ip3, dst_ip4)'''
'''print(rv_dest_ip)
teste = socket.inet_ntoa(rv_dest_ip)
print(teste)'''

'''pkt_x = []
pkt_bin= []
cont = 0
for a in teste:
    pkt_x.append(format(a,'x'))
for a in teste:
    pkt_bin.append(format(a,'b'))
print(pkt_x)
print(pkt_bin)'''