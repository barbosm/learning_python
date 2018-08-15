#!/usr/bin/env python3

import os

WINDOWS = False

base_cmd_linux = 'ping -c 2 '
base_cmd_windows = 'ping -n 2 '
# Ternary operator
base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux


base_ip = '192.168.0.'
list_ip = []

for host_ip in range(1,10):
    list_ip.append(base_ip + str(host_ip))
    # print(list_ip)


for i, ip in enumerate(list_ip):
    print('{} ---> {}'.format(i, ip))

new_range = list_ip[2:6]

for ip in new_range:
    os.system(base_cmd + ip)