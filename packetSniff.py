from __future__ import print_function
from scapy.all import *
 
## Create a Packet Counter
counter = 0
 
## Define our Custom Action function
def fetch_packets(packet):
    global counter
    counter += 1
    
    return 'Packet #{}: {} ==> {}'.format(counter, packet[0][1].src, packet[0][1].dst)
 
## Setup sniff, filtering for IP traffic
#count = 10 is used for testing
pkts = sniff(filter="tcp", prn = fetch_packets , count = 10)

#code is tested with different filters
#to print packet summary
pkts.summary()
pkts[0].show()




