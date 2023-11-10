import socket
import sys
import struct

ifaces = [iface for iface in socket.getaddrinfo(socket.gethostname(), None)]

for iface in enumerate(ifaces):
    print (iface[0], '->', iface[1][4][0], file=sys.stderr)

print ("Digite o número da interface para sniff: ", file=sys.stderr, end='')
HOST = ifaces[int(input ())][4][0]
print ("Sniff da interface: ", HOST, file=sys.stderr)

# create a raw socket and bind it to the public interface
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
s.bind((HOST, socket.IPPROTO_IP))

# receive all packages -- Nao parece necessário, já no nível de IP.
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# receive packages
while True:
    packet, origin = s.recvfrom(65565)
    (versHlen, tos, length,
        id, frag, ttl,
        prot, check,
        source,
        dest) =  struct.unpack('BBHHHBBH4s4s', packet[:20])

    hlen = (versHlen & 0x0F) << 2
    source = socket.inet_ntoa(source)
    dest = socket.inet_ntoa(dest)
    print(f"{source} -> {dest} : {packet[hlen:]}", file=sys.stdout)

# disabled promiscuous mode
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
s.close()