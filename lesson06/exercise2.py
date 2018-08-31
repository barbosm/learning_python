#!/usr/bin/env python3

from netmiko import Netmiko
from getpass import getpass

pwd = getpass()

my_dev = {
    'host': '192.168.0.1',
    'username': 'admin',
    'password': pwd,
    'device_type': 'fortinet',
}

net_conn = Netmiko(**my_dev)

cmd = 'get sys arp'

out = net_conn.send_command(cmd)
print(out)

net_conn.disconnect()