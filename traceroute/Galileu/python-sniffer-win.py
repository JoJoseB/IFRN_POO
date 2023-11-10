import socket
import struct
# the public network interface
HOST = socket.gethostbyname(socket.gethostname())

# create a raw socket and bind it to the public interface
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
s.bind((HOST, 0))

# Include IP headers
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# receive all packages
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)


    # receive a package
pkt,ip_rcv = s.recvfrom(65565)
version_ihl, dscp_ecn, t_len, id, flag_frag,ttl, proto, chksum, src_ip, src_ip2, src_ip3, src_ip4, dst_ip, dst_ip2, dst_ip3, dst_ip4 = struct.unpack(f'! 2b 3H B b H 8B', pkt[0:20])
print(version_ihl, dscp_ecn, t_len, id, flag_frag, ttl, proto, chksum, src_ip,src_ip2,src_ip3,src_ip4, dst_ip, dst_ip2, dst_ip3, dst_ip4)

# disabled promiscuous mode
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)