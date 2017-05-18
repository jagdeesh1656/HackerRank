#!/bin/python3

import sys

def getWays(squares, d, m):
    res = 0
    for i in range(len(squares)):
        if len(squares[i:i+m]) == m and sum(squares[i:i+m]) == d:
            res = res + 1
    return res

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d,m = input().strip().split(' ')
d,m = [int(d),int(m)]
result = getWays(s, d, m)
print(result)
