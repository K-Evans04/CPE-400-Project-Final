# Keegan Evans
# CPE 400 Final Project - Xbox Gameplay Network Analysis
# Purpose: This script analyzes captured network traffic from Xbox gameplay.

from scapy.all import rdpcap
import pandas as pd

packets = rdpcap("xbox_gameplay_capture.pcapng")

data = []

for pkt in packets:
    if pkt.haslayer("IP"):
        data.append({
            "src": pkt["IP"].src,
            "dst": pkt["IP"].dst,
            "protocol": pkt["IP"].proto,
            "length": len(pkt)
        })

df = pd.DataFrame(data)

print(df.head())
print(df["src"].value_counts())