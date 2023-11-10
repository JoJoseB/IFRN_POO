import struct
import socket

# Dump packets in readable text. This is part of
# A simple yet complete sniffer for IPv4
# by Galileu Batista - galileu.batista at ifrn edu br
# Mar 2021

# Specification format of several types of packets:
# mask:   define fields composing the packet in terms of bytes/words/dwords
# fields: For each field, define where can it could be find in mask
#           Field Name
#           Position in mask
#           Inicial and final bits inside position in the mask

ETH_FRAME = { 'mask': ">6s6sH",
              'fields' :  {'eth.macdest': [0, 0, 47],
                           'eth.macsrc': [1, 0, 47],
                           'eth.type': [2, 0, 15]
                           }
            }

IP_DGRAM = { 'mask': ">BBHHHBBHII",
             'fields' :  {'ip.version': [0, 4, 7],
                          'ip.hlen': [0, 0, 3],
                          'ip.tos': [1, 0, 7],
                          'ip.totlen': [2, 0, 15],
                          'ip.id': [3, 0, 15],
                          'ip.dntfrag': [4, 13, 13],
                          'ip.morefrags': [4, 12, 12],
                          'ip.fragoff': [4, 0, 11],
                          'ip.ttl': [5, 0, 7],
                          'ip.prot': [6, 0, 7],
                          'ip.checksum': [7, 0, 15],
                          'ip.source': [8, 0, 31],
                          'ip.dest': [9, 0, 31] }
            }

ICMP_PACKET = { 'mask': ">BBH",
               'fields' : { 'icmp.type': [0, 0, 7],
                            'icmp.code': [1, 0, 7],
                            'icmp.checksum': [2, 0, 15]
                          }
}

ICMPTYPES = {0: 'Echo Reply', 3: 'IGMP Error', 5: 'Redirect',
             8: 'Echo Request', 11: 'TTL Exceeded'}

UDP_DGRAM = { 'mask': ">HHHH",
              'fields' : { 'udp.sport': [0, 0, 15],
                           'udp.dport': [1, 0, 15],
                           'udp.len': [2, 0, 15],
                           'udp.checksum': [3, 0, 15]
                         }
}

TCP_SEGM = { 'mask': ">HHIIBBHHH",
              'fields' : { 'tcp.sport': [0, 0, 15],
                           'tcp.dport': [1, 0, 15],
                           'tcp.seqnum': [2, 0, 31],
                           'tcp.acknum': [3, 0, 31],
                           'tcp.hlen': [4, 4, 7],
                           'tcp.FIN': [5, 0, 0],
                           'tcp.SYN': [5, 1, 1],
                           'tcp.RST': [5, 2, 2],
                           'tcp.PSH': [5, 3, 3],
                           'tcp.ACK': [5, 4, 4],
                           'tcp.ACK': [5, 5, 5],
                           'tcp.wss': [6, 0, 15],
                           'tcp.checksum': [7, 0, 15],
                           'tcp.urgent': [8, 0, 15]
                        }
}


def dumpPacket (packet, PACKDESC):
    lenHeader    = struct.calcsize(PACKDESC['mask'])
    dictpack = {}
    try:
        fieldsValues = struct.unpack(PACKDESC['mask'], packet[:lenHeader])
        fieldsDesc   = PACKDESC['fields']
        for desc in fieldsDesc:
            fieldvalue = fieldsValues[fieldsDesc[desc][0]]
            bitstart = fieldsDesc[desc][1]
            bitend = fieldsDesc[desc][2]
            if bitend < 32:
                dictpack [desc] = ((fieldvalue >> bitstart) &
                                   ((1 << (bitend-bitstart+1)) - 1))
            else:
                dictpack [desc] = fieldvalue
    except Exception as e:
        dictpack['error'] = 'erro de decodificacao'
    return dictpack, packet[lenHeader:]

def convToIP (dic, key):
    ip = struct.pack('>I', dic[key])
    dic[key] = socket.inet_ntoa(ip)

def convToMAC (dic, key):
    mac = ':'.join([f"{x:02x}" for x in struct.unpack('BBBBBB', dic[key])])
    dic[key] = mac

def dumpICMP (packet):
    icmpDict, data = dumpPacket(packet, ICMP_PACKET)

    typeNum  = icmpDict['icmp.type']
    typeName = ICMPTYPES.get(typeNum,'?')
    icmpDict['icmp.type'] = f"{typeNum} ({typeName})"
    return icmpDict, data

def dumpUDP (packet):
    udpDict, data = dumpPacket(packet, UDP_DGRAM)
    return udpDict, data

def dumpTCP (packet):
    tcpDict, data = dumpPacket(packet, TCP_SEGM)
    tcpDict['tcp.hlen'] *= 4

    return tcpDict, packet[tcpDict['tcp.hlen']:]

def dumpGeneric(packet):
    return {}, packet

def updateProto(fields, fieldProt):
    protoNum = fields[fieldProt]
    protoName = PROTOS.get(protoNum, ['?'])[0]
    fields[fieldProt] = f"{protoNum} ({protoName})"
    return protoNum

def dumpEthFrame (packet):
    ethDict, data = dumpPacket(packet, ETH_FRAME)
    convToMAC (ethDict, 'eth.macdest')
    convToMAC (ethDict, 'eth.macsrc')

    protoNum = updateProto(ethDict, 'eth.type')
    protoDumper = PROTOS.get(protoNum, [0, dumpGeneric])[1]
    upperDict, data = protoDumper (data)

    ethDict.update(upperDict)
    return ethDict, data


def dumpIPV4 (dgram):
    ipDict, data = dumpPacket(dgram, IP_DGRAM)
    ipDict['ip.hlen'] *= 4

    # Show IP as text
    convToIP (ipDict, 'ip.source')
    convToIP (ipDict, 'ip.dest')

    protoNum = updateProto(ipDict, 'ip.prot')
    protoDumper = PROTOS.get(protoNum, [0, dumpGeneric])[1]
    upperDict, data = protoDumper (dgram[ipDict['ip.hlen']:])

    ipDict.update(upperDict)
    return ipDict, data


PROTOS = {1:        ['ICMP', dumpICMP],
          2:        ['IGMP', dumpGeneric],
          6:        ['TCP', dumpTCP],
          17:       ['UDP', dumpUDP],
          0x0800:   ['IPV4', dumpIPV4],
          0x0806:   ['ARP', dumpGeneric],
          0x8035:   ['RARP', dumpGeneric]
        }

fname = {'ip.version': 'IP Version',
         'ip.hlen': 'IP Header Len',
         'ip.tos': 'IP Type of Service',
         'ip.totlen': 'IP Total Len',
         'ip.id': 'Identification',
         'ip.dntfrag': 'Dont Fragment',
         'ip.morefrags': 'More Fragments',
         'ip.fragoff': 'Fragment Offset',
         'ip.ttl': 'TTL',
         'ip.prot': 'Protocol',
         'ip.checksum': 'Header Checksum',
         'ip.source': 'Source IP',
         'ip.dest': 'Destination IP',
         'udp.sport': 'Source Port',
         'udp.dport': 'Destination Port',
         'udp.len': 'Datagram Len',
         'udp.checksum': 'Checksum',
         'tcp.sport': 'Source Port',
         'tcp.dport': 'Destination Port',
         'tcp.seqnum': 'Sequence Number',
         'tcp.acknum': 'ACK Number',
         'tcp.hlen': 'Header Len',
         'tcp.FIN': 'FIN',
         'tcp.SYN': 'SYN',
         'tcp.RST':'RST',
         'tcp.PSH': 'PSH',
         'tcp.ACK':'ACK',
         'tcp.ACK': 'URG',
         'tcp.wss': 'Window Size',
         'tcp.checksum': 'Checksum',
         'tcp.urgent': 'Urgent Point',
         'imcp.type': 'Type',
         'icmp.code': 'Code',
         'icmp.checksum': 'Checksum'
    }




'''
#coloque aqui os bytes de um pacote IP
#Se preferir, crie um pacote usando struct

print ("="*10+" IP Packet "+"="*10)
ipPacket = b"\x45\x00\x00\x38\x04\x88\x40\x00\x80\x11\x69\x34\xc0\xa8\x01\x69\xac\xd9\x1e\x0e"
ipAsDict = dumpIPV4(ipPacket)
for field in ipAsDict:
    print (field+':', ipAsDict[field])
print ("="*30)

print ("="*10+" UDP Packet "+"="*10)
udpPacket = b"\x45\x80\x00\x32\x00\x00\x40\x00\x36\x11\x6d\xa1\xac\xd9\x1d\xae\x0a\x1b\x01\xf8\x01\xbb\xe5\xd9\x00\x1e\x3f\x23\x41\x23\xc4\x1d\x71\x17\x17\x87\x6d\xce\xbd\x03\x90\x68\x0f\x6d\xd4\x3d\x84\x0f\x51\x8b"
udpAsDict = dumpIPV4(udpPacket)
for field in udpAsDict:
    print (field+':', udpAsDict[field])
print ("*"*30)

print ("="*10+" TCP Packet "+"="*10)
tcpPacket = b"\x45\xc0\x00\x50\xea\x14\x00\x00\x01\x59\xd8\x6f\x0a\x0a\x0c\x02\xe0\x00\x00\x05\x02\x01\x00\x30\x0a\x0a\x0c\x02\x00\x00\x00\x00\x94\x6c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\x00\x00\x0a\x12\x01\x00\x00\x00\x28\x0a\x0a\x0c\x02\x0a\x0a\x0c\x01\x0a\x0a\x0c\x01\xff\xf6\x00\x03\x00\x01\x00\x04\x00\x00\x00\x01"
tcpAsDict = dumpIPV4(tcpPacket)
for field in tcpAsDict:
    print (field+':', tcpAsDict[field])
print ("*"*30)
'''