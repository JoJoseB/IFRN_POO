import socket
import struct


class WIRESHARK():
    def __init__(self,ip) -> None:
        ip = socket.gethostbyname(socket.gethostname())
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW,socket.IPPROTO_IP)
        s.bind((ip,socket.IPPROTO_IP))
        s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    
    def receber_pkt(self,socket_ip):
        pkt,ip_origem = socket_ip.recvfrom(65536)
        version_header_length = pkt[0]
        version = version_header_length >> 4
        header_length = (version_header_length & 15) * 4
        print(version)
        print(header_length)
        ttl, proto, src_ip, dest_ip = struct.unpack('! B B 2x 4s 4s', pkt[8:20])
        
        return print(ttl, proto, src_ip, dest_ip)
    
    def trace_route(self):
        #ou checkar vulnerabilidade de porta
        pass