#!/usr/bin/env python3

with open('show_arp.txt') as f:
    out = f.read()

show_arp = out.splitlines()

arp_table = []

found = 0

for line in show_arp:
    if 'Protocol' in line:
        continue
    fields = line.split()
    ip_addr = fields[1]
    mac_addr = fields[3]
    if '10.220.88.1' in ip_addr:
        print('Default gateway IP/Mac: {} - {}'.format(ip_addr, mac_addr))
        found += 1
    elif '10.220.88.30' in ip_addr:
        print('Arista3 IP/Mac: {} - {}'.format(ip_addr, mac_addr))
        found += 1
    elif found == 2:
        break
else:
    print('no break')
