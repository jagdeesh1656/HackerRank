#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
E = 100
for i in range(0,n,k):
    if i != 0:
        if c[i] == 0:
            E -= 1
        else:
            E -= 3
if c[0] == 0:
    print (E-1) 
else:
    print (E-3)