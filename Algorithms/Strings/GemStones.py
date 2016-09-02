import re

s = []
n = int(input().strip())
for i in range(n):
    s.append(input().strip())
see = [('').join(set(se)) for se in s]
fs = ('').join(see)

gems = {}
for char in fs:
	if fs.count(char) == n:
		gems[char] = n

if len(gems) > 0:
    print (len(gems))
else:
    print ('0')