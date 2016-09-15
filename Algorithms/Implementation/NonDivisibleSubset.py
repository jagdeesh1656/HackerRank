import itertools

def isDivisibleBy(sum, n):
	if sum % n == 0:
		return 1
	else:
		return 0

        
        
n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
l = list(itertools.combinations(a, 2))
nl = []
nls = []

for pair in l:
	if isDivisibleBy(sum(pair), k):
		if pair[0] in nl:
			nls.append(pair[0])
		if pair[1] in nl:
			nls.append(pair[1])
                nl.append(pair[0])
                nl.append(pair[1])
print (len(set(a) - set(nls)))