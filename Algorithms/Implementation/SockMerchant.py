#!/bin/python3

import sys

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
c.sort()
count = i = 0

while(i <= n-2):
    if c[i] == c[i+1]:
        count = count + 1
        i = i + 2
    else:
        i = i + 1

print (count)