#!/bin/python3
import sys

nkq = input().strip().split(' ')
n = int(nkq[0])
k = int(nkq[1])
q = int(nkq[2])

a = input().strip().split(' ')

k = k%n

for i in range(int(q)):
    qu = int(input().strip());
    if  qu - k >= 0:
        print (a[qu-k])
    else:
        print (a[qu-k+len(a)])

