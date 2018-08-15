#!/usr/bin/env python3

from pprint import pprint

with open('show_vlan.txt') as f:
    out = f.read()

show_vlan = out.splitlines()

vlans = []

for line in show_vlan:
    if 'VLAN' in line or line.startswith(' ') or line.startswith('-'):
        continue
    vlan_id = line.split()[0]
    vlan_name = line.split()[1]
    vlans += [(vlan_id, vlan_name)]
    # vlans.append((vlan_id, vlan_name)) # alternative
    # print(vlan_id, vlan_name)

pprint(vlans)