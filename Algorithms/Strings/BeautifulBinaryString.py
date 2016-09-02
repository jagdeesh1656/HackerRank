import re

s = '0101010'
p = re.compile('010')

print (len(re.findall(p,s)))