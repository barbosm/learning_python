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

print(net_conn.find_prompt())

net_conn.disconnect()