#!/bin/python3

import sys


h = list(map(int, input().strip().split(' ')))
word = input().strip()
max1 = 0
for c in word:
    if max1 < h[ord(c) - ord('a')]:
        max1 = h[ord(c) - ord('a')]
        
print (len(word) * max1) 