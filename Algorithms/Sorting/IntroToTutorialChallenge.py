v = input()
n = input()
v, n = int(v), int(n)
l = [int(a) for a in input().strip().split(' ')]
for i in range(n):
    if v == l[i]:
        print (i)