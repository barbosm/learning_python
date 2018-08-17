#!/usr/bin/env python3

import re

with open('show_ipv6_intf.txt') as f:
    out = f.read()

# 'Ethernet2/4, Interface status: protocol-up/link-up/admin-up, iod: 40\n'
#  '  IPv6 address:\n'
#  '    2001:11:2233::a1/24 [VALID]\n'
#  '    2001:cc11:22bb:0:2ec2:60ff:fe4f:feb2/64\n'
#  '  IPv6 subnet:  2001::/24\n'

ip6_addr = []

match = re.search(r'(.*)IPv6 address:\s+(\S+)\s+\S+\s+(\S+).*', out, flags=re.DOTALL)

ip6_addr.append(match.group(2))
ip6_addr.append(match.group(3))

print(ip6_addr)