genes = ['a','b','c','aa','d','b']
healths = [1, 2, 3, 4, 5, 6]
firsts = [1, 0, 2]
lasts = [5, 4, 4]
dnas = ['caaab', 'xyz', 'bcdybc']

for i in range(3):
	first = firsts[i]
	last = lasts[i]
	dna = dnas[i]
	gene_seq = genes[first:(last+1)]
	heal_seq = {}
	count = []
	maxi = 0

	for gene in gene_seq:
		if len(gene) > maxi:
			maxi = len(gene)

	for gene in gene_seq:
		if gene in heal_seq:
			heal_seq[gene].append(healths[first])
		else:
			heal_seq[gene] = list(map(int, str(healths[first])))
		first = first + 1
	print (heal_seq)

	for cindex in range(len(dna)):
		if dna[cindex] in gene_seq:
			count.append(heal_seq[dna[cindex]])
		else:
			cindex2 = cindex
			temp_s = ''
			while(len(temp_s) < maxi + 1):
				temp_s = dna[cindex2:(cindex2 + 2)]
				print (temp_s)
				if temp_s in gene_seq:
					count.append(heal_seq[temp_s])
				cindex2 = cindex2 + 1
	print (count)