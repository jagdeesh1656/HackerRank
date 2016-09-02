#!/bin/python3

import sys

x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

if v1!=v2:
    numOfSteps = (x2-x1)/(v1-v2)
    if numOfSteps <= 0 or (x2>x1 and v2>v1):
        print ('NO')
    elif numOfSteps > 0 and ((x2-x1) % (v1-v2) == 0):
        print ('YES')
    else:
        print ('NO')
else:
    if x2 > x1:
        print ('NO')
