#!/usr/bin/env python3

with open('show_lldp_neighbors_detail.txt') as f:
    out = f.read()


found_sysname, found_portid = (False, False)
sysname = ''
portid = ''

for line in out.splitlines():
    if 'System Name' in line:
        found_sysname = True
        sysname = line.split()[2]
    elif 'Port id' in line:
        found_portid = True
        portid = line.split()[2]
    elif found_sysname and found_portid:
        print('Found both, exiting...')
        break
else:
    print('not break')

print(sysname)
print(portid)
