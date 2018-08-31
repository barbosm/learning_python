#!/usr/bin/env python3

import pdb

def normalize_mac_addr(mac_addr):
    new_mac = []
    mac_addr = mac_addr.upper()
    mac_addr = ''.join(mac_addr.split('.')) # remove dots
    mac_addr = ''.join(mac_addr.split('-')) # remove dash
    
    if ':' in mac_addr:
        mac_addr = mac_addr.split(':')
        for octect in mac_addr:
            pdb.set_trace()
            if len(octect) < 2:
                octect = '0' + octect
            new_mac.append(octect)
    else:
        while len(mac_addr) > 0:
            new_mac.append(mac_addr[:2])
            mac_addr = mac_addr[2:]

    new_mac = ':'.join(new_mac)    
    return new_mac

print()
#pdb.set_trace()
print(normalize_mac_addr('0000.aaaa.bbbb'))
print(normalize_mac_addr('00-00-aa-aa-bb-bb'))
print(normalize_mac_addr('a:b:c:d:e:f'))
print(normalize_mac_addr('1a:b:c:2d:e:f'))
print()#!/usr/bin/env python3
