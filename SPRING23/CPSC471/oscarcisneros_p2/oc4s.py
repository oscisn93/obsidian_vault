from socket import *
from math import floor
from time import time

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', 12000))
last = -1
gap = 0

while True:
    # Receive the client packet along with the addressit is coming from
    message, address = server_socket.recvfrom(1024)
    t = floor(time())
    
    if last > 0:
        gap = t - last
        if gap > 20:
            print('No heartbeat after 20 seconds. Server Quits')
            break
    print(f'Server received: {message.decode()} Last heartbeat received {gap} seconds ago.')  
    server_socket.sendto(message, address)
    last = t

