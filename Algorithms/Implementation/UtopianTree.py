#!/bin/python3

import sys

h = 0
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    h = 1
    for i in range(n+1):
        if i != 0:
            if i % 2 == 0:
                h += 1
            if i % 2 != 0:
                h *= 2
    print (h)
    
