from socket import *
from time import gmtime, strftime, time_ns
from math import floor
from sys import maxsize


SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 12000
ping_count = 0

min_rtt = maxsize
max_rtt = -1
total_rtt = 0
packet_loss = 0

format_as_ms = lambda ns: floor(ns * 10e-4)/100
print('UDP Ping Client is Up...\n')


while ping_count < 50:
    with socket(AF_INET, SOCK_DGRAM) as client_socket:
        #increment count
        ping_count += 1
        # create message
        t = gmtime()        
        message = f'Oscar {ping_count} {strftime("%a %b %d %H:%M:%S %Y", t)}'
        # calculate start time in ns 
        sent_ns = time_ns()

        client_socket.settimeout(.01)

        try:
            # send the message
            client_socket.sendto(message.encode(),(SERVER_ADDRESS, SERVER_PORT))
            # received and print
            received, server_address = client_socket.recvfrom(1024)
            # calculate difference 
            received_ns = time_ns()
            difference = format_as_ms(received_ns - sent_ns)
            # print final output string
            print(f'Oscar {ping_count}: server reply: {received.decode()}, RTT = {difference:.2f}')

            if difference > max_rtt:
                max_rtt = difference
            if difference < min_rtt:
                min_rtt = difference
            total_rtt += difference

        except TimeoutError:
            packet_loss += 1
            print(f'Oscar {ping_count}: timed out, message was lost')

print(f'Min RTT = {min_rtt:.2f}\nMax RTT = {max_rtt:.2f}\nAvg RTT = {(total_rtt/50):.2f}\nPacket Lost = {(packet_loss/.5):.2f} %')



