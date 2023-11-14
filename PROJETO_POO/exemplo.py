import socket
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(3))
pkt, connection = s.recvfrom(65000)
print(connection)