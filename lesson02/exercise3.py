#!/usr/bin/env python3

from pprint import pprint


with open('show_arp.txt') as f:
    out = f.readlines()

arp = out[1:]

pprint(arp)

# Use the list .sort() method to sort the list based on IP addresses.

arp_entries = arp[0:3]

arp_entries_line = '\n'.join(arp_entries)

f = open('arp_entries.txt', mode='w')
f.write(arp_entries_line)
f.close()

# alternative way to write
# with open("arp_entries.txt", "wt") as f:
#     f.write(my_entries)
