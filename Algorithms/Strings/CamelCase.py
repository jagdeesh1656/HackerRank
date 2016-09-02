import re

s = 'saveCahngesInEditot'
p = re.compile(r'[A-Z]')

print (len(re.findall(p, s)) + 1)