from scapy.all import *
import os

# Implement your ICMP receiver here
# check if the packet is an ICMP packet and call process_packet
def receive_icmp():
    sniff(filter="icmp", prn=process_packet) 

# print the packet if the TTL is 1 and exit the program 
def process_packet(packet):
    if packet.haslayer(ICMP) and packet[IP].ttl == 1:
        print(packet.show())
        os._exit(0); # exit the program after printing the packet

if __name__ == "__main__":
    receive_icmp()