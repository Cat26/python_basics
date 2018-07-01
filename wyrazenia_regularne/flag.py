import re

text ='python Python PYTHON'
text2 ='Py\nthon'

print(re.findall(r'python', text))
print(re.findall(r'python', text, re.IGNORECASE))

print(re.findall(r'.+', text2))
print(re.findall(r'.+', text2, re.DOTALL))

print(re.sub(r'Py', 'My', text, count = 2, flags = re.IGNORECASE))