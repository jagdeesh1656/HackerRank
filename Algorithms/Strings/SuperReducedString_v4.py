import re
s = 'jaaaagdeesh2198qerner/f;3565erbl;weiuhh[gewebfkn'
p = re.compile(r'(\w)\1')
se = re.findall(p, s)

print se