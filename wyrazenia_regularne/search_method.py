import re

text1 = 'Today is a beautiful weather, Tom is very happy'
print(re.search(r'is', text1))

m = re.search(r'is', text1)
print(m.group())

print(m.start(), m.end())
print(m.span())