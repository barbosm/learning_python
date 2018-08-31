#!/usr/bin/env python3

import random


def rand_ip_addr(base_net='10.10.10.'):
    ip_addr = base_net + str(random.randint(1, 254))
    print(ip_addr)

print()
rand_ip_addr()
rand_ip_addr('172.16.10.')
rand_ip_addr(base_net='192.168.1.')
print()
