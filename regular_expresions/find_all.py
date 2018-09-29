import re

text1 = 'Today is a beautiful weather, Tom is very happy'
text2 = 'abbbabbababababababab'

print(re.findall(r'is', text1))
ba = re.finditer(r'ba', text2)

count = 0
for el in ba:
    count += 1
    print(el.group(), el.start(), el.end())
print(count)