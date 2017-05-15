import re

s = input().strip()
p = re.compile(r'(\w)\1')

while re.search(p, s):
	se = re.search(p, s)
	s = s.replace(se.group(), '')
if len(s) > 0:
    print (s)
else:
    print ("Empty String")