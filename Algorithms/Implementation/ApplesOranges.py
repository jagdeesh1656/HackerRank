#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

appleCount = orangeCount = 0

for ap in apple:
    if a >= 0 and a + ap >= s and a + ap <= t :
        appleCount = appleCount + 1
            
for o in orange:
    if o <= 0 and b + o <= t and b + o >= s :
        orangeCount = orangeCount + 1

print (appleCount)
print (orangeCount)
            
