genes = ['a','b','c','aa','d','b']
healths = [1, 2, 3, 4, 5, 6]
firsts = [1, 0, 2]
lasts = [5, 4, 4]
dnas = ['caaab', 'xyz', 'bcdybc']
counts = []
maximum = 0
minimum = sum(healths)

for i in range(3):
	first = firsts[i]
	last = lasts[i]
	dna = dnas[i]
	gene_seq = genes[first:(last+1)]
	heal_seq = healths[first:(last+1)]
	sum1 = 0
	print (gene_seq, heal_seq)
	for j in range(len(gene_seq)):
		for i in range(0, len(dna)):
			if dna[i:(i+len(gene_seq[j]))] == gene_seq[j]:
				sum1 = sum1 + heal_seq[j]
	if sum1 > maximum:
		maximum = sum1
	if sum1 < minimum:
		minimum = sum1
	# for i in range(len(dna)):
	# 	for j in range(i+1, i+maxi+1):
	# 		if j > len(dna):
	# 			break
	# 		if dna[i:j] in gene_seq:
	# 			print (i, j, dna[i:j])
	# count = 0
	# for k in gene_seq:
	# 	if k == dna[i:j]:
	# 		count = count + 1
	# print (count)
print (maximum, minimum)