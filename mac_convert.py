# dirty script to convert MACs of different formats
# Rusty Tyner - 6/25/18

import netaddr
from netaddr import EUI
 
def convertMac(octet):
    return EUI(netaddr.strategy.eui48.packed_to_int(octet))

from netaddr import EUI
import netaddr

in_mac = input("Input your MAC here: ")
print(input)

mac = EUI(in_mac)
print(mac)

mac.dialect = netaddr.mac_cisco
print(mac)

mac.dialect = netaddr.mac_bare
print(mac)

mac.dialect = netaddr.mac_unix_expanded
print(mac)