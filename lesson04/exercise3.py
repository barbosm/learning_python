#!/usr/bin/env python3

import re

with open('show_version.txt') as f:
    out = f.read()




# Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.4(2)T1, RELEASE SOFTWARE (fc3)
# Processor board ID FTX0000038X
# Configuration register is 0x2102

os_version = re.search(r'^.*Version (\S+),.*$', out, flags=re.M).group(1)
serial_number = re.search(r'^Processor board ID (\S+)$', out, flags=re.M).group(1)
conf_register = re.search(r'^Configuration register is (\S+)$', out, flags=re.M).group(1)

print()
print('{:>20}: {}'.format('OS Version', os_version))
print('{:>20}: {}'.format('Serial Number', serial_number))
print('{:>20}: {}'.format('Config Register', conf_register))
print()
