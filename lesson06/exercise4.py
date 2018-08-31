#!/usr/bin/env python3

from netmiko import Netmiko

my_dev = {
    'host': '10.99.236.231',
    'username': 'admin',
    'password': '',
    'device_type': 'fortinet',
}

net_conn = Netmiko(**my_dev)


# Config
cfg_cmds = [
    'config system global', 
      'set hostname fgvm_test',
    'end'
]

out = net_conn.send_config_set(cfg_cmds)

out = net_conn.send_config_from_file('config_changes.txt')

# Check
cmd = 'sh sys gl'
out = net_conn.send_command(cmd)

print(out)

net_conn.disconnect()
