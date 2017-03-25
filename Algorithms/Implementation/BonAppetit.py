
n, k = input().strip().split(' ')
n, k = int(n), int(k)

a = [_a for _a in input().strip().split(' ')]

sum = 0
for _a in a:
    sum = sum + int(_a)
    
shareOfEach = (sum - int(a[k])) / 2

charged = input().strip()

if (int(charged) == shareOfEach):
    print ("Bon Appetit")
else:
    print (int(abs(shareOfEach - int(charged))))