#!/usr/bin/env python3

from netmiko import Netmiko
from getpass import getpass

#pwd = getpass()

my_dev = {
    'host': '10.99.236.231',
    'username': 'admin',
    'password': '',
    'device_type': 'fortinet',
}

net_conn = Netmiko(**my_dev)

cmd = 'exec reboot'
out = net_conn.send_command_timing(cmd)

print(out)

'''
fg # exec reboot
This operation will reboot the system !
Do you want to continue? (y/n)n
'''

if 'continue' in out:
    out += net_conn.send_command_timing('y\n')

print(out)

net_conn.disconnect()