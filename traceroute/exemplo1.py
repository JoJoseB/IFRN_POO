'''
    A simple traceroute only based on ICMP
    by Galileu Batista
    IFRN.edu.br
    Abr / 2021

    Make sure your fw accept ICMP Traffic
    On windows, run:
        netsh advfirewall firewall add rule name="All ICMP v4" dir=in action=allow protocol=icmpv4:any,any
'''
#pip install netifaces
import socket, struct, select, time, netifaces, struct

#----------------------------------------------------------------------------------------------
def getDefaultIP():
    def_gw_dev = netifaces.gateways()['default'][netifaces.AF_INET][1]
    def_ip = netifaces.ifaddresses(def_gw_dev)[netifaces.AF_INET][0]['addr']
    return def_ip

#----------------------------------------------------------------------------------------------
def createSocket (myIP, timeout):
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    mySocket.bind((myIP, socket.IPPROTO_ICMP))
    mySocket.settimeout(timeout)
    mySocket.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    return mySocket

#----------------------------------------------------------------------------------------------
def checksum(source_bytes):
    sum = 0
    countTo = (len(source_bytes)/2)*2
    count = 0
    while count<countTo:
        thisVal = source_bytes[count + 1] * 256 + source_bytes[count]
        sum = sum + thisVal
        sum = sum & 0xffffffff
        count = count + 2

    if countTo<len(source_bytes):
        sum = sum + source_bytes[len(source_bytes) - 1]
        sum = sum & 0xffffffff

    sum = (sum >> 16)  +  (sum & 0xffff)
    sum = sum + (sum >> 16)
    answer = ~sum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8)
    return answer & 0xFFFF

#----------------------------------------------------------------------------------------------
def send_ping(mySocket, destination, ID):
    # Header format:
    # type (8), code (8), checksum (16), id (16), sequence (16)
    ICMP_ECHO_REQUEST = 8
    my_checksum = 0

    # Make a dummy heder with a 0 checksum.
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, my_checksum, ID, 1)
    bytesInDouble = struct.calcsize("d")
    data = (192 - bytesInDouble) * "."
    data = struct.pack("d", time.time()) + data.encode()

    # Calculate the checksum on the data and dummy header.
    my_checksum = checksum(header + data)

    # Update checksum. In fact, it creates a new header
    header = struct.pack(
        "bbHHh", ICMP_ECHO_REQUEST, 0, socket.htons(my_checksum), ID, 1
    )
    packet = header + data
    mySocket.sendto(packet, (destination, 1))

#----------------------------------------------------------------------------------------------
def rec_ping_ttl (my_socket, ID, timeout):
    recTime = time.time()
    maxTime = recTime + timeout
    while recTime <= maxTime:
        try:
            recPacket, addr = my_socket.recvfrom(1024)
            recTime  = time.time()
        except socket.timeout as t:
            return ('*', recTime)

        icmpHeader = recPacket[20:28]
        type, code, checksum, packetID, sequence = struct.unpack(
            "bbHHh", icmpHeader
        )

        # Echo Reply (0) or TLL Exceeded (11)
        # GBAT: This need to be improved. it can´t work if two
        #       or more instances are runnig at the same time
        #       Verify if receiving correspondent packet.
        if (type == 0 or type == 11):
            return (socket.inet_ntoa(recPacket[12:16]), recTime)

    return ('*', None)

#----------------------------------------------------------------------------------------------
def tracert(destination, timeout=5, maxRetries=3, maxHops=30, DEBUG=False):
    myIP = getDefaultIP()
    destination = socket.gethostbyname(destination)
    mySocket = createSocket (myIP, timeout)

    hops = {}
    ip = None
    ID = checksum(b'GBAT')

    retries = maxRetries
    ttl = 1
    while (ttl < maxHops) and ((ip == None) or (ip != destination)):
        mySocket.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, ttl)

        t1 = time.time()
        try:
            send_ping(mySocket, destination, ID)
            (ip, recTime) = rec_ping_ttl (mySocket, ID, timeout)

            delay = (recTime - t1) * 1000
            if DEBUG: print (f"#{ttl} - {ip} - {delay:5.2f}ms")
            hops [ttl] = (ip, delay)

            ttl += 1
            ID  += 1
        except socket.timeout as t:
            retries -= 1
            if retries == 0:
                if DEBUG: print (f"#{ttl} - *")
                ttl += 1
                retries = maxRetries

    mySocket.close()
    mySocket.close()
    return hops


#----------------------------------------------------------------------------------------------
hops = tracert (input('Destino: '), DEBUG=True)
print (hops)

# Chamada no servidor TCP a ser tomada como referência
# roteadores = tracert(nome_dominio)