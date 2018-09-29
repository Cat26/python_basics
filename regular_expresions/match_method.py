import re

text1 = 'Today is a beautiful weather, Tom is very happy'
text2 = 'is today beautifu day, is it?'

m = re.match(r'is', text1)
n = re.match(r'is', text2)

print(m, n)