import sys

lDiagonal = rDiagonal = 0
n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
a_n = [item for sublist in a for item in sublist]    
for a_j in range(0,len(a_n),n+1):
    rDiagonal = rDiagonal + a_n[a_j]
for a_k in range(n,len(a_n),n-1):
    lDiagonal = lDiagonal + a_n[a_k-1]
print (abs(rDiagonal - lDiagonal))