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
# need to have this loop through the entire list - also need to prompt for what type of MAC you want to convert to.
mac = EUI(in_mac[1])
print(mac)

mac.dialect = netaddr.mac_cisco
print(mac)

mac.dialect = netaddr.mac_bare
print(mac)

mac.dialect = netaddr.mac_unix_expanded
print(mac)
