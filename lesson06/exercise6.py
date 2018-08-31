#!/usr/bin/env python3

from netmiko import Netmiko
from getpass import getpass

pwd = ''

dev1 = {
    'host': '10.99.236.233',
    'username': 'admin',
    'password': pwd,
    'device_type': 'fortinet',
}

dev2 = {
    'host': '10.99.236.234',
    'username': 'admin',
    'password': pwd,
    'device_type': 'fortinet',
}

dev3 = {
    'host': '10.99.236.235',
    'username': 'admin',
    'password': pwd,
    'device_type': 'fortinet',
}

for device in dev1, dev2, dev3:
    net_conn = Netmiko(**device)
    cmd = 'get sys stat'
    out = net_conn.send_command(cmd)
    print(out)
    net_conn.disconnect()