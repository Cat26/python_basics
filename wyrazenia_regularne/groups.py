import re

text ='My phone number is 123-563-756'

print(re.findall(r'[\d]{3}-[\d]{3}-[\d]{3}', text))

m = re.search(r'([\d]{3})-(?P<middle>[\d]{3})-([\d]{3})', text) # name group ?P<name>
print(m.group())
print(m.groups())
print(m.group(2))
print(m.group('middle'))