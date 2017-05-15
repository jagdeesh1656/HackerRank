#!/bin/python3
import sys

ss = "hackerrank"
q = int(input().strip())
for a0 in range(q):
    ss_index = 0
    s = input().strip()
    for i in range(len(s)):
        if ss_index == len(ss):
            break
        if s[i] == ss[ss_index]:
            ss_index = ss_index + 1
    if ss_index == len(ss):
        print ("YES")
    else:
        print ("NO")
