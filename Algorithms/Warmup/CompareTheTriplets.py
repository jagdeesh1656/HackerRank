#!/bin/python3

import sys

aPoints = bPoints = 0;
a0,a1,a2 = input().strip().split(' ')
a = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b = [int(b0),int(b1),int(b2)]

for i in range(0,3):
    if a[i] > b[i]:
        aPoints = aPoints + 1;
    elif a[i] < b[i]:
        bPoints = bPoints + 1;
print (aPoints, bPoints)