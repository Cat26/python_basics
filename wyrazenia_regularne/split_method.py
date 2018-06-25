import re

text = 'hello; miauu;grrr,trata ttyy'
s = re.split(r'[ ;,]\s*', text)
print(s)