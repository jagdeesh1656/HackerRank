import re

s = ['abcdde','baccd','eeabg']
see = [('').join(set(se)) for se in s]
fs = ('').join(see)

p = re.compile(r'(\w)\1*')
print re.findall(p,fs)

