#!/usr/bin/env python3

from netmiko import Netmiko

my_dev = {
    'host': '10.99.236.231',
    'username': 'admin',
    'password': '',
    'device_type': 'fortinet',
}

net_conn = Netmiko(**my_dev)

cmd = 'get sys stat'
out = net_conn.send_command(cmd, use_textfsm=True)

print(out)

net_conn.disconnect()