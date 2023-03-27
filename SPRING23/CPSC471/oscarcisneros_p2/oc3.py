from socket import *
from time import sleep
from random import randint


server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', 12000))
ping_count = 0
loss_count = 0

while True:
    ping_count += 1
    # Receive the client packet along with the addressit is coming from
    message, address = server_socket.recvfrom(1024)
    
    n = randint(9, 13)
    lost = randint(0, 100)
    sleep(n/10000)
    
    if lost > 10 and (loss_count + 1) > (ping_count*0.1):
        server_socket.sendto(message, address)
        continue


    loss_count +=1
