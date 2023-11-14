import socket,struct,time,platform

#This sniffer by default work on linux SO
'''TODO:
Make the sniffer work on windows SO
Make the sniffer automatically recognize the OS (platform lib)
'''

class SNIFFER:
    __conn = None
    
    def __init__(self, interface):
        self.__conn = socket.socket(socket.AF_INET,socket.SOCK_RAW)
        
        pass