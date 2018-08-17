#!/usr/bin/env python3

import re

show_version = '''
Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX0000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)
'''

device = re.search(r'^Cisco (?P<model>.*?)\s.*with (?P<memory>.*) bytes.*', show_version.splitlines()[1]).groupdict()

# alternative
# match = re.search...
# model = match.groupdict()['model']

print()
print('Model: ' + device['model'])
print('Memory: ' + device['memory'])
print()
