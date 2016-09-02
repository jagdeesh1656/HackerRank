#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    studentsPresentForClass = 0
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]

    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    for i in range(len(a)):
        if a[i] <= 0:
            studentsPresentForClass  = studentsPresentForClass + 1
    if studentsPresentForClass >= k:
        print ('NO')
    else:
        print ('YES')