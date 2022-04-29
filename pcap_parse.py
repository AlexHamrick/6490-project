
# import pure_pcapy as pcapy
import dpkt
from scapy.all import rdpcap, PcapReader
import argparse



def main():
    packets = PcapReader('turn_off_1.pcapng')
    # print(packets.summary)
    for pkt in packets:
        print(pkt)

if __name__ == "__main__":
    main()