#!/usr/bin/env python3

net_dev = {
    'ip_addr': '1.1.1.1', 
    'vendor': 'cisco', 
    'username': 'admin', 
    'password': 'cisco',
    }

print(net_dev['ip_addr'])

if 'cisco' in net_dev['vendor']:
    net_dev['platform'] = 'ios'
elif 'juniper' in net_dev['vendor']:
    net_dev['platform'] = 'junos'
else:
    net_dev['platform'] = 'other'

bgp_fields = {  
    'bgp_as': '6500',
    'peer_as': '6501',
    'peer_ip': '2.2.2.2',
    }

net_dev.update(bgp_fields)

for key in net_dev:
    print(key)

for key, value in net_dev.items():
    print(key, value)
