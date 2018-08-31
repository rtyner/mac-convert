# types of macs to convert from/to
# eui48 - 71-54-ED-69-9B-E9
# unix - 71:54:ed:69:9b:e9
# cisco - 7154.ed69.9be9
# bare - 7154ED699BE9

import sys
import netaddr
from netaddr import EUI

# take certain input here, and be able to act on it. 
# if mac_type == 'Cisco':
#   print(netaddr.mac_cisco) - something like that, not sure on the syntax yet
mac_type = input("What format is the input file? Cisco, Bare, Unix, or ")

# take file as input
in_file = sys.argv[1]

def convert_mac(octet):
    return EUI(netaddr.strategy.eui48.packed_to_int(octet))

with open(in_file,'r') as i: # open and read file
    lines = i.readlines()
    for line in lines:
        mac = EUI(line)
        
        # would like to devise a way to clean up and condense this block below
        mac.dialect = netaddr.mac_bare
        print(mac) 

        mac.dialect = netaddr.mac_cisco
        print(mac) 

        mac.dialect = netaddr.mac_unix_expanded
        print(mac) 
        
        mac.dialect = netaddr.mac_eui48
        print(mac) 

