#!/usr/bin/env python3

def ssh_conn(ip_addr, username, password, device_type='cisco_ios'):
    print()
    print('IP Address: {}'.format(ip_addr))
    print('Username: {}'.format(username))
    print('Password: {}'.format(password))
    print('Device Type: {}'.format(device_type))
    print()

ssh_conn('1.1.1.1', 'admin', 'pass')

ssh_conn('1.1.1.1', 'admin', 'pass', 'junos')

d = {'ip_addr': '2.2.2.2', 'username':'dic_admin', 'password':'dic_pass', 'device_type':'fortios'}

ssh_conn(**d)