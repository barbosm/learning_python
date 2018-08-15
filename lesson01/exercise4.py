#!/usr/bin/env python3

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "

version = show_version.strip().split()

model = version[1]
serial_number = version[2]

is_in_model = 'cisco' in model.lower()
print('Cisco is in model? : {}'.format(is_in_model))

is_in_model = '881' in model.lower()
print('881 is in model? : {}'.format(is_in_model))

print('Model: {}'.format(model))
print('SN: {}'.format(serial_number))