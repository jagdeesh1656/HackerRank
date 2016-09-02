#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

print (len([pInt for pInt in arr if pInt > 0]) / len(arr))
print (len([nInt for nInt in arr if nInt < 0]) / len(arr))
print (len([zInt for zInt in arr if zInt == 0]) / len(arr))