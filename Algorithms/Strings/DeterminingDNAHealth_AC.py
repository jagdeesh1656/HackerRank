# genes = ['he', 'she', 'hers', 'his']
# genes = ['ogwwsenipa', 'obsehkjfcj', 'dhqvptquuu', 'kkdgivnvfc', 'ytdqxmciue', 'rznhvdcnxw', 'kihnqpkdnp', 'hlimdfbfnv', 'mguznrcpfc', 'nrmweeookb', 'drolersfwh', 'ckpykeqotx', 'sioefulviv', 'wnmkasbuzz', 'ddkscwwukr', 'rfzhjgbwbl', 'rzagjaymua', 'mxdyrhunbg', 'eulfdxogtr', 'rnrrtctrpp', 'tdmzbfgxsi', 'fyereiquol', 'liyebrhvly', 'kgbzfeembz', 'wgxazdirzx', 'flfdrgxydi', 'woqzpwdvkg', 'ugpuiqxrix', 'qnkxsbfpcj', 'zazqaqmdly', 'mgebaorzfz', 'yxoiuhmayo', 'lyqkoqacwn', 'aivgjxucxc', 'cxzsgwbuya', 'klyavotxsp', 'muzickfwmc', 'aqccjiakey', 'mojmqgajfu', 'yrozzqjfpw', 'jrmltxvtkz', 'twpejgmlpr', 'gqlwpknbre', 'xdvlqplmkv', 'ngtfmelzsc', 'qyudukojnh', 'nkmjxdairm', 'fgublhhygz', 'byxvcuhsdu', 'btgocgreqk', 'syqnzeuicc', 'ifahdebmwh', 'jaapoexhio', 'rcmjpnnlxq', 'nfvonauqnt', 'xwtznjdlqn', 'bjqnshcgtz', 'yghvwuwrml', 'kmhdlumrhe', 'einwxhebpx', 'bnfilcejts', 'ufebiqxwjh', 'cnprmnysoq', 'rrfwbqahzv', 'atagwkwwif', 'dkvsbjhcby', 'surxqvqter', 'oenpljzjhi', 'rkuofwxoaa', 'osugrmdjfh', 'bwoolbzmkh', 'wdtrrypqpp', 'qdjmlcbomi', 'wpekdpleex', 'nabhtuhinw', 'zfcksnntcb', 'dyqiktzxzd', 'ungxuzubkh', 'almcwgrlbt', 'mftcndxoaw', 'sxjawdzshl', 'zjxonvwegy', 'ysfruuxtiz', 'payzavecpn', 'ppwofjjbop', 'bojghfaeyj', 'golgpodtst', 'hhifwprhqf', 'xuvgacodjm', 'orcbxrpbnj', 'uwtebrtsyl', 'zxfugizuli', 'gzzjawcszp', 'btnwxrnqlm', 'enljjrrile', 'ssdtdgsfar', 'xdlmaidpbp', 'dhepqngkws', 'oomuipccwc', 'ttfeihplxs']
healths = [1, 2, 3, 4]
firsts = [0]
lasts = [4]
# dnas = ['bdecabbbbbeeeeeecccccaaabbba']
trie = {}
outs = {}
failure = {}
prev = set()
big_q = []
states = 1

for gene in genes:
	prev = prev.union(set(gene))
print ("prev done")
queue = []

for i in range(len(genes)):
    currentState = 0
    for j in range(len(genes[i])):
    	ch = ord(genes[i][j]) - 96
    	# states = states + 1
        temp = '%s%s' % (currentState, genes[i][j],)
        if temp not in trie.keys(): 
            trie[temp] = [states, 0]
            # queue.append('%s-%s' % (temp, ch))
        currentState = trie[temp][0]
    if currentState in outs.keys():
    	outs[currentState].append(genes[i])
    else:
    	outs[currentState] = [genes[i]]

for char in prev:
    temp = '%s%s' % (0, char,)
    if temp in trie.keys():
        # queue.append('%s-%s' % (temp,trie[temp][0]))
        big_q.append('%s-%s' % (temp,trie[temp][0]))

while len(queue) > 0:
    state = queue[-1].split('-')[1]
    parent = queue[-1].split('-')[0]
    queue = queue[:-1]
    for pre in prev:
        temp = '%s%s' % (state, pre)
        if temp in trie.keys():
            queue.append('%s-%s' % (temp,trie[temp][0]))
            # big_q.append('%s-%d' % (temp,trie[temp][0]))
            fail = trie[parent][1]
            temp2 = '%s%s' % (fail, pre)
            if temp2 in trie.keys():
                trie[temp][1] = trie[temp2][0]
            else:
                trie[temp][1] = fail
big_dict = {}
for l in queue:
    if l.split('-')[0] not in big_dict.keys():
        big_dict[l.split('-')[0]] = l.split('-')[1]

# print (trie)
# print (outs)
# for i in range(1):
# 	first = firsts[i]
# 	last = lasts[i]
# 	dna = dnas[i]
# 	gene_seq = genes[first:(last+1)]
# 	# print (gene_seq)
# 	# heal_seq = healths[first:(last+1)]
# 	states = 1	
# 	for i in range(len(gene_seq)):
# 		# print (gene_seq[i])
# 		# out = 0
# 		currentState = 0
# 		for j in range(len(gene_seq[i])):
# 			temp = '%s%s' % (currentState, gene_seq[i][j],)
# 			if temp not in trie.keys():
# 				states = states + 1
# 				trie[temp] = [states, 0]
# 			currentState = trie[temp][0]
# 		# outs[currentState] = gene_seq[i] 
# 	queue = []
	# print ("something done")
	# for char in prev:
	# 	temp = '%s%s' % (0, char,)
	# 	if temp in trie.keys():
	# 		queue.append('%s-%s' % (temp,trie[temp][0]))
	# 		big_q.append('%s-%s' % (temp,trie[temp][0]))

# 	while len(queue) > 0:
# 		state = queue[-1].split('-')[1]
# 		parent = queue[-1].split('-')[0]
# 		queue = queue[:-1]
# 		for pre in prev:
# 			temp = '%s%s' % (state, pre)
# 			if temp in trie.keys():
# 				queue.append('%s-%d' % (temp,trie[temp][0]))
# 				big_q.append('%s-%d' % (temp,trie[temp][0]))
# 				fail = trie[parent][1]
# 				temp2 = '%s%s' % (fail, pre)
# 				if temp2 in trie.keys():
# 					trie[temp][1] = trie[temp2][0]
# 				else:
# 					trie[temp][1] = fail

# big_dict = {}
# for l in big_q:
# 	if l.split('-')[1] not in big_dict.keys():
# 		big_dict[l.split('-')[1]] = l.split('-')[0]

# print ("automata done")
# currentState = '0'
# answer = currentState

# for dna in dnas:
# 	for letter in dna:
# 		temp = '%s%s' % (currentState, letter)
# 		print (temp)
# 		if temp in trie.keys():
# 			answer = trie[temp][0]
# 			if answer in outs:
# 				print (outs[answer])
# 		else:
# 			if (currentState) in big_dict.keys():
# 				while trie[big_dict[(currentState)]][1] != 0:
# 					print (trie[big_dict[(currentState)]][1])
# 					temp2 = '%s%s' % (trie[big_dict[(currentState)]][1], letter)
# 					if temp2 in trie.keys():
# 						answer = trie[temp2][0]
# 						break
# 					else:
# 						currentState = trie[big_dict[(currentState)]][1]
# 						print (currentState)
# 						break
# 			if (currentState) not in big_dict.keys():
# 				currentState = 0
# 			elif trie[big_dict[(currentState)]][1] == 0:
# 				t = '%s%s' % ('0',letter)
# 				if t in trie.keys():
# 					answer = trie[t][0]
# 				else:
# 					answer = 0
# 					break
# 		currentState = answer
# 		print (letter, answer)

