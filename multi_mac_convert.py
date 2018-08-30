import sys
import netaddr
from netaddr import EUI

# take file as input
in_file = sys.argv[1]

def convert_mac(octet):
    return EUI(netaddr.strategy.eui48.packed_to_int(octet))

# open and read file
with open(in_file,'r') as i:
    lines = i.readlines()
    for line in lines:
        mac = EUI(line)
        mac.dialect = netaddr.mac_bare
        print(line) 