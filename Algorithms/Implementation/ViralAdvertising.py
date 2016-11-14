import math

n = int(input().strip())
first = 5
temp1 = 0

for i in range(n):
    temp1 = temp1 + math.floor(first/2)
    first = math.floor(first/2) * 3
    
print (temp1)