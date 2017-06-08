n = 5
k = 1
l = [1, 2, 3, 4, 5]
d = {}

for i in l:
	d[i] = 0
for x in l:
	if d[x] == 0:
		d[x] = x
		if (x + k in d.keys() and d[x + k] == 0) or (x - k in d.keys() and d[x - k] == 0):
			d[x + k] = x
			d[x - k] = x
print d