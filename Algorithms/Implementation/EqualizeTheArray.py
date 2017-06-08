n = int(input())
l = [int(temp) for temp in input().strip().split(' ')]
ndict = {}
for number in l:
    if number in ndict:
        ndict[number] = ndict[number] + 1
    else:
        ndict[number] = 1
maxi = 0
for number in ndict.keys():
    if ndict[number] > maxi:
        maxi = ndict[number]
print (len(l) - maxi)