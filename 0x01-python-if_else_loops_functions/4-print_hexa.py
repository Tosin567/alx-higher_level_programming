#!/usr/bin/python3

for num in range(0, 99):
    print("{} = 0x{}".format(num, hex(num)[2:]), end="\n")
