#!/usr/bin/env python3

# ip_addr = input("Please enter an IP address: ")
ip_addr = '80.98.100.240'

HEADER = 'Octect'

print('\n')
print('{:^15}{:^15}{:^15}{:^15}'.format(HEADER + '1', HEADER + '2', HEADER + '3', HEADER + '4',))

print('-' * 60)

my_ip = ip_addr.split('.')


# print('{:^15}{:^15}{:^15}{:^15}'.format(my_ip[0], my_ip[1], my_ip[2], my_ip[3]))
print('{:^15}{:^15}{:^15}{:^15}'.format(*my_ip))

print('{:^15}{:^15}{:^15}{:^15}'.format(bin(int(my_ip[0])), bin(int(my_ip[1])), bin(int(my_ip[2])), bin(int(my_ip[3]))))

print('{:^15}{:^15}{:^15}{:^15}'.format(hex(int(my_ip[0])), hex(int(my_ip[1])), hex(int(my_ip[2])), hex(int(my_ip[3]))))

print('-' * 60)
print('\n')