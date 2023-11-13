import socket
import struct
import time
class SNIFFER:
    def __init__(self,interface):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        self.s.bind((interface,socket.IPPROTO_TCP))

    def getatt(self):
        return self.s

    def getpackets(self,tempo):
        timeout = time.time() + tempo
        while True:
            pkt,origem = self.s.recvfrom(1024)
            print(pkt)
            if time.time() > timeout:
                break
        return