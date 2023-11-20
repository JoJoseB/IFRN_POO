from objetos import *

# cria o objeto que faz sniffing do servidor django
teste = SNIFFER()
# guarda os pacotes
teste.getpacket()
# lê os pacotes
#todo: aprimorar esse método
teste.packet_unpack()
