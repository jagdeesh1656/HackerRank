import sys
import math

s = input().strip()
lenrootmin = math.floor(math.sqrt(len(s)))
lenrootmax = math.ceil(math.sqrt(len(s)))
rows = columns = lenrootmin
if abs(lenrootmin - lenrootmax) == 0:
	rows = lenrootmin
	columns = lenrootmax
else:
    rows = lenrootmax
    columns = lenrootmax

if (rows * columns) >= len(s):
	matrix = [[s[r * int(columns) + c ] if (r * int(columns) + c < len(s)) else '' for c in range(int(columns))] for r in range(int(rows))]
	answer = ' '.join([''.join([row[i] for row in matrix]) for i in range(int(columns))])
	print (answer)