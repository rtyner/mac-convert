###################################################################################
# Rusty Tyner                                                                     #
# 7/10/18                                                                         #
# Take MAC address file as input and convert to different formats                 #
#                                                                                 #  
# TODO: Loop through input file, output to csv, prompt for MAC type to convert to #
###################################################################################

import sys
import netaddr
from netaddr import EUI

# take file as input
in_file = sys.argv[1]
# out_file = sys.argv[2]

def convert_mac(octet):
    return EUI(netaddr.strategy.eui48.packed_to_int(octet))

# open and read file
with open(in_file,'r') as i:
    lines = i.readlines()
    for line in lines:
        #print(line, end="")
        mac = EUI(line)
        print(line)
# in this code block the list is being read with \n at the end of each line, need to remove that.
# netaddr.core.AddrFormatError: failed to detect EUI version: '13:1B:E5:CC:E6:B3    \n'



# store input from file into in_mac variable
#in_mac = lines

#mac = EUI(in_mac[1])
#print(mac)

#mac.dialect = netaddr.mac_cisco
#print(mac)

#mac.dialect = netaddr.mac_bare
#print(mac)

#mac.dialect = netaddr.mac_unix_expanded
#print(mac)