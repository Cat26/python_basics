import re

text = 'aabbabbba bbaaabbbba  ababbbbbabbabs'

print(re.findall(r'bbb*', text)) # 'bb' + 0 or more b's
print(re.findall(r'bbb+', text)) # 'bb' + 1 or more b's
print(re.findall(r'bbb?', text)) # 'bb' + 1 or 0 b's

print(re.findall(r'bbb.', text)) # 'bbb' + single character not newline

print(re.findall(r'bbb{3}', text)) # 3 b's
print(re.findall(r'b{1,3}', text)) # 1- 3 b's
print(re.findall(r'b{3,}', text)) # tree or more b's