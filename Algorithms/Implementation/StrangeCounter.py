#!/bin/python3

import sys
import math

t = int(input().strip())
temp = (t + 2) / 3
cycle = math.floor(math.log (temp, 2) + 1)
cycleStart = 1
value = 3

if cycle > 1:
    cycleStart = (3 * math.pow(2, cycle - 1)) - 2
    value = (3 * math.pow(2, cycle - 1))

print (math.floor(value - (t - cycleStart)))