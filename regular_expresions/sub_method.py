import re

text1 = 'helolorkhelokkhhheloghtlokglo'
s =re.sub(r'lo', 'xx', text1)
print(s)

s =re.sub(r'xx', 'lo', s, count =2)
print(s)

pat = re.compile(r'lo')
print(re.findall(pat, text1))