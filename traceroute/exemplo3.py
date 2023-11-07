import socket
import struct

ip = socket.gethostbyname(socket.gethostname())
s = socket.socket(socket.AF_INET, socket.SOCK_RAW,socket.IPPROTO_IP)
s.bind((ip,socket.IPPROTO_IP))
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

pkt,ip_origem = s.recvfrom(65536)
version_header_length = pkt[0]
version = version_header_length >> 4
header_length = (version_header_length & 15) * 4
print(version)
print(header_length)
ttl, proto, src_ip, dest_ip = struct.unpack('!  B B 2x 4s 4s', pkt[8:20])
print(ttl, proto, src_ip, dest_ip)