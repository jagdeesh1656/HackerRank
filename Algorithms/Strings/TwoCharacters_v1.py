#!/bin/python3
import string
import sys

def altering_chars(s):
	new_s = ''
	for i in range(len(s)):
		if i % 2 == 0:
			new_s += s[0] 
		else:
			new_s += s[1]
	if new_s == s:
		return new_s
	else:
		return str(0)

s_len = int(input().strip())
s = input().strip()
orig_s = s

l = list(set(s))
max_len = 1

for i in range(len(l)):
	for j in range(i+1, len(l)):
		for k in range(len(l)):
			if k !=i and k!=j:
				s = s.replace(l[k],'')
		if len(altering_chars(s)) > max_len:
			max_len = len(altering_chars(s))
			max_s = s	
		s = orig_s

if max_len > 1:
	print (max_len)
else:
	print (0)
