# Rusty Tyner
# 7/10/18
# Take MAC address file as input and convert to different formats

# TODO:
# Loop through input file, output to csv, prompt for MAC type to convert to

import sys
import netaddr
from netaddr import EUI

in_file = sys.argv[1]
# out_file = sys.argv[2]

def convert_mac(octet):
    return EUI(netaddr.strategy.eui48.packed_to_int(octet))

with open(in_file,'r') as i:
    lines = i.readlines()

in_mac = lines

mac = EUI(in_mac[1])
print(mac)

mac.dialect = netaddr.mac_cisco
print(mac)

mac.dialect = netaddr.mac_bare
print(mac)

mac.dialect = netaddr.mac_unix_expanded
print(mac)
