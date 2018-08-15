#!/usr/bin/env python3

with open('show_ip_bgp_summ.txt') as f:
    out = f.readlines()

first = out[0]
last = out[-1]

as_number = first.split()[-1]
peer_ip = last.split()[0]

print('AS: {:5} - Peer IP: {:5}'.format(as_number, peer_ip))