# CodeAlpha_BasicNetworkSniffer

Python Network Packet Sniffer

A simple beginner-friendly Python script that captures and analyzes real-time network traffic using Scapy. This tool is designed for learning and understanding how data flows across a network and how protocols like IP, TCP, and UDP work at a packet level.

Features

 - Captures live network packets
 - Displays source and destination IP addresses
 - Identifies whether traffic uses TCP or UDP
 - Extracts and prints packet payload (if available)
 - Automatically stops after capturing 20 packets

Requirements:

Before running the script, install the required dependency:

pip install scapy


Windows Users:
Scapy may require additional dependencies to enable full packet sniffing functionality. Running the script with administrator privileges is recommended.

How to Run

Clone the repository:

git clone https://github.com/yourusername/network-sniffer.git
cd network-sniffer


Run the script:

python sniffer.py


On Windows or macOS, you may need to run the terminal as Administrator / Root for packet sniffing.

How It Works

This program listens to network traffic and processes each received packet. If the packet contains an IP layer, the script extracts:

Source IP address

Destination IP address

Protocol type (TCP / UDP)
