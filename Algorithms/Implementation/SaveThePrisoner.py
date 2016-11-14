T = int(input().strip())

for i in range(T):
    l = [int(x) for x in input().strip().split(' ')]
    N = int(l[0])
    M = int(l[1])
    S = int(l[2])
    print (((S + M - 2) %  N) + 1)