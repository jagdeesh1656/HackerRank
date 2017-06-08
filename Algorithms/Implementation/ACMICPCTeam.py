#!/bin/python3

import sys

def findones(maxi):
    count = 0
    maxs = str(bin(maxi))
    for s in maxs:
        if s == '1':
            count = count + 1
    return count

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
topics_perperson = []
for person in range(n):
    topics_known = str(input())
    topics_perperson.append(topics_known)
count = 0
maxi = 0
count = [0 for i in range(0, m + 1)]
i = 0
maxi2 = 0
for person in range(n):
    for person2 in range(person + 1, n):
        bitor = int(topics_perperson[person], 2) | int(topics_perperson[person2], 2)
        x = findones(bitor)
        if x > maxi:
            maxi = x
        count[x] = count[x] + 1
print (maxi)
print (count[maxi])
