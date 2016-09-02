#!/bin/python3
import sys

s = input().strip()
s = s.lower()
l = set(s.replace(' ', ''))

if (len(l) == 26):
    print ('pangram')
else:
    print ('not pangram')