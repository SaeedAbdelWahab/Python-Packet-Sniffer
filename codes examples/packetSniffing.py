from __future__ import print_function
from scapy.all import *
 
## Create a Packet Counter
counter = 0
counter2 = 0
counter3 = 0
 


##Filter Function (not working with the output yet)
def FilterBy(fltr):
    filters = ["arp","ipv4","ipv6","tcp","udp","dhcp","http"]

    if fltr in filters:
        #filtername = fltr
        #print(fltr)
        #return filtername
        packet= sniff(filter=fltr,  prn= first_window )

    else:
        print('Unrecognized filter')

#FilterBy('udp')

## Define our Main Action function

def fetch_packets(packet):
    global counter
    counter += 1
    
    return 'Packet #{}: {} ==> {}'.format(counter, packet[0][1].src, packet[0][1].dst)

## Setup sniff, filtering for IP traffic
#count = 10 is used for testing 
pkts = sniff(filter="udp", prn=fetch_packets, count=10)

#code is tested with different filters
#to print packet summary
#pkts.summary()

##Function printing src IP Address:
def PacketSrc(pkts):
    global counter2
    counter2 += 1
    
    for packet in pkts:
        fetch_packets(packet)

    #print is used for testing    
    #print( 'Packet Src #{}: {}'.format(counter2, packet[0][1].src) )
    return packet[0][1].src  #use return to print in column directly

pSrc = sniff(filter='udp',prn= PacketSrc, count=10)


##function printing destination IP Address: (to add it as a column in the main table)
def PacketDest(pkts):
    global counter3
    counter3 += 1
    
    for packet in pkts:
        fetch_packets(packet)

    #print is used for testing    
    print('Packet Dest #{}: {}'.format(counter3, packet[0][1].dst) )
    #return packet[0][1].dst  #use return to print in column directly

pDest = sniff(filter='udp',prn= PacketDest, count=10)

#pkts.summary()

##Middle Window
#index is defined in window1 get from fetching packets
def second_window(pkts,index):
	pkts[index].show()

second_window(packet,1)