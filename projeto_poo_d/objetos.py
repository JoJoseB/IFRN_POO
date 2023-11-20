import os, socket, struct, time

class SNIFFER:
    def __init__(self):
        __pid = os.popen(f'ps aux').readlines()
        for a in __pid:
            if 'runserver' in a:
                __index_process = __pid.index(a)+1
                break
        #print(__pid)
        __pid = __pid[__index_process].split()[1]
        __process = (os.popen(f'lsof -i | grep {__pid}').readlines()[-1]).split()[-2]
        __ip,__port = __process.split(':',1)
        self.s = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_TCP)
        self.s.bind((__ip,socket.IPPROTO_TCP))
    
    '''def getatt(self):
        return self.s'''
    
    def getpacket(self,tempo=5):
        __timeout = time.time() + tempo
        while True:
            __pkt,__origem = self.s.recvfrom(65535)
            with open('packet.txt','ab') as f:
                f.write(__pkt)
            if time.time() >= __timeout:
                break
    
    def packet_unpack(self):
        with open('packet.txt','rb') as f:
            teste = f.readline()
            print(type(teste))
            print(teste)
            ver_len = teste[0]
            ver = ver_len >> 4
            head_len = (ver_len & 15) * 4
            print(ver, head_len)
            ttl, proto, src, dest = struct.unpack('! 8x B B 2x 4s 4s', teste[:20])
            ip_addr = socket.inet_ntoa(src)
            ip_addr2 = socket.inet_ntoa(dest)
            print(ttl, proto, ip_addr, ip_addr2)
            #---------------------------
            (src_port,dest_port,sqc,ack, offset_flags) = struct.unpack('! H H L L H',teste[head_len: head_len + 14])
            offset = (offset_flags >> 12) * 4
            flag_urg = (offset_flags & 32) >> 5
            flag_ack = (offset_flags & 16) >> 4
            flag_psh = (offset_flags & 8) >> 3
            flag_rst = (offset_flags & 4) >> 2
            flag_syn = (offset_flags & 2) >> 1
            flag_fin = offset_flags & 1
            print((src_port,dest_port,sqc,ack,offset_flags,offset,flag_urg,flag_ack, flag_psh,flag_rst,flag_syn,flag_fin))