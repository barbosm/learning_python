#!/usr/bin/env python3

f = open('show_version.txt')
out = f.read()
print(out)
print()
print(type(out))
print()
f.close()

with open('show_version.txt') as f:
    out = f.readlines()

print(out)
print(type(out))