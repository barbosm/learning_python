#!/usr/bin/env python3

my_ip_list = ['1.1.1.1', '1.1.1.2', '1.1.1.3', '1.1.1.4', '1.1.1.5']

my_ip_list.append('1.1.1.6')

my_ip_list.extend(['1.1.1.7', '1.1.1.8'])

my_ip_list += ['1.1.1.9', '1.1.1.10']

print(my_ip_list)

print(my_ip_list[0])

print(my_ip_list[-1])

my_ip_list.pop(0)

my_ip_list.pop()

my_ip_list[0] = '2.2.2.2'

print(my_ip_list[0])