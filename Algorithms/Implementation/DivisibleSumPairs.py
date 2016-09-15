#!/bin/python3

import sys
import itertools

def isDivisibleBy(pair, divisor):
    if pair[0] % divisor != 0 and pair[1] % divisor != 0:
        return 1
    else:
        return 0

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
lis = list(itertools.combinations(a, 2))
count = 0
for pair in lis:
    if isDivisibleBy(pair, k):
        count = count + 1
        
print (count)