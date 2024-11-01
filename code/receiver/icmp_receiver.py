from scapy.all import *

# Implement your ICMP receiver here

# listen for ICMP packets on all interfaces
def receive_icmp():
    sniff(filter="icmp", prn=process_packet) 

# print the packet if the TTL is 1 and the packet is an ICMP packet 
def process_packet(packet):
    if packet.haslayer(ICMP) and packet[IP].ttl == 1:
        print(packet.show())

if __name__ == "__main__":
    receive_icmp()