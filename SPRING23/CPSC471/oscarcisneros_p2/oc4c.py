from socket import *
from time import gmtime, strftime, time, sleep
from random import randint


SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 12000
client_no = int(input())

while True:
    with socket(AF_INET, SOCK_DGRAM) as client_socket:
        # create message
        t = gmtime()        
        
        message = f'Oscar client{client_no} heartbeat at {strftime("%a %b %d %H:%M:%S %Y", t)}'
        
        delay = randint(2,26)
        sleep(delay)

        # send the message
        client_socket.sendto(message.encode(),(SERVER_ADDRESS, SERVER_PORT))


        # received and print
        received, server_address = client_socket.recvfrom(1024)
        
        # print final output string
        print(received.decode())


