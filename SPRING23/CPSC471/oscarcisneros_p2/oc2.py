from socket import *
from time import sleep
from random import randint


server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', 12000))
print('UDP Pinger Server is Up...\n')

while True:
    # Receive the client packet along with the addressit is coming from
    message, address = server_socket.recvfrom(1024)
    
    n = randint(9, 12)
    sleep(n/10000)
    server_socket.sendto(message, address)

