
n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
d = {}
number = 0

a = [int(_a) for _a in input().strip().split(' ')]
for _a in a:
    count = d.setdefault(_a % k, 0)
    d[_a % k] = count + 1

i = 1
while 2 * i < k:
    number = number + max(d.setdefault(i, 0), d.setdefault(k - i, 0))
    i = i + 1

if 2 * i == k:
    number = number + 1
    

print (number)