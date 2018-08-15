#!/usr/bin/env python3

# ip_addr = input("Please enter an IP address: ")
ip_addr = '2001:0db8:85a3:0000:0000:8a2e:0370:7334'
IP_ADDR = '2001:0db8:85a3:0000:0000:8a2e:0370:7335'
ipv6_add = '2001:0db8:85a3:0000:0000:8a2e:0370:7336'

print('\n')
print('var1 eq to var2 ?: {}'.format(ip_addr == IP_ADDR))
print('var2 not eq to var3?: {}'.format(IP_ADDR != ipv6_add))
print('\n')
