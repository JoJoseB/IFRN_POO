import socket
import struct
import sys
import netifaces

dest_addr = socket.gethostbyname('google.com')
proto     = socket.getprotobyname('icmp')
proto2    = socket.getprotobyname('udp')


teste = socket.socket(socket.AF_INET,socket.SOCK_RAW, 1)
#print(teste)
teste2= socket.socket(socket.AF_INET,socket.SOCK_DGRAM, 17)
#print(teste2)
ttl = 1
#print(teste2.getsockopt(socket.SOL_IP, socket.IP_TTL, ttl))
timeout = struct.pack('ll',5,0)
#print(timeout)
timeout2 = struct.unpack('ll',timeout)
#print(timeout2)


def_gw = netifaces.gateways()['default'][netifaces.AF_INET][1]
print(def_gw)
def_ip = netifaces.ifaddresses(def_gw)[netifaces.AF_INET][0]['addr']
print(def_ip)
#for a in faces:
#    print(netifaces.ifaddresses(a))