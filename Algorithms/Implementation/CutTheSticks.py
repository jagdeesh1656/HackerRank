#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

while(len(arr) > 0):
	print (len(arr))
	arr = [element for element in arr if element != min(arr)]
