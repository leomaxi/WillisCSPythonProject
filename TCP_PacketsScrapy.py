from scapy.all import *

def tcp_packet_sender(ip, port):
    # Make TCP SYN packet
    ip_layer = IP(dst=ip)
    tcp_layer = TCP(dport=port, flags='S')  # 'S' = SYN
    packet = ip_layer / tcp_layer
    print(f"Test sending TCP SYN to {ip}:{port}...")

    # Transfer packet and but wait for response (with 3 min timeout)
    traffic_response = sr1(packet, timeout=3, verbose=0)

    if traffic_response:
        print(f"Received response from :{ip}")
        traffic_response.show()
    else:
        print("No response received.")

# call function with attributes
tcp_packet_sender("104.21.80.1", 80)
