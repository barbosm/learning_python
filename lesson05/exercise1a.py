#!/usr/bin/env python3

def ssh_conn(ip_addr, username, password):
    print()
    print('IP Address: {}'.format(ip_addr))
    print('Username: {}'.format(username))
    print('Password: {}'.format(password))
    print()

ssh_conn('1.1.1.1', 'admin', 'pass')

ssh_conn(password='1.1.1.1', ip_addr='admin', username='pass')

ssh_conn('1.1.1.1', password='admin', username='pass')