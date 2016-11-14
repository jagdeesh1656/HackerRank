#!/bin/python3

import sys
from collections import Counter

Q = int(input().strip())
for a0 in range(Q):
    D = {}
    count = 0
    got = 1
    n = int(input().strip())
    b = input().strip()
    temp = b.replace("_", "")

    if temp == "":
        print ("YES")
        continue
    if "_" in b:
        D = Counter(temp)
        for i in D.keys():
            if D[i] > 1:
                count = count + 1
        if count == len(D.keys()):
            print ("YES")
        else:
            print ("NO")
    if "_" not in b:
        if len(b) == 1:
            print ("NO")
            continue
        if (len(b) == 2) and (b[0] != b[1]):
            print ("NO")
            continue
        if len(b) > 2:
            if b[0] != b[1]:
                got = 0
                print ("NO")
                continue
            for i in range(1, len(b)-1):
                if ((b[i] == b[i+1]) or (b[i-1] == b[i])):
                    continue
                else:
                    got = 0
                    print ("NO")
                    break
            if got and (b[len(b)-2] != b[len(b)-1]):
                got = 0
                print ("NO")
                continue
        if (got):
            print ("YES")
        
    
        
        