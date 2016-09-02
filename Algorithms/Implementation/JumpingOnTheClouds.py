#!/bin/python3

import sys
from itertools import groupby

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

c = [list(g) for k,g in groupby(c,lambda x: x != 1) if k]
steps = 0

for elist in c:
	steps = steps + ((int)(len(elist)/2)) 

print ((steps) + (len(c) - 1))