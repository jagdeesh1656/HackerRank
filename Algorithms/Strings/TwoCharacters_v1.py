#!/bin/python3
import string
import sys

def altering_chars(s):
	j = len(s)-1
	for i in range(int(len(s)/2)):
		if s[i] != s[j]:
			return str(0)
		j = j - 1
	return s

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
