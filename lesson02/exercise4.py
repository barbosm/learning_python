#!/usr/bin/env python3

with open('show_ip_int_brief.txt') as f:
    out = f.readlines()

fe4 = out[5]

fe4.split()

intf_ip = (fe4.split()[0], fe4.split()[1])

print(intf_ip)
