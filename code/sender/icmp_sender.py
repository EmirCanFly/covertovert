from scapy.all import *

# Implement your ICMP sender here
def send_ICMP():
    # create an IP packet with the destination IP address and a TTL of 1
    ip = IP(dst = "receiver", ttl = 1)

    # create an ICMP packet
    icmp = ICMP()

    # combine the IP and ICMP packets
    packet = ip / icmp

    # send the packet
    send(packet)

# send an ICMP packet
if __name__ == "__main__":
    send_ICMP()