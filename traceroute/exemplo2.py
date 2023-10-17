'''
REFERENCIAS
https://itecnote.com/tecnote/python-raw-sockets-windows-sniffing-ethernet-frames/
'''

import socket
import time
HOST = socket.gethostbyname(socket.gethostname())
s = socket.socket(socket.AF_INET, socket.SOCK_RAW)
s.bind((HOST, 0))
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
while True:
    pkt = s.recvfrom(4096)
    print(pkt)
    time.sleep(1)