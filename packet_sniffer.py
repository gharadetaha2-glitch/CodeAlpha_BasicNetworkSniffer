from scapy.all import sniff, IP, TCP, UDP, Raw

def packet_info(packet):
    if IP in packet:
        print("\n========== Packet Captured ==========")
        print(f"Source: {packet[IP].src}")
        print(f"Destination: {packet[IP].dst}")

        if TCP in packet:
            print(f"Protocol: TCP | Ports: {packet[TCP].sport} -> {packet[TCP].dport}")
        elif UDP in packet:
            print(f"Protocol: UDP | Ports: {packet[UDP].sport} -> {packet[UDP].dport}")
        else:
            print("Protocol: Other")

        if Raw in packet:
            print(f"Payload: {packet[Raw].load}")

sniff(prn=packet_info, count=20)
