
s = 'baab'
finalString = ''
tuples = [s[i:i+2] for i in range(0, len(s), 2)]

for tup in tuples:
	if len(tup) == 2 and len(tup) == tup.count(tup[0]):
		s = s.replace(tup, '')

print s