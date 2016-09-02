#!/bin/python3

import sys

try:
    n = int(input().strip())
except SyntaxError:
    n = None
if n is not None:
    if n > 0:
        try:
            arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
            sum = sum(arr)
            print (sum)
        except:
            arr = None
    